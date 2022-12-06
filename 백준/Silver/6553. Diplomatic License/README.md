# [Silver V] Diplomatic License - 6553 

[문제 링크](https://www.acmicpc.net/problem/6553) 

### 성능 요약

메모리: 115384 KB, 시간: 164 ms

### 분류

기하학(geometry)

### 문제 설명

<p>In an effort to minimize the expenses for foreign affairs the countries of the world have argued as follows. It is not enough that each country maintains diplomatic relations with at most one other country, for then, since there are more than two countries in the world, some countries cannot communicate with each other through (a chain of) diplomats.</p>

<p>Now, let us assume that each country maintains diplomatic relations with at most two other countries. It is an unwritten diplomatic <em>"must be"</em> issue that every country is treated in an equal fashion. It follows that each country maintains diplomatic relations with exactly two other countries.</p>

<p>International topologists have proposed a structure that fits these needs. They will arrange the countries to form a circle and let each country have diplomatic relations with its left and right neighbours. In the real world, the Foreign Office is located in every country's capital. For simplicity, let us assume that its location is given as a point in a two-dimensional plane. If you connect the Foreign Offices of the diplomatically related countries by a straight line, the result is a polygon.</p>

<p>It is now necessary to establish locations for bilateral diplomatic meetings. Again, for diplomatic reasons, it is necessary that both diplomats will have to travel equal distances to the location. For efficiency reasons, the travel distance should be minimized. Get ready for your task!</p>

### 입력 

 <p>The input contains several testcases. Each starts with the number <em>n</em> of countries involved. You may assume that <em>n>=3</em> is an odd number. Then follow <em>n</em> pairs of x- and y-coordinates denoting the locations of the Foreign Offices. The coordinates of the Foreign Offices are integer numbers whose absolute value is less than <em>10<sup>12</sup></em>. The countries are arranged in the same order as they appear in the input. Additionally, the first country is a neighbour of the last country in the list. Input is terminated by <em>EOF</em>.</p>

### 출력 

 <p>For each test case output the number of meeting locations (<em>=n</em>) followed by the x- and y-coordinates of the locations. The order of the meeting locations should be the same as specified by the input order. Start with the meeting locations for the first two countries up to the last two countries. Finally output the meeting location for the <em>n</em>-th and the first country.</p>

