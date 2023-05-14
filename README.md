# Python_Concurrent_Programming
Refer to Inflearn Lecture - Python Concurrent Programming

2023.04.18 ~

## Section 0
### 동시성 프로그래밍
- 클라이언트와 서버간 통신
- 시스템 디스크 파일 읽기/쓰기
- 데이터베이스 쿼리 작업
- API 사용
### 병렬성 프로그래밍
- 비디오, 오디오 또는 이미지 처리
- 컴퓨터 비전
- 머신러닝
- 딥러닝

## Section 1: Python Coroutine & Async Function
- I/O Bound & CPU Bound
- Sync & Async
- Coroutine

## Section 2: Python Multithreading & Multiprocessing
- Understanding Computer Organization and Basic of OS
- Concurrency & Parallelism
  - Concurrency: 한 번에 여러 작업을 동시에 다루는 것을 의미 - 스위칭을 하며 작업을 동시에 다룸
      (ex. 요리사 한 명이 요리 3개를 동시에 요리) 
      동시성은 논리적 개념으로 멀티 스레딩에서 사용되기도 하고 싱글 스레드에서 사용되기도 합니다.
      또한 싱글 코어 뿐만 아니라 멀티 코어에서도 각각의 코어가 동시성을 사용할 수 있습니다.
  - Parallelism: 한 번에 여러 작업을 병렬적으로 처리하는 것을 의미 (at the same time)
      (ex. 요리사 세 명이 각각 요리 1개씩 요리)
  - WEB -> MultiThreading
  - CPU related (simple calculation) -> MultiProcessing

## Section 3: Data Collecting using Concurrent Programming

## Section 4: Understanding MongoDB

## Section 5: Actual Project (Fast API)

## Section 6: AWS Cloud Computing (Distributing Project)
