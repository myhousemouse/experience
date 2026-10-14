"""Recompute aggregate survey counts without exporting individual answers.
Usage: python recompute_survey.py --xlsx SOURCE.xlsx --out OUTPUT.json
Requires openpyxl. Workbook first sheet, original 34-column layout.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from openpyxl import load_workbook


def aggregate(path):
    sheet = load_workbook(path, data_only=True).active
    records = list(sheet.iter_rows(values_only=True))
    headers = records[0]
    if len(headers) != 34:
        raise ValueError('Expected original 34-column survey schema')
    rows = [row for row in records[1:] if any(value is not None for value in row)]
    questions = {}
    # Whitelisted categorical columns only; omit artist names and all free text.
    selected = [1, 2, 4, 7, 10, 15, 16, 18, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    for index in selected:
        counts = Counter(str(row[index]).strip() for row in rows
                         if row[index] is not None and str(row[index]).strip())
        questions[str(index + 1)] = {'question': headers[index],
                                    'valid_n': sum(counts.values()), 'counts': dict(counts)}
    return {'source_sheet': sheet.title, 'total_records': len(rows),
            'collection_start': min(row[0] for row in rows).date().isoformat(),
            'collection_end': max(row[0] for row in rows).date().isoformat(),
            'questions': questions,
            'privacy': 'aggregate only; timestamps per respondent, names, artist preferences, free text omitted'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--xlsx', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    result = aggregate(args.xlsx)
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Aggregate saved: {result['total_records']} records, {len(result['questions'])} categorical questions")


if __name__ == '__main__':
    main()
