# [Silver II] Lexical - 9912 

[문제 링크](https://www.acmicpc.net/problem/9912) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

조합론, 수학

### 제출 일자

2025년 1월 8일 20:27:47

### 문제 설명

<p>A permutation of a set is a sequence in which every element of the set occurs exactly once.  For example, the sequence 3201 is a permutation of the set {0, 1, 2, 3}, where the number 3 appears first, the number 2 appears second, the number 0 appears third and the number 1 appears last in the sequence.  We can order the permutations of a set in a “lexicon” by looking at the first position where the permutations are different.  For example, the permutation 3201 appears before 3210 in the lexicon, because at the first position where the permutations are different, the first permutation has a 0 whereas the second permutation has a bigger number, namely 1.</p>

<p>Given an integer n (1 ≤ n ≤ 13) and a permutation of the set { 0, 1, 2, …, n – 1 }, determine the position of the permutation in the lexicon.</p>

<p>Example: For n = 4, the lexicon has 24 entries and looks like this:</p>

<p style="text-align: center;">0123,   0132,   0213,   0231,   0312,   0321,   1023,   1032,   1203, … ,   3201,   3210.</p>

<p>The permutation 3 2 0 1 appears at position 23.</p>

<p>The task is to determine at which position a given permutation appears in the lexicon.</p>

<p>Hint: If n is close to 13, it will be too slow to construct the entire lexicon, because the size of the lexicon is 1 × 2 × 3 × ... × n.</p>

### 입력 

 <p>The input consists of the following two lines:</p>

<ol>
	<li>The first line contains an integer indicating the number n.</li>
	<li>The second line consists of a permutation, namely a sequence of numbers from { 0, 1, 2, …, n – 1 } separated by a space.</li>
</ol>

### 출력 

 <p>The output contains a single integer value, which is the position of the permutation in the lexicon.</p>

