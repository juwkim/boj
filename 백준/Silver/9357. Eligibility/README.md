# [Silver IV] Eligibility - 9357 

[문제 링크](https://www.acmicpc.net/problem/9357) 

### 성능 요약

메모리: 2056 KB, 시간: 184 ms

### 분류

자료 구조(data_structures), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Regional Contest Director Osama Ismail knows that an individual cannot participate in the regional contest more than 5 times. Given a list of contestant names and the previous years they participated in, print which contestant is eligible.</p>

### 입력 

 <p>The first line of the input contains a single integer T representing the number of the test cases</p>

<p>The first line of each test case contains a single integer N</p>

<p>N lines follow in this test case each having the format "Name Year" denoting that contestant Name participated in a regional contest in year Year</p>

<ul>
	<li>T ≤ 100</li>
	<li>0 ≤ N ≤ 500</li>
	<li>Name is sequence of lowercase English letters, spaces and contains up to 20 characters </li>
	<li>1970 ≤ Year ≤ 2070</li>
</ul>

<p>Note that since he collected the data from multiple sources it may contain duplicate records (if a contestant X have competed in year Y, you might find multiple lines "X Y" in the same test case)</p>

### 출력 

 <p>For each test case, print a line containing the test case number as formatted in the sample and then for each eligible contestant print his\her name on a single line and note that you must print the names of the contestants in lexicographic order</p>

