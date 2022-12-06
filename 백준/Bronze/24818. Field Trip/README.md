# [Bronze I] Field Trip - 24818 

[문제 링크](https://www.acmicpc.net/problem/24818) 

### 성능 요약

메모리: 118336 KB, 시간: 492 ms

### 분류

구현(implementation)

### 문제 설명

<p>You and your classmates are going on an exciting field trip to a downtown museum. Because the museum is an hour away, three buses of identical capacity and a van are dispatched as a means of transportation to the museum and back. The buses will first start loading only students, and once all students have been loaded then teachers will begin to fill in the remaining spots on the buses. Any remaining teachers will ride on the van. To make the bus ride more exciting, all the students are hoping for a "teacher free bus ride"! A teacher free bus ride is when none of the teachers are on a bus.</p>

<p>Students are grouped in $n$ class sections of different sizes. Each class section is assigned a number from $1$ to $n$. All students in one class section must ride on the same bus. The buses will board class sections in increasing order by number. In other words, the first bus will load sections numbered $1$ to $i$, the second bus will load sections numbered $i+1$ to $j$, and the third bus will load the sections numbered $j+1$ to $n$. Every bus must have at least one class section assigned to it.</p>

<p>Given the sizes of each of the class sections, determine if it is possible to load students onto $3$ identical buses and end up with a "teacher free bus ride!"</p>

### 입력 

 <p>The first line of input contains one integer $N$, the number of class sections ($3 \le N \le 1,000,000$). The second line of input contains $N$ integers, the $i^{\text{th}}$ integer represents the size of class section with number $i$. Class section sizes can range from $[1, 10\,000]$.</p>

### 출력 

 <p>If it is possible to load the students onto three identical buses in the above-described fashion and have a teacher free bus ride, then output two integers $i$ and $j$ ($1 \le i < j < n$) where $i$ is the number of the class section which is to be loaded last into the first bus, and $j$ is the class section which is to be loaded last into the second bus. We can assume the third bus will load class sections $j+1$ to $n$.</p>

<p>If it is not possible, print "<code>-1</code>".</p>

