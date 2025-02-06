# [Silver II] Password - 8914 

[문제 링크](https://www.acmicpc.net/problem/8914) 

### 성능 요약

메모리: 123244 KB, 시간: 624 ms

### 분류

구현, 문자열

### 제출 일자

2025년 2월 7일 07:43:11

### 문제 설명

<p>Shoulder-surfing is the behavior of intentionally and stealthily watching the screen of another person's electronic device, such as laptop computer or mobile phone. Since mobile devices prevail, it is getting serious to steal personal information by shoulder-surfing.</p>

<p>Suppose that we have a smart phone. If we touch the screen keyboard directly to enter the password, this is very vulnerable since a shoulder-surfer easily knows what we have typed. So it is desirable to conceal the input information to discourage shoulder-surfers around us. Let me explain one way to do this.</p>

<p>You are given a 6 × 5 grid. Each column can be considered the visible part of a wheel. So you can easily rotate each column wheel independently to make password characters visible. In this problem, we assume that each wheel contains the 26 upper letters of English alphabet. See the following Figure 1.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8914/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-05%20%EC%98%A4%ED%9B%84%204.21.32.png" style="height:237px; width:444px"></p>

<p style="text-align: center;">Figure 1. 6 × 5 window clips a valid grid representation for a password.</p>

<p>Assume that we have a length-5 password such as p<sub>1</sub> p<sub>2</sub> p<sub>3</sub> p<sub>4</sub> p<sub>5</sub>. In order to pass the authentication procedure, we should construct a configuration of grid space where each p<sub>i</sub> appears in the i-th column of the grid. In that situation we say that the user password is accepted.</p>

<p>Let me start with one example. Suppose that our password was set 'COMPU'. If we construct the grid as shown in Figure 2 on next page, then the authentication is successfully processed. </p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8914/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-05%20%EC%98%A4%ED%9B%84%204.23.19.png" style="height:152px; width:145px"></p>

<p style="text-align: center;">Figure 2. A valid grid representation for password 'COMPU'.</p>

<p>In this password system, the position of each password character in each column is meaningless. If each of the 5 characters in p<sub>1</sub> p<sub>2</sub> p<sub>3</sub> p<sub>4</sub> p<sub>5</sub> appears in the corresponding column, that can be considered the correct password. So there are many grid configurations allowing one password. Note that the sequence of letters on each wheel is randomly determined for each trial and for each column. In practice, the user is able to rotate each column and press “Enter” key, so a should-surfer cannot perceive the password by observing the 6 × 5 grid since there are too many password candidates. In this 6 × 5 grid space, maximally 6<sup>5</sup> =7,776 cases are possible. This is the basic idea of the proposed password system against shoulder-surfers.</p>

<p>Unfortunately there is a problem. If a shoulder-surfer can observe more than two grid plate configurations for a person, then the shoulder-surfer can reduce the searching space and guess the correct password. Even though it is not easy to stealthily observe other's more than once, this is one weakness of implicit grid passwords.</p>

<p>Let me show one example with two observed configurations for a grid password. The user password is 'COMPU', but 'DPMAG' is also one candidate password derived from the following configuration.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8914/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-05%20%EC%98%A4%ED%9B%84%204.24.52.png" style="height:181px; width:371px"></p>

<p style="text-align: center;">Figure 3. Both of 'COMPU' and 'DPMAG' are feasible password .</p>

<p>You are given two configurations of grid password from a shoulder-surfer. Suppose that you have succeeded to stealthily record snapshots of the target person‟s device (e.g. smart phone). Then your next task is to reconstruct all possible passwords from these two snapshots. Since there are lots of password candidates, you are asked for the k-th password among all candidates in lexicographical order. In Figure 3, let us show the first 5 valid password. The first 5 valid passwords are 'ABGAG', 'ABGAS', 'ABGAU', 'ABGPG' and 'ABGPS'.</p>

<p>The number k is given in each test case differently. If there does not exist a k-th password since k is larger than the number of all possible passwords, then you should print 'NO' in the output.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. The first line of each test case contains one integer, K, the order of the password you should find. Note that 1 ≤ K ≤ 7,777. Next the following 6 lines show the 6 rows of the first grid and another 6 lines represent the 6 rows of the second grid.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly the k-th password (including 'NO') in one line for each test case. </p>

