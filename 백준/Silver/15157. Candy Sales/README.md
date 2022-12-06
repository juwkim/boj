# [Silver V] Candy Sales - 15157 

[문제 링크](https://www.acmicpc.net/problem/15157) 

### 성능 요약

메모리: 137332 KB, 시간: 204 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Cathy’s favourite candy brand is releasing n new flavours of candy: one new flavour on each of the next n days. A pack of candy flavour i (the new flavour released on the i th day) will cost w<sub>i</sub> dollars on the day that it is released, but in order to encourage customers to try the new flavours, each candy flavour increases in price by one dollar on each day after it has been released. Precisely, on day j ≥ i, a pack of the candy flavour released on day i costs</p>

<p style="text-align:center">w<sub>i</sub> + (j − i)</p>

<p>dollars.</p>

<p>Cathy wants to buy exactly one pack of candy on each one of the next n days and wants to get the most candy for her money. Calculate the price of the cheapest pack of candy available on each of the next n days. There is an unlimited number of packs of each flavour of candy and each flavour is available on the day of its release and all subsequent days.</p>

### 입력 

 <p>The input consists of two lines. The first line contains an integer n (1 ≤ n ≤ 200 000), which is the number of flavours. The second line contains n integers w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub> (1 ≤ w<sub>i</sub> ≤ 100 000), where w<sub>i</sub> is the initial price of the i th candy flavour in dollars.</p>

### 출력 

 <p>Display n integers, the i th of which is the price of the cheapest pack of candy that Cathy can buy on day i.</p>

