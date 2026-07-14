# ERD와 데이터 모델링

태그: #erd #database #jpa

## 핵심 엔티티

- User
- EmailAuth
- Point
- Recruit
- Category
- PointCategory
- RecruitCategory
- UserCategory
- PointBookmark
- RecruitBookmark

## 개인 기여

ERD는 팀원 1명과 함께 작업했고, 본인 기여도는 약 50%로 정리한다.

원본: https://app.notion.com/p/ERD-0fe3eee3a70483b08e5901ca2c74e887?source=copy_link

## 관계 설계

- User와 EmailAuth는 이메일 인증 흐름을 위해 1:1 관계로 연결된다.
- User는 관심 카테고리를 여러 개 가질 수 있다.
- Point와 Recruit은 Category와 N:M 관계로 연결된다.
- PointBookmark, RecruitBookmark는 사용자별 북마크 상태를 관리한다.

## 설계 의도

카테고리/태그 구조를 공통화한 이유는 포인트 활동과 채용 공고, 사용자 관심사를 같은 기준으로 연결하기 위해서다. 이 구조 덕분에 다음 기능이 가능해졌다.

- 관심 분야 기반 추천
- 태그 클릭 기반 필터링
- 포인트 활동과 채용 공고의 공통 분류
- 사용자별 북마크 토글
- 향후 추천 모델이나 데이터 분석으로 확장

## 면접에서 강조할 지점

단순히 테이블을 만든 것이 아니라, 추천과 필터링을 고려해 N:M 구조를 설계했다는 점이 중요하다. 특히 포인트 활동과 채용 공고가 서로 다른 도메인이지만 카테고리 기준으로 묶인다는 점이 제품 기능과 DB 설계가 연결되는 지점이다.

면접에서는 `ERD를 팀원 1명과 함께 절반 정도 담당했고, 추천/필터링 기능을 고려해 User-Point-Recruit-Category-Bookmark 관계를 구조화했다`고 말하는 것이 가장 정확하다.
