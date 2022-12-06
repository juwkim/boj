# [Bronze II] ROOMS - 3282 

[문제 링크](https://www.acmicpc.net/problem/3282) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A hotel has N rooms with two beds, numbered with numbers from 1 to N.</p>

<p>When a group of guests arrive, they are accommodated in the following way: While there are empty rooms, each pair of guests is accommodated in an empty room with lowest number. If there is odd number of guests in a group then the last person will be accommodated alone in an empty room with lowest number. If there are no more empty rooms, then each guest is accommodated in a room with lowest number occupied by one guest, i.e. together with a guest from some other group.</p>

<p>The hotel is initially empty. The order of arrivals of groups is known in advance. Write a program that will determine how many guests there will be in every room after last of them is accommodated.</p>

### 입력 

 <p>The first line of input file contains two integers N, 1 ≤ N ≤ 100, and G separated by a space character. Number N is number of rooms in a hotel and G is number of groups of guests.</p>

<p>The next G lines contain numbers of guests in each group – (i+1)th line contains number of guests in ith group (groups are numbered by order of arrival to a hotel).</p>

<p>Total number of guests (i.e. the sum of all numbers of guests in all groups) will be less than or equal to the number of all available beds in the hotel rooms.</p>

### 출력 

 <p>The output file should consist of N lines: ith line should contain number of guests in ith room after all guests were accommodated in the hotel.</p>

