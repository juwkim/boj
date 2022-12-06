# [Bronze I] Sunflowers - 16020 

[문제 링크](https://www.acmicpc.net/problem/16020) 

### 성능 요약

메모리: 29284 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Barbara plants N different sunflowers, each with a unique height, ordered from smallest to largest, and records their heights for N consecutive days. Each day, all of her flowers grow taller than they were the day before.</p>

<p>She records each of these measurements in a table, with one row for each plant, with the first row recording the shortest sunflower’s growth and the last row recording the tallest sunflower’s growth. The leftmost column is the first measurement for each sunflower, and the rightmost column is the last measurement for each sunflower.</p>

<p>If a sunflower was smaller than another when initially planted, it remains smaller for every measurement.</p>

<p>Unfortunately, her children may have altered her measurements by rotating her table by a multiple of 90 degrees.</p>

<p>Your job is to help Barbara determine her original data.</p>

### 입력 

 <p>The first line of input contains the number N (2 ≤ N ≤ 100). The next N lines each contain N positive integers, each of which is at most 10<sup>9</sup>. It is guaranteed that the input grid represents a rotated version of Barbara’s grid.</p>

### 출력 

 <p>Output Barbara’s original data, consisting of N lines, each of which contain N positive integers.</p>

