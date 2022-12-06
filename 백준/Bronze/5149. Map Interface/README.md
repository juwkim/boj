# [Bronze II] Map Interface - 5149 

[문제 링크](https://www.acmicpc.net/problem/5149) 

### 성능 요약

메모리: 30840 KB, 시간: 184 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Many public transit systems have online interfaces for figuring out the route you want to take. One principle of good user interface design here is that the system should show you all the relevant information, but no more, so you can zoom in on the important part. For a graphical user interface showing a system map, this means showing you a map containing all the stations you will cross, but as few extra stations as possible. On the other hand, most users are used to rectangular maps with uniform scale, so we will stick with that.</p>

<p>So here is the problem more concretely. You will be given the locations (as (x,y) coordinates) for all stations in the system. Then, you will also be given the list of stations (in order) that your line takes you through. You are to compute how many stations total will be in the smallest rectangle that contains your entire trip.</p>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line contains two integers n,m. 2 ≤ n ≤ 500 is the total number of stations in the system, and 2 ≤ m ≤ n the number of stations you travel through.</p>

<p>The next n lines give you pairs of integers xi yi, the coordinates of the ith station. The following line contains m integers, the stations you visit in order.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the total number of stations visible in the smallest rectangle containing all of your trip. Each data set should be followed by a blank line.</p>

