# [Silver III] 혼긱대학교 - 32345 

[문제 링크](https://www.acmicpc.net/problem/32345) 

### 성능 요약

메모리: 112720 KB, 시간: 152 ms

### 분류

조합론, 수학, 문자열

### 제출 일자

2024년 9월 23일 06:27:11

### 문제 설명

<p>홍익대학교의 영어 이름은 <span style="color:#e74c3c;"><code>hongik university</code></span>이다. 하지만 읽는 사람에 따라 이를 <span style="color:#e74c3c;"><code>hong/ik</code></span>으로 발음하지 않고, <span style="color:#e74c3c;"><code>hon/gik</code></span>으로 발음해 혼긱대학교가 되는 웃지 못할 상황이 종종 벌어지곤 한다. </p>

<p>자음이 앞 모음에 붙느냐, 뒤 모음에 붙느냐에 따라 단어의 발음이 다른 것을 신기하게 여긴 동현이는 비슷한 상황인 영어 단어들을 조사해서 발음이 얼마나 다양하게 될 수 있는지를 알아보려 한다. 하지만, 영어를 잘 못하는 동현이는 아래의 규칙에 따라서만 발음을 파악한다. </p>

<ul>
	<li>영어 모음은 <span style="color:#e74c3c;"><code>a</code></span>, <span style="color:#e74c3c;"><code>e</code></span>, <span style="color:#e74c3c;"><code>i</code></span>, <span style="color:#e74c3c;"><code>o</code></span>, <span style="color:#e74c3c;"><code>u</code></span> 5개이며, 자음은 모음을 제외한 나머지 21개의 알파벳이다.</li>
	<li>1개의 모음에 0개 이상의 자음이 앞뒤로 붙어서 하나의 음이 되고, 음들이 모여서 단어의 발음이 된다. 
	<ul>
		<li>예) <code><span style="color:#e74c3c;">h</span>, <span style="color:#e74c3c;">o</span>, <span style="color:#e74c3c;">n</span>, <span style="color:#e74c3c;">g</span>, <span style="color:#e74c3c;">i</span>, <span style="color:#e74c3c;">k</span> →</code> <code><span style="color:#e74c3c;">hong</span>, <span style="color:#e74c3c;">ik</span></code> <code>→</code> <span style="color:#e74c3c;"><code>hongik</code></span></li>
	</ul>
	</li>
	<li>자음과 자음, 자음과 모음은 인접했을 때만 한 음으로 모일 수 있다.</li>
	<li>음에 구성된 알파벳의 개수, 구성, 순서가 다른 경우 다른 음으로 취급한다.
	<ul>
		<li>예) <span style="color:#e74c3c;"><code>ab</code></span>와 <span style="color:#e74c3c;"><code>abb</code></span>, <span style="color:#e74c3c;"><code>ba</code></span>는 모두 다른 음이다.</li>
	</ul>
	</li>
	<li>주어진 단어의 알파벳을 각각 1회씩 사용해서 발음을 만들어야 한다.</li>
	<li>각 음의 구성이 다른 경우 단어의 발음이 다른 것으로 생각한다.</li>
</ul>

<p>이와 같은 규칙에 따라 단어들이 발음될 수 있는 경우의 수를 출력해 보자.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(T\)</span></mjx-container>가 주어진다.  <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\((1 ≤ T ≤ 100\,000)\)</span> </mjx-container></p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(T\)</span></mjx-container>개의 줄에 걸쳐, 알파벳 소문자로 이루어진 단어 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(S\)</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>S</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><mn>300</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\((1 ≤ |S| ≤ 300\,000)\)</span> </mjx-container></p>

<p>모든 테스트 케이스에 대해 단어의 길이의 합은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(1\,000\,000\)</span></mjx-container> 이하이다.</p>

### 출력 

 <p>매 줄마다, 각 테스트 케이스에서 단어의 발음의 경우의 수를 출력한다.</p>

<p>이때 경우의 수가 너무 커질 수 있으므로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup><mo>+</mo><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(10^9+7\)</span></mjx-container>로 나눈 나머지를 출력하자.</p>

<p>만약 모음이 없어서 발음 할 수 없을 경우 <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다.</p>

