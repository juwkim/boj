# [Silver IV] Politics - 9491 

[문제 링크](https://www.acmicpc.net/problem/9491) 

### 성능 요약

메모리: 186480 KB, 시간: 1248 ms

### 분류

정렬

### 문제 설명

<p>You are helping a political party canvass their members. The party has a list of candidates they wish to support, and they also have a list of members, each of which supports one candidate. </p>

<p>The party wants for you to sort the list of members, according to some rules. You will be given the list of candidates, in the desired order. Then, you’ll have access to a list of supporters; each supporter will have one candidate that they support.</p>

<p>The party wants you to put the list of supporters in order, sorted by their preferred candidate. There may be some supporters who support the same candidate. If so, order them in the order that they appear on the original list. Some supporters may have a ‘write-in’ candidate, thereby mentioning a candidate who was not on the original preferred candidate list. Put these supporters at the end, grouped by candidate, in the order that their candidates appear in the list of supporters. There also may be candidates who have no supporters. They will probably be taken off the list later, but that’s just the politics of the situation.</p>

### 입력 

 <p>There will be several test cases in the input. Each test case will begin with a line with two integers, n (1≤n≤1,000) and m (1≤m≤100,000), where n is the number of candidates, and m is the number of supporters. On the following n lines will be the names of the candidates, one per line. These names will each be a single word consisting of from 1 to 30 capital letters. All n listed candidate names in any test case will be unique. After the candidates, the next m lines will describe the supporters, one per line. Each of these lines will contain two words separated with a single space. Each word contains from 1 to 30 capital letters. The first word is the name of the supporter, and the second is the name of the candidate that they support. The input will end with a line with two 0s.</p>

### 출력 

 <p>For each test case, print out the names of the supporters, one name per line, in the requested order. Do not output any spaces. Do not separate answers with a blank line.</p>

