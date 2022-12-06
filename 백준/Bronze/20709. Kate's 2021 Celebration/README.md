# [Bronze II] Kate's 2021 Celebration - 20709 

[문제 링크](https://www.acmicpc.net/problem/20709) 

### 성능 요약

메모리: 29028 KB, 시간: 112 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Kate did not have a good year 2020 and she is glad that it is coming to an end. She is planning to celebrate New Year 2021 on a grand scale. </p>

<p>Kate has decided to buy four balloons with digits <code>2</code> <code>0</code> <code>2</code> <code>1</code> painted on them for her 2021 celebration. She went to a store's web site and has found that balloons with digits are sold in packs containing different assortments of balloons of various sizes, colors, and with different digits painted on them. Kate does not care about their size, color, or other attributes. She only cares about digits written on those balloons. Fortunately, the store has all the information about different packs of balloons that are available. Kate has managed to retrieve it through the store's REST API and extracted just the information she needs --- the price and the digits that are written on balloons in each pack. </p>

<p>Please, help Kate with the final task of figuring out what is the cheapest pack of balloons she can buy that would get her the four digits she needs for her 2021 celebration.</p>

### 입력 

 <p>The first line of the input file contains an integer $n$ ($1 \le n \le 1000$) --- the number of packs of balloons available in the store.  </p>

<p>The next $n$ lines contain descriptions of packs, one line per pack. Each pack is described by an integer $p$ ($1 \le p \le 10^5$) --- the price of the pack in roubles, followed by a string of at least one and at most $100$ digits (each digit is from <code>0</code> to <code>9</code>) --- the digits on the balloons in the pack.</p>

### 출력 

 <p>Output a single integer --- the number of the cheapest pack that Kate can buy to get the digits for her $2021$ celebration. Packs of balloons are numbered starting from $1$ in the order they are given in the input. If there are multiple packs with the same price, output any one of them.</p>

<p>Output $0$ if there is no pack in the store that Kate can buy for her 2021 celebration.</p>

