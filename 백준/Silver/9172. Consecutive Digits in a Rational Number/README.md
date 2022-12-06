# [Silver V] Consecutive Digits in a Rational Number - 9172 

[문제 링크](https://www.acmicpc.net/problem/9172) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 정수론(number_theory)

### 문제 설명

<p>As a recruiting ploy, Google once posted billboards in Harvard Square and in the Silicon Valley area just stating “{first 10-digit prime found in consecutive digits of e}.com”. In other words, find that 10-digit sequence and then connect to the web site — and find out that Google is trying to hire people who can solve a particular kind of problem.</p>

<p>Not to be outdone, Gaggle (a loosey-goosey fuzzy logic search firm), has devised its own recruiting problem. Consider the base 7 expansion of a rational number. For example, the first few digits of the base 7 expansion of 1/5<sub>10</sub> = 0.12541...<sub>7</sub>, 33/4<sub>10</sub> = 11.15151...<sub>7</sub>, and 6/49<sub>10</sub> = 0.06000<sub>7</sub>. From this expansion, find the digits in a particular range of positions to the right of the "decimal" point.</p>

### 입력 

 <p>The input file begins with a line containing a single integer specifying the number of problem sets in the file. Each problem set is specified by four base 10 numbers on a single line, n d f l, where n and d are the numerator and denominator of the rational number and 0 ≤ n ≤ 5,000 and 1 ≤ d ≤5,000. f and l are the first and last positions for the desired range of digits, with 0 ≤ f, l ≤ 250 and 0 ≤ (l-f) ≤ 20. Note that 0 is the position immediately to the right of the decimal point.</p>

### 출력 

 <p>Each problem set will be numbered (beginning at one) and will generate a single line:</p>

<p>Problem set k: n / d, base 7 digits f through l: result</p>

<p>where k is replaced by the problem set number, result is your computed result, and the other values are the corresponding input values. Make sure your output is formatted as shown in the sample output below.</p>

