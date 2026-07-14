# API와 시스템 구조

전체 구조: https://app.notion.com/p/3633eee3a7048394b401815c4813a57e
단계별 구현: https://app.notion.com/p/7823eee3a7048388a568817accd30344
공용 API 명세: https://app.notion.com/p/0e33eee3a70482189a580109d15ba438
태그: #architecture #api #spring #rag

## 초기 목표 구조

```text
[로우코드 프론트]
  -> [Spring Boot 서버]
  -> [PostgreSQL]
  -> [Python FastAPI RAG 서버]
```

## 초기 역할

- 로우코드: 화면, 지도, 버튼, 폼, API 호출
- Spring Boot: 데이터 수집/가공, 공공데이터 API, 위험도 API, RAG 중계
- PostgreSQL: 도로, 기상, 제보, 임베딩 데이터 저장
- Python FastAPI: 문서 기반 AI 질의응답

## 주요 API

- `POST /api/route`: 출발지-도착지 경로 도로와 위험도 반환
- `GET /api/risk/road/{id}`: 특정 도로 최신 위험도 반환
- `GET /api/risk/top`: 위험도 TOP 10 반환
- `GET /api/risk/near`: 주변 도로 위험도 반환
- `POST /rag/query`: 빙판길 관련 AI 질의응답
- `GET /api/roads`: 도로 리스트 조회
- `POST /api/report`: 시민 제보 등록
- `GET /api/health`: 서버 상태 확인

## 데이터 모델

- `road_info`: 도로 기본 정보
- `weather_log`: 기상청 API로 수집한 기상 데이터
- `report`: 시민 제보
- `doc_embedding`: RAG 검색용 임베딩 데이터

## 최종 구현과의 차이

초기 구조는 정석적인 서버 구조였지만, 최종 구현에서는 로우코드 공모전의 목적과 일정, 툴 제약을 고려해 일부 흐름을 단순화했다.

- 시민 제보 저장: Spring/PostgreSQL 중심 계획 -> Google Sheets 연동
- 지도 중심 시각화 -> 위험도 TOP 10 리스트 중심
- Python RAG 서버 -> OpenAI API 직접 호출과 프롬프트 엔지니어링

## 관계

- initial-plan-for: [[로우코드 구현과 기술 의사결정]]
- documents: [[협업 페이지 정리]]
- source-of-truth-if-api: 공용 API 명세서

