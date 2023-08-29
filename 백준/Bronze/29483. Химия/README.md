# [Bronze II] Химия - 29483 

[문제 링크](https://www.acmicpc.net/problem/29483) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

사칙연산, 구현, 수학, 파싱, 문자열

### 문제 설명

<p>Ваша задача --- вычислить массу молекулы вещества, заданного химической формулой. Формула представляет собой перечисление элементов входящих в молекулу вещества. Для сокращения записи формулы используется обозначение <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D438 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$E n$</span></mjx-container>, которое означает, что элемент <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D438 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$E$</span></mjx-container> надо повторить <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> раз. Масса молекулы вещества --- это сумма весов всех его элементов.</p>

<table class="table table-bordered th-center td-center table-center-30">
	<tbody>
		<tr>
			<th>Название элемента</th>
			<th>Обозначение</th>
			<th>Масса</th>
		</tr>
		<tr>
			<td>Водород</td>
			<td>H</td>
			<td>1</td>
		</tr>
		<tr>
			<td>Углерод</td>
			<td>C</td>
			<td>12</td>
		</tr>
		<tr>
			<td>Азот</td>
			<td>N</td>
			<td>14</td>
		</tr>
		<tr>
			<td>Кислород</td>
			<td>O</td>
			<td>16</td>
		</tr>
	</tbody>
</table>

<p>В единственной строке входного файла записана формула. Ее длина не превышает 20 символов. Формула состоит из букв <<CHNO>> и цифр от 1 до 9. Цифра всегда идет после буквы.</p>

### 입력 

 <p>В выходной файл выведите одно число --- массу молекулы.</p>

### 출력 

 Empty

