# [Silver III] Eeny Meeny Moo - 6602 

[문제 링크](https://www.acmicpc.net/problem/6602) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘, 자료 구조, 구현, 큐, 시뮬레이션

### 제출 일자

2024년 3월 9일 23:41:17

### 문제 설명

<p>Surely you have made the experience that when too many people use the Internet simultaneously, the net becomes very, very slow.</p>

<p>To put an end to this problem, the University of Ulm has developed a contingency scheme for times of peak load to cut off net access for some cities of the country in a systematic, totally fair manner. Germany's cities were enumerated randomly from 1 to <em>n</em>. Freiburg was number 1, Ulm was number 2, Karlsruhe was number 3, and so on in a purely random order.</p>

<p>Then a number <em>m</em> would be picked at random, and Internet access would first be cut off in city 1 (clearly the fairest starting point) and then in every <em>m</em>th city after that, wrapping around to 1 after <em>n</em>, and ignoring cities already cut off. For example, if <em>n</em>=17 and <em>m</em>=5, net access would be cut off to the cities in the order [1,6,11,16,5,12,2,9,17,10,4,15,14,3,8,13,7]. The problem is that it is clearly fairest to cut off Ulm last (after all, this is where the best programmers come from), so for a given <em>n</em>, the random number <em>m</em> needs to be carefully chosen so that city 2 is the last city selected.</p>

<p>Your job is to write a program that will read in a number of cities <em>n</em> and then determine the smallest integer <em>m</em> that will ensure that Ulm can surf the net while the rest of the country is cut off.</p>

### 입력 

 <p>The input file will contain one or more lines, each line containing one integer <em>n</em> with 3 ≤ <em>n</em> < 150, representing the number of cities in the country. Input is terminated by a value of zero (0) for <em>n</em>.</p>

### 출력 

 <p>For each line of the input, print one line containing the integer <em>m</em> fulfilling the requirement specified above.</p>

