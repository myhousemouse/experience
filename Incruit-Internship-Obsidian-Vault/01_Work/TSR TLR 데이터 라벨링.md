# TSR TLR 데이터 라벨링

---
type: work
tags:
  - data-labeling
  - autonomous-driving
  - ai-training-data
source: https://app.notion.com/p/2463eee3a704817eb765eda61c4b475a
---

## 업무 개요

자율주행 자동차 데이터 처리 프로젝트에서 TSR과 TLR 데이터를 라벨링하고 검수했다.

- TSR: Traffic Sign Recognition, 교통 표지판 인식
- TLR: Traffic Light Recognition, 신호등 인식
- 프로젝트 구조: STRAD사 외주 프로젝트
- 처리 흐름: 원천 이미지 데이터 -> 베트남 외주사 1차 작업 -> 인크루트 데이터라벨링팀 검수/정교화 -> STRAD 전달

## 수행 내용

- 1월: TSR/TLR 매뉴얼 학습, 내부 ERP 공고 검수 프로젝트 병행
- 2월: 실제 데이터 처리 투입
- 약 3,000장 이상의 이미지 데이터 처리
- 베트남 외주사가 1차 작업한 데이터의 정확성 검수
- 신호등, 교통 표지판의 분류 기준을 매뉴얼에 맞춰 적용

## 단순 반복이 아니었던 이유

이미지마다 상황이 다르고, 국가별 표지판/신호등 형태가 달라 매뉴얼만으로 판단하기 어려운 케이스가 있었다. 따라서 단순히 정답을 찍는 작업이 아니라, 애매한 기준을 수집하고 팀과 합의해 라벨링 기준을 정교화하는 과정이 필요했다.

## 연결

- `problem` -> [[라벨링 기준 모호성 해결]]
- `result` -> [[면접용 포인트]]

