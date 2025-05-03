# [Silver I] Sheldon Numbers - 11684 

[문제 링크](https://www.acmicpc.net/problem/11684) 

### 성능 요약

메모리: 110760 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2025년 5월 4일 00:18:43

### 문제 설명

<p>According to Sheldon Cooper, the best number is 73. In his own words, “The best number is 73. 73 is the 21st prime number. Its mirror, 37, is the 12th, and its mirror, 21, is the product of multiplying 7 and 3. In binary, 73 is a palindrome: 1001001, which backwards is 1001001. Exactly the same.”</p>

<p>Prime numbers are boring stuff, and so are palindromes. On the other hand, the binary representation of 73 is rather remarkable: it’s 1 one followed by 2 zeroes, followed by 1 one, followed by 2 zeros, followed by 1 one. This is an interesting pattern that we can generalize: N ones, followed by M zeros, followed by N ones, followed by M zeros, etc, ending in either N ones or M zeroes. For 73, N is 1, M is 2, and there are 5 runs of equal symbols. With N = 2, M = 1 and 4 runs, we would have the string 110110, which is the binary representation of 54.</p>

<p>Acknowledging Sheldon’s powerful insight, let us introduce the concept of a Sheldon number: a positive integer whose binary representation matches the pattern ABABAB . . . ABA or the pattern ABABAB . . . AB, where all the occurrences of A represent a string with N occurrences of the bit 1 and where all the occurrences of B represent a string with M occurrences of the bit 0, with N > 0 and M > 0. Furthermore, in the representation, there must be at least one occurrence of the string A (but the number of occurrences of the string B may be zero).</p>

<p>Many important numbers are Sheldon numbers: 1755, the year of the great Lisbon earthquake, 1984, of Orwellian fame, and 2015, the current year! Also, 21, which Sheldon mentions, is a Sheldon number, and so is 42, the answer given by the Deep Thought computer to the Great Question of Life, the Universe and Everything.</p>

<p>Clearly, there is an infinite number of Sheldon numbers, but are they more dense or less dense than prime numbers?</p>

<p>Your task is to write a program that, given two positive integers, computes the number of Sheldon numbers that exist in the range defined by the given numbers.</p>

### 입력 

 <p>The input contains one line, with two space separated integer numbers, X and Y.</p>

### 출력 

 <p>The output contains one line, with one number, representing the number of Sheldon numbers that are greater or equal to X and less or equal to Y.</p>

