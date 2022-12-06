# [Bronze I] Molar mass - 8941 

[문제 링크](https://www.acmicpc.net/problem/8941) 

### 성능 요약

메모리: 28776 KB, 시간: 76 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p><img alt="" src="" style="float:right; height:190px; width:215px">An organic compound is any member of a large class of chemical compounds whose molecules contain carbon. The molar mass of an organic compound is the mass of one mole of the organic compound. The molar mass of an organic compound can be computed from the standard atomic weights of the elements.</p>

<p>When an organic compound is given as a molecular formula, Dr. CHON wants to find its molar mass. A molecular formula, such as C3H4O3, identifies each constituent element by its chemical symbol and indicates the number of atoms of each element found in each discrete molecule of that compound. If a molecule contains more than one atom of a particular element, this quantity is indicated using a subscript after the chemical symbol.</p>

<p>In this problem, we assume that the molecular formula is represented by only four elements, ‘C’ (Carbon), ‘H’ (Hydrogen), ‘O’ (Oxygen), and ‘N’ (Nitrogen) without parentheses. </p>

<p>The following table shows that the standard atomic weights for ‘C’, ‘H’, ‘O’, and ‘N’. </p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>Atomic Name</th>
			<th>Carbon</th>
			<th>Hydrogen</th>
			<th>Oxygen</th>
			<th>Nitrogen</th>
			<th> </th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>Standard Atomic Weight</th>
			<td>12.01 g/mol</td>
			<td>1.008 g/mol</td>
			<td>16.00 g/mol</td>
			<td>14.01 g/mol</td>
		</tr>
	</tbody>
</table>

<p>For example, the molar mass of a molecular formula C6H5OH is 94.108 g/mol which is computed by 6×(12.01 g/mol) + 6×(1.008 g/mol) + 1×(16.00 g/mol). Given a molecular formula, write a program to compute the molar mass of the formula.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case is given in a single line, which contains a molecular formula as a string. The chemical symbol is given by a capital letter and the length of the string is greater than 0 and less than 80. The quantity number n which is represented after the chemical symbol would be omitted when the number is 1 ( 2 ≤ n ≤ 99 ). </p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. The line should contain the molar mass of the given molecular formula. </p>

