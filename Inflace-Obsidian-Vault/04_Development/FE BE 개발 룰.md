# FE BE 개발 룰

원본: https://app.notion.com/p/dea3eee3a704829989a5016eb07e3bd3
태그: #development #frontend #backend #api #collaboration

## 역할

프론트엔드와 백엔드 개발 일관성을 확보하고 협업 비용을 줄이기 위한 개발 규칙 문서다.

## 주요 기준

- API path: `api/v1/{domain}/{feature}`
- HTTP 메서드 기준: GET, POST, PUT, PATCH, DELETE 역할 구분
- 에러 코드: 도메인 full name + HTTP status
- 인증: JWT Access Token + Refresh Token
- 토큰 전달: `Authorization: Bearer {accessToken}`
- 응답 형식: 공통 Response Wrapper 사용
- JSON 필드명: `camelCase`
- URL path: `kebab-case`
- 빈 배열은 `[]`, 없는 값은 `null`
- 페이지네이션은 커서 기반을 기본으로 사용

## API 협업 프로세스

```text
기획 확정
-> BE API 인터페이스 정의
-> FE/BE 합의
-> FE MSW 또는 Mock 병렬 개발
-> BE 구현 완료 후 Swagger 업데이트와 공유
-> 통합 테스트
```

## 관계

- 근거: [[PRD]], [[기능명세서]]
- 구현: [[API 기본 명세서]]
- 운영: API 스펙 변경은 Slack과 Swagger로 공유
- 소통: FE/BE 사이의 요청, 응답, 변경 공유 기준
- 검증: [[QA시트]]
