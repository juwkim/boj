# [Silver V] Ambiguous permutations - 6526 

[문제 링크](https://www.acmicpc.net/problem/6526) 

### 성능 요약

메모리: 136868 KB, 시간: 232 ms

### 분류

구현(implementation), 순열 사이클 분할(permutation_cycle_decomposition)

### 문제 설명

<p>Some programming contest problems are really tricky: not only do they require a different output format from what you might have expected, but also the sample output does not show the difference. For an example, let us look at permutations.</p>

<p>A permutation of the integers <em>1</em> to <em>n</em> is an ordering of these integers. So the natural way to represent a permutation is to list the integers in this order. With <em>n = 5</em>, a permutation might look like 2, 3, 4, 5, 1.</p>

<p>However, there is another possibility of representing a permutation: You create a list of numbers where the <em>i</em>-th number is the position of the integer <em>i</em> in the permutation. Let us call this second possibility an inverse permutation. The inverse permutation for the sequence above is 5, 1, 2, 3, 4.</p>

<p>An ambiguous permutation is a permutation which cannot be distinguished from its inverse permutation. The permutation 1, 4, 3, 2 for example is ambiguous, because its inverse permutation is the same. To get rid of such annoying sample test cases, you have to write a program which detects if a given permutation is ambiguous or not.</p>

### 입력 

 <p>The input contains several test cases.</p>

<p>The first line of each test case contains an integer <em>n</em> (<em>1 ≤ n ≤ 100000</em>). Then a permutation of the integers <em>1</em> to <em>n</em> follows in the next line. There is exactly one space character between consecutive integers. You can assume that every integer between <em>1</em> and <em>n</em> appears exactly once in the permutation.</p>

<p>The last test case is followed by a zero.</p>

### 출력 

 <p>For each test case output whether the permutation is ambiguous or not. Adhere to the format shown in the sample output.</p>

