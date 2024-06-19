# [Silver III] COMPRESS - 4875 

[문제 링크](https://www.acmicpc.net/problem/4875) 

### 성능 요약

메모리: 111660 KB, 시간: 132 ms

### 분류

수학, 정수론, 파싱, 문자열

### 제출 일자

2024년 6월 19일 16:50:55

### 문제 설명

<p>Reduce the number of digits.</p>

<p>An experimental physicist generates a great deal of data from experiments that he performs. The data generated from these experiments has a special property, and he wants to take advantage of this property to reduce the amount of space needed to store the results.</p>

<p>The data is generated in pairs of numbers, where the first number is always less than the second number. The way that the physicist wants to store these numbers is similar to the how some people abbreviate a range of numbers in a book. For example, when they refer to pages 11 through 18 in a book, they will sometimes denote it as 11-8.</p>

<p>Some notation definitions:</p>

<table class="table table-bordered" width="100%">
	<tbody>
		<tr>
			<td><b>Definitions</b></td>
			<td><b>For example</b></td>
		</tr>
		<tr>
			<td>The first of a pair of numbers is denoted by F.</td>
			<td>in "18482-02", F = 18482</td>
		</tr>
		<tr>
			<td>The second of a pair of numbers (in compressed form) is denoted by C.</td>
			<td>in "18482-02", C = 02</td>
		</tr>
		<tr>
			<td>The second of a pair of numbers (in decoded form) is denoted by R.</td>
			<td>in "18482-02", R = 18502</td>
		</tr>
		<tr>
			<td>MSD(x,y) refers to the 'x' most significant digits of 'y' when 'y' is denoted in base ten, which is the null string for x <= 0</td>
			<td>MSD(3,19283) = 192, MSD(0,12)=''</td>
		</tr>
		<tr>
			<td>LSD(x,y) refers to the 'x' least significant digits of 'y' when 'y' is denoted in base ten (possibly padded with zeros).</td>
			<td>LSD(2, 48290) = 90, LSD(2,3)= 03</td>
		</tr>
	</tbody>
</table>

<p>The rules for decoding the "compressed" second number are as follows:</p>

<table border="1" cellpadding="2" cellspacing="2" class="table table-bordered" width="100%">
	<tbody>
		<tr>
			<td><b>Rule</b></td>
			<td><b>An example</b></td>
		</tr>
		<tr>
			<td>The number C is always written with the fewest possible digits.</td>
			<td> </td>
		</tr>
		<tr>
			<td>If the number C is larger than F, then R is the same as C.</td>
			<td>given "123-283", then F=123, C=283, and R would be 283</td>
		</tr>
		<tr>
			<td>If C is less than or equal to F, then the following rules apply:</td>
			<td> </td>
		</tr>
		<tr>
			<td>LSD(length(C), R) will always be the same as C.</td>
			<td> </td>
		</tr>
		<tr>
			<td>If LSD(length(C), F) is less than C, then R is equal to MSD(length(F) - length(C), F), prepended to the digits of C.</td>
			<td>given: "4137-223", then:<br>
			F=4137, C=223:<br>
			LSD(length(C),R) = 223<br>
			MSD(4 - 3, 4137) = 4<br>
			R would be 4223</td>
		</tr>
		<tr>
			<td>If LSD(length(C), F) is greater than or equal to C, then R is equal to 10^(length(C)) added to the following value: MSD(length(F) - length(C), F), prepended to the digits of C.</td>
			<td>given: "8543-13", then<br>
			F=8543, C=13:<br>
			LSD(length(C),R) = 13<br>
			MSD(4 - 2, 8543) = 85<br>
			10^(2) = 100<br>
			R would be 8513 + 100 = 8613</td>
		</tr>
	</tbody>
</table>

<p>Please note that leading zeros on the number C are significant. '7' is not the same as '07', and neither of them are the same as '007'.  For example:</p>

<blockquote>
<p>given: "2839-06", then F=2839, C=06 so R would be 2906<br>
given: "2839-006", then F=2839, C=006 so R would be 3006</p>
</blockquote>

<p>Your task is to compute the "compressed" second number format from it's uncompressed version.</p>

### 입력 

 <p>In the input file, each line of input will consist of a pair of non-negative integers separated by a hyphen, where the second number is always larger than the first number. The second number will always be less than 2<sup>31</sup>-1. </p>

### 출력 

 <p>Other than the standard header and trailer messages, each line of input will produce one line of output. Each line of output will consist of the first number, followed by a hyphen, followed by the "compressed" version of the second number.</p>

