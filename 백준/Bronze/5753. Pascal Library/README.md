# [Bronze III] Pascal Library - 5753 

[문제 링크](https://www.acmicpc.net/problem/5753) 

### 성능 요약

메모리: 28776 KB, 시간: 92 ms

### 분류

구현(implementation)

### 문제 설명

<p>Pascal University, one of the oldest in the country, needs to renovate its Library Building, because after all these centuries the building started to show the effects of supporting the weight of the enormous amount of books it houses.</p>

<p>To help in the renovation, the Alumni Association of the University decided to organize a series of fund-raising dinners, for which all alumni were invited. These events proved to be a huge success and several were organized during the past year. (One of the reasons for the success of this initiative seems to be the fact that students that went through the Pascal system of education have fond memories of that time and would love to see a renovated Pascal Library.)</p>

<p>The organizers maintained a spreadsheet indicating which alumni participated in each dinner. Now they want your help to determine whether any alumnus or alumna took part in all of the dinners.</p>

### 입력 

 <p>The input contains several test cases. The first line of a test case contains two integers N and D indicating respectively the number of alumni and the number of dinners organized (1 ≤ N ≤ 100 and 1 ≤ D ≤ 500). Alumni are identified by integers from 1 to N. Each of the next D lines describes the attendees of a dinner, and contains N integers X<sub>i</sub> indicating if the alumnus/alumna i attended that dinner (X<sub>i</sub> = 1) or not (X<sub>i</sub> = 0). The end of input is indicated by N = D = 0.</p>

### 출력 

 <p>For each test case in the input your program must produce one line of output, containing either the word ‘yes’, in case there exists at least one alumnus/alumna that attended all dinners, or the word ‘no’ otherwise.</p>

