# [Silver I] Hauling Ore - 5248 

[문제 링크](https://www.acmicpc.net/problem/5248) 

### 성능 요약

메모리: 110064 KB, 시간: 100 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 파싱, 문자열

### 제출 일자

2025년 8월 3일 23:42:41

### 문제 설명

<p>Administrator Selfridge is analyzing possible mining routes on Pandora. He has collected some data in the form of a graph. The latest ore carriers can visit exactly 3 mining camps. Your goal is to help him find out which mines may be visited from other mines with 2 stops (but not fewer).</p>

### 입력 

 <p>Connections between mines are described beginning with the line ”GRAPH BEGIN”. Additional lines lists individual mines (nodes), followed (on the same line) by their neighboring mines (edges). The line ”GRAPH END” ends the list of path descriptions. The next lines list mines for which answers need to be calculated, each on a single line. Following these lines, a completely new instance of the problem can be given, starting from scratch.</p>

<p>Some mines may appear only as neighboring mines, without being described on a separate line. Mine names can be arbitrary strings, as long as they don’t contain any whitespace.</p>

### 출력 

 <p>Your output should consist one line (for each mine analyzed), consisting of the name of the mine, followed by the mines, in alphabetical order, that can be visited with exactly 2 stops but not fewer, starting from the given mine.</p>

