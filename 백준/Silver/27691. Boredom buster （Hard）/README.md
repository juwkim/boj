# [Silver I] Boredom buster (Hard) - 27691 

[문제 링크](https://www.acmicpc.net/problem/27691) 

### 성능 요약

메모리: 109108 KB, 시간: 116 ms

### 분류

다이나믹 프로그래밍, 수학

### 제출 일자

2024년 3월 18일 13:55:12

### 문제 설명

<p>Gillian is normally a very lively child. Most of the time she plays with her friends and tries to indulge in some mischief. But today is diﬀerent, today Gillian woke up with the ﬂu so she has to stay in bed – still and bored. To entertain her, her brother came up with the following game.</p>

<p>When Gillian has an integer x greater than 1, she can split it up into two positive integers y and z such that x = y + z. After performing this operation, her brother gives her y ⋅ z hazelnuts. However, not all pairs of y,z are valid – there are some rules Gillian must comply with. These rules diﬀer between the easy and hard subproblems; they are listed in the problem speciﬁcation section.</p>

<p>Numbers that are obtained as a result of this operation can be also split up. At the beginning of the game, Gillian starts with a single integer n. She performs a series of operations described above until she is left with n copies of number 1. What is the maximum number of hazelnuts she can win if she chooses her moves wisely?</p>

<p>Gillian can pick any integer k satisfying 1 < k ≤ x and split up number x into y = ⌊x∕k⌋ and z = x −⌊x∕k⌋.</p>

### 입력 

 <p>The ﬁrst line of the input ﬁle contains an integer t ≤ 1000 specifying the number of test cases. Each test case is preceded by a blank line.</p>

<p>Each test case contains a single line with Gillian’s initial integer n > 1. You may assume that n ≤ 10<sup>9</sup>.</p>

### 출력 

 <p>For each test case, output a single line with the maximum number of hazelnuts.</p>

