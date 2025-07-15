# [Silver I] Pizza Anyone? - 6460 

[문제 링크](https://www.acmicpc.net/problem/6460) 

### 성능 요약

메모리: 112136 KB, 시간: 264 ms

### 분류

비트마스킹, 브루트포스 알고리즘

### 제출 일자

2025년 7월 16일 07:06:50

### 문제 설명

<p>You are responsible for ordering a large pizza for you and your friends. Each of them has told you what he wants on a pizza and what he does not; of course they all understand that since there is only going to be one pizza, no one is likely to have all their requirements satisfied. Can you order a pizza that will satisfy at least one request from all your friends?</p>

<p>The pizza parlor you are calling offers the following pizza toppings; you can include or omit any of them in a pizza:</p>

<table class="table table-bordered" style="width:353px">
	<thead>
		<tr>
			<th>Input Code</th>
			<th>Topping</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>A</td>
			<td>Anchovies</td>
		</tr>
		<tr>
			<td>B</td>
			<td>Black Olives</td>
		</tr>
		<tr>
			<td>C</td>
			<td>Canadian Bacon</td>
		</tr>
		<tr>
			<td>D</td>
			<td>Diced Garlic</td>
		</tr>
		<tr>
			<td>E</td>
			<td>Extra Cheese</td>
		</tr>
		<tr>
			<td>F</td>
			<td>Fresh Broccoli</td>
		</tr>
		<tr>
			<td>G</td>
			<td>Green Peppers</td>
		</tr>
		<tr>
			<td>H</td>
			<td>Ham</td>
		</tr>
		<tr>
			<td>I</td>
			<td>Italian Sausage</td>
		</tr>
		<tr>
			<td>J</td>
			<td>Jalapeno Peppers</td>
		</tr>
		<tr>
			<td>K</td>
			<td>Kielbasa</td>
		</tr>
		<tr>
			<td>L</td>
			<td>Lean Ground Beef</td>
		</tr>
		<tr>
			<td>M</td>
			<td>Mushrooms</td>
		</tr>
		<tr>
			<td>N</td>
			<td>Nonfat Feta Cheese</td>
		</tr>
		<tr>
			<td>O</td>
			<td>Onions</td>
		</tr>
		<tr>
			<td>P</td>
			<td>Pepperoni</td>
		</tr>
	</tbody>
</table>

<p>Your friends provide you with a line of text that describes their pizza preferences. For example, the line</p>

<p>+O-H+P;</p>

<p>reveals that someone will accept a pizza with onion, or without ham, or with pepperoni, and the line</p>

<p>-E-I-D+A+J;</p>

<p>indicates that someone else will accept a pizza that omits extra cheese, or Italian sausage, or diced garlic, or that includes anchovies or jalapenos.</p>

### 입력 

 <p>The input consists of a series of pizza constraints.</p>

<p>A pizza constraint is a list of 1 to 12 topping constraint lists each on a line by itself followed by a period on a line by itself.</p>

<p>A topping constraint list is a series of topping requests terminated by a single semicolon.</p>

<p>An topping request is a sign character (+/-) and then an uppercase letter from A to P.</p>

### 출력 

 <p>For each pizza constraint, provide a description of a pizza that satisfies it. A description is the string "Toppings: " in columns 1 through 10 and then a series of letters, in alphabetical order, listing the toppings on the pizza. So, a pizza with onion, anchovies, fresh broccoli and Canadian bacon would be described by:</p>

<p>Toppings: ACFO</p>

<p>If no combination toppings can be found which satisfies at least one request of every person, your program should print the string</p>

<p>"No pizza can satisfy these requests." on a line by itself starting in column 1. </p>

