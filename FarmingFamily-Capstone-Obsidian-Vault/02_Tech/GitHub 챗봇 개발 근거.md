# GitHub 챗봇 개발 근거

태그: #github #chatbot #fastapi #langgraph #rag #code-evidence

## 기준 저장소

- GitHub 조직: https://github.com/KSEB-AI-3
- AI 챗봇 서버: https://github.com/KSEB-AI-3/gardendoctor_ai-server
- 백엔드 서버: https://github.com/KSEB-AI-3/gardendoctor-backend
- 앱: https://github.com/KSEB-AI-3/gardendoctor-app

챗봇 개발 근거는 `gardendoctor_ai-server` 저장소를 기준으로 정리한다. 이 저장소의 설명은 `chat-bot`이며, 주 언어는 Python이다.

## 본인 계정

- GitHub 계정: `myhousemouse`
- 커밋 작성자: `eunji <rkvpd1@naver.com>`

`myhousemouse`는 남은지 본인 GitHub 계정이다.

## 확인된 본인 커밋

### 1. 농업 AI 챗봇 프로젝트 초기 구현

커밋: `1232ed0f3d501a998f5a1a39c897d0efee41098b`  
메시지: `Initial commit: 농업 AI 챗봇 프로젝트 추가`

커밋 메시지에 명시된 범위:

- FastAPI 챗봇 서버 구현
- LangGraph Agent React 구조
- 벡터 DB(FAISS) 통합
- 농진청 API 연동
- 농업 전문 지식 fallback 시스템

추가된 주요 파일:

- `chat_server.py`
- `langgraph_agent_react.py`
- `embeddings/build_vector_db.py`
- `embeddings/docs/Kmelon.pdf`
- `embeddings/docs/straw.pdf`
- `requirements.txt`
- `.gitignore`
- `.gitattributes`

### 2. CORS 및 실행 의존성 보강

커밋: `410a3c9a2bda5883774a0cbb28ff7fb7b69d4f48`  
메시지: `feat:CORSadd`

변경 범위:

- `chat_server.py`: FastAPI CORS middleware 추가
- `requirements.txt`: FastAPI, LangChain, LangGraph, OpenAI, FAISS, sentence-transformers, Tavily, PyMuPDF 등 의존성 버전 정리

의미:

- Flutter/프론트엔드에서 AI 서버를 호출할 수 있도록 API 서버 연동 조건을 보강했다.
- 실행 환경 재현성을 높이기 위해 requirements를 구체화했다.

### 3. 챗봇 세션 기능 개선

커밋: `ff14926c7054fe0461da1fc90aed6cfc5867b562`  
메시지: `챗봇 개선`

변경 범위:

- `chat_server.py`: 챗봇 세션 목록 조회, 특정 세션 조회, 세션 삭제, 세션 기반 대화 API 추가
- `database.py`: `ChatSession`, `ChatMessage` 테이블 추가
- `models.py`: `ChatRequest`, `ChatSessionResponse`, `ChatSessionWithMessages`, `ChatMessage` 모델 추가

의미:

- 단발성 `/api/chat` 응답에서 대화 세션을 저장하고 이어갈 수 있는 구조로 확장했다.
- 이전 대화 히스토리를 현재 질문과 함께 agent에 전달해, 맥락 기반 응답이 가능하도록 설계했다.

## 코드 기준 핵심 구현

### FastAPI 챗봇 API

파일: `chat_server.py`

주요 기능:

- `POST /api/chat`: 챗봇과 대화하기
- `GET /api/chat/sessions`: 챗봇 대화 세션 목록 조회
- `GET /api/chat/sessions/{session_id}`: 특정 세션 메시지 조회
- `DELETE /api/chat/sessions/{session_id}`: 세션 삭제
- CORS middleware 설정
- AI 응답 생성 실패 시 rollback 및 예외 처리

### LangGraph/ReAct Agent

파일: `langgraph_agent_react.py`

도구:

- `direct_answer`: 일반 작물 재배/상식 질문에 GPT 직접 답변
- `knowledge_db`: 전문 PDF/농사로 데이터 기반 RAG 검색
- `web_search`: 실시간 날씨/기온/뉴스 등 웹검색

구조:

- `Tool` 기반 기능 분리
- `AgentType.OPENAI_FUNCTIONS` 기반 agent 구성
- `StateGraph`로 agent 실행 노드 구성
- FastAPI에서 호출 가능한 `run_agent(query)` 함수 제공

### RAG/벡터 DB 구축

파일: `embeddings/build_vector_db.py`

구현 흐름:

1. PDF 문서 로드
2. 농진청 병해충 발생정보 API 호출
3. 병해충 PDF 다운로드
4. PyMuPDF 기반 텍스트 추출
5. RecursiveCharacterTextSplitter로 청크 분할
6. Hugging Face `sentence-transformers/all-MiniLM-L6-v2` 임베딩 생성
7. FAISS 벡터스토어 저장

## 면접에서 쓸 수 있는 표현

`기획 담당이었지만 챗봇이 병해충 진단 이후 사용자의 2차 질문을 처리하는 핵심 접점이라고 판단해 Python/FastAPI 기반 AI 서버를 직접 구현했습니다. GitHub 기준으로 FastAPI 챗봇 서버, LangGraph ReAct agent, FAISS 기반 RAG, 농진청 API 연동, 농업 전문 fallback, CORS 설정, 챗봇 세션 저장/조회/삭제 API 구현 근거가 확인됩니다.`

## 포지셔닝

### AI/AX

- 질문 유형별로 GPT 직접 답변, 전문 DB 검색, 웹검색을 분기한 에이전트형 UX 설계
- RAG와 fallback을 함께 사용해 농업 도메인 답변 신뢰도 보강

### 백엔드/개발

- FastAPI 서버 구현
- API 엔드포인트 설계
- CORS와 requirements 정리
- SQLite/SQLAlchemy 기반 챗봇 세션 저장 구조 구현

### PM/서비스 기획

- 병해충 진단 이후 2차 질문 니즈를 제품 핵심 흐름으로 정의
- 챗봇을 부가 기능이 아니라 진단 후 상담 경험을 완성하는 핵심 기능으로 판단
