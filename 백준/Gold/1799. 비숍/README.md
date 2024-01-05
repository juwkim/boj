# [Gold I] 비숍 - 1799 

[문제 링크](https://www.acmicpc.net/problem/1799) 

### 성능 요약

메모리: 110864 KB, 시간: 128 ms

### 분류

백트래킹

### 제출 일자

2024년 1월 6일 04:10:03

### 문제 설명

<p>서양 장기인 체스에는 대각선 방향으로 움직일 수 있는 비숍(bishop)이 있다. < 그림 1 >과 같은 정사각형 체스판 위에 B라고 표시된 곳에 비숍이 있을 때 비숍은 대각선 방향으로 움직여 O로 표시된 칸에 있는 다른 말을 잡을 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c3f4ac55-3e37-4bed-a381-7d407b2f9b4f/-/preview/" style="width: 211px; height: 212px;"></p>

<p style="text-align: center;">< 그림 1 ></p>

<p>그런데 체스판 위에는 비숍이 놓일 수 없는 곳이 있다. < 그림 2 >에서 체스판에 색칠된 부분은 비숍이 놓일 수 없다고 하자. 이와 같은 체스판에 서로가 서로를 잡을 수 없도록 하면서 비숍을 놓는다면 < 그림 3 >과 같이 최대 7개의 비숍을 놓을 수 있다.  색칠된 부분에는 비숍이 놓일 수 없지만 지나갈 수는 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3d44f5a2-bd28-41bd-9959-0f8f8bfbff3f/-/preview/" style="width: 176px; height: 174px;"></p>

<p style="text-align: center;">< 그림 2 ></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/49405f78-09c9-4220-8687-ec3269dd6c1b/-/preview/" style="width: 176px; height: 174px;"></p>

<p style="text-align: center;">< 그림 3 ></p>

<p>정사각형 체스판의 한 변에 놓인 칸의 개수를 체스판의 크기라고 한다. 체스판의 크기와 체스판 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 주어질 때, 서로가 서로를 잡을 수 없는 위치에 놓을 수 있는 비숍의 최대 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 체스판의 크기가 주어진다. 체스판의 크기는 10이하의 자연수이다. 둘째 줄부터 아래의 예와 같이 체스판의 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 체스판 한 줄 단위로 한 줄씩 주어진다. 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0이 빈칸을 사이에 두고 주어진다.</p>

### 출력 

 <p>첫째 줄에 주어진 체스판 위에 놓을 수 있는 비숍의 최대 개수를 출력한다.</p>

