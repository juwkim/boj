# [Bronze II] Scaling Recipes - 11640 

[문제 링크](https://www.acmicpc.net/problem/11640) 

### 성능 요약

메모리: 30840 KB, 시간: 972 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>A recipe is a list of ingredients and a set of instructions to prepare a dish. It is often written for a particular number of portions. If you have a recipe for 4 portions and you want to make 6 portions, it turns out that simply multiplying the amounts for each ingredient by 1.5 is often wrong! The reason is that the original recipe may have been rounded to the nearest teaspoon, gram, etc., and the rounding errors magnify when a recipe is scaled.</p>

<p>Some recipes are specifically written to ease the task of scaling. These recipes are developed using “Baker’s percentages.” Each ingredient is listed not only by weight (in grams), but also as a percentage relative to the “main ingredient.” The main ingredient will always have a 100% Baker’s percentage. Note that the sum of the Baker’s percentages from all ingredients is greater than 100%, and that the Baker’s percentages of some ingredients may exceed 100%.</p>

<p>Table 1: Example Recipe</p>

<table class="table table-bordered" style="width:40%">
	<thead>
		<tr>
			<th>Ingredient</th>
			<th>Weight (g)</th>
			<th>Percentage (%)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Olive Oil</td>
			<td>50.9</td>
			<td>11.2</td>
		</tr>
		<tr>
			<td>Garlic</td>
			<td>12.0</td>
			<td>2.7</td>
		</tr>
		<tr>
			<td>Beef</td>
			<td>453.6</td>
			<td>100.0</td>
		</tr>
		<tr>
			<td>Onions</td>
			<td>1134.0</td>
			<td>250.0</td>
		</tr>
		<tr>
			<td>Raisins</td>
			<td>82.5</td>
			<td>18.2</td>
		</tr>
		<tr>
			<td>Bouillon</td>
			<td>10.0</td>
			<td>2.2</td>
		</tr>
	</tbody>
</table>

<p>To scale a recipe:</p>

<ol>
	<li>determine the scaling factor by dividing the number of desired portions by the number of portions for which the recipe is written;</li>
	<li>multiply the weight of the main ingredient with a 100% Baker’s percentage by the scaling factor. This is the scaled weight of the main ingredient;</li>
	<li>calculate the scaled weight of every other ingredient by multiplying its Baker’s percentage by the scaled weight of the main ingredient.</li>
</ol>

### 입력 

 <p>The first line of input specifies a positive integer T ≤ 1000, consisting of the cases to follow. Each case starts with a line with three integers R, P, and D: 1 ≤ R ≤ 20 is the number of ingredients, 1 ≤ P ≤ 12 is the number of portions for which the recipe is written, and 1 ≤ D ≤ 1000 is the number of desired portions. Each of the next R lines is of the form</p>

<pre><name> <weight> <percentage></pre>

<p>where <name> is the name of the ingredient (an alphabetic string of up to 20 characters with no embedded spaces), <weight> is the weight in grams for that ingredient, and <percentage> is its Baker’s percentage. Both <weight> and <percentage> are floating-point numbers with exactly one digit after the decimal point. Each recipe will only have one ingredient with a Baker’s percentage of 100%.</p>

### 출력 

 <p>For each case, print Recipe # followed by a space and the appropriate case number (see sample output below). This is followed by the list of ingredients and their scaled weights in grams. The name of the ingredient and its weight should be separated by a single space. Each ingredient is listed on its own line, in the same order as in the input. After each case, print a line of 40 dashes (’-’). Answers within 0.1g of the correct result are acceptable.</p>

