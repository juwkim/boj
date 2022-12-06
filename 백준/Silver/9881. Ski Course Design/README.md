# [Silver V] Ski Course Design - 9881 

[문제 링크](https://www.acmicpc.net/problem/9881) 

### 성능 요약

메모리: 28776 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 스위핑(sweeping)

### 문제 설명

<p>Farmer John has N hills on his farm (1 <= N <= 1,000), each with an integer elevation in the range 0 .. 100.  In the winter, since there is abundant snow on these hills, FJ routinely operates a ski training camp.</p><p>Unfortunately, FJ has just found out about a new tax that will be assessed next year on farms used as ski training camps.  Upon careful reading of the law, however, he discovers that the official definition of a ski camp requires the difference between the highest and lowest hill on his property to be strictly larger than 17.  Therefore, if he shortens his tallest hills and adds mass to increase the height of his shorter hills, FJ can avoid paying the tax as long as the new difference between the highest and lowest hill is at most 17.</p><p>If it costs x^2 units of money to change the height of a hill by x units, what is the minimum amount of money FJ will need to pay?  FJ is only willing to change the height of each hill by an integer amount.</p>

### 입력 

 <ul><li>Line 1: The integer N.</li><li>Lines 2..1+N: Each line contains the elevation of a single hill.</li></ul>

### 출력 

 <ul><li>Line 1: The minimum amount FJ needs to pay to modify the elevations of his hills so the difference between largest and smallest is at most 17 units.</li></ul>

