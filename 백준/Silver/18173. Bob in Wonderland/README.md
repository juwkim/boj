# [Silver I] Bob in Wonderland - 18173 

[문제 링크](https://www.acmicpc.net/problem/18173) 

### 성능 요약

메모리: 113608 KB, 시간: 212 ms

### 분류

그래프 이론, 트리

### 제출 일자

2025년 4월 9일 10:44:23

### 문제 설명

<p>A chain, as everybody knows, is made of connected links. Typically, all links are of the same shape and size. Bob is a blacksmith apprentice, and he is making his own first iridium chain. He follows the traditional formula of chain-making. It says:</p>

<ul>
	<li>If there is no chain yet, make a link and it will be a piece of your chain.</li>
	<li>If there is a piece of chain, make another link and connect it to one other link in the piece of chain you already have.</li>
</ul>

<p>Bob made the first link. Then, each time he made another link, he connected it to some other link in his piece of chain, exactly as the formula told him to do.</p>

<p>When he finished, he realized that the object he created did not resemble a usual chain at all. In an effort to straighten the chain, he repeatedly took two links which seemed to be at the ends of the chain and tried to pull them apart as far as he could. But there were some more pieces of the “chain” dangling down from the straightened piece at various places.</p>

<p>It was obvious to Bob that his work is not finished yet and he decided to call the object he produced the unfinished chain. After some more pondering, Bob came to a conclusion that he has to break some links and reconnect them to the rest of the unfinished chain more cautiously to obtain a straight chain he aims to produce. In a straight chain, each link is connected to at most two other links and a straight chain cannot be separated into more pieces without breaking a link.</p>

<p>Being now more careful, Bob is going to progress in simple steps. In one step he will choose a link, say A, connected to another link, say B, in the unfinished chain. He will then break A, disconnect it from B and reconnect A to some other link, say C, in the unfinished chain. If there are more links other than B originally connected to A, Bob will keep them connected to A during the whole step.</p>

<p>What is the minimum number of steps Bob has to perform to get a straight chain?</p>

### 입력 

 <p>The first line contains one integer N (1 ≤ N ≤ 3 · 10<sup>5</sup>), the number of links in the unfinished chain. The links are labeled 1, 2, . . . , N. Each of the next N − 1 lines has two integers denoting the labels of two connected links in the unfinished chain. The connections are listed in arbitrary order. The unfinished chain is guaranteed to form only one piece.</p>

### 출력 

 <p>Output the minimum number of steps which will turn Bob’s unfinished chain into a straight chain.</p>

