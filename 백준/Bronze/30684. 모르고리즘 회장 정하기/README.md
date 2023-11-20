# [Bronze III] 모르고리즘 회장 정하기 - 30684 

[문제 링크](https://www.acmicpc.net/problem/30684) 

### 성능 요약

메모리: 115580 KB, 시간: 180 ms

### 분류

정렬, 문자열

### 제출 일자

2023년 11월 20일 12:15:59

### 문제 설명

<p>모르고리즘 회장 태윤이는 2024년 모르고리즘을 이끌어갈 회장을 고르려고 한다. 태윤이가 회장을 직접 고르는 이유는 아무도 회장을 맡고 싶어 하지 않기 때문이다. 따라서 태윤이는 이름이 세 글자인 사람 중에서, 사전 순으로 가장 앞선 사람을 회장으로 뽑으려고 한다.</p>

<p>사람들의 이름은 모두 서로 다르고, 길이가 $2$ 이상 $5$ 이하인 알파벳 대문자 <span style="color:#e74c3c;"><code>A</code></span> - <span style="color:#e74c3c;"><code>Z</code></span>로 이루어져 있다.</p>

<p>이름 $S$가 이름 $T$에 비해 사전 순으로 앞선다는 것은 아래 두 조건 중 하나가 성립하는 것과 동치이다. 이때 $\lvert S \rvert$는 $S$의 길이이고, $S[i]$는 $S$의 $i$번째 문자를 의미한다.</p>

<ul>
	<li>$S$가 $T$의 접두사이다. 즉, $\lvert S \rvert < \lvert T \rvert$이고, 모든 $1 \leq i \leq \lvert S \rvert$에 대해 $S[i] = T[i]$이다.</li>
	<li>처음으로 $S[i] \neq T[i]$인 $i$에 대해 $S[i] < T[i]$이다. ($1 \leq i \leq \min(\lvert S \rvert, \lvert T \rvert)$)</li>
</ul>

<p>어떤 사람이 회장으로 선정될지 결과를 예측해 보자.</p>

### 입력 

 <p>입력은 다음과 같이 주어진다.</p>

<div style="background:#eeeeee;border:1px solid #cccccc;padding:5px 10px;">
<p>$N$</p>

<p>$name_1$</p>

<p>$name_2$</p>

<p>$\cdots$</p>

<p>$name_{N-1}$</p>

<p>$name_N$</p>
</div>

<p>첫째 줄에 사람의 수 $N$이 주어진다.</p>

<p>이어 $N$줄에 걸쳐 사람들의 이름 $name_i$가 주어진다.</p>

### 출력 

 <p>회장으로 뽑힐 사람을 출력한다.</p>

