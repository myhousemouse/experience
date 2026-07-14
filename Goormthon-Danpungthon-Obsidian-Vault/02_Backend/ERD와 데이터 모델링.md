# ERD와 데이터 모델링

## ERD 출처

- ERDCloud: https://www.erdcloud.com/d/gBo8Xo9WguahAigju
- 협업 Notion ERD 작업: https://app.notion.com/p/5843eee3a70483c6a2530174cc732b20

## 코드 기준 주요 도메인

### user

- `Users`
- `RefreshToken`
- 회원가입/로그인/JWT/카카오 로그인 흐름과 연결

### application

- `Applications`
- `ApplicationStatus`
- `CapacityPlan`
- 사용자의 버스 신청, 희망 도서/프로그램, 서비스 날짜, 신청 상태 저장

### region

- `Regions`
- 지역 검색과 운행 서비스 조회의 기준
- 신청 현황과 정류장 정보의 기준 데이터

### bus

- `Buses`
- `BusLive`
- `BusState`
- `Course`
- `CourseStops`
- `Stops`
- 코스, 정류장, 실시간 버스 상태를 구성

## 설계 포인트

- 신청 현황은 `Applications`의 지역/날짜 기준 count로 계산
- 정류장 검색은 `Stops` 좌표와 사용자 좌표 사이의 거리 계산으로 처리
- 실시간 버스 정보는 `BusLive`의 최신 스냅샷과 `CourseStops`의 정류장 순서를 조합해 응답
- 지역/노선 검색은 `Regions`, `Course`, `CourseStops` 연결을 통해 날짜별 운행 코스를 반환

## 연결

- `depends_on` [[02_Backend/API 설계와 프론트 협업]]
- `evidenced_by` [[02_Backend/GitHub 코드 근거]]
