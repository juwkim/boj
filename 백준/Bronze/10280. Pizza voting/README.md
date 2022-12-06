# [Bronze I] Pizza voting - 10280 

[문제 링크](https://www.acmicpc.net/problem/10280) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>You are training for a programming contest with your team members Alice and Bob. After some hours of hard training you want to have a break and eat pizza. You decided to order a big pizza for all three of you. But you have to choose the kind of pizza you want to eat.</p>

<p>You know your favorite kind. But Alice and Bob have other constraints: Alice is on a diet so she wants a pizza with less calories as possible. Bob is just mean to Alice so he votes for as much calories as possible.</p>

<p>You decide to vote on which kind of pizza you order. As voting for one pizza wouldn’t lead anywhere, you decide to use a veto voting. So everyone of you veto on pizza in a round robin manner. First Alice vetos one pizza, then Bob vetos one, at last you are allowed to veto. Then Alice has the next veto again, then Bob etc. until only one pizza is left.</p>

<p>Reminder: Alice will always veto the pizza with the most calories. Bob vetos always the pizza with least calories. You try to be clever in such a way that your favorite pizza is the remaining pizza.</p>

### 입력 

 <p>The input starts with the number of pizzas n (1 ≤ n ≤ 100 000) and the index of your favorite pizza p (1 ≤ p ≤ n) (1-indexed). Then follow the description of the n pizzas, each given in one line. The description consists of one integer c (0 ≤ c ≤ 1 000 000) giving the calories followed by a single word w giving the name of the pizza (up to 100 characters). The pizzas are ordered from low calories to high calories and the number of calories is unique for every pizza. </p>

### 출력 

 <p>Output one line. “YES” if you can vote in a way, such that your pizza will be selected. “NO” if you are not able to influence the vote in a way that your pizza will be selected.</p>

