# [Silver IV] Investigating Zeroes and Ones - 29994 

[문제 링크](https://www.acmicpc.net/problem/29994) 

### 성능 요약

메모리: 120836 KB, 시간: 128 ms

### 분류

다이나믹 프로그래밍, 누적 합

### 제출 일자

2023년 11월 24일 08:01:19

### 문제 설명

<p>You find yourself in a mysterious binary world, where an array of N binary digits awaits your scrutiny. Each digit is either a zero or a one, creating a unique pattern across the landscape. Your quest is to uncover the hidden patterns of this binary realm by unraveling the significance of subarrays with an odd number of ones.</p>

<p>The array of digits is denoted as b<sub>1</sub>, b<sub>2</sub>, . . . , b<sub>N</sub>. Your task is to embark on a journey to discover the enigmatic subarrays – segments of consecutive digits – and determine the count of subarrays that harbor an odd number of ones.</p>

<p>As you traverse this binary landscape, remember that a subarray is defined by its starting and ending digits. For instance, in the sequence [b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub>], subarrays include [b<sub>1</sub>], [b<sub>2</sub>], [b<sub>3</sub>], [b<sub>1</sub>, b<sub>2</sub>], [b<sub>2</sub>, b<sub>3</sub>], and [b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub>].</p>

<p>Your mission is to design an algorithm that determines the total number of subarrays containing an odd number of ones within this binary sequence. Please don’t forget that the answer might not fit in a 32-bits integer.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 10<sup>5</sup>) representing the length of the binary sequence.</p>

<p>The second line contains N binary digits b<sub>1</sub>, b<sub>2</sub>, . . . , b<sub>N</sub> (b<sub>i</sub> ∈ {0, 1}) representing the elements of the sequence.</p>

### 출력 

 <p>Output a single line with an integer representing the count of subarrays in the sequence that hold an odd number of ones.</p>

