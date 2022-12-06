# [Bronze II] Skew Binary - 4678 

[문제 링크](https://www.acmicpc.net/problem/4678) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>When a number is expressed in decimal, the k<sup>th</sup> digit represents a multiple of 10<sup>k</sup>. (Digits are numbered from right to left, where the least significant digit is number 0.) For example,</p>

<pre>81307<sub>10</sub> = 8×10<sup>4</sup> + 1×10<sup>3</sup> + 3×10<sup>2</sup> + 0×10<sup>1</sup> + 7×10<sup>0</sup> 
     <sub>  </sub> = 80000+1000+300+0+7
     <sub>  </sub> = 81307.</pre>

<p><span style="line-height:1.6em">When a number is expressed in binary, the k<sup>th</sup> digit represents a multiple of 2<sup>k</sup>. For example,</span></p>

<pre>10011<sub>2</sub> = 1×2<sup>4</sup> + 0×2<sup>3</sup> + 0×2<sup>2</sup> + 1×2<sup>1</sup> + 1×2<sup>0</sup> 
     <sub> </sub> = 16 + 0 + 0 + 2 + 1
     <sub> </sub> = 19.</pre>

<p>In skew binary, the k<sup>th</sup> digit represents a multiple of 2<sup>k+1</sup> − 1. The only possible digits are 0 and 1, except that the least-significant nonzero digit can be a 2. For example,</p>

<pre>10120<sub>skew</sub> = 1×(2<sup>5</sup>−1) + 0×(2<sup>4</sup>−1) + 1×(2<sup>3</sup>−1) + 2×(2<sup>2</sup>−1) + 0×(2<sup>1</sup>−1) 
     <sub>    </sub> = 31 + 0 + 7 + 6 + 0
     <sub>    </sub> = 44.</pre>

<p>The first 10 numbers in skew binary are 0, 1, 2, 10, 11, 12, 20, 100, 101, and 102. (Skew binary is useful in some applications because it is possible to add 1 with at most one carry. However, this has nothing to do with the current problem.)</p>

### 입력 

 <p>The input file contains one or more lines, each of which contains an integer n. If n = 0 it signals the end of the input, and otherwise n is a nonnegative integer in skew binary. The decimal value of n will be at most 2<sup>31</sup> − 1 = 2147483647.</p>

### 출력 

 <p>For each number, output the decimal equivalent.</p>

