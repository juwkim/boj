# [Gold III] DFS 스페셜 저지 - 16964 

[문제 링크](https://www.acmicpc.net/problem/16964) 

### 성능 요약

메모리: 162292 KB, 시간: 504 ms

### 분류

자료 구조, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 정렬

### 제출 일자

2024년 5월 28일 00:53:59

### 문제 설명

<p>BOJ에서 정답이 여러가지인 경우에는 스페셜 저지를 사용한다. 스페셜 저지는 유저가 출력한 답을 검증하는 코드를 통해서 정답 유무를 결정하는 방식이다. 오늘은 스페셜 저지 코드를 하나 만들어보려고 한다.</p>

<p>정점의 개수가 N이고, 정점에 1부터 N까지 번호가 매겨져있는 양방향 그래프가 있을 때, DFS 알고리즘은 다음과 같은 형태로 이루어져 있다.</p>

<div><div id="highlighter_228404" class="syntaxhighlighter  c"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="c keyword bold">void</code> <code class="c plain">dfs(</code><code class="c color1 bold">int</code> <code class="c plain">x) {</code></div><div class="line number2 index1 alt1"><code class="c spaces">    </code><code class="c keyword bold">if</code> <code class="c plain">(check[x] == </code><code class="c keyword bold">true</code><code class="c plain">) {</code></div><div class="line number3 index2 alt2"><code class="c spaces">        </code><code class="c keyword bold">return</code><code class="c plain">;</code></div><div class="line number4 index3 alt1"><code class="c spaces">    </code><code class="c plain">}</code></div><div class="line number5 index4 alt2"><code class="c spaces">    </code><code class="c plain">check[x] = </code><code class="c keyword bold">true</code><code class="c plain">;</code></div><div class="line number6 index5 alt1"><code class="c spaces">    </code><code class="c comments">// x를 방문</code></div><div class="line number7 index6 alt2"><code class="c spaces">    </code><code class="c keyword bold">for</code> <code class="c plain">(</code><code class="c color1 bold">int</code> <code class="c plain">y : x와 인접한 정점) {</code></div><div class="line number8 index7 alt1"><code class="c spaces">        </code><code class="c keyword bold">if</code> <code class="c plain">(check[y] == </code><code class="c keyword bold">false</code><code class="c plain">) {</code></div><div class="line number9 index8 alt2"><code class="c spaces">            </code><code class="c plain">dfs(y);</code></div><div class="line number10 index9 alt1"><code class="c spaces">        </code><code class="c plain">}</code></div><div class="line number11 index10 alt2"><code class="c spaces">    </code><code class="c plain">}</code></div><div class="line number12 index11 alt1"><code class="c plain">}</code></div></div></td></tr></tbody></table></div></div>

<p>이 문제에서 시작 정점은 1이기 때문에 가장 처음에 호출하는 함수는 <code>dfs(1)</code>이다. DFS 방문 순서는 <code>dfs</code>함수에서 <code>// x를 방문</code> 이라고 적힌 곳에 도착한 정점 번호를 순서대로 나열한 것이다.</p>

<p>트리가 주어졌을 때, 올바른 DFS 방문 순서인지 구해보자.</p>

### 입력 

 <p>첫째 줄에 정점의 수 N(2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에는 트리의 간선 정보가 주어진다. 마지막 줄에는 DFS 방문 순서가 주어진다. DFS 방문 순서는 항상 N개의 정수로 이루어져 있으며, 1부터 N까지 자연수가 한 번씩 등장한다.</p>

### 출력 

 <p>입력으로 주어진 DFS 방문 순서가 올바른 순서면 1, 아니면 0을 출력한다.</p>

