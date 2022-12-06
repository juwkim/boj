# [Silver V] Trip Odometer - 24936 

[문제 링크](https://www.acmicpc.net/problem/24936) 

### 성능 요약

메모리: 128044 KB, 시간: 144 ms

### 분류

구현(implementation), 수학(math), 정렬(sorting)

### 문제 설명

<p>A trip odometer can be used to record the distance driven on a single trip. You are very diligent: at the start of each trip you reset the trip odometer to read $0$ and at the end of each trip you write down the distance travelled.</p>

<p>Thus, you maintain a list of distances (in kilometers) taken by all trips. Unfortunately, exactly one number from this list is spurious; you mistakenly recorded the length of one trip you took in another vehicle. You also forget which entry in your list corresponds to this trip.</p>

<p>You want to know all possible total distances that you could have taken in your own vehicle given that one of the written distances was fake. More specifically, all values $D$ such that it is possible to remove one trip from your list and have the remaining distances sum to $D$.</p>

### 입력 

 <p>The first line of input contains a single integer $N$ ($2≤N≤10^5$), the number of distances you wrote down. The second line of input consists of $N$ integers $d_1,d_2, \dots ,d_N$ ($1≤d_i≤10^4$), where $d_i$ is the length of the $i$th trip you recorded.</p>

### 출력 

 <p>Display two lines. The first line should contain a single number $K$, which is the number of possible distinct distances that could be obtained. The second line should contain the list of the $K$ distinct integers, each of which is a possible sum that can be obtained by removing exactly one of the written distances. The list should be displayed in ascending order.</p>

