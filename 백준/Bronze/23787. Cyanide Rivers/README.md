# [Bronze II] Cyanide Rivers - 23787 

[문제 링크](https://www.acmicpc.net/problem/23787) 

### 성능 요약

메모리: 34140 KB, 시간: 84 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Cyanide rivers flowing out from Martian south polar ice cap are quite dangerous due to their toxic contents and any activity in their close proximity is often extremely time consuming.</p>

<p>A row of communication towers has been built in the area, before the rivers even appeared after Martian global warming events.</p>

<p>Some of the towers are now standing directly in a river, some remain standing outside, on the river shores or on islands in the rivers. The first and the last tower in the row stand on river shores.</p>

<p>All towers are to be officially certified for the next operation period in the present difficult conditions.</p>

<p>The towers which are standing on the shore or on an island can be certified immediately. The access to the towers in rivers is hazardous and requires a lot of caution. The certification process of a tower standing in a river takes one whole day. Moreover, a tower standing in a river can be certified only if at least one of its immediate neighbour towers has been certified at least one day earlier. Fortunately, the certification process can be performed independently on each tower, thus it is possible to certify more than one tower in a day.</p>

<p>The certification process has to be completed as soon as possible.</p>

### 입력 

 <p>The input consists of one line containing an odd binary number with up to 300 000 digits and with no leading zeros. Each digit represents one tower. Towers standing in a river are represented by 0’s, remaining towers are represented by 1’s. The order of the digits is the same as the order of towers in the row.</p>

### 출력 

 <p>Print minimum number of whole days in which all towers can be certified.</p>

