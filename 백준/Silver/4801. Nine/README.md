# [Silver V] Nine - 4801 

[문제 링크](https://www.acmicpc.net/problem/4801) 

### 성능 요약

메모리: 119308 KB, 시간: 1600 ms

### 분류

브루트포스 알고리즘(bruteforcing), 많은 조건 분기(case_work), 구현(implementation), 문자열(string)

### 문제 설명

<p><img alt="" src="" style="float:right; height:467px; width:263px">Randall Munroe from xkcd.com pointed out that 9 is the most rarely used key on a microwave. Let's all share the load.</p>

<p>Given a desired cooking time, find a sequence of keys with the greatest number of 9's such that the resulting time has less than 10% error compared to the desired cooking time. In other words, if T is the desired cooking time in seconds, and T9 is the cooking time specified by the found sequence, then 10|T - T9| < T. If there are multiple possibilities, choose the one that has the smallest error (in magnitude). If there are still ties, choose the one that is lexicographically smallest.</p>

<p>For example, for T = 01:15, the times 00:68-00:82 and 1:08-1:22 have less than 10% error. Of these, 00:69, 00:79, 01:09, and 01:19 have the greatest number of 9's, and the ones with the smallest error are 00:79 and 01:19. The lexicographically smaller of these is 00:79.</p>

### 입력 

 <p>The input consists of a number of cases. For each case, the desired cooking time in MM:SS format is specified on one line. Each M or S can be any digit from 0 to 9. The end of input is indicated by 00:00.</p>

### 출력 

 <p>For each case, output on a single line the four keys to use as input to the microwave, in MM:SS format.</p>

