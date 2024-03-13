# [Silver III] Weighted Window Sums - 30218 

[문제 링크](https://www.acmicpc.net/problem/30218) 

### 성능 요약

메모리: 152588 KB, 시간: 520 ms

### 분류

수학, 누적 합, 정렬

### 제출 일자

2024년 3월 14일 02:39:22

### 문제 설명

<p>Given a sequence of numbers, we define a window within the sequence to be a contiguous subsequence of those numbers. For example, in the sequence [3, 6, 2, 3, 5, 4], there are four windows of size 3: [3, 6, 2], [6, 2, 3], [2, 3, 5] and [3, 5, 4]. We call window i of size k the window which starts with the i<sup>th</sup> value in the list and includes exactly k consecutive values, ending with the (i+k-1)<sup>th</sup> value in the list.</p>

<p>For a window with values a<sub>1</sub>, a<sub>2</sub>, …, a<sub>k</sub>, define its weighted window sum to be:</p>

<p style="text-align: center;">1a<sub>1</sub> + 2a<sub>2</sub> + 3a<sub>3</sub> + … + ka<sub>k</sub></p>

<p>For the four window sums described above, the corresponding weighted window sums are:</p>

<p style="text-align: center;">[3, 6, 2] → 1 × 3 + 2 × 6 + 3 × 2 = 21 (Rank 2)</p>

<p style="text-align: center;">[6, 2, 3] → 1 × 6 + 2 × 2 + 3 × 3 = 19 (Rank 1)</p>

<p style="text-align: center;">[2, 3, 5] → 1 × 2 + 2 × 3 + 3 × 5 = 23 (Rank 3)</p>

<p style="text-align: center;">[3, 5, 4] → 1 × 3 + 2 × 5 + 3 × 4 = 25 (Rank 4)</p>

<p>For each window of a given size within a sequence of numbers, we sort those windows in increasing order of weighted window sum, breaking ties by the starting index of the window, from smallest index to largest index.</p>

<p>Given a sequence of integers and the size of a window, sort each window of the given size in the sequence by weighted window sum in increasing order, breaking ties by the starting index of the window.</p>

### 입력 

 <p>The first input line contains two integers: n (1 ≤ n ≤ 2 × 10<sup>5</sup>) and k (1 ≤ k ≤ n), representing the length of the sequence and the size of the window. Each of the next n input lines will contain one number of the sequence, in order. Each of these values will be in between 1 and 10<sup>8</sup>, inclusive.</p>

### 출력 

 <p>Print a sorted list of the windows, with one window per line. For each window, output its starting index, followed by the weighted window sum of that window.</p>

