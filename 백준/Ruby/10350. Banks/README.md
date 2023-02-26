# [Ruby V] Banks - 10350 

[문제 링크](https://www.acmicpc.net/problem/10350) 

### 성능 요약

메모리: 115160 KB, 시간: 996 ms

### 분류

애드 혹(ad_hoc), 수학(math), 누적 합(prefix_sum)

### 문제 설명

<p>On Wall Street from Wonderland, we have n banks, with 10000 > n > 0. Each bank has exactly two neighbours, the left (L) and right (R) neighbour. The first bank’s left neighbour is the last bank, while the last bank’s right neighbour is the first bank. Each bank i(n>i≥0) has a capital k<sub>i</sub> with 32000>k<sub>i</sub>>-32000. The entire capital of all banks put together is known to be positive. Whenever some capital k<sub>i</sub> of bank i is negative, the Bank Fairy can do a magic move and turn the capital into a positive one. For instance, if k<sub>i</sub>=-7, after the magic move, k<sub>i</sub>=7. Unfortunately, the magic move has consequences for both neighbours of bank i. Each sees its capital reduced with the absolute value of the capital of bank i. For instance if bank L has capital k<sub>L</sub>=5 and bank R has capital k<sub>R</sub>=11, then after the magic move k<sub>L</sub>=-2 and k<sub>R</sub>=4.</p>

<p>Which is the minimal number of magic moves which the Bank Fairy has to do in order to make the capital of all banks greater than or equal to 0?</p>

### 입력 

 <p>On the first input line, we have the number n of banks. On the second input line, we have the capitals k<sub>i</sub>(n>i≥0) of all banks, in the order in which they are found on Wall Street from Wonderland. Each capital is separated by a single whitespace from the next one, except for the final capital which is directly followed by the newline character.</p>

### 출력 

 <p>The output contains a single line with the value of the minimal number of magic moves.</p>

