# [Silver V] Array Manipulation at Moloco (Easy) - 15516 

[문제 링크](https://www.acmicpc.net/problem/15516) 

### 성능 요약

메모리: 30840 KB, 시간: 160 ms

### 분류

구현(implementation)

### 문제 설명

<p>At Moloco, management and analysis of big data is an important part of its core business solution. One day, a very complicated issue was raised by a fellow employee, and you need to help resolve it.</p>

<p>You are given an array <em>A</em> of <em>n</em> distinct integers that describe the raw data. You need to manipulate this array to obtain a new array <em>S</em> of <em>n</em> integers where <em>S</em>[i] = |{j : (1 ≤ j < <em>i</em>) ∧ (<em>A</em>[<em>j</em>] < <em>A</em>[<em>i</em>])}|. </p>

<p>For instance, if <em>A</em> = [10, 5, 12, 1, 11], then <em>S</em> = [0, 0, 2, 0, 3]. </p>

### 입력 

 <p>The first line contains an integer <em>n</em> between 1 and 1,000.</p>

<p>The following <em>n</em> lines contain one integer per line where <em>i</em>+1th line describes <em>A</em>[<em>i</em>]. Assume |<em>A</em>[<em>i</em>]| ≤ 2,000,000,000.</p>

### 출력 

 <p>Your output should consist of <em>n</em> lines where <em>i</em>th line contains a single integer that describes <em>S</em>[<em>i</em>].</p>

