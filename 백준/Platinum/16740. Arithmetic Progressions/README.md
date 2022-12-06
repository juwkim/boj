# [Platinum V] Arithmetic Progressions - 16740 

[문제 링크](https://www.acmicpc.net/problem/16740) 

### 성능 요약

메모리: 99892 KB, 시간: 596 ms

### 분류

자료 구조(data_structures), 다이나믹 프로그래밍(dp), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p>An arithmetic progression is a sequence of numbers a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>k</sub> where the difference of consecutive members a<sub>i+1</sub> − a<sub>i</sub> is a constant (1 ≤ i ≤ k −1). For example, the sequence 5, 8, 11, 14, 17 is an arithmetic progression of length 5 with the common difference 3.</p>

<p>In this problem, you are requested to find the longest arithmetic progression which can be formed selecting some numbers from a given set of numbers. For example, if the given set of numbers is {0, 1, 3, 5, 6, 9}, you can form arithmetic progressions such as 0, 3, 6, 9 with the common difference 3, or 9, 5, 1 with the common difference −4. In this case, the progressions 0, 3, 6, 9 and 9, 6, 3, 0 are the longest.</p>

### 입력 

 <p>The input consists of a single test case of the following format.</p>

<pre>n
v<sub>1</sub> v<sub>2</sub> ··· v<sub>n</sub></pre>

<p>n is the number of elements of the set, which is an integer satisfying 2 ≤ n ≤ 5000. Each v<sub>i</sub> (1 ≤ i ≤ n) is an element of the set, which is an integer satisfying 0 ≤ v<sub>i</sub> ≤ 10<sup>9</sup>. v<sub>i</sub>’s are all different, i.e., v<sub>i</sub> ≠ v<sub>j</sub> if i ≠ j.</p>

### 출력 

 <p>Output the length of the longest arithmetic progressions which can be formed selecting some numbers from the given set of numbers.</p>

