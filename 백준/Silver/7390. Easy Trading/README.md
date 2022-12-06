# [Silver V] Easy Trading - 7390 

[문제 링크](https://www.acmicpc.net/problem/7390) 

### 성능 요약

메모리: 29028 KB, 시간: 468 ms

### 분류

구현(implementation)

### 문제 설명

<p>Frank is a professional stock trader for <em>Advanced Commercial Markets Limited</em> (<em>ACM Ltd</em>). He likes "easy trading" --- using a straightforward strategy to decide when to buy stock and when to sell it.</p>

<p>Frank has a database of historical stock prices for each day. He uses two integer numbers $m$ and $n$ ($1 \le m < n \le 100$) as parameters of his trading strategy. Every day he computes two numbers: $P(m)$ --- an average stock price for the previous $m$ days, and $P(n)$ --- an average stock price for the previous $n$ days. $P(m) > P(n)$ is an indicator of the upward trend (traders call it <em>bullish</em> trend), and $P(m) < P(n)$ is an indicator of the downward trend (traders call it <em>bearish</em> trend). In practice the values for $P(m)$ and $P(n)$ are never equal.</p>

<p>When a trend reverses from bearish to bullish it is a signal for Frank to buy stock. When a trend reverses from bullish to bearish it is a signal to sell.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 581px; height: 227px;"></p>

<p>Frank has different values for $m$ and $n$ in mind and he wants to <em>backtest</em> them using historical prices. He takes a set of $k$ ($n < k \le 10\,000$) historical prices $p_i$ ($0 < p_i < 100$ for $1 \le i \le k$). For each $i$ ($n \le i \le k$) he computes $P_i(m)$ and $P_i(n)$ --- an arithmetic average of $p_{i-m+1} \dots p_i$ and $p_{i-n+1} \dots p_i$ respectively.</p>

<p>Backtesting generates trading signals according to the following rules.</p>

<ul>
	<li>If $P_i(m) > P_i(n)$ there is a bullish trend for day $i$ and a "<code>BUY ON DAY </code>$i$" signal is generated if $i=n$ or there was a bearish trend on day $i-1$.</li>
	<li>If $P_i(m) < P_i(n)$ there is a bearish tread for day $i$ and a "<code>SELL ON DAY </code>$i$" signal is generated if $i=n$ or there was a bullish trend on day $i-1$.</li>
</ul>

<p>Your task is to write a program that backtests a specified strategy for Frank --- you shall print a signal for the first tested day (day $n$) followed by the signals in increasing day numbers.</p>

### 입력 

 <p>The first line of the input file contains three integer numbers $m$, $n$, and $k$. It is followed by $k$ lines with stock prices for days 1 to $k$. Each stock price $p_i$ is specified with two digits after decimal point. Prices in the input file are such that $P_i(m) \ne P_i(n)$ for all $i$ ($n \le i \le k$).</p>

### 출력 

 <p>Write to the output file a list of signals --- one signal on a line, as described in the problem statement. </p>

