# [Gold V] 진우의 달 여행 (Large) - 17485 

[문제 링크](https://www.acmicpc.net/problem/17485) 

### 성능 요약

메모리: 113696 KB, 시간: 344 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2023년 12월 29일 05:59:36

### 문제 설명

<p>우주비행이 꿈이였던 진우는 음식점 '매일매일싱싱'에서 열심히 일한 결과 달 여행에 필요한 자금을 모두 마련하였다! 지구와 우주사이는 N X M 행렬로 나타낼 수 있으며 각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양이다.</p>

<p style="text-align: center;">[예시]</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9e155c65-43ea-492b-af73-d3f9f9c9dc44/-/preview/" style="height: 353px; width: 150px;"></p>

<p>진우는 여행경비를 아끼기 위해 조금 특이한 우주선을 선택하였다. 진우가 선택한 우주선의 특징은 아래와 같다.</p>

<p><strong>1. 지구 -> 달로 가는 경우 우주선이 움직일 수 있는 방향은 아래와 같다.</strong></p>

<p><img alt="" src="https://upload.acmicpc.net/8f6fc516-9870-4ef6-8474-b5d82f7b6f21/-/preview/" style="width: 200px; height: 200px;"><img alt="" src="https://upload.acmicpc.net/eb6f87f0-f4d0-43cc-8e9d-5d94bfc41936/-/preview/" style="width: 200px; height: 200px;"><img alt="" src="https://upload.acmicpc.net/e7b501aa-c92c-4a17-aed7-c7868b89af7a/-/preview/" style="width: 200px; height: 200px;"></p>

<p><strong>2. 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다.</strong></p>

<p>진우의 목표는 <strong>연료를 최대한 아끼며 지구의 어느위치에서든 출발하여 달의 어느위치든 착륙하는 것</strong>이다.</p>

<p>최대한 돈을 아끼고 살아서 달에 도착하고 싶은 진우를 위해 달에 도달하기 위해 필요한 연료의 최소값을 계산해 주자.</p>

### 입력 

 <p>첫줄에 지구와 달 사이 공간을 나타내는 행렬의 크기를 나타내는 <strong>N, M (2 ≤ N, M ≤ 1000)</strong>이 주어진다.</p>

<p>다음 N줄 동안 각 행렬의 원소 값이 주어진다. 각 행렬의 원소값은 100 이하의 자연수이다.</p>

### 출력 

 <p>달 여행에 필요한 최소 연료의 값을 출력한다.</p>

