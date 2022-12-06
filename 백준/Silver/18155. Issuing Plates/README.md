# [Silver V] Issuing Plates - 18155 

[문제 링크](https://www.acmicpc.net/problem/18155) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>You are writing the code to check license plates. These consist of upper letters ‘A’–‘Z’ and numbers ‘0’–‘9’. You want to make sure the codes do not contain any bad words, even considering leetspeak.</p>

<p>Given some input strings, which are valid license plates?</p>

<p>In leetspeak we have the following equivalences: 0=O 1=L 2=Z 3=E 5=S 6=B 7=T 8=B</p>

### 입력 

 <p>The first line will contain the integers N and M with 0 ≤ N, M ≤ 100. Following this will be N lines containing bad words; each such word will contain only uppercase alphabetic characters (‘A’–‘Z’) and be at most 25 characters long. Then there will be M lines containing the plates to check; each such plate will consist of only uppercase alphabetic characters and numeric digits (‘0’–‘9’) and be at most 25 characters long.</p>

### 출력 

 <p>Your output will be M lines, one per plate, in the same order as the plates are given on the input. If the plate is valid, write out the string ‘VALID’; otherwise write out the string ‘INVALID’.</p>

