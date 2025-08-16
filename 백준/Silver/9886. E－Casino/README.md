# [Silver I] E-Casino - 9886 

[문제 링크](https://www.acmicpc.net/problem/9886) 

### 성능 요약

메모리: 110720 KB, 시간: 100 ms

### 분류

비트마스킹, 브루트포스 알고리즘, 슬라이딩 윈도우

### 제출 일자

2025년 8월 16일 16:27:58

### 문제 설명

<p>A <em>pseudo random number generator</em> (PRNG) is a program that, taking an input (known as seed), outputs a sequence of random bits r[0], r[1], . . .. (The value of a bit is either 0 or 1.)</p>

<p>Consider a particular PRNG and a seed. A <em>gambler</em> is a person (or a computer) who has observed the first L bits of the output r[0], r[1], . . ., r[L − 1]. The gambler knows the algorithm of that particular PRNG, and hence is aware of the internal mechanism of random bits generation. However, he does not know the value of the seed. With the knowledge of the PRNG algorithm and the first L bits r[0], r[1], . . ., r[L − 1], the gambler wants to predict the subsequent output bits r[L], r[L + 1], . . ., that follow the observed bits.</p>

<p>It is not easy to design a PRNG that is unpredictable. The company E-Casino employs the following method. First, by observing some natural phenomenon, the company created a long sequence of N random bits S[0], S[1], . . ., S[N − 1]. This array S is made public and everyone, including gamblers, can access it. The seed is a tuple (k, m), which consists of an integer k (0 ≤ k < N) and an M-bit sequence m = hm[0], m[1], . . . , m[M − 1]i. For j = 0, 1, 2, . . ., the output bit r[j] is</p>

<p style="text-align: center;">r[j] = S[(k + j) mod N] xor m[j mod M]. (1)</p>

<p>The operator xor is the “exclusive or” operation. That is, for any bits a, b,</p>

<p style="text-align: center;">a xor b = (a + b) mod 2.</p>

<p>The company <em>always</em> uses</p>

<p style="text-align: center;">N = 2048, M = 32.</p>

<p>But every morning, the managers of E-Casino will collectively choose a secret seed (k, m), which is to be used in generating a random sequence.</p>

<p>Suppose you are the gambler and for a particular day you have observed the first 2M = 64 bits of the output sequence: r[0], r[1], . . ., r[63]. You also know the values of the array S. However, you do not know the value k and the sequence m. Your ultimate goal is to determine the subsequent bits. In order to do that however, you have to first determine the value of k in the secret seed (k, m). In this task, you are to find the smallest possible k.</p>

### 입력 

 <p>The input contains only one line. The first 2M characters of the input are the observed bits r[0], r[1], . . ., r[2M − 1]. Each bit is represented by the character ‘0’ or ‘1’. The very first character represents r[0], followed by r[1] and so on. Immediately following the 2M characters is the character ‘%’, which marks the start of the array S. The array S is represented as a string of ‘0’ and ‘1’. The first character immediately following the marker ‘%’ is S[0], and the next character is S[1], and so on. In total, the input consists of 2M + 1 + N = 2113 input characters.</p>

<p>Note that for your task it is always N = 2048 and M = 32. But for the given example N = 10 and M = 3.</p>

### 출력 

 <p>The output file contains an integer, which is the secret k.</p>

