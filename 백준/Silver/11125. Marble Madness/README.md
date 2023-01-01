# [Silver IV] Marble Madness - 11125 

[문제 링크](https://www.acmicpc.net/problem/11125) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

수학(math)

### 문제 설명

<p>Øyvind likes to test his future employees, especially with funny games. This time he has invented a game where you start out with B black marbles and W white ones in a bag. You also have endless supplies of both kinds of marbles outside the bag. The game proceeds in rounds. In each round, you take two marbles at random out of the bag, and put one marble back in (possibly another color than any of the two you took out), obeying the following rules:</p>

<ol>
	<li>When you take out two white marbles, you put a black one back in.</li>
	<li>When you take out one black and one white, you put a white marble back in.</li>
	<li>When you take out two black marbles, you put a black one back in.</li>
</ol>

<p>At the end of this game, there will only be one marble in the bag. This marble may be white with a probability and black with a probability given the number of marbles of each colour you start with. Your job is to find these probabilities.</p>

### 입력 

 <p>The input will start with a line giving the number of test cases, T. Each test case will be presented at one line with two integers, B and W, separated by a single space, representing the number of black and white marbles respectively.</p>

<ul>
	<li>0 < T ≤ 100</li>
	<li>0 ≤ B, W ≤ 50000</li>
	<li>0 < B + W</li>
	<li>Any answer within 10<sup>−6</sup> of the correct one will be accepted.</li>
</ul>

### 출력 

 <p>There should be one line of output for each test case with two floating point numbers separated by a single space. The first number should represent the probability that the last marble is black, and the second the probability that the last marble is white.</p>

