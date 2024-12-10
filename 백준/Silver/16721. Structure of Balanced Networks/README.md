# [Silver II] Structure of Balanced Networks - 16721 

[문제 링크](https://www.acmicpc.net/problem/16721) 

### 성능 요약

메모리: 135888 KB, 시간: 576 ms

### 분류

구현

### 제출 일자

2024년 12월 11일 04:36:09

### 문제 설명

<p><strong>Structure of Balanced Networks</strong>란 <strong>Complete Signed Graph</strong>(모든 노드 사이에 간선이 존재하고, 각 간선에 부호가 부여된 그래프)에서 모든 ① <strong>triad</strong>가 ② <strong>balance</strong>된 상태를 뜻한다. 여기서 각 용어의 정의는 다음과 같다.</p>

<ol>
	<li>triad : 그래프 상의 임의의 노드 3개를 선택했을 때 형성되는 삼각형</li>
	<li>balance : 아래의 그림 중 (a), (c)의 상태</li>
</ol>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/51c0e31b-5b56-44b9-89fe-a838cded92a5/-/preview/"></p>

<ol style="list-style-type: lower-alpha;">
	<li>모든 관계가 +이므로 전부 친구 관계가 되어 balance 상태</li>
	<li>B와 C가 A라는 공동의 친구를 가지고 있는 상태, 이 경우 A가 B와 C를 화해시키거나(상태 (a)로 바뀜) B와 C가 서로 A와의 관계를 이간질 시킴(상태 (c)로 바뀜)</li>
	<li>A와 B가 C라는 공동의 적을 가지고 있어서 balance 상태</li>
	<li>관계가 -이지만, 세 사람 중에 제일 싫어하는 사람을 상대하기 위해 임시적 동맹을 맺음(상태 (c)로 바뀜)</li>
</ol>

<p>다음은 balance된 예시와, balance하지 않은 예시이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7cb3852e-9f23-4f42-b0c9-8ebe838dd9d3/-/preview/"></p>

<p>일방적인 관계는 없다. 즉, A와 B의 관계는 B와 A의 관계이다.</p>

<p>Structure of Balanced Networks와 임의의 두 노드 B, C가 여러 번 주어졌을 때, 각각의 B와 C의 관계의 부호를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 노드의 개수 n(3 ≤ n ≤ 5000)가 주어진다.</p>

<p>둘째 줄부터 n줄 동안 각 줄마다 n개의 노드의 관계가 주어진다.  i+1번째 줄의 j번째 문자가 ‘ + ’ 일 경우 친구, ' - ' 일 경우 적, ' 0 '은 자기 자신을 뜻한다.</p>

<p>그 다음 줄에는 질의의 개수 m(1 ≤ m ≤ 100)이 주어진다.</p>

<p>다음 m줄 동안 노드 B의 번호 b(0 ≤ b < n), 노드 C의 번호 c(0 ≤ c < n)가 주어진다.</p>

<p>각 노드는 0부터 n-1까지의 수로 표현되고 B, C는 서로 다른 노드 번호로 주어진다.</p>

### 출력 

 <p>m줄동안 B와 C의 관계를 출력한다.</p>

