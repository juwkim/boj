# [Bronze I] File names - 21890 

[문제 링크](https://www.acmicpc.net/problem/21890) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Petya and Vasya love to develop their own operating systems, so Petya uses PetOS operating system on his computer, and Vasya uses VasOS on his computer.</p>

<p>One day Petya wanted to send Vasya some files from his computer, but it turned out that it was not so easy to do. The problem is that in PetOS the name of file can be any string consisting of Latin letters and dots, with length in range from 1 to 20, and VasOS only supports the names of the form <code><filename>.<extension></code>, where <code><filename></code> and <code><extension></code> are non-empty strings of Latin letters, with the length of <code><filename></code> not greater than 8, and the length of <code><extension></code> not greater than 3.</p>

<p>Help Petya to calculate how many files from his list can be transferred to Vasya without changing their name.</p>

### 입력 

 <p>The first line contains the number $n$, the number of files Petya wants to transfer ($1 \le n \le 100$). The following $n$ lines contain file names. All names have a length of 1 to 20 characters and contain only lowercase Latin letters and dots.</p>

### 출력 

 <p>Output the number of files that Petya can transfer to Vasya without renaming.</p>

