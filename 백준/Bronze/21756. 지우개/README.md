# [Bronze II] 지우개 - 21756 

[문제 링크](https://www.acmicpc.net/problem/21756) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>$N$개의 칸에 $1$ 부터 $N$ 까지의 수들이 왼쪽부터 순서대로 저장되어 있다. 또, 각 칸은 왼쪽부터 $1$ 부터 $N$까지 순서대로 번호가 붙어 있다. 즉, 처음에는 각 칸의 번호와 각 칸에 저장된 수가 같다.</p>

<p>아래 그림은 $N = 7$일 때의 예이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 361px; height: 90px;"></p>

<p>다음 작업을 수가 정확히 하나가 남을 때 까지 반복한다.</p>

<p>(A) 홀수번 칸의 수들을 모두 지운다 (B) 남은 수들을 왼쪽으로 모은다.</p>

<p>제일 첫 작업의 (A) 단계가 끝나면 칸들의 상태는 다음과 같을 것이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 361px; height: 90px;"></p>

<p>(B) 단계가 끝나면 다음과 같을 것이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 361px; height: 90px;"></p>

<p>두번째 작업이 진행되면 칸들은 아래 두 그림과 같이 바뀔 것이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 361px; height: 90px;"></p>

<p style="text-align: center;"><img alt="" src="" style="width: 361px; height: 90px;"></p>

<p>이제 수가 하나 남았으므로 작업은 더 이상 진행되지 않는다.</p>

<p>$N$을 입력으로 받아 위와 같이 작업을 진행했을 때 마지막으로 남는 수를 계산하는 프로그램을 작성하라.</p>

### 입력 

 <p>첫 번째 줄에 정수 $N$이 주어진다.</p>

### 출력 

 <p>마지막으로 남는 수를 한 줄에 출력한다.</p>

