# [Bronze III] Astrology - 31097 

[문제 링크](https://www.acmicpc.net/problem/31097) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2024년 1월 4일 01:06:04

### 문제 설명

<p>The famous astrologer Pavel Globus writes a bot for trading stocks in the stock market. Pavel is going to predict the stock price <em>by the stars</em>. He analyzed historical data and noticed that, for example, when Mars was in Capricorn, the stock price fell, and when the moon was in Gemini, the quotes went up. Of course, Pavel will not reveal all the details of his algorithm.</p>

<p>Pavel is not so good at programming, and one of the parts of the program that he cannot cope with is determining the zodiac sign, in which the Sun is located, depending on the current date. The zodiac sign for the current date can be determined from the following table:</p>

<table class="table table-bordered table-center-50 td-center">
	<tbody>
		<tr>
			<td><code>Aries</code></td>
			<td>March 21 --- April 19</td>
		</tr>
		<tr>
			<td><code>Taurus</code></td>
			<td>April 20 --- May 20</td>
		</tr>
		<tr>
			<td><code>Gemini</code></td>
			<td>May 21 --- June 20</td>
		</tr>
		<tr>
			<td><code>Cancer</code></td>
			<td>June 21 --- July 22</td>
		</tr>
		<tr>
			<td><code>Leo</code></td>
			<td>July 23 --- August 22</td>
		</tr>
		<tr>
			<td><code>Virgo</code></td>
			<td>August 23 --- September 22</td>
		</tr>
		<tr>
			<td><code>Libra</code></td>
			<td>September 23 --- October 22</td>
		</tr>
		<tr>
			<td><code>Scorpio</code></td>
			<td>October 23 --- November 22</td>
		</tr>
		<tr>
			<td><code>Sagittarius</code></td>
			<td>November 23 --- December 21</td>
		</tr>
		<tr>
			<td><code>Capricorn</code></td>
			<td>December 22 --- January 19</td>
		</tr>
		<tr>
			<td><code>Aquarius</code></td>
			<td>January 20 --- February 18</td>
		</tr>
		<tr>
			<td><code>Pisces</code></td>
			<td>February 19 --- March 20</td>
		</tr>
	</tbody>
</table>

<p>Help Pavel and write a program that determines the zodiac sign by the current date. Pavel, in return, will help you increase your capital.</p>

### 입력 

 <p>You are given a string in format <<<code>YYYY-MM-DD</code>>>, indicating the current date, where <code>YYYY</code> --- year (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2021</mn><mo>≤</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2021 \le$</span></mjx-container> <code>YYYY</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>≤</mo><mn>2050</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\le 2050$</span></mjx-container>), <code>MM</code> --- month (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>01</mn><mo>≤</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$01 \le$</span></mjx-container> <code>MM</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>≤</mo><mn>12</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\le 12$</span></mjx-container>), and <code>YYYY</code> --- day (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>01</mn><mo>≤</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$01 \le$</span></mjx-container> <code>DD</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>≤</mo><mn>31</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\le 31$</span></mjx-container>).</p>

<p>The date is real.</p>

### 출력 

 <p>Print one of the words from the list <<<code>Aries</code>>>, <<<code>Taurus</code>>>, <<<code>Gemini</code>>>, <<<code>Cancer</code>>>, <<<code>Leo</code>>>, <<<code>Virgo</code>>>, <<<code>Libra</code>>>, <<<code>Scorpio</code>>>, <<<code>Sagittarius</code>>>, <<<code>Capricorn</code>>>, <<<code>Aquarius</code>>>, <<<code>Pisces</code>>>, corresponding to the zodiac sign.</p>

