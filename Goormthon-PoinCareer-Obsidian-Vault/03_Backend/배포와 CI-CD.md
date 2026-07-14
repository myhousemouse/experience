# 배포와 CI-CD

태그: #deployment #docker #aws #github-actions

## 배포 방향

EC2 환경에서 Docker 기반으로 백엔드 서버를 띄우는 방식으로 배포를 진행했다. 본인은 배포 전체를 주도하기보다는 Dockerfile 작성, env 작성, Docker 실행 환경 세팅 후 팀에 전달하는 방식으로 기여했다.

## 사용 도구

- AWS EC2
- Docker
- Docker Compose
- GitHub Actions
- Nginx
- MySQL
- Redis

## 코드 기준 DB 확인

코드 기준 최종 DB는 MySQL이다.

- `application.yml`: `MYSQL_URL`, `MYSQL_USERNAME`, `MYSQL_PASSWORD` 사용
- JDBC driver: `com.mysql.cj.jdbc.Driver`
- Hibernate dialect: `org.hibernate.dialect.MySQL8Dialect`
- `build.gradle`: `com.mysql:mysql-connector-j` 의존성 사용

`docker-compose.yml`에는 Redis 컨테이너 설정만 존재한다. 따라서 docker-compose에서 확인되는 컨테이너는 DB가 아니라 Redis이며, 서비스 DB 기준은 MySQL로 정리한다.

## 마주한 문제

- 환경 변수 주입 문제
- 3306, 8080 포트 충돌
- EC2 권한 문제
- Docker 실행 권한
- GitHub Actions 실행 권한
- `gradlew` 실행 권한
- 로컬과 서버 환경 차이

## 참여 방식

- Dockerfile을 추가했다.
- env 파일을 작성했다.
- Docker로 서버를 띄우기 위한 실행 환경을 세팅했다.
- 세팅한 환경을 팀에 전달해 배포 과정에 연결했다.
- 배포 전체를 주도한 것은 아니며, 팀 배포 과정에서 보조 역할을 수행했다.
- 환경 변수, 포트, 권한, GitHub Actions 등은 팀 단위로 함께 확인한 이슈로 정리한다.

## 경험의 의미

이 경험은 백엔드 개발을 API 구현에서 끝내지 않고, 실제 시연 가능한 서버 환경까지 연결해본 경험이라는 점에서 중요하다. 다만 면접에서는 배포를 혼자 주도했다고 말하기보다, `Dockerfile과 env를 작성하고 Docker 실행 환경을 세팅해 팀에 전달했으며, 이후 팀 배포 과정을 보조했다`고 말하는 것이 정확하다.
