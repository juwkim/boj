# [Bronze II] Laps - 16623 

[문제 링크](https://www.acmicpc.net/problem/16623) 

### 성능 요약

메모리: 41532 KB, 시간: 108 ms

### 분류

애드 혹(ad_hoc), 사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Bethany is training for an athletics contest. Yesterday, she ran laps around an oval athletics track. She recorded her location on the track every minute. She has now forgotten how many laps she did yesterday. Bethany has given you this list of locations on the track. Each location is the number of metres Bethany has run since the last time she passed the start point. Bethany always starts at the start point. Note that it is possible that Bethany does not move between two entries in the list. However, she will never run backwards. The athletics track is n metres long. This means that if Bethany ran n metres in total she would return to the start point.</p>

<p>Suppose you have a 300 metre long track and Bethany ran 200 metres from the start point. Bethany would record 200. Then, if she ran another 200 metres, she would record 100 having crossed the start point.</p>

<p>She wants to determine the minimum number of laps she could have completed. Can you help?</p>

### 입력 

 <p>The first line of input contains two integers n (1 ≤ n ≤ 10<sup>9</sup>) and m (1 ≤ m ≤ 10<sup>5</sup>), the length of the track and the number of locations Bethany recorded in her list. The next line contains m integers each of which is at least 0 and at most n − 1. These are the list of locations Bethany recorded. The list is in increasing order of time.</p>

### 출력 

 <p>Display the minimum number of laps Bethany could have completed.</p>

