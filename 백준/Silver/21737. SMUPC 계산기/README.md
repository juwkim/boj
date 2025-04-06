# [Silver I] SMUPC 계산기 - 21737 

[문제 링크](https://www.acmicpc.net/problem/21737) 

### 성능 요약

메모리: 113408 KB, 시간: 168 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 4월 6일 18:41:41

### 문제 설명

<p>SMUPC를 기념하기 위해 ALGOS와 DSC Sookmyung에서는 SMUPC의 각 글자로 계산이 이루어지는 계산기를 만들었다. 가은이와 혜민이는 이 계산기와 같은 방식으로 작동하는 프로그램을 만들고자 한다. 가은이와 혜민이는 몇 가지 계산 작업을 통해 SMUPC에 해당하는 각 기호가 아래의 표와 같이 동작함을 밝혀낼 수 있었다.</p>

<p style="text-align: center;">[SMUPC 계산기의 동작 방식]</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 800px;">
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>알파벳</strong></td>
			<td style="text-align: center;"><strong> S </strong></td>
			<td style="text-align: center;"><strong> M </strong></td>
			<td style="text-align: center;"><strong> U </strong></td>
			<td style="text-align: center;"><strong> P </strong></td>
			<td style="text-align: center;"><strong> C </strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">  해당 수식  </td>
			<td style="text-align: center;">        -        </td>
			<td style="text-align: center;">        *        </td>
			<td>
			<p style="text-align: center;">/</p>

			<p style="text-align: center;">   (정수 몫   </p>

			<p style="text-align: center;">나눗셈)</p>
			</td>
			<td style="text-align: center;">        +        </td>
			<td>
			<p style="text-align: center;">여태까지의</p>

			<p style="text-align: center;">계산 결괏값</p>

			<p style="text-align: center;">반환</p>
			</td>
		</tr>
	</tbody>
</table>

<p>SMUPC 계산기는 기존의 사칙연산 방식과는 다르게 앞에서부터 순서대로 계산이 이루어진다. 단, 이 계산기에서 음수를 양수로 나누는 경우는 C++14의 기준을 따른다. 이는 음수에 -1을 곱해 양수로 바꾼 뒤 몫을 취하고, 그 몫에 -1을 곱한 것과 같다. 예를 들어, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2F"></mjx-c></mjx-mo></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mrow data-mjx-texclass="ORD"><mo>/</mo></mrow><mn>3</mn><mo>=</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5 / 3 = 1$</span></mjx-container>, (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-5$</span></mjx-container>) <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2F"></mjx-c></mjx-mo></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mo>/</mo></mrow><mn>3</mn><mo>=</mo><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$/ 3 = -1$</span></mjx-container> 로 계산된다. 더불어 SMUPC 계산기에 입력하는 수식은 다음과 같은 규칙을 따라야 한다고 한다.</p>

<ul>
	<li>수식은 0부터 9까지의 숫자와 <span style="color:#e74c3c;"><code>S</code></span>, <code><span style="color:#e74c3c;">M</span></code>, <code><span style="color:#e74c3c;">U</span></code>, <code><span style="color:#e74c3c;">P</span></code>, <code><span style="color:#e74c3c;">C</span></code>의 알파벳만을 포함할 수 있다.</li>
	<li>수식은 수로 시작해야 하며, 알파벳으로 끝나야 한다.</li>
	<li>수식에 음수를 입력할 수 없다.</li>
	<li>수식에 입력하는 수는 0으로 시작할 수 있다.</li>
	<li>알파벳 <span style="color:#e74c3c;"><code>C</code></span>로 계산 결괏값을 반환한 후에 추가적인 계산을 원한다면 알파벳 기호를 추가적으로 사용하여 입력을 이어나가야 한다.</li>
	<li>알파벳 <code><span style="color:#e74c3c;">S</span></code>, <code><span style="color:#e74c3c;">M</span></code>, <code><span style="color:#e74c3c;">U</span></code>, <code><span style="color:#e74c3c;">P</span></code>는 서로 연속해서 입력할 수 없으며 알파벳 <code><span style="color:#e74c3c;">S</span></code>, <code><span style="color:#e74c3c;">M</span></code>, <code><span style="color:#e74c3c;">U</span></code>, <code><span style="color:#e74c3c;">P</span></code>을 입력한 직후 다른 수의 입력 없이 알파벳 <span style="color:#e74c3c;"><code>C</code></span>를 바로 입력할 수 없다.</li>
</ul>

<p>SMUPC 계산기와 같은 작업을 수행할 수 있는 프로그램을 작성하여라.</p>

### 입력 

 <p>첫째 줄에 수식에 들어갈 기호의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>500</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$ 1 \leq N \leq 500\,000$</span></mjx-container>)이 주어진다.</p>

<p>둘째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 기호가 사용된 수식이 주어진다. 수식의 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,000\,000$</span></mjx-container>을 넘지 않는다. 단, 계산 도중 입력되는 수나 계산 결괏값의 범위는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mn>31</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-2^{31}$</span> </mjx-container><sup> </sup>이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mn>31</mn></mrow></msup><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2^{31}-1$</span></mjx-container> 이하이다. 더불어 어떤 수를 0으로 나누는 경우는 존재하지 않는다.</p>

### 출력 

 <p>알파벳 <span style="color:#e74c3c;"><code>C</code></span>가 나올 때마다 여태까지의 계산 결과 값을 띄어쓰기 간격으로 출력하도록 한다. 알파벳 <span style="color:#e74c3c;"><code>C</code></span>가 한번도 나오지 않을 경우 <span style="color:#e74c3c;"><code>NO OUTPUT</code></span>을 출력한다.</p>

