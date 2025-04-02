# [Silver II] Halt and Catch Fire - 33245 

[문제 링크](https://www.acmicpc.net/problem/33245) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 시뮬레이션, 트리를 사용한 집합과 맵

### 제출 일자

2025년 4월 2일 19:45:44

### 문제 설명

<p>Research has led to the creating of a new super fast CPU called the Fast Processing Chip (FPC). This product has a never-before seen debugging function: an instruction called <code>hcf</code>, providing debugging power unmatched by any previously designed CPU.</p>

<p>With the product becoming popular fast, companies can't wait to get their hands on the chip to start development immediately. One problem, however, is the chip is too expensive to just hand over to every developer all willy-nilly.</p>

<p>You have been hired to design a program that runs as if it were a processor, so the programmers can write programs and easily test these programs without needing the hardware.</p>

### 입력 

 <ul>
	<li>One line with one integer: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq n \leq 1000$</span></mjx-container>, the number of lines in the program.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines with three sections, separated with spaces:
	<ul>
		<li>The operation, always 3 characters</li>
		<li>An argument: Either an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mn>31</mn></mrow></msup><mo>≤</mo><mi>a</mi><mo>≤</mo><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mn>31</mn></mrow></msup><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-2^{31} \leq a \leq 2^{31}-1$</span></mjx-container> or a variable prepended with <code>$</code></li>
		<li>An argument: Either an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mn>31</mn></mrow></msup><mo>≤</mo><mi>b</mi><mo>≤</mo><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mn>31</mn></mrow></msup><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-2^{31} \leq b \leq 2^{31}-1$</span></mjx-container> or a variable prepended with <code>$</code></li>
	</ul>
	</li>
</ul>

<p>There are five possible operations:</p>

<ul>
	<li><code>mov</code> -- Move value from the first argument to the second</li>
	<li><code>add</code> -- Add value from the second argument to the first and store in <code>$acc</code></li>
	<li><code>sub</code> -- Subtract value of the second argument from the first and store in <code>$acc</code></li>
	<li><code>jeq</code> -- Jump to the instruction on the value of the second argument if the value of the first argument equals <code>$cmp</code></li>
	<li><code>hcf</code> -- Halt and Catch Fire: Stop the program immediately, takes only integer arguments</li>
</ul>

<p>An argument can be noted as an integer immediate or a variable reference, in which case it's prepended by <code>$</code>. All variable names consist of at most 20 lowercase characters from the English alphabet (<code>a-z</code>) or underscores (<code>_</code>).</p>

<p>There are four predefined variables:</p>

<ul>
	<li><code>$acc</code> -- Contains the value of an <code>add</code> or <code>sub</code> operation</li>
	<li><code>$pc </code> -- Contains the address of the currently processed operation</li>
	<li><code>$cmp</code> -- Used to compare with the <code>jeq</code> operation</li>
	<li><code>$out</code> -- Should be output when the program finishes</li>
</ul>

<p>Any other variables are defined as soon as a value is moved to them.</p>

<p>Assume any given input program to be syntactically correct.</p>

<p>Integers will never over- or underflow.</p>

### 출력 

 <p>The program exits either when the value of the <code>$pc</code> variable reaches out of the bounds of the program, or when an <code>hcf</code> instruction is reached.</p>

<ul>
	<li>In the first case, output one line containing the value of <code>$out</code> at the end of the program.</li>
	<li>In the second case, output the following:
	<ul>
		<li>One line containing the <code>hcf</code> instruction that was called.</li>
		<li>One line containing the content of the <code>$acc</code> variable.</li>
		<li>One line containing the content of the <code>$cmp</code> variable.</li>
		<li>One line containing the content of the <code>$out</code> variable.</li>
	</ul>
	</li>
</ul>

