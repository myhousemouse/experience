# FastAPI와 RAG

원본: https://app.notion.com/p/2313eee3a7048053bc64c0256c042484
태그: #fastapi #rag #langchain #api #backend

## 학습 내용

FastAPI 페이지에서는 RAG 파이프라인과 LangChain 기반 구현 방법을 정리했다.

## RAG 파이프라인

RAG는 문서를 숫자로 변환해 저장하고, 사용자 질문에 맞는 문서를 검색한 뒤 답변 생성에 활용하는 구조다.

구성 요소:

- 문서 로더
- 문서 분할기
- 임베딩 모델
- 벡터 DB
- Retriever
- LLM

구현 흐름:

1. 문서 업로드
2. 문서 분할
3. 문서 임베딩
4. 임베딩 검색
5. 답변 생성

## FastAPI 역할

FastAPI는 챗봇과 프론트엔드 사이의 API 서버 역할을 한다.

핵심 엔드포인트:

- `POST /api/chat`: 사용자 질문을 받아 LangGraph/ReAct agent에 전달하고 답변 반환
- `GET /api/chat/sessions`: 저장된 챗봇 세션 목록 조회
- `GET /api/chat/sessions/{session_id}`: 특정 세션 메시지 조회
- `DELETE /api/chat/sessions/{session_id}`: 특정 세션 삭제

GitHub 기준으로 `myhousemouse` 계정의 `챗봇 개선` 커밋에서 세션 기반 대화 저장/조회/삭제 구조가 추가되었다. 자세한 코드 근거는 [[GitHub 챗봇 개발 근거]]에 정리했다.

## 병해충 진단 API와 연결

백업 코드에는 이미지 기반 작물 질병 진단 API와 챗봇 API가 함께 구성되어 있다.

주요 기능:

- 작물 이미지 업로드 진단
- 이미지 URL 기반 진단
- 진단 결과 DB 저장
- 진단 피드백 저장
- 챗봇 히스토리 저장

## 데이터베이스 구조

SQLite 기반으로 다음 테이블을 사용했다.

- `diagnoses`: 진단 기록
- `feedback`: 진단 결과 피드백
- `chat_history`: 챗봇 대화 히스토리
- `chat_sessions`: 챗봇 대화 세션
- `chat_messages`: 세션별 사용자/AI 메시지

## 배포/문서화

최종 산출물에는 Swagger 주소가 포함되어 있다.

- http://52.78.38.133:8000/docs
- http://52.78.38.133:8080/swagger-ui/index.html

## 관계

- 구현: [[챗봇 시스템 구현]]
- 코드근거: [[GitHub 챗봇 개발 근거]]
- 산출: [[최종 산출물]]
- 데이터: [[데이터 링크 정리]]
