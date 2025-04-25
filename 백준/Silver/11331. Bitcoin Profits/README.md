# [Silver II] Bitcoin Profits - 11331 

[문제 링크](https://www.acmicpc.net/problem/11331) 

### 성능 요약

메모리: 259900 KB, 시간: 1160 ms

### 분류

누적 합, 정렬

### 제출 일자

2025년 4월 25일 20:05:49

### 문제 설명

<p>Bitcoin mining was all the rage in 2013, when the cryptocurrency's conversion value spiked to over <span>$</span>1000 USD per Bitcoin. Bitcoins are "mined" through a process that involves calculating a one-way pseudo-random function that outputs a large integer. A global "difficulty" is set, and a "block" represents a claim that bitcoins have been generated, and will only be accepted by others on the network if the pseudo-random function outputs a value that satisfies the difficulty requirement.</p>

<p>However, with the advent of dedicated mining hardware that is cheaper, faster, and more power-efficient, it quickly became infeasible to find a block with general-purpose computers. Mining "pools" quickly cropped up, where a number of people donate processing power to the pool in return for a proportional fraction of the reward of finding a block.</p>

<p>To calculate the proportion, miners participate in a reduced-difficulty arena, for example, at 1,048,576<sup>th</sup> the real difficulty, for pool "shares". However, if a share is found that surpasses the difficulty requirements, it will be assigned a "share difficulty" based on the ratio.</p>

<p>To save on network bandwidth, pool members can request a higher base level of share difficulty (for example, at 524,288<sup>th</sup> the real difficulty). To even the higher computational requirements out, the reward is increased linearly: if a share is <strong>k</strong> times as hard to find, then <strong>k</strong> times the proportional value is given. Any share found with a difficulty less than <strong>k</strong> is discarded. However, a miner must request a difficulty for all shares, and cannot select the optimal difficulty for each share found.</p>

<p>Now, given a list of earned share difficulties (as multiples of the base pool difficulty), can you calculate the requested difficulty that would have maximized the earned number of shares?</p>

### 입력 

 <p>Each input contains multiple test cases. Each test case begins with an integer 0 < <strong>N</strong> < 1000000, the number of shares accepted. Following is a line containing the numbers 0 ≤ <strong>d</strong><sub>1</sub>, ... , <strong>d</strong><sub><strong>N</strong></sub> ≤ 10<sup>6</sup>, the difficulty of each accepted share.</p>

<p>The input file ends with a line containing zero.</p>

### 출력 

 <p>For each test case, output the difficulty multiplier that gives the greatest rewards. If more than one exists, output the lowest such value.</p>

