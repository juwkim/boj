# [Bronze II] Hexadecimal Conversion - 6040 

[문제 링크](https://www.acmicpc.net/problem/6040) 

### 성능 요약

메모리: 28904 KB, 시간: 68 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 구현(implementation), 수학(math)

### 문제 설명

<p>Bessie was teaching Jessie, her protege interesting in programming contests the binary facts of life. She explained that computers work in binary (base 2) and that all computer numbers in general are stored as 0's and 1's. Jessie was a bit unclear on the concept, so Bessie made her an exercise, shown below.</p>

<p>Write a program that converts an unsigned hexadecimal number to octal (base 8) form.  Hexadecimal number can have at most 100,000 digits and is composed of digits and capital letters from A to F.</p>

<p>Note: a hexadecimal number is a special way of representing numbers in base 16. The digits 0-9 still correspond to 0-9, and then A (capital A!) corresponds to 10, B to 11, etc. (F stands for 15).</p>

<p>For example, the hexadecimal number A10B corresponds to the (decimal) number 10*16^3 + 1*16^2 + 0*16^1 + 11*16^0 = 41227. The corresponding octal (base 8) number would be 120413, since 1*8^5 + 2*8^4 + 0*8^3 + 4*8^2 + 1*8^1 + 3*8^0 = 41227.</p>

<p>Hint: there is an easier way to convert from hexadecimal to octal than by converting hexadecimal -> decimal -> octal. It might help to think about the numbers in binary (base 2).</p>

### 입력 

 <ul>
	<li>Line 1: A single hexadecimal number. Multidigit numbers will have no leading zeroes (i.e., A1 instead of 00A1). 0 (by itself) is a valid input.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The octal value with no leading zeros.  If the input is 0, the output should also be 0.</li>
</ul>

<p> </p>

