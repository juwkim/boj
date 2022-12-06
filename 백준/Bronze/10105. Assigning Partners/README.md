# [Bronze I] Assigning Partners - 10105 

[문제 링크](https://www.acmicpc.net/problem/10105) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 문자열(string)

### 문제 설명

<p>The CEMC is organizing a workshop with an activity involving pairs of students. They decided to assign partners ahead of time. You need to determine if they did this consistently. That is, whenever A is a partner of B, then B is also a partner of A, and no one is a partner of themselves.</p>

### 입력 

 <p>The input consists of three lines. The first line consists of an integer N (1 < N ≤ 30), which is the number of students in the class. The second line contains the first names of the N students separated by single spaces. (Names contain only uppercase or lowercase letters, and no two students have the same first name). The third line contains the same N names in some order, separated by single spaces.</p>

<p>The positions of the names in the last two lines indicate the assignment of partners: the ith name on the second line is the assigned partner of the ith name on the third line.</p>

### 출력 

 <p>The output will be good if the two lists of names are arranged consistently, and bad if the arrangement of partners is not consistent.</p>

