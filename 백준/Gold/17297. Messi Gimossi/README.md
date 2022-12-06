# [Gold III] Messi Gimossi - 17297 

[문제 링크](https://www.acmicpc.net/problem/17297) 

### 성능 요약

메모리: 32904 KB, 시간: 76 ms

### 분류

분할 정복(divide_and_conquer), 다이나믹 프로그래밍(dp)

### 문제 설명

<p><a href="https://www.acmicpc.net/user/messi">메시</a>는 축구 선수이다. 메시는 기분이 좋다.</p>

<p>messi(1): <em>Messi</em></p>

<p>messi(2)​​: <em>Messi Gimossi</em></p>

<p>messi(3)​​​​​​: <em>Messi Gimossi Messi</em></p>

<p>messi(4): <em>Messi Gimossi Messi Messi Gimossi</em></p>

<p>messi(5): <em>Messi Gimossi Messi Messi Gimossi</em> <em>Messi Gimossi Messi</em></p>

<p>메시의 외침은 피보나치 수열과 유사하게 정의된다. messi(N)은 messi(N-1), 공백, messi(N-2)을 차례로 이어붙여서 만든 문자열이다.</p>

<p>욱제는 N이 충분히 클 때, messi(N)의 M번째 글자가 뭔지 궁금해졌다.</p>

### 입력 

 <p>정수 M이 주어진다. (1 ≤ M ≤ 2<sup>30</sup>-1)</p>

### 출력 

 <p>N이 충분히 클 때, messi(N)의 M번째 글자가 공백(' ')이 아닐 경우에는 그 글자를 출력한다.</p>

<p>M번째 글자가 공백(' ')일 경우에는 <em>Messi Messi Gimossi</em>를 출력한다.</p>

<p>정답은 <strong>대소문자를 구분</strong>하므로 출력에 주의한다.</p>

