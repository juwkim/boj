# [Silver I] Special Substring - 21014 

[문제 링크](https://www.acmicpc.net/problem/21014) 

### 성능 요약

메모리: 111556 KB, 시간: 132 ms

### 분류

문자열, 누적 합, 슬라이딩 윈도우

### 제출 일자

2025년 5월 8일 18:48:42

### 문제 설명

<p>A substring of a string is a contiguous sequence of characters from the string. For example, <code>BC</code> is a substring of <code>ABCD</code> which starts from the second character of <code>ABCD</code>. Another example, <code>ABC</code> is a substring of <code>ABCD</code> which starts from the first character of <code>ABCD</code>. Note that <code>ABCD</code> itself is also a substring of <code>ABCD</code>.</p>

<p>In this problem, we define a special substring as a non-empty substring that contains only the same character. For example, <code>B</code> and <code>CC</code> are special substrings of <code>ABBCCC</code>, while <code>ABBC</code> and <code>BC</code> are not special substrings.</p>

<p>You are given a string S of length N and an integer K. Your task is to determine the minimum number of characters of S that need to be changed such that there exists a special substring of length K in S.</p>

<p>For example, let N = 6, K = 4, and S = <code>ABBCCC</code>. In this example, we only need to change the third character of S to C (i.e. <code>ABBCCC</code> → <code>ABCCCC</code>) so that we have a special substring <code>CCCC</code> of length 4.</p>

### 입력 

 <p>Input begins with a line containing two integers: N K (1 ≤ K ≤ N ≤ 100 000) representing the length of the string and the length of a special substring that should be produced, respectively. The next line contains a string S containing N uppercase alphabetical character, i.e. S<sub>i</sub> ∈ [<code>A-Z</code>].</p>

### 출력 

 <p>Output in a line an integer representing the minimum number of characters of S that need to be changed such that there exists a special substring of length K in the given S.</p>

