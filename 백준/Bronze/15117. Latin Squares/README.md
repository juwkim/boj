# [Bronze I] Latin Squares - 15117 

[문제 링크](https://www.acmicpc.net/problem/15117) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>A Latin Square is an n-by-n array filled with n different digits, each digit occurring exactly once in each row and once in each column. (The name “Latin Square” was inspired by the work of Leonhard Euler, who used Latin characters in his papers on the topic.)</p>

<p>A Latin Square is said to be in reduced form if both its top row and leftmost column are in their natural order. The natural order of a set of digits is by increasing value.</p>

<p>Your team is to write a program that will read an n-by-n array, and determine whether it is a Latin Square, and if so, whether it is in reduced form.</p>

### 입력 

 <p>The first line of input contains a single integer n (2 ≤ n ≤ 36). Each of the next n lines contains n digits in base n, with the normal digits ‘0’ through ‘9’ for digit values below 10 and uppercase letters ‘A’ through ‘Z’ representing digit values 10 through 35. All digits will be legal for base n; for instance, if n is 3, the only legal characters in the n input lines describing the square will be ‘0’, ‘1’, and ‘2’.</p>

### 출력 

 <p>If the given array is not a Latin Square, print “No” on a single line (without quotation marks). If it is a Latin Square, but not in reduced form, print “Not Reduced” on a single line (without quotation marks). If it is a Latin Square in reduced form, print “Reduced” on a single line (without quotation marks).</p>

