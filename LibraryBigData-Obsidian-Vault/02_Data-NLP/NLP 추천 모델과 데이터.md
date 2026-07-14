# NLP 추천 모델과 데이터

아이디어 페이지: https://app.notion.com/p/3973eee3a7048053b921de99826f4842
개인 정리: https://app.notion.com/p/24cb941e2c07471fa8e26df465b9871c
태그: #nlp #recommendation #data #python

## 활용 데이터

- 도서관 정보나루 데이터
- 도서관 정보나루 이달의 키워드
- 인디펍 독립서적 데이터
- 인디펍 이용자 리뷰/커뮤니티 데이터
- 독립서점/독립출판 관련 참고자료

## 코드/데이터 산출물

개인 Notion 페이지에는 다음 파일들이 정리되어 있었다.

- `indi_crawling.ipynb`
- `indi_crawling_test.ipynb`
- `indi_crawling_eun.ipynb`
- `indi_crawling_(01_10).ipynb`
- `indi_crawling_(1).ipynb`
- `full_code.ipynb`
- `indi_crawling2.ipynb`
- `indi_*.xlsx`
- `Demo*_베스트 셀러.xlsx`
- `도서관정보나루_이달의 키워드(2024-06).xlsx`

## 추천 알고리즘 방향

참고한 자연어처리 기반 책 추천 구조는 다음과 같다.

1. 책 설명과 사용자 입력 키워드를 텍스트 데이터로 구성한다.
2. 책 설명의 단어 빈도를 TF-IDF 행렬로 표현한다.
3. Word2Vec 등 임베딩 모델로 의미적으로 유사한 단어를 확장한다.
4. 코사인 유사도를 사용해 사용자 입력과 도서 설명 간 유사도를 계산한다.
5. 유사도가 높은 독립서적을 추천한다.

## 기획적 의미

이 프로젝트에서 NLP는 단순 기술 실험이 아니라 `잘 팔리는 책`이 아니라 `사용자 취향과 의미적으로 맞는 독립서적`을 찾기 위한 방법이었다. 공모전의 도서관 데이터 활용 조건과 독립서적 추천의 차별성을 연결하는 핵심 장치였다.

## 관계

- implements: [[독립서적 추천 서비스 기획]]
- supports: [[개인 기여 정리]]
- evidence-for: [[면접용 포인트]]

