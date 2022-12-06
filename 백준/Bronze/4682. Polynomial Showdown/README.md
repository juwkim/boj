# [Bronze I] Polynomial Showdown - 4682 

[문제 링크](https://www.acmicpc.net/problem/4682) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

많은 조건 분기(case_work), 구현(implementation)

### 문제 설명

<p>Given the coefficients of a polynomial from degree 8 down to 0, you are to format the polynomial in a readable format with unnecessary characters removed. For instance, given the coefficients 0, 0, 0, 1, 22, -333, 0, 1, and -1, you should generate an output line which displays x^5 + 22x^4 - 333x^3 + x - 1.</p>

<p>The formatting rules which must be adhered to are as follows:</p>

<ol>
	<li>Terms must appear in decreasing order of degree.</li>
	<li>Exponents should appear after a caret "^".</li>
	<li>The constant term appears as only the constant.</li>
	<li>Only terms with nonzero coefficients should appear, unless all terms have zero coefficients in which case the constant term should appear.</li>
	<li>The only spaces should be a single space on either side of the binary + and - operators.</li>
	<li>If the leading term is positive then no sign should precede it; a negative leading term should be preceded by a minus sign, as in -7x^2 + 30x + 66.</li>
	<li>Negated terms should apear as a subtracted unnegated term (with the exception of a negative leading term which should appear as described above.) That is, rather than x^2 + -3x, the output should be x^2 - 3x.</li>
	<li>The constants 1 and -1 should appear only as the constant term. That is, rather than -1x^3 + 1x^2 +3x^1 - 1, the output should appear as -x^3 + x^2 + 3x -1.</li>
</ol>

### 입력 

 <p>The input file contain one or more lines of coefficients delimited by one or more spaces. There are nine coefficients per line, each coefficient eing an integer with a magnitude of less than 1000. </p>

### 출력 

 <p>The output file should contain the formatted polynomials, one per line.</p>

