# [Silver V] Gold Rush - 18331 

[문제 링크](https://www.acmicpc.net/problem/18331) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Again, Neverland has experienced a very bad economic condition over the past few months. The value of Oshloob, the national currency of Neverland, changes against one unit of gold very rapidly. People in Neverland, all wondering about their savings, are trying to exchange their savings with gold coins.</p>

<p>Dr. Predictman who is a data scientist, has obtained a prediction of the price (in Oshloobs) of a gold coin for the next n days based on the existing data over the past 40 years. He believes his prediction, and now he want to increase his savings based on it. He was wondering how much savings he has at the end of the n-th day assuming that he has c Oshloobs at the beginning of the first day. Since Dr. Predictman is not a programmer, he asks you to help to find his answer.</p>

### 입력 

 <p>The first line of the input contains two integers c (0 ⩽ c ⩽ 3000), Dr. Predictman’s initial savings in Oshloobs, and n (0 ⩽ n ⩽ 30), the period of his prediction. Each of the next following n lines contains an integer p<sub>i</sub> (1000 ⩽ p<sub>i</sub> ⩽ 2000) denoting the price of a gold coin at day i (1 ⩽ i ⩽ n) in Oshloobs.</p>

### 출력 

 <p>The output contains just an integer, which indicates the maximum savings he can obtain at the end of the n-th day assuming that Dr. Predictman exchanges all his remaining gold coins (if there is any) to Oshloobs at the end of the n-th day.</p>

