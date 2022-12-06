# [Bronze I] Web Colors - 10600 

[문제 링크](https://www.acmicpc.net/problem/10600) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

Empty

### 문제 설명

<p>Web colors are colors used in displaying web pages. Each color may be specified either as an RGB triple, or a common English name used for that color. Colors are specified according to the intensity of their red, green and blue components, each represented by eight bits. Thus, there are 24 bits used to specify a web color, and totally 16,777,216 colors can be imagined as web colors. But the HTML 4 specification defines only 16 named colors as shown in the table.</p>

<p>It is often useful to map one given color to one of the HTML named colors. The goal of this problem is to perform just such a mapping in the RGB color space. The input to the program consists of a collection of RGB color values to be mapped to the closest HTML named color.</p>

<p>For a given color, the “closest” color in the HTML color names is a color with the smallest Euclidean distance from the given color. That is, if rgb is the color to be mapped, and {\(R_1G_1B_1\), . . . , \(R_{16}G_{16}B_{16}\)} is the set of the HTML colors, the closest color is the one which minimizes the distance expression</p>

<p>\[d = \sqrt{(R_i-r)^2 + (G_i - g)^2 + (B_i - b)^2}\]</p>

<p>where \(i\) is an integer from 1 to 16.</p>

<table class="table table-bordered" style="width:50%">
	<thead>
		<tr>
			<th>#</th>
			<th>Name</th>
			<th>Red</th>
			<th>Green</th>
			<th>Blue</th>

		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>White</td>
			<td>255</td>
			<td>255</td>
			<td>255</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Silver</td>
			<td>192</td>
			<td>192</td>
			<td>192</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Gray</td>
			<td>128</td>
			<td>128</td>
			<td>128</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Black</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Red</td>
			<td>255</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>6</td>
			<td>Maroon</td>
			<td>128</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>7</td>
			<td>Yellow</td>
			<td>255</td>
			<td>255</td>
			<td>0</td>
		</tr>
		<tr>
			<td>8</td>
			<td>Olive</td>
			<td>128</td>
			<td>128</td>
			<td>0</td>
		</tr>
		<tr>
			<td>9</td>
			<td>Lime</td>
			<td>0</td>
			<td>255</td>
			<td>0</td>
		</tr>
		<tr>
			<td>10</td>
			<td>Green</td>
			<td>0</td>
			<td>128</td>
			<td>0</td>
		</tr>
		<tr>
			<td>11</td>
			<td>Aqua</td>
			<td>0</td>
			<td>255</td>
			<td>255</td>
		</tr>
		<tr>
			<td>12</td>
			<td>Teal</td>
			<td>0</td>
			<td>128</td>
			<td>128</td>
		</tr>
		<tr>
			<td>13</td>
			<td>Blue</td>
			<td>0</td>
			<td>0</td>
			<td>255</td>
		</tr>
		<tr>
			<td>14</td>
			<td>Navy</td>
			<td>0</td>
			<td>0</td>
			<td>128</td>
		</tr>
		<tr>
			<td>15</td>
			<td>Fuchsia</td>
			<td>255</td>
			<td>0</td>
			<td>255</td>
		</tr>
		<tr>
			<td>16</td>
			<td>Purple</td>
			<td>128</td>
			<td>0</td>
			<td>128</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>There are multiple test cases in the input. Each test case consists of a line containing three integers 0 ⩽ r, g, b ⩽ 255 which are the Red, Green and Blue intensities of the color, respectively. The input terminates with -1 -1 -1 which should not be processed.</p>

### 출력 

 <p>For each test case, output a line containing the name of the closest HTML color to the given color. If there are more than one closest color, print the one which has a smaller associated number in the above table.</p>

