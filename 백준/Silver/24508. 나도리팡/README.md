# [Silver I] 나도리팡 - 24508 

[문제 링크](https://www.acmicpc.net/problem/24508) 

### 성능 요약

메모리: 42028 KB, 시간: 176 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting), 두 포인터(two_pointer)

### 문제 설명

<p>나도리는 귀여운 노란색 공 모양 캐릭터이다. 나도리는 바구니에 들어가 있는 것을 좋아한다.</p>

<p style="text-align: center;"><img alt="귀여운 나도리" src="" style="max-height:100px; object-fit:contain; display:inline-block;"></p>

<p style="text-align: center;"><strong>[그림] 나도리</strong></p>

<p>하지만 나도리에게는 최근 슬픈 일이 생겼다. 왜냐하면 나도리 $K$ 마리가 한 바구니에 모인다면 빡! 하고 터져버리는 무서운 저주에 걸렸기 때문이다.</p>

<p style="text-align: center;"><img alt="귀여운 나도리" src="" style="max-height:100px; object-fit:contain; display:inline-block;"></p>

<p style="text-align: center;"><strong>[그림] 슬픈 나도리</strong></p>

<p>현재 $N$ 개의 바구니가 있고, $i$ 번째 바구니에는 나도리가 $A_i$ 마리 담겨 있다. 프즈슈와는 나도리를 괴롭히는 것을 좋아하기 때문에, 한 바구니에 있는 나도리 한 마리를 다른 바구니로 옮기는 행동을 최대 $T$ 회 반복하여 모든 나도리들을 터트릴 수 있는지 알고 싶다. 바구니의 개수가 많아 쉽사리 계산하지 못 하고 있는 그를 위해 대신 답을 구해서 알려주자.</p>

### 입력 

 <p>첫 번째 줄에는 정수 $N$, $K$, $T$ 가 공백을 사이에 두고 주어진다. ($2 \le N, K \le 10^5$, $0 \le T \le 10^9$)</p>

<p>두 번째 줄에는 정수 $A_1, A_2, \cdots, A_N$ 이 공백을 사이에 두고 주어진다. ($0 \le A_1, A_2, \cdots, A_N \lt K$)</p>

### 출력 

 <p>$T$ 회 이하로 나도리를 옮겨 모두 터트리는 것이 가능하다면 <code>YES</code>를, 불가능하다면 <code>NO</code> 를 첫째 줄에 출력한다.</p>

