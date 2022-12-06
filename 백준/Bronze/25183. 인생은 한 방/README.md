# [Bronze I] 인생은 한 방 - 25183 

[문제 링크](https://www.acmicpc.net/problem/25183) 

### 성능 요약

메모리: 37764 KB, 시간: 104 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>재형이는 인생 역전을 위해 오늘도 로또를 샀다. 로또를 구매하면 알파벳 대문자 $N$개가 일렬로 적힌 문자열이 주어진다.</p>

<p>로또에 당첨되기 위해선 인접한 문자가 모두 사전상에서 이웃한, 길이 $5$ 이상의 부분 문자열이 로또 문자열에 존재해야 한다.</p>

<p>예를 들어 'C'와 사전상에서 이웃한 문자는 'B'와 'D'이고, 'Z'와 이웃한 문자는 'Y' 하나이며, 자기 자신과는 이웃하지 않는다. </p>

<p>따라서, 로또 문자열이 "<strong>ABCDE</strong>", "ASG<strong>XYZYX</strong>E", "W<strong>EFGHIJK</strong>A"인 경우는 당첨이고, "ABCDF", "CXYZAB", "AAAAA"는 당첨되지 않은 경우이다.  </p>

<p>알파벳 대문자 $N$개로 이루어진 문자열이 주어질 때, 로또에 당첨되었는지를 구해보자.</p>

### 입력 

 <p>첫째 줄에 로또 문자열의 길이 $N(5 \leq N \leq 100\,000)$이 주어진다. </p>

<p>둘째 줄에 로또 문자열 $S$가 주어진다. </p>

### 출력 

 <p>로또에 당첨된 경우라면 <span style="color:#e74c3c;"><code>YES</code></span>를, 아니면 <span style="color:#e74c3c;"><code>NO</code></span>를 출력한다.</p>

