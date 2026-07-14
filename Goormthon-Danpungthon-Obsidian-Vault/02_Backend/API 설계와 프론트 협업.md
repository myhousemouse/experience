# API 설계와 프론트 협업

## API 문서 기준

협업 Notion의 API 문서와 GitHub 코드 기준으로 다음 API가 정리되어 있다.

배포된 Swagger 링크는 없고, 최종 API 확인 기준은 Notion API 문서다.

- API 문서 공유 링크: https://app.notion.com/p/API-DOCS-SUBPAGE-2a93eee3a704812bacaee5fdf21c96c9?source=copy_link

## 인증

- `POST /auth/register`: 회원가입
- `POST /auth/login`: 로그인 및 JWT 발급
- `POST /auth/kakao`: 카카오 인증 코드 기반 소셜 로그인
- `POST /auth/token/refresh`: 토큰 재발급

카카오 로그인 흐름은 프론트가 인가 코드를 받은 뒤 백엔드에 전달하고, 백엔드는 카카오 토큰 발급/사용자 정보 조회/서비스 JWT 발급을 처리하는 구조로 문서화되어 있다.

## 신청

- `POST /applications`: 버스 이용 신청
- `GET /applications/summary`: 지역/날짜 기준 신청 인원, 정원, 잔여, 충족률 제공
  - API 문서에서 체크 표시가 있는 직접 구현 기능

## 지역/노선

- `GET /regions/search`: 지역 계층 검색
- `GET /regions/{regionId}/service`: 지역과 날짜 기준 해당 노선/정류장 목록 조회
  - GitHub 커밋 기준 구현 근거 확인

## 정류장/버스

- `GET /stops/nearest`: 현재 위치 기준 가장 가까운 정류장
  - API 문서에서 체크 표시가 있는 직접 구현 기능
- `GET /stops/{stopId}`: 마커 선택 시 정류장 상세 모달
  - API 문서에서 체크 표시가 있는 직접 구현 기능
- `GET /courses/{courseId}/live`: 코스별 실시간 버스 상태, 현재/다음 정류장, ETA, 정차 잔여 시간
  - GitHub 커밋 기준 구현 근거 확인

## 프론트 협업에서 중요했던 지점

- 정류장 모달은 기본 진입 시 가장 가까운 정류장, 마커 선택 시 특정 정류장 상세로 분리
- 실시간 버스 정보는 정류장 단위가 아니라 코스 단위 조회로 정리
- 정차 중이면 현재 정류장, 도착 시간, 잔여 이용 시간을 반환
- 이동 중이면 다음 정류장, 도착 시간을 반환하고 잔여 정차 시간은 비워둠
- Swagger만으로 어려울 수 있어 Notion API 문서도 병행

## 출처

- API DOCS: https://app.notion.com/p/2a93eee3a704812bacaee5fdf21c96c9
- API DOCS 공유 링크: https://app.notion.com/p/API-DOCS-SUBPAGE-2a93eee3a704812bacaee5fdf21c96c9?source=copy_link
- 카카오 로그인 문서: https://app.notion.com/p/2a93eee3a7048101b06ad21d6a781393

## 연결

- `implemented_by` [[02_Backend/GitHub 코드 근거]]
- `decided_by` [[03_Collaboration/팀 협업 구조와 회의]]
