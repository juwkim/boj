# [Silver IV] Prehistoric Operating Systems - 7515 

[문제 링크](https://www.acmicpc.net/problem/7515) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

다이나믹 프로그래밍(dp)

### 문제 설명

<p>It is the year 2254. Ohio Smith is a specialist in dealing with ancient operating systems. For research purposes, he tries to install several operating systems on his computer which were used about 250 years ago.</p>

<p>Prior research has yielded the result that the order those ancient operating systems is installed in does not matter most of the time. However, the operating system of a certain brand, the DOORS OS, has an interesting quirk: Two versions of DOORS cannot be installed in succession. There always has to be another operating system installed in between (for reasons that seem to be related to some entity called MBR, but Ohio is not yet sure of the details).</p>

<p>Ohio Smith wants to install n operating systems on his computer. In how many ways can he choose between DOORS and other operating systems?</p>

<p>You are given the number of operating systems that Ohio wants to install. Your task is to compute the number of valid OS install sequences.</p>

### 입력 

 <p>The first line contains the number of scenarios.</p>

<p>Every scenario consists of a single line containing the number 1 ≤ n ≤ 40 operting systems.</p>

### 출력 

 <p>The output for every scenario begins with a line containing “Scenario #i:”, where i is the number of the scenario starting at 1.</p>

<p>Then, for each scenario, print the number of possible installation sequences on a single line.</p>

