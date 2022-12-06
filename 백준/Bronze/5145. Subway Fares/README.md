# [Bronze II] Subway Fares - 5145 

[문제 링크](https://www.acmicpc.net/problem/5145) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

구현(implementation)

### 문제 설명

<p>One of the first questions faced by the traveler in a subway system is: How much will the trip cost? While it should be fairly straightforward to present this information clearly, it actually sometimes takes lookups in several tables, posted in different places in a subway station, followed by complicated computations. Then, if you make the right sacrifices, invoke the right demons, etc., you might eventually get the right answer. Given the risks with invoking the wrong demons, it would be preferable to write a computer program to help with this. And that’s what we’re going to do now.</p>

<p>We’ll focus on just one subway line. You’ll be given a price table stating how much a trip of s stations costs, for each s ≥ 1. Then, you’ll be given the names of the stations in order, as well as the names of your starting and ending station. You are to compute the fare. Notice that you can use the subway line in both directions.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of each data set contains an integer 2 ≤ n ≤ 50. That’s the number of stops of this line. This is followed by n − 1 lines, with line s giving you an integer, the price for going s stops. (s = 1 means you get off at the next stop after you get on. There will be no cases where you get off at the same stop.) Next come n lines, each with the name of a station (in order), which consists of just lowercase letters. All station names will of course be distinct.</p>

<p>The last two lines are the name of your starting and ending stations. They will match the names of stations on the list, and be different from each other.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, output the price for your trip. Each data set should be followed by a blank line.</p>

