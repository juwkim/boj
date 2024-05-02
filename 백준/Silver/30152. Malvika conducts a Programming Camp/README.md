# [Silver III] Malvika conducts a Programming Camp - 30152 

[문제 링크](https://www.acmicpc.net/problem/30152) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

애드 혹, 수학

### 제출 일자

2024년 5월 2일 19:37:37

### 문제 설명

<p>After acquiring an extraordinary amount of knowledge through programming contests, Malvika decided to harness her expertise to train the next generation of Indian programmers. So, she decided to hold a programming camp. In the camp, she held a discussion session for n members (n-1 students, and herself). They are sitting in a line from left to right numbered through 1 to n.</p>

<p>Malvika is sitting in the n<sup>th</sup> spot. She wants to teach m topics of competitive programming to the students. As the people taking part in the camp are all newbies, they know none of the topics being taught, i.e., initially, the first n - 1 people in the line know none of the topics, while the n<sup>th</sup> knows all of them.</p>

<p>It takes one hour for a person to learn a topic from his neighbour. Obviously, one person cannot both teach a topic as well as learn one during the same hour. That is, in any particular hour, a person can either teach a topic that he knows to one of his neighbors, or he can learn a topic from one of his neighbors, or he can sit idly. It is also obvious that if person x is learning from person y at a particular hour, then person y must be teaching person x at that hour. Also, note that people can work parallely too, i.e., in the same hour when the 4th person is teaching the 3rd person, the 1st person can also teach the 2nd or learn from 2nd.</p>

<p>Find out the minimum number of hours needed so that each person learns all the m topics.</p>

### 입력 

 <p style="display: block; width: 0px; height: 0px; padding: 0px; border: 0px; margin: 0px; position: absolute; top: 0px; left: -9999px; opacity: 0; overflow: hidden;"> </p>

<p>The first line of input contains a single integer T denoting number of test cases.</p>

<p>The only line of each test case contains two space separated integers n, m as defined in the statement.</p>

<p style="display: block; width: 0px; height: 0px; padding: 0px; border: 0px; margin: 0px; position: absolute; top: 0px; left: -9999px; opacity: 0; overflow: hidden;"> </p>

### 출력 

 <p>For each test case, output a single integer in a line corresponding to the answer of the problem.</p>

