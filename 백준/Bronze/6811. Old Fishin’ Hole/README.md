# [Bronze II] Old Fishin’ Hole - 6811 

[문제 링크](https://www.acmicpc.net/problem/6811) 

### 성능 요약

메모리: 30840 KB, 시간: 284 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Fishing habitat and fish species are a resource that must be carefully managed to ensure that they will be there for the future. Accordingly, fishing limits have been established for a particular river based on the population of each species. Specifically, points are associated with the fish caught and the total points you catch must be less than or equal to the points allowed for that river.</p>

<p>As an example, suppose each brown trout counts as 2 points, each northern pike counts as 5 points and each yellow pickerel counts as 2 points, and the total points allowed must be less than or equal to 12. One acceptable catch could consist of 3 brown trout and 1 northern pike, but, other combinations would also be allowed.</p>

<p>Your job is to write a program to input the points allocated for a river, and find how many different ways an angler who catches at least one fish can stay within his/her limit.</p>

### 입력 

 <p>You will be given 4 integers, one per line, representing trout points, pike points, pickerel points, and total points allowed in that order.</p>

<p>You can assume that each integer will be greater than 0 and less than or equal to 100.</p>

### 출력 

 <p>For each different combination of fish caught, output the combination of brown trout, northern pike, and yellow pickerel in that order. The combinations may be listed in any order. The last line of output should display the total number of unique ways to catch fish within the established limit.</p>

