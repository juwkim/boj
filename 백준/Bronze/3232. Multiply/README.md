# [Bronze I] Multiply - 3232 

[문제 링크](https://www.acmicpc.net/problem/3232) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

수학(math)

### 문제 설명

<p>“6 × 9 = 42” is not true for base 10, but is true for base 13. That is, 6<sub>(13)</sub> × 9<sub>(13)</sub> = 42<sub>(13)</sub> because 42<sub>(13)</sub> = 4 × 13<sup>1</sup> + 2 × 13<sup>0</sup> = 54<sub>(10)</sub>.</p>

<p>You are to write a program which inputs three integers p, q, and r and determines the base B (2 ≤ B ≤ 16) for which p × q = r. If there are many candidates for B, output the smallest one. For example, let p = 11, q = 11, and r = 121. Then we have 11<sub>(3)</sub> × 11<sub>(3)</sub> = 121<sub>(3)</sub> because 11<sub>(3)</sub> = 1 × 3<sup>1</sup> + 1 × 3<sup>0</sup> = 4<sub>(10)</sub> and 121<sub>(3)</sub> = 1 × 3<sup>2</sup> + 2 × 3<sup>1</sup>+ 1 × 3<sup>0</sup> = 16<sub>(10)</sub>. For another base such as 10, we also have 11<sub>(10)</sub> × 11<sub>(10)</sub> = 121<sub>(10)</sub>. In this case, your program should output 3 which is the smallest base. If there is no candidate for B, output 0.</p>

### 입력 

 <p>The input consists of T test cases. The number of test cases (T ) is given in the first line of the input file. Each test case consists of three integers p, q, and r in a line. All digits of p, q, and r are numeric digits and 1 ≤ p, q, r ≤ 1,000,000.</p>

### 출력 

 <p>Print exactly one line for each test case. The line should contain one integer which is the smallest base for which p × q = r. If there is no such base, your program should output 0.</p>

