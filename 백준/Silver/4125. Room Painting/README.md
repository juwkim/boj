# [Silver III] Room Painting - 4125 

[문제 링크](https://www.acmicpc.net/problem/4125) 

### 성능 요약

메모리: 115192 KB, 시간: 204 ms

### 분류

자료 구조, 정렬, 트리를 사용한 집합과 맵, 두 포인터

### 제출 일자

2024년 4월 15일 09:25:37

### 문제 설명

<p>Joe's landlord has allowed him to paint his room any colour that he wants, even multiple colours. Joe has come up with a very colourful design. Now he needs to buy the paint. Being a struggling student, Joe does not want to waste any money, so he has calculated the exact amount that he needs of each colour down to the microlitre. To his surprise, however, the local paint shop is unwilling to sell him a can of exactly 3.141592 litres of red paint. No, the shop has a set of specific paint can sizes. Joe has no choice but to buy a little bit more paint than he really needs. Still, he would like to minimize the amount of paint wasted. In addition, he does not want to buy more than one can of any given colour.</p>

### 입력 

 <p>The first line of input contains two integers 0 < n <= 100000 and 0 < m <= 100000, the number of paint can sizes offered by the paint shop, and the number of colours that Joe needs. Each of the next n lines contains the size of a can offered by the paint shop, in microlitres. Each can contains no more than 1000 litres. Each of the next m lines contains the number of microlitres that Joe needs of a given colour. It is guaranteed that for each colour, the paint shop sells a can large enough to satisfy Joe's needs.</p>

### 출력 

 <p>Output a single line, the total number of microlitres of paint wasted if Joe buys, for each colour, the smallest can that satisfies his needs.</p>

