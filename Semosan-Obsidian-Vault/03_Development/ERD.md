# ERD

원본: https://app.notion.com/p/0df3eee3a70483c59d79816b2307ed7f
태그: #backend #erd #database

## 역할

세모산 DB 구조를 dbdiagram 형식으로 정리한 문서다.

백엔드 파트에서 객체 모델과 데이터 관계를 파악하기 위한 기준 문서다.

## 주요 도메인

- 산: `mountains`, `courses`, `mountain_images`
- 날씨: `weather_forecasts`
- 교통: `mountain_traffic_info`
- 유저: `users`
- 리뷰: `reviews`, `review_images`, `review_tag_types`, `review_tags`
- 편의시설: `facilities`
- 맛집: `restaurant_categories`, `restaurants`, `restaurant_menus`, `mountain_restaurants`

## 주요 관계

- 산은 여러 코스와 이미지를 가진다.
- 코스와 이미지는 산 삭제 시 함께 삭제된다.
- 유저는 리뷰를 작성한다.
- 리뷰는 산과 유저에 연결된다.
- 산은 편의시설, 교통 정보, 주변 맛집과 연결된다.

## 연결

- [[Backend]]
- [[개발 데이터]]
- [[API 명세서]]
- [[기능 명세서]]

## 관계

- 데이터: 산, 코스, 유저, 리뷰, 편의시설, 맛집 등 핵심 객체 모델과 관계
- 구현: [[API 명세서]]의 요청/응답과 백엔드 도메인 설계의 기반
- 근거: [[기능 명세서]]와 최종 화면에서 필요한 데이터 요구사항
- 소통: [[Backend]] 내부 데이터 모델 기준
