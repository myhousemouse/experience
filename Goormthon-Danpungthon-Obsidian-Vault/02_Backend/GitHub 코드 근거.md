# GitHub 코드 근거

## 저장소

- Backend: https://github.com/9oormthon-univ/2025_SEASONTHON_TEAM_26_BE
- 계정: `myhousemouse`
- 언어/프레임워크: Java, Spring Boot

## 확인된 커밋

| 커밋 | 날짜 | 메시지 | 근거 범위 |
| --- | --- | --- | --- |
| `61ac28a` | 2025-09-01 | `first commit` | Spring Boot 프로젝트 초기 구조, application/bus/user 도메인 기본 골격 |
| `7391996` | 2025-09-03 | `[Application] 버스 신청 현황 로직 (#5)` | 신청 현황 요약 컨트롤러/서비스/DTO/Repository, Applications/Regions 연결 |
| `d3f3edc` | 2025-09-04 | `feat: [bus]가장 가까운 정류장(#7)` | 가장 가까운 정류장, 정류장 상세, 거리 계산, StopsRepository |
| `3c41832` | 2025-09-05 | `feat: [region] 지역검색&노선검색(#12)` | 지역 계층 검색, 지역별 운행 코스/정류장 조회, `regions.json` |
| `d983048` | 2025-09-05 | `fix: [region] 지역검색&노선검색 누락 레포지토리 추가 (#12)` | Course/CourseStops Repository 추가 |
| `ada0cd5` | 2025-09-05 | `fix: [bus] 가장 가까운 정류장&정류장 상세조회 dto 수정 및 swagger 예시 응답 추가 (#7)` | 정류장 API 응답 DTO 및 Swagger 예시 수정 |
| `cb8c691` | 2025-09-05 | 동일 이슈 수정 | `NearestStopResponseDto` |
| `0dafe44` | 2025-09-05 | 동일 이슈 수정 | `StopDetailResponseDto` |
| `f2fa573` | 2025-09-05 | 동일 이슈 수정 | `NearestStopController` |
| `6a7ed82` | 2025-09-05 | 동일 이슈 수정 | `NearestStopService` |
| `1ffb0c3` | 2025-09-06 | `feat: [bus] 실시간 버스 정보 (#17)` | 실시간 버스 정보 컨트롤러/서비스/DTO/Repository |

## 주요 변경 파일

### 신청 현황

- `domain/application/controller/ApplicationController.java`
- `domain/application/controller/ApplicationSummaryController.java`
- `domain/application/service/ApplicationService.java`
- `domain/application/service/ApplicationSummaryService.java`
- `domain/application/repository/ApplicationsRepository.java`
- `domain/application/dto/ApplicationSummaryResponseDto.java`

### 지역/노선

- `domain/region/controller/RegionsController.java`
- `domain/region/service/RegionsService.java`
- `domain/region/service/RegionHierarchyProvider.java`
- `domain/region/dto/RegionHierarchySearchResponseDto.java`
- `domain/region/dto/RegionServiceResponseDto.java`
- `src/main/resources/regions.json`

### 정류장/실시간 버스

- `domain/bus/controller/NearestStopController.java`
- `domain/bus/service/NearestStopService.java`
- `domain/bus/controller/BusLiveController.java`
- `domain/bus/service/BusLiveService.java`
- `domain/bus/dto/NearestStopResponseDto.java`
- `domain/bus/dto/StopDetailResponseDto.java`
- `domain/bus/dto/BusLiveResponseDto.java`

## 면접에서 말할 수 있는 기술 포인트

- 지도/정류장 UI가 필요로 하는 응답을 API 단위로 분해했다.
- 사용자 좌표 기반 가까운 정류장을 계산하고, 지도 모달에 필요한 좌표/거리/ETA/정차 시간을 함께 반환했다.
- 코스별 실시간 버스 상태를 `STOPPED`, `IN_SERVICE`, `OFFLINE`으로 판정하고 현재/다음 정류장 progress를 계산했다.
- 프론트 연동을 위해 Swagger 예시 응답과 Notion API 문서를 함께 정리했다.
- MySQL/Docker Compose 기반으로 팀 개발 환경을 맞췄다.
