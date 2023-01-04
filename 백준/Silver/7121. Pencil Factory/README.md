# [Silver IV] Pencil Factory - 7121 

[문제 링크](https://www.acmicpc.net/problem/7121) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

유클리드 호제법(euclidean), 포함 배제의 원리(inclusion_and_exclusion), 수학(math), 정수론(number_theory)

### 문제 설명

<p>In a pencil factory every uncompleted pencil is processed in the following way - at first it is painted in the painting machine an immediately afterwards handed over to the varnishing machine. However neither of the machines is properly tuned. The painting machine does not paint an uncompleted pencil after painting n pencils. In addition, the varnishing machine does not varnish a pencil after varnishing m pencils. Thus the factory produces three types of incomplete pencils: a completely unprocessed pencil, painted, but not varnished and varnished, but not painted pencils.</p>

<p>Your task is to write a program that for the given numbers n, m and k (the number of uncompleted pencils to be processed) computes the number of fully processed pencils and the number of each type of incomplete pencils. It is known that the uncompleted pencil before processing the pencils that interest us was neither painted, nor varnished.</p>

<p>Thus, for example, if n=3, m=5 and k=17, then the pencil processing can be illustrated by the following table (✍️ means that the current operation has been performed, ⚫ - that it has not been performed):</p>

<table class="table table-bordered th-center td-center">
	<thead>
		<tr>
			<th> </th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
			<th>7</th>
			<th>8</th>
			<th>9</th>
			<th>10</th>
			<th>11</th>
			<th>12</th>
			<th>13</th>
			<th>14</th>
			<th>15</th>
			<th>16</th>
			<th>17</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Painting</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>⚫</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>⚫</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>⚫</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>⚫</td>
			<td>✍️</td>
		</tr>
		<tr>
			<td>Varnishing</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>⚫</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>⚫</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
			<td>✍️</td>
		</tr>
	</tbody>
</table>

<p>As is shown in the picture, only 12 out of the 17 pencils are fully processed. One (12th) has been left completely unprocessed. One pencil (6th) has been painted, but not varnished. Three pencils (4th, 8th and 16th) have been varnished, but not painted.</p>

### 입력 

 <p>The first line of input contains values of three natural numbers n, m and k.</p>

<p>It is known that 0 < n < 10<sup>6</sup>, 0 < m < 10<sup>6</sup>, 0 < k < 10<sup>9</sup>. The values of these numbers are separated by space symbols.</p>

### 출력 

 <p>Output four integer numbers into the first line of output:</p>

<ol style="list-style-type:lower-alpha;">
	<li>The number of pencils that have been both painted and varnished;</li>
	<li>the number of pencils neither painted nor varnished;</li>
	<li>the number of painted but not varnished pencils;</li>
	<li>the number of varnished but not painted pencils.</li>
</ol>

<p>The numbers must appear in the output in the above order. There must be a space between any two numbers next to each other.</p>

