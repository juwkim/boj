# [Silver IV] Tons of Orcs, no Fibbin’ - 11366 

[문제 링크](https://www.acmicpc.net/problem/11366) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

수학

### 문제 설명

<p>The armies of Mordor are fearsome in both stature and numbers. How did they raise such a host in so short a time? It turns out, orcs breed very quickly. For any given year, their population equals the sum of the populations from the previous two years. For example, if there are 14 orcs in year 7 and 20 orcs in year 8, then we can calculate a total population of 34 orcs in year 9, and a total population of 54 orcs in year 10. Given the populations in two previous years, calculate the population at the nth following year.</p>

### 입력 

 <p>Each test case is on its own line, each of the form a b c; Here a and b are non-negative integers denoting the number of orcs in the previous two years, and c is the number of years in the future to calculate the population in. The end of input is marked by a line of the form ”0 0 0”, which should produce no output. No values will exceed the value that can be stored in an int variable.</p>

### 출력 

 <p>For each test case, output one integer on its own line describing the number of orcs in the specified year. No values will exceed the value that can be stored in an int variable.</p>

