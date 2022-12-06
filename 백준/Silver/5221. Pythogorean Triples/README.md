# [Silver V] Pythogorean Triples - 5221 

[문제 링크](https://www.acmicpc.net/problem/5221) 

### 성능 요약

메모리: 114488 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘(bruteforcing), 정렬(sorting), 문자열(string)

### 문제 설명

<p>In pursuit of one of the Infinity Gems, rumored to be in possession of Loki, Thor and the Avengers have reached what they believe to be one of Loki’s dens. However, their attempt to infiltrate is thwarted by a locked door. The Avengers need to quickly figure out which number (key) to enter on the keypad to gain access; however, they don’t the time to try the trillions of possible combinations. Thor notices a sequence of numbers on a nearby wall. Thor knows Loki well (they are half-brothers after all), and believes that the key is a Pythogorean triple, with the numbers drawn from the sequence.</p>

<p>A triple {x, y, z}, x < y < z is called a Pythogorean triple if: x 2 + y 2 = z 2 . So, for example, {3,4,5} is a Pythogorean triple, while {1,2,3} is not.</p>

<p>Your goal is to write a computer program that helps the Avengers. More specifically, given a sequence of positive integers x1, · · · , xn, all different from each other, your goal is find all the Pythogorean triples in that sequence.</p>

<p>For example, given a sequence, 13, 12, 3, 4, 5, there are two Pythogorean triples in it: {3, 4, 5} and {5, 12, 13}.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case: the first number is n (3 ≤ n ≤ 50), the size of the sequence, and the following n numbers are the sequence (not necessarily in any order). None of the individual numbers are greater than 2<sup>24</sup>.</p>

### 출력 

 <p>For each test case, you are to output the different Pythogorean triples. The exact form of the output is shown below.</p>

