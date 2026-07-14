# GitHub 코드 근거

태그: #github #code-evidence #backend

## 기준 저장소

- GitHub 조직: https://github.com/PointCareer
- 백엔드 저장소: https://github.com/PointCareer/Server
- 저장소 설명: 경기대생을 위한 맞춤형 포인트 관리 & 교내 추천 채용 정보 서비스
- 언어: Java

## 기여자 기준

GitHub contributors 기준으로 백엔드 저장소에는 다음 계정들이 확인된다.

- `sunkong25`
- `CommonLion`
- `myhousemouse`

`myhousemouse`는 남은지 본인 GitHub 계정이다. 따라서 이 문서는 `myhousemouse` 커밋을 본인 코드 근거로 정리한다.

## myhousemouse 커밋 기준 확인된 작업

### Recruit, Mypage 기능 추가

커밋: `26955a1`  
메시지: `Recruit, Mypage 기능 추가`

변경 범위:

- `RecruitController`
- `RecruitService`
- `RecruitServiceImpl`
- `RecruitRepository`
- `RecruitListResponse`
- `RecruitDetailResponse`
- `Recruit`
- `RecruitType`
- `MyPageController`
- `MyPageService`
- `MyPageRepository`
- `MyPageResponse`
- `UserProfileResponse`
- `UserProfileUpdateRequest`
- `UserProfileUpdateResponse`
- `BookmarkServiceImpl`
- `PointBookmarkRepository`
- `RecruitBookmarkRepository`

### 프로필 수정 기능 수정

커밋: `44f6809`  
메시지: `프로필 수정 기능 수정`

변경 범위:

- `MyPageController`
- `MyPageService`

### Entity/Category 구조 수정

커밋: `ff080be`, `6d8789a`, `c67c552`, `7d3d9ee`

확인된 변경:

- `Point`, `Recruit`, `User` Entity 수정
- `PointBookmark`, `RecruitBookmark` Entity 수정
- `Category`, `CategoryName`, `CategoryType` 추가/이동
- `PointCategory`, `RecruitCategory`, `UserCategory` 추가/이동
- 기존 Tag 구조를 Category 구조로 재정리
- `BaseEntity` 추가

### Dockerfile 추가

커밋: `7689aa5`  
메시지: `Dockerfile 추가`

변경 범위:

- `Dockerfile`

## 현재 코드 기준 직접 설명 가능한 API

### 교내 추천 채용

파일:

- `domain/recruit/controller/RecruitController.java`
- `domain/recruit/service/RecruitServiceImpl.java`
- `domain/recruit/repository/RecruitRepository.java`

API:

- `GET /api/v1/recruits`: 교내 추천 채용 목록 조회
- `GET /api/v1/recruits/sort?sortType=...`: 교내 추천 채용 정렬 조회
- `GET /api/v1/recruits/{recruitId}`: 교내 추천 채용 상세 조회
- `GET /api/v1/recruits/search?keyword=...`: 채용 공고 검색

구현 로직:

- 전체 채용 공고 조회
- 최신순/마감순 정렬
- 제목/회사명 기준 검색
- 상세 조회 시 존재하지 않는 공고에 대한 예외 처리
- RecruitJob, Favorite 카테고리 매핑

### 마이페이지

파일:

- `domain/mypage/controller/MyPageController.java`
- `domain/mypage/service/MyPageService.java`
- `domain/mypage/repository/MyPageRepository.java`
- `domain/mypage/dto/*`

API:

- `GET /api/v1/users/profile`: 프로필 + 포인트 북마크 + 채용 북마크 일괄 조회
- `PUT /api/v1/users/profile`: 프로필 수정

구현 로직:

- 사용자 프로필 조회
- 포인트 북마크 목록 조회
- 채용 북마크 목록 조회
- 북마크별 카테고리 매핑
- 전공, 학년, 학기, 관심 카테고리 수정
- 존재하지 않는 사용자에 대한 예외 처리

## 면접에서 쓸 수 있는 표현

`GitHub 커밋 기준으로 교내 추천 채용 도메인의 목록/정렬/검색/상세 API와 마이페이지 프로필/북마크 조회 및 프로필 수정 API 구현에 참여했습니다. 특히 Recruit, Mypage Controller-Service-Repository-DTO 흐름을 구성했고, Category 구조를 Entity에 연결해 채용/포인트/사용자 관심사를 API 응답에 매핑했습니다.`
