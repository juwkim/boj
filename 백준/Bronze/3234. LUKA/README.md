# [Bronze II] LUKA - 3234 

[문제 링크](https://www.acmicpc.net/problem/3234) 

### 성능 요약

메모리: 30840 KB, 시간: 132 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>Luka came to National Competition ten days earlier in order to get some hints by eavesdropping on the The Task Makers' conversations. He knows that The Task Makers take daily walks through the town of Cres, during which they quietly discuss about the tasks.</p>

<p>Curiously, the city of Cres is built in such a fashion, that it can be represented as a planar coordinate grid. The Task Makers start their walks at point (0,0), and in every turn they move on the coordinate plain in one of the four directions: right (they increase their x coordinate by one), up (they increase their y coordinate by one), left or down.</p>

<p>Luka is positioned at point (X,Y) on the coordinate plain, and he can overhear bits of information only at times The Task Makers are located on the same position as Luka or one of the other eight adjacent positions.</p>

<p>Your task is to write a program that will find out the time on which Luka has heard the conversation. </p>

### 입력 

 <p>The first line of the input file consists of two inegers X and Y, -10000 ≤ X,Y ≤ 10000, Luka's position.</p>

<p>In the next line is an integer K, 1 ≤ K ≤ 100,000.</p>

<p>The following line holds K charachters that show us the route that The Task Makers were taking that day. Those charachters will be either 'I' - east (or right), 'S' - north (or up), 'Z' - west (or left) or 'J'-south (or down).</p>

### 출력 

 <p>In the output file you have to write the times from the Task text. The numbers have be outputted in a strictly ascending order, and each one of them has to be in a separate line.</p>

<p>If Luka wasn't able to overhear the taskmasters, in the first and only line of the output file you have to write '-1'.</p>

