# [Bronze II] Highways - 7477 

[문제 링크](https://www.acmicpc.net/problem/7477) 

### 성능 요약

메모리: 35508 KB, 시간: 92 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>In a distant country Lineland there are <em>N</em> cities and they are all located along the highway. The highway is a straight line; it starts from the first city and runs through the second, third city and so on, ending in the <em>N</em>-th city. The <em>i</em>-th city is located at the distance of <em>X<sub>i</sub></em> miles from the first one.</p>

<p>The highway is wide and smooth, so it is a pleasure for all people to drive along it. But there is one problem — all roads in Lineland, including the highway, are one-way. So people are only allowed to drive along the highway from the city with smaller number to the city with greater number and they have to use country roads to get back, and that is not such a great pleasure indeed.</p>

<p>After the new president Mr. Pathwayson was elected in Lineland, he has decided that he would like to make it easier for people to get from one town to another. But he does not dare to change the traditions, and make the highway two-way. Therefore he has decided to build new highways to connect the cities, so that it would be possible to get from any city to any other one by highways. Traditionally, the new highways must be one-way.</p>

<p>Of course, Mr. Pathwayson is a great president, and he wants people to remember him in years. After a thought he has decided that building just one highway would not be enough for that. Therefore he has decided that he must build two new highways. Each highway would connect two different cities. Since people are anxious about their health, and cars running along the highway produce dangerous wastes, each new highway must not pass through any cities, except the cities it connects. Also building two new highways in one city would disturb people too much, so all the cities that would be the ends of the new highways must be different.</p>

<p>You are the assistant of the minister of transportation of Lineland, so you are asked to choose the cities to be connected by the new highways. Since the cost of building a highway is proportional to its length, the total length of the highways must be minimal possible. Write a program to solve this problem. You may assume that the distance between two cities along the new highway is equal to the distance between those cities along the main highway.</p>

### 입력 

 <p>The first line of the input file contains <em>N</em> (2 ≤ <em>N</em> ≤ 50 000). Next line contains <em>N</em> − 1 integer numbers: X<sub>2</sub>, X<sub>3</sub>, ... , X<sub>N</sub> (1 ≤ X<sub>2</sub> < X<sub>3</sub> < . . . < X<sub>N</sub> ≤ 10<sup>9</sup> ).</p>

### 출력 

 <p>If it is impossible to build the highways satisfying all requirements, print number 0 on the first line of the output file.</p>

<p>In the other case on the first line of the output file print the minimal possible total length of the highways to be built. On the second line print S<sub>1</sub>, E<sub>1</sub>, S<sub>2</sub> and E<sub>2</sub> — the numbers of the cities to connect by the first and the second highway, respectively. Note that highways are one-way and must run from S<sub>1</sub> to E<sub>1</sub> and from S<sub>2</sub> to E<sub>2</sub>.</p>

