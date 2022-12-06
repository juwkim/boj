# [Silver V] Gene Shuffle - 5390 

[문제 링크](https://www.acmicpc.net/problem/5390) 

### 성능 요약

메모리: 146280 KB, 시간: 292 ms

### 분류

자료 구조(data_structures), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>The genomes of two related species, like that of cabbage and turnip, may contain similar genes. Their order in the genome may be different due to genome transpositions during evolution.</p>

<p>Your task is to compare two gene sequences, and to determine the segments that are common to the genomes, i.e., the segments that contain the same genes in both genomes (although in a possibly different order).</p>

<p>Genes in this application are not given by sequences of bases A, C, G and T as is usually done, but are coded as a single integer. The two genomes that are compared consist of the same set of integers, each a permutation of the numbers 1,... ,N, where N is the length of the genome. A common segment i-j of the genomes is an interval 1 ≤ i ≤ j ≤ N such that elements starting at position i and ending at position j of the first genome make up the same set of genes (integers) as the elements at the same positions in the second genome, but possibly in a different order. We are looking for minimal common segments, i.e., segments cannot contain smaller segments.</p>

### 입력 

 <p>The first line of the input contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line with one integer N, satisfying 1 ≤ N ≤ 100, 000: the length of the genome.</li>
	<li>One line with a permutation of the N integers 1,... ,N, representing the first genome.</li>
	<li>One line with a permutation of the N integers 1,... ,N, representing the second genome.</li>
</ul>

<p>Integers on the same line are separated by single spaces.</p>

### 출력 

 <p>For every test case in the input, the output should contain a single line, listing the minimal segments i-j common to the two genomes, ordered from left to right. Segments are separated by single spaces.</p>

