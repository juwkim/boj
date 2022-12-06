# [Bronze I] PUTOVANJE - 11923 

[문제 링크](https://www.acmicpc.net/problem/11923) 

### 성능 요약

메모리: 30840 KB, 시간: 184 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Young Mislav loves spending time in nature and, most of all, he loves spending time in forests. The fresh air and lovely sounds make the forest his favourite location. Mislav has decided to spend this afternoon in a forest and, because he’s so practical, he’s also decided to stuff himself with food. His belly can contain C amount of food.</p>

<p>He will have the opportunity to eat various fruits of nature (mushrooms, chestnuts, berries, and so on) while walking through the forest. All fruits are mutually different given their type and he’d like to eat as much different fruits as possible, but with the condition that he doesn’t overeat. In other words, the total weight of the fruits he’s eaten must not be larger than C. Also, when Mislav decides to start eating, he tries to eat every next fruit if it’s possible to eat it and not overeat. In the case when he doesn’t have the capacity to eat it, he just moves on.</p>

<p>An array of weights of N fruits represents the weight and order of fruits that Mislav came across in the forest. Determine the maximum amount of different fruits that Mislav can eat.</p>

### 입력 

 <p>The first line of input contains two integers N and C (1 ≤ N ≤ 1 000, 1 ≤ C ≤ 1 000 000) from the task.</p>

<p>The second line contains N integers w<sub>i</sub> (1 ≤ w<sub>i</sub> ≤ 1000) that represent the fruits’ weight.</p>

### 출력 

 <p>The first and only line of output must contain the maximum possible amount of different fruits that Mislav can eat.</p>

