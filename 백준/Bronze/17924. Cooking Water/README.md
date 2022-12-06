# [Bronze II] Cooking Water - 17924 

[문제 링크](https://www.acmicpc.net/problem/17924) 

### 성능 요약

메모리: 28776 KB, 시간: 244 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>"A watched pot never boils", as the saying goes. Chef Edward has been cooking for ages, and empirically the saying seems to be true in his kitchen -- he has yet to see a pot actually start boiling. His wife Gunilla is a bit suspicious of Edward's claim though. She knows how he often loses focus after a little while, and thinks that it is very likely Edward gets tired of watching after about the same period of time starting when he puts it on the stove.</p>

<p>Being scientifically minded, Gunilla quickly designed an experiment which could help Edward gain more insight into the boiling of pots. Every time during the last week when Edward boiled a pot of water, he wrote down the intervals of time when he was not watching the pot. Now, he has a large log of these intervals, and wonders whether Gunilla is right (i.e. it may be the case Edward just happened to watch away every time the pot started boiling), or if his hypothesis is correct.</p>

<p>Given this data, is it possible that the pot actually starts boiling after the same amount of time, every time?</p>

### 입력 

 <p>The first line of the input contains an integer $1 \le N \le 1\,000$, the number of times Edward boiled water in the last week. Then, $N$ descriptions of a boiling follow. Each description contains two numbers $0 \le a \le b \le 1\,000$. This means that Edward looked away during seconds $[a, b]$ (i.e. from the start of second $a$, to the end of second $b$), and that Edward first saw the pot boiling once he looked back.</p>

### 출력 

 <p>If it is impossible that all the pots actually started boiling at the same point in time, output <code>edward is right</code>. Otherwise, output <code>gunilla has a point</code>.</p>

