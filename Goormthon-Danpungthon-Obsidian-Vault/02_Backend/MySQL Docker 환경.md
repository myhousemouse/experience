# MySQL Docker 환경

## 목적

팀원들이 동일한 DB 환경에서 개발할 수 있도록 MySQL을 Docker Compose로 띄우는 가이드를 만들었다.

## 코드 기준 설정

- DBMS: MySQL 8.0
- 컨테이너명: `dreambus-mysql`
- DB: `dreambus`
- 포트: 로컬 `3308` -> 컨테이너 `3306`
- 사용자: `app`
- Spring datasource: `jdbc:mysql://${DB_HOST:localhost}:${DB_PORT:3308}/${DB_NAME:dreambus}`

## 관련 파일

- `docker-compose.yml`
- `application.yml`
- `Dockerfile`

## Dockerfile 역할

- Gradle/JDK17 빌드 스테이지에서 `bootJar` 생성
- Eclipse Temurin 17 JRE 런타임 이미지에서 앱 실행
- Render 등 외부 배포 환경에서 주입되는 `PORT`를 `server.port`로 연결

## 출처

- MySQL 도커 가이드: https://app.notion.com/p/2a93eee3a704814f9c15fdc7d6183d37
- GitHub 저장소: https://github.com/9oormthon-univ/2025_SEASONTHON_TEAM_26_BE

## 연결

- `supports` [[02_Backend/백엔드 역할 정리]]
- `evidenced_by` [[02_Backend/GitHub 코드 근거]]
