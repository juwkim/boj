# [Silver II] Reveals - 30427 

[문제 링크](https://www.acmicpc.net/problem/30427) 

### 성능 요약

메모리: 110576 KB, 시간: 104 ms

### 분류

애드 혹, 많은 조건 분기, 자료 구조, 해시를 사용한 집합과 맵, 구현

### 제출 일자

2024년 12월 11일 03:12:19

### 문제 설명

<blockquote>
<p>흐에에…</p>
</blockquote>

<p>누군가가 어둠을 틈타, 시이(<span style="color:#e74c3c;"><code>swi</code></span>)의 엄청난 케이크를 먹어버렸다!</p>

<p>시이는 케이크를 좋아하는 사람이다. 따라서, 시이는 여느 때처럼 근처의 가게에서 사 온 굉장히 엄청난 케이크를 식탁 위에 올려놓고 케이크를 감상하고 있었다. 하지만 방이 너무 따뜻했기 때문에 시이는 잠에 들고 말았고… 케이크는 사라져 있었다!</p>

<p>사건이 일어났을 때, 집 안에는 시이와 시이를 제외한 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>명의 다른 사람들이 있었다. 케이크를 먹은 범인은 사건이 일어났을 때 집 안에 있던 사람들 중 하나이다.</p>

<p>시이는 주변을 수소문한 결과, 사건이 일어나지 않은 곳에서 사건이 일어났을 때 목격된 사람들의 이름 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개를 얻었다.</p>

<p>이 사건은 추리 소설의 원칙을 따를 것이기 때문에, 범인을 다음과 같이 추리할 수 있다.</p>

<ol start="0">
	<li>아래 규칙은 우선순위대로 주어진다. 따라서, 두 개 이상의 규칙들이 동시에 범인을 찾아냈을 경우에는 더 규칙 번호가 작은 쪽을 우선으로 한다.</li>
	<li>동호는 악질이다. 사건 당시에 <span style="color:#e74c3c;"><code>dongho</code></span>가 집에 존재했을 경우, 목격담에 관계없이 <span style="color:#e74c3c;"><code>dongho</code></span>가 범인이다.</li>
	<li>집에 있던 사람 중 목격담이 없는 사람이 단 한 명일 경우, 소거법에 의해 당연히 그 사람이 범인이다.</li>
	<li>목격담이 없는, 이름이 <span style="color:#e74c3c;"><code>bumin</code></span>인 사람이 집에 있었다면, 그 사람이 범인이다.</li>
	<li>목격담이 없는, 이름이 <span style="color:#e74c3c;"><code>cake</code></span>인 사람이 집에 있었다면, 케이크는 거짓말이기 때문에 (The cake is a lie) 그 사람이 범인이다.</li>
	<li>목격담이 없는, 이름이 <span style="color:#e74c3c;"><code>lawyer</code></span>인 사람이 집에 있었다면, 변호사는 항상 범인이기 때문에 그 사람이 범인이다.</li>
	<li>빠르면 케이크를 몰래 먹기 쉽기 때문에, 집에 있던 <strong>시이가 아닌</strong> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>명의 사람들 중, 목격담이 없고 사전순으로 가장 이름이 빠른 사람이 범인이다.</li>
</ol>

<p>케이크가 있는 방에서 잠에 든 시이는 다른 곳에서 목격되지 않는다.</p>

<p>한 사람의 이름은 유일하고, 동명이인이 존재하지 않는다.</p>

<p>한 사람이 여러 번 목격되었을 수 있고, 목격된 사람이 사건이 일어났을 때 집 밖에 있었을 수도 있다.</p>

<p>시이의 케이크를 먹은 범인을 찾아주자.</p>

### 입력 

 <p>첫 번째 줄에, 시이의 케이크가 없어졌다는 메시지가 입력된다. (<span style="color:#e74c3c;"><code>swi's cake is missing!</code></span>)</p>

<p>두 번째 줄에, 집 안에 있던 시이를 제외한 사람의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>그다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개 줄에, 집 안에 있던 시이를 제외한 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>명 각각의 이름이 한 줄에 하나씩 주어진다. 이름은 영문 소문자로만 이루어진 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>글자 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container>글자 이하의 문자열이다.</p>

<p>그다음 줄에, 목격담의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다.</p>

<p>그다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개 줄에, 사건이 일어나지 않은 곳에서 목격된 사람의 이름이 주어진다.</p>

### 출력 

 <p>문제의 규칙에 따라, 시이의 케이크를 먹은 범인의 이름을 출력한다.</p>

