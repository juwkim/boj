# [Bronze I] Rhonda - 26507 

[문제 링크](https://www.acmicpc.net/problem/26507) 

### 성능 요약

메모리: 116024 KB, 시간: 168 ms

### 분류

구현(implementation)

### 문제 설명

<p>Rhonda is printing processor chips, which can be made from fabricated components inscribed onto thin layers. As she prints the chips, Rhonda stacks two or more layers together to create a final chip made up of multiple layers.</p>

<p>She has several unique layers that can be combined into various numbers of layers, which allows her to create a variety of chips. Each layered component is represented by a 10x10 grid of integers, with each cell containing an integer ranging from 0 to 9. The final chip is also 10x10 grid, with each cell being the sum of all the cells in that position for the layers that were used to create the chip.</p>

<p>For example, if Rhonda has fabricated 3 layers:</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td>
			<pre>0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
</pre>
			</td>
			<td>
			<pre>1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
</pre>
			</td>
			<td>
			<pre>0011001100
1100110011
0011001100
1100110011
0011001100
1100110011
0011001100
1100110011
0011001100
1100110011
</pre>
			</td>
		</tr>
	</tbody>
</table>

<p>and decides to create a final chip that combines only the first and second layers, the resulting chip is represented by the 10x10 grid below:</p>

<pre>01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10
01 02 03 04 05 06 07 08 09 10</pre>

<p>Each layer is indexed by the order given (starting at zero). The data set for this chip would be:</p>

<pre>0 1</pre>

<p>since this chip is made by combining the first and second layer in the order given.</p>

<p>The cell values of each individual layer will be in the range 0-9, and the cell values of the final chip combined chips will in the range 0-99. All original fabricated layers will be unique.</p>

### 입력 

 <p>The first line of the input will an integer, i, representing the number of unique layers Rhonda has fabricated. This is followed by i sets of 10x10 grid of integers, each followed by a new line, representing the i fabricated layers. The next line will be a single positive integer, n, indication the number of data sets that follow. Each data set is a list of integers, all on one line, separated by spaces, which represent the layers added to create a chip.</p>

### 출력 

 <p>A 10x10 integer grid with each of the 10x10 cells represented by 2 digits and a space, the whole grid representing the final summed chip.</p>

