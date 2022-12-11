# [Silver IV] 박스 그림 문자 - 23038 

[문제 링크](https://www.acmicpc.net/problem/23038) 

### 성능 요약

메모리: 151436 KB, 시간: 308 ms

### 분류

구현(implementation)

### 문제 설명

<p>유니코드 문자 중에는 box-drawing character(박스 그림 문자)라는 종류의 문자들이 있다. 이 문자들은 텍스트 UI에서 구역을 나누는 테두리를 그리기 위해 만들어진 것으로, 상하좌우 방향의 선들로 이루어져 있다. 박스 그림 문자의 종류는 다음과 같이 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$11$</span></mjx-container>가지이다.</p>

<p style="text-align: center;"><strong>┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘ ─ │</strong></p>

<p>이 문자들을 이용하면 다음과 같이 재밌는 모양들을 만들 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b94f0ae0-7378-4a23-872e-2a8abfb97ff5/-/preview/" style="width: 519px; height: 269px;"></p>

<p>위 모양들은 모두 선이 끊어지는 곳이 없다는 특징이 있다. 예를 들어 어떤 문자가 오른쪽 방향의 선을 갖고 있다면, 그 오른쪽에는 반드시 왼쪽 방향의 선을 갖고 있는 문자가 있다. 이러한 특징을 갖는 모양들을 <strong>아름다운 모양</strong>이라고 하자. 다음은 아름다운 모양이 아닌 모양의 예시이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ff0307da-1a64-452b-821a-3082a8b503db/-/preview/" style="width: 266px; height: 264px;"></p>

<p>실버는 아름다운 모양 하나를 만들어 파일로 저장해 두었다. 하지만 컴퓨터가 바이러스에 감염되어 파일의 일부분이 <code>.</code>으로 날아가버렸다!</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/aa6b6e6d-b616-480b-806a-8696b0dfa0b4/-/preview/" style="width: 263px; height: 259px;"></p>

<p>다행히도 <code>.</code>으로 대체된 부분들은 체스판처럼 배열되어 있다. 다시 말하면, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D457 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>+</mo><mi>j</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i+j$</span></mjx-container>가 홀수일 때 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>행 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D457 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>j</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$j$</span></mjx-container>열의 문자가 <code>.</code>으로 대체되어 있다. 자신의 작품이 망가져 좌절한 실버를 도와 모양을 복원해 보자. 단, 당신은 박스 그림 문자를 제대로 출력할 줄 모르기 때문에 각 문자들을 다음의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>×</mo><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \times 3$</span></mjx-container> 블록으로 치환하여 입출력할 것이다.</p>

<table align="center" class="table-23038 table table-bordered text-center">
	<tbody>
		<tr>
			<td style="border-top: 1px solid #333;">
			<pre>...
.##
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>...
###
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>...
##.
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>.#.
.## 
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>.#.
###
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>.#.
##.
.#.</pre>
			</td>
		</tr>
		<tr>
			<td style="background-color: #eee;">┌</td>
			<td style="background-color: #eee;">┬</td>
			<td style="background-color: #eee;">┐</td>
			<td style="background-color: #eee;">├</td>
			<td style="background-color: #eee;">┼</td>
			<td style="background-color: #eee;">┤</td>
		</tr>
		<tr>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
		</tr>
		<tr>
			<td>
			<pre>.#.
.##
...</pre>
			</td>
			<td>
			<pre>.#.
###
...</pre>
			</td>
			<td>
			<pre>.#.
##.
...</pre>
			</td>
			<td>
			<pre>...
###
...</pre>
			</td>
			<td>
			<pre>.#.
.#.
.#.</pre>
			</td>
			<td>
			<pre>...
...
...</pre>
			</td>
		</tr>
		<tr>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">└</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">┴</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">┘</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">─</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">│</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">.</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 실버가 만든 모양의 행 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 열 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백을 사이에 두고 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>300</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le N \le 300$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>300</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le M \le 300$</span></mjx-container>)</p>

<p>이후 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3N$</span></mjx-container>개의 줄에 걸쳐 실버가 만든 모양이 주어진다. 각 줄은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3M$</span></mjx-container>개의 문자로 이루어져 있으며, 각 문자는 <code>.</code> 또는 <code>#</code>이다.</p>

### 출력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3N$</span></mjx-container>개의 줄에 걸쳐 복원된 실버의 작품을 출력한다.</p>

