# [Bronze II] I Flipped The Calendar... - 33358 

[문제 링크](https://www.acmicpc.net/problem/33358) 

### 성능 요약

메모리: 122644 KB, 시간: 208 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2025년 2월 11일 05:57:17

### 문제 설명

<p>While flipping through the calendar, Nikolai wondered: how many rows are in the calendar for a specific year?</p>

<p>The calendar consists of 12 sheets, each corresponding to a month from January to December. Each sheet lists all the days of the respective month. The days on each sheet are arranged in rows by week: the days of one week are in one row, the days of different weeks are in different rows. In this calendar, the week starts on Monday.</p>

<p>For example, if a month has 31 days and the first day of the month is Sunday (as in January 2023), then there will be six rows on the calendar sheet for that month:</p>

<table class="table table-bordered table-center-20 td-center">
	<tbody>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td>6</td>
			<td>7</td>
			<td>8</td>
		</tr>
		<tr>
			<td>9</td>
			<td>10</td>
			<td>11</td>
			<td>12</td>
			<td>13</td>
			<td>14</td>
			<td>15</td>
		</tr>
		<tr>
			<td>16</td>
			<td>17</td>
			<td>18</td>
			<td>19</td>
			<td>20</td>
			<td>21</td>
			<td>22</td>
		</tr>
		<tr>
			<td>23</td>
			<td>24</td>
			<td>25</td>
			<td>26</td>
			<td>27</td>
			<td>28</td>
			<td>29</td>
		</tr>
		<tr>
			<td>30</td>
			<td>31</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>Remember that in a leap year, February has 29 days, and in a non-leap year, it has 28 days. A year is considered a leap year if its number is divisible by 400 or divisible by 4 but not by 100. For example, 2000, 2004, and 2040 are leap years, while 1900, 1982, and 2039 are not.</p>

### 입력 

 <p>The first line contains the year number <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$y$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c37"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1970</mn><mo>≤</mo><mi>y</mi><mo>≤</mo><mn>2037</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1970 \le y \le 2037$</span></mjx-container>).</p>

### 출력 

 <p>Output the number of rows in the calendar for the given year.</p>

