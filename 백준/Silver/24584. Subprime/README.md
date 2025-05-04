# [Silver I] Subprime - 24584 

[문제 링크](https://www.acmicpc.net/problem/24584) 

### 성능 요약

메모리: 127136 KB, 시간: 152 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체, 문자열

### 제출 일자

2025년 5월 4일 09:04:11

### 문제 설명

<p>There is an open math problem: Is every non-negative integer a substring of at least one prime number when expressed in base ten?</p>

<p>A positive integer is a prime number if it is greater than one and not a product of two smaller positive integers. Integer a is a substring of integer b if it is equal to an integer derived from b by deleting zero or more consecutive digits of the most and least significant digits of b. For example, 123 is a substring of: <u>123</u>, 56<u>123</u>, <u>123</u>789, 501823<u>123</u>65, 4<u>123</u>7912<u>123</u>.</p>

<p>Given two integers l and h along with an integer p, you are to check how many primes between the lth smallest prime and the hth smallest prime (both ends are inclusive) contain a substring that equals p. We are interested in substrings that may include significant leading zeroes, and thus p may have leading zeroes. A prime shall be counted only once even if the integer p occurs more than once as its substring.</p>

<p>For example, consider l = 1, h = 10 and p = 9. This is a search from the 1st smallest prime (2) to the 10th smallest prime (29) for any prime containing the substring “9”. There are 2 such primes: 1<u>9</u> and 2<u>9</u>.</p>

### 입력 

 <p>The first line of input has two integers l and h (1 ≤ l ≤ h ≤ 10<sup>5</sup>). The second line has a sequence of 1 to 6 digits giving the integer p, which may be zero or have significant leading zeroes.</p>

### 출력 

 <p>Output the count of prime numbers in the given range that contain p as a substring.</p>

