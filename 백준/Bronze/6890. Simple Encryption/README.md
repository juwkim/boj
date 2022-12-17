# [Bronze II] Simple Encryption - 6890 

[문제 링크](https://www.acmicpc.net/problem/6890) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>One of the simplest ways of coding a message is to do a letter shift.</p>

<p>For example, if you shift the letters in the original message by <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> then <code>A</code> in your original message becomes <code>F</code> in the coded message. (<code>B</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo accent="false" stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\to$</span></mjx-container> <code>G</code>, <code>C</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo accent="false" stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\to$</span></mjx-container> <code>H</code>, …, <code>T</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo accent="false" stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\to$</span></mjx-container> <code>Y</code>, <code>U</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo accent="false" stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\to$</span></mjx-container> <code>Z</code>, <code>V</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo accent="false" stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\to$</span></mjx-container> <code>A</code>, …, <code>Z</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo accent="false" stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\to$</span></mjx-container> <code>E</code>). To decode the message, you simply need to shift back by the same number.</p>

<p>A slightly trickier encryption uses a keyword to determine the amount of the shift. Suppose you were using the keyword <code>ACT</code>. To encode the message, you take the original message, remove everything but the alphabetic characters, and form the message into a block that has the same width as the keyword. Here is a sample message to encrypt:</p>

<p><code>BANANA & PEEL</code></p>

<p>The blocked version of the message is shown below with the keyword <code>ACT</code> as a header.</p>

<table class="table table-bordered td-center table-center-30">
	<tbody>
		<tr>
			<td>A</td>
			<td>C</td>
			<td>T</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>B</td>
			<td>A</td>
			<td>N</td>
		</tr>
		<tr>
			<td>A</td>
			<td>N</td>
			<td>A</td>
		</tr>
		<tr>
			<td>P</td>
			<td>E</td>
			<td>E</td>
		</tr>
		<tr>
			<td>L</td>
			<td> </td>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>Now, the message is encoded using a letter shift. However, this time it is not a uniform shift, it will depend upon the keyword letter at the top of the column. If the letter at the top of the column is an <code>A</code>, then the letters in that column are not shifted. If the letter is a <code>B</code>, then the letters in that column shift by <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>, and so on. In the example, the letters in the third column will shift by <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$19$</span></mjx-container> since the <code>T</code> is the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>th letter of the alphabet.</p>

<p>The encoded message is:</p>

<table class="table table-bordered td-center table-center-30">
	<tbody>
		<tr>
			<td>A</td>
			<td>C</td>
			<td>T</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>B</td>
			<td>C</td>
			<td>G</td>
		</tr>
		<tr>
			<td>A</td>
			<td>P</td>
			<td>T</td>
		</tr>
		<tr>
			<td>P</td>
			<td>G</td>
			<td>X</td>
		</tr>
		<tr>
			<td>L</td>
			<td> </td>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>You will write a program that will accept a keyword and a string to be encoded. The keyword will never have more than <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$6$</span></mjx-container> characters. The message will always be given in all uppercase characters.</p>

### 입력 

 <p>The first line of input consists of the keyword. The second line of the input is the message to be encoded. The keyword length will never exceed <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$6$</span></mjx-container> characters. The total message length also will never exceed <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$60$</span></mjx-container> characters.</p>

### 출력 

 <p>Output the encoded message on a single line.</p>

