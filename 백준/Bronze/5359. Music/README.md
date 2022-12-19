# [Bronze I] Music - 5359 

[문제 링크](https://www.acmicpc.net/problem/5359) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Silence is useless. We need the world to be full of music. In computer music, volume is represented as an array of integers of length n. Silence in music is defined by 2 parameters c and m. Silence occurs in any sub-array of length m where the difference between the minimum element and the maximal element is no greater than c. For example if the volume array is [1,3,2,7,5,4,6,6] and m = 3, c = 2. Then silence occurs in the subarrays of size 3 indexed at 0, 4, and 5. Output the total number of silence intervals.</p>

### 입력 

 <p>The first line in the data file is an integer that represents the number of data sets to follow. Each data set is 2 lines. The first line contains n, m, c (n <= 20, m<=20, c<=1000). The second line contains n integers representing the volume array. Each integer is less than or equal to 1000.</p>

### 출력 

 <p>Print the total number of silence intervals for each data set.</p>

