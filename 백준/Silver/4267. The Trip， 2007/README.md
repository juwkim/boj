# [Silver III] The Trip, 2007 - 4267 

[문제 링크](https://www.acmicpc.net/problem/4267) 

### 성능 요약

메모리: 119480 KB, 시간: 180 ms

### 분류

애드 혹, 그리디 알고리즘

### 제출 일자

2024년 5월 4일 04:02:13

### 문제 설명

<p>A number of students are members of a club that travels annually to exotic locations. Their destinations in the past have included Indianapolis, Phoenix, Nashville, Philadelphia, San Jose, Atlanta, Eindhoven, Orlando, Vancouver, Honolulu, Beverly Hills, Prague, Shanghai, and San Antonio. This spring they are hoping to make a similar trip but aren't quite sure where or when.</p>

<p>An issue with the trip is that their very generous sponsors always give them various knapsacks and other carrying bags that they must pack for their trip home. As the airline allows only so many pieces of luggage, they decide to pool their gifts and to pack one bag within another so as to minimize the total number of pieces they must carry.</p>

<p>The bags are all exactly the same shape and differ only in their linear dimension which is a positive integer not exceeding 1000000. A bag with smaller dimension will fit in one with larger dimension. You are to compute which bags to pack within which others so as to minimize the overall number of pieces of luggage (i.e. the number of outermost bags). While maintaining the minimal number of pieces you are also to minimize the total number of bags in any one piece that must be carried.</p>

### 입력 

 <p>Standard input contains several test cases. Each test case consists of an integer <i>1 ≤ n ≤ 10000</i> giving the number of bags followed by <i>n</i> integers on one or more lines, each giving the dimension of a piece. A line containing 0 follows the last test case.</p>

### 출력 

 <p>For each test case your output should consist of <i>k</i>, the minimum number of pieces, followed by <i>k</i> lines, each giving the dimensions of the bags comprising one piece, separated by spaces. Each dimension in the input should appear exactly once in the output, and the bags in each piece must fit nested one within another. If there is more than one solution, any will do. Output an empty line between cases.</p>

