# [Silver IV] Suspicious Stocks - 6640 

[문제 링크](https://www.acmicpc.net/problem/6640) 

### 성능 요약

메모리: 140980 KB, 시간: 256 ms

### 분류

다이나믹 프로그래밍(dp), 그리디 알고리즘(greedy)

### 문제 설명

<p>The corruption is always extremely difficult to prove. Even if we know that some people accept bribes, it is almost impossible to punish them, because the only witnesses are them and the people who offered the bribe. Neither of them is likely to testify.</p>

<p>One way to prove that something illegal has happened is to count the money a person has and then give evidence that it was impossible for him/her to earn that money legally. However, this is not so easy. For example, the person may easily claim that the money have been donated by their uncle or earned by trading stocks.</p>

<p>ACM would like to be able to verify these explanations. Since it is impossible to verify the existence of “uncles”, we will concentrate on the stocks. You are given the history of stock prices, and your task is to compute the maximal profit that could possibly be earned by buying and selling the stock.</p>

### 입력 

 <p>The input will consist of several test scenarios, each of them consisting of two lines of text. The first line of a scenario contains two positive integers D and M (1 ≤ D ≤ 70000, 1 ≤ M ≤ 40000) separated by a space. D is the number of days when the trading took place, M is the amount of money available at the beginning.</p>

<p>The second line of each scenario contains D positive integers p1, p2, p3,...,pD (1 ≤ pi ≤ 40000) separated by a space. The number pi denotes the price of one piece of stock at day i, meaning it is possible to buy or sell one piece for that price on that day.</p>

<p>The last scenario is followed by a line containing single zero.</p>

### 출력 

 <p>For each scenario, output one line containing one number: The maximum profit that could be achieved by at most one Buy operation followed by one Sell operation. Assume that there is no stock at the beginning and that it is possible to do only one Buy during the whole trading.</p>

<p>For simplicity, assume that it is possible to buy as many pieces of stock as there are money for, but we can only buy and sell whole pieces (integer number) of stock, not fractions. For example, if the stock price is \$3 and we have \$11, we can only buy 3 pieces.</p>

<p>The Buy operation is followed by exactly one Sell operation on some of the following days. Of course, it is possible (and recommended) to sell all the pieces of stock to maximize profit.</p>

