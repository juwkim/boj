# [Bronze III] TV Reports - 6249 

[문제 링크](https://www.acmicpc.net/problem/6249) 

### 성능 요약

메모리: 121220 KB, 시간: 100 ms

### 분류

구현(implementation)

### 문제 설명

<p>Neverland has experienced a very bad economic condition over the past few months. The national currency of Neverland, Oshloob, has lost its value against Dollar very rapidly. People in Neverland, all wondering about the falling down of their currency, are checking the exchange rates of Dollar almost every day.</p>

<p>There are two TV channels accessible to the public in Neverland: National TV (abbreviated as NTV) which is only interested in reporting good economic news, and a foreign media, called BBTV, which is interested in reporting (negative) breaking news. At the end of each day, if the price of Dollar goes down compared to its preceding day, National TV makes a headline, saying “Dollar dropped by n Oshloobs”, where n is the difference between the prices of Dollar in that particular day compared to its preceding day (surprisingly, Dollar never drops by 1 Oshloob in Neverland). Whenever the price of Dollar reaches its all-time highest record (i.e. greater than all prices up to that day), BBTV makes a headline, saying “Dollar reached m Oshloobs, A record!”, where m is the price of Dollar in that particular day.</p>

<p>A company has hired you to record the headlines related to the price of Dollar broadcasted on these two TV channels over a specific period. Since you do not like to watch all TV news to extract the Dollar-related ones, you have decided to obtain the price of Dollar from a reliable source, and produce the headlines yourself.</p>

### 입력 

 <p>The first line of the input contains three positive integers n, p, and h (separated by a space), where n (1 ≤ n,p,h ≤ 10,000) specifies the number of days you are hired for to record the headlines, p is the price of Dollar one day before you start your job, and h (≥ p) is the all-time highest price of Dollar just before you start your job. The next n lines, each contains an integer less than 10,000; the number given in the i<sup>th</sup> line specifies the price of Dollar at the i<sup>th</sup> day of your job.</p>

### 출력 

 <p>For each headline reported by the two TV channels, write a single line on the standard output containing the name of the TV channel (either NTV or BBTV), followed by the headline broadcasted by that TV channel. The output must be sorted based on the reported times of the headlines. The format of the output must conform to the format indicated in the Standard Output below.</p>

