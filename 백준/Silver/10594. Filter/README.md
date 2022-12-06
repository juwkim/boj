# [Silver IV] Filter - 10594 

[문제 링크](https://www.acmicpc.net/problem/10594) 

### 성능 요약

메모리: 1316 KB, 시간: 8 ms

### 분류

비트마스킹(bitmask), 비트 집합(bitset), 구현(implementation)

### 문제 설명

<p>You are working on a new high-performance database engine — Instant Compression and Processing Codec (ICPC). ICPC stores user activity records. Each user activity record has an integer user identifier. The records are stored in a number of data files. Each data file is compressed and can contain records from multiple users, however ICPC has to process queries that look for a specific subsets of users. In order to do so, there has to be a way to quickly determine which data files may contain records for a specific user before attempting to decompress them, which may be a long and CPU-consuming process.</p>

<p>ICPC uses an algorithm called Bloom Filter. The way it is implemented in ICPC is described below. For each ICPC database the following integer parameters are chosen:</p>

<ul>
	<li>m is the number of bits in the filter;</li>
	<li>f is the number of hash functions in the filter;</li>
	<li>a<sub>i</sub> are the parameters for hash functions for 0 ≤ i < f.</li>
</ul>

<p>A value of the bloom filter is computed for each data file. The data file’s bloom filter is a vector of m bits. A bit number j (0 ≤ j < m) is set to one if and only if there is a record in this data file for some user identifier u<sub>k</sub>, such that for some hash function i (0 ≤ i < f) the following equality holds:</p>

<p style="text-align:center">j = (u<sub>k</sub> · a<sub>i</sub>) mod m (1)</p>

<p>Your task is to implement ICPC filtering logic. You are given filter parameters and values for a number of data files and a set of user identifiers. Your task is determine which data files may contain record with at least one user identifier from the specified set. A data file may contain a record with a user identifier u<sub>k</sub> if and only if for all i (0 ≤ i < f) all the bits j given by equality (1) in its filter value are set to one.</p>

### 입력 

 <p>The first line of the input file contains filter parameters — integer numbers m, f, and a<sub>i</sub> for 0 ≤ i < f (1 ≤ m ≤ 1000, 1 ≤ f ≤ 100, 1 ≤ a<sub>i</sub> < 2<sup>31</sup>).</p>

<p>The second line of the input file contains an integer n — the number of data files (1 ≤ n ≤ 1000). Each of the following n lines contains bloom filter value of the corresponding file in hexadecimal form. Each value is represented by a string of ⌈m/4⌉ hexadecimal digits (one of 0123456789abcdef). The first digit of the string represents bits 0–3 of the value (stored in order from the least significant bit of a hexadecimal digit to the most significant bit), the second digit — bits 4–7, the third — 8–11, etc. When m mod 4 ≠ 0, then the last hexadecimal digit represents the last m mod 4 bits of the value in its least significant bits.</p>

<p>The following line of the input file contains an integer q — the number of user identifiers in a query (1 ≤ q ≤ 1000), followed by q integers u<sub>k</sub> — the set of distinct user identifiers in the query (1 ≤ u<sub>k</sub> < 2<sup>31</sup>).</p>

### 출력 

 <p>Write a line with the integer number s to the output file — the number of data files that may contain a record with at least one user identifier from the specified set, followed by s numbers d<sub>t</sub> (0 ≤ d<sub>t</sub> < n) — the 0-based numbers of the corresponding data files in ascending order.</p>

