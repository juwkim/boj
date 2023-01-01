# [Gold V] 파이프 옮기기 1 - 17070 

[문제 링크](https://www.acmicpc.net/problem/17070) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍(dp), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.</p>

<p>오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3ceac594-87df-487d-9152-c532f7136e1e/-/preview/" style="width: 138px; height: 70px;"></p>

<p>파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b29efafa-dbae-4522-809c-76d5c184a231/-/preview/" style="width: 427px; height: 136px;"></p>

<p>파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.</p>

<p>파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.</p>

<p>파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.</p>

<p>아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0f445b26-4e5b-4169-8a1a-89c9e115907e/-/preview/" style="width: 578px; height: 203px;"></p>

<p style="text-align: center;">가로</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/045d071f-0ea2-4ab5-a8db-61c215e7e7b7/-/preview/" style="width: 579px; height: 203px;"></p>

<p style="text-align: center;">세로</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ace5e982-6a52-4982-b51d-6c33c6b742bf/-/preview/" style="width: 886px; height: 203px;"></p>

<p style="text-align: center;">대각선</p>

<p>가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.</p>

### 입력 

 <p>첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.</p>

### 출력 

 <p>첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.</p>

