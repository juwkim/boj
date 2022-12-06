# [Bronze I] Casting Out Nines - 4927 

[문제 링크](https://www.acmicpc.net/problem/4927) 

### 성능 요약

메모리: 30840 KB, 시간: 1092 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>You must have heard of the great mathematician Leonardo da Pisa Fibonacci (1170-1240). Among the many algorithms that he described in his Liber Abaci book, (which was first published in 1202,) Fibonacci described the Casting Out Nines procedure for checking out addition, subtraction, and multiplication. According to historians, the procedure was transmitted to Europe by the Arabs, but was probably developed somewhere on the Indian subcontinent and is therefore sometimes also called “the Hindu check.”</p>

<p>“Casting out nines” is an elementary check of a multiplication which makes use of the congruence 10x ≡ 1 (mod 9). Remember that when writing x ≡ y (mod z) we’re actually saying that (x mod z) is equal to (y mod z).</p>

<p>Let a, b be natural numbers whose product is c. Let the sums of the digits of these numbers be a ̄,  ̄b, a n d c ̄ . T h e n a ≡ a ̄ ( m o d 9 ) , b ≡  ̄b ( m o d 9 ) , a n d c ≡ c ̄ ( m o d 9 ) . F u r t h e r m o r e a × b ≡ a ̄ ×  ̄b ( m o d 9 ) , and so a ̄ ×  ̄b ≡ c ̄ (mod 9). So if c and a ̄ ×  ̄b are incongruent (mod 9), the multiplication has been done incorrectly.</p>

<p>For example, 12345 × 67890 = 838102050. The sum-of-digits of 12345 and 67890 are 15 and 30, respectively, and the product of these is 450. Similarly, the sum-of-digits of 838102050 is 27. And since 450 ≡ 27 ≡ 0 (mod 9), so the Hindu Check shows agreement.</p>

<p>As another example, say someone incorrectly calculates 13579×24680 = 334129720. Since a ̄× ̄b = 25 × 20 = 500 ≡ 5 (mod 9) whereas c ̄ = 31 ≡ 4 (mod 9). So the multiplication is definitely incorrect.</p>

<p>The Hindu check can also be used to check on additions, since a + b ≡ a ̄ +  ̄b (mod 9).</p>

<p>Write a program that determines if a given addition or multiplication passes the Hindu Check or not.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. Each test case is specified on a separate input line. Each line is of the form:</p>

<p>a+b=c.</p>

<p>Or,</p>

<p>a*b=c.</p>

<p>Notice the ’.’ at the end of the line. ’a’, ’b’, and ’c’ are natural numbers. There are no spaces between the numbers and the symbols (’+’, ’*’, ’=’, and ’.’,) but trailing white-space may appear after the ’.’.</p>

<p>The last line of the input file, which is not part of the test cases, will have a single ’.’.</p>

### 출력 

 <p>For each test case, output the result on a single line using the following format:</p>

<p>k.␣result</p>

<p>Where k is the test case number (starting at 1,) and result is "PASS" if the addition or multiplication operation of this test case passes the Hindu Check. Otherwise, result is "NOT!".</p>

