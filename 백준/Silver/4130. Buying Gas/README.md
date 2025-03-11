# [Silver II] Buying Gas - 4130 

[문제 링크](https://www.acmicpc.net/problem/4130) 

### 성능 요약

메모리: 120928 KB, 시간: 372 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 3월 11일 21:49:45

### 문제 설명

<p>Gasoline is expensive these days. Many people go out of their way to find the cheapest gas. You could write a computer program to help with this. But on the other hand, searching around too much can waste a lot of time. It could even happen that the driver searches so long that he runs out of gas, which is a major nuisance.</p>

<p>Deciding where to buy gas is even more important on a long trip. Such a trip already takes a long time, so you don't want to waste any more time than you have to. And the consequences of running out are all the more bothersome when far away from home.</p>

<p>Your task here is to write a program that finds the optimal places where to buy gas on a long trip. Of course, the answer must ensure that the car never runs out of gas. Furthermore, it must minimize the number of times that the car stops to fill up.</p>

### 입력 

 <p>The first line of input contains three integers 0 < n <= 100, 0 <= m <= 100000, 0 <= d <= 100000, the capacity of the gas tank in litres, the number of gas stations along the route, and the total length of the trip in kilometres. The following m lines each contain two integers, the distance in kilometres from the starting point of the trip to the gas station, and the price of gas at the gas station in tenths of a cent per litre. The car begins the trip with a full tank of gas, and uses 0.1 litres of gas for each kilometre travelled.</p>

### 출력 

 <p>Find the optimal set of gas stations at which to stop to get gas. Output a single integer, the number of gas stations in this set. If it is not possible to make the trip without running out of gas, output the integer -1.</p>

