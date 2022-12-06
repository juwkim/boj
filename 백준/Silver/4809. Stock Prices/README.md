# [Silver V] Stock Prices - 4809 

[문제 링크](https://www.acmicpc.net/problem/4809) 

### 성능 요약

메모리: 233240 KB, 시간: 3148 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Buy low, sell high. That is what one should do to make profit in the stock market (we will ignore short selling here). Of course, no one can tell the price of a stock in the future, so it is difficult to know exactly when to buy and sell and how much profit one can make by repeatedly buying and selling a stock.</p>

<p>But if you do have the history of price of a stock for the last n days, it is certainly possible to determine the maximum profit that could have been made. Instead, we are interested in finding the k1 lowest prices and k2 highest prices in the history.</p>

### 입력 

 <p>The input consists of a number of cases. The first line of each case starts with positive integers n, k1, and k2 on a line (n <= 1,000,000, k1 + k2 <= n, k1, k2 <= 100). The next line contains integers giving the prices of a stock in the last n days: the i-th integer (1 <= i <= n) gives the stock price on day i. The stock prices are non-negative. The input is terminated by n = k1 = k2 = 0, and that case should not be processed.</p>

### 출력 

 <p>For each case, produce three lines of output. The first line contains the case number (starting from 1) on one line. The second line specifies the days on which the k1 lowest stock prices occur. The days are sorted in ascending order. The third line specifies the days on which the k2 highest stock prices occur, and the days sorted in descending order. The entries in each list should be separated by a single space. If there are multiple correct lists for the lowest prices, choose the lexicographically smallest list. If there are multiple correct lists for the highest prices, choose the lexicographically largest list.</p>

