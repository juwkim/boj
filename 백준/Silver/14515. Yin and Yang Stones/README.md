# [Silver III] Yin and Yang Stones - 14515 

[문제 링크](https://www.acmicpc.net/problem/14515) 

### 성능 요약

메모리: 114460 KB, 시간: 112 ms

### 분류

애드 혹(ad_hoc), 그리디 알고리즘(greedy)

### 문제 설명

<p>A mysterious circular arrangement of black stones and white stones has appeared. Ming has been tasked with balancing the stones so that only one black and one white stone remain.</p>

<p>Ming has two operations for balancing the stones:</p>

<ol>
	<li>Take some consecutive sequence of stones where there is exactly one more black stone than a white stone and replace the stones with a single black stone</li>
	<li>Take some consecutive sequence of stones where there is exactly one more white stone than black stone and replace the stones with a single white stone</li>
</ol>

<p>Given a circular arrangement, determine if it is possible for Ming to balance the stones.</p>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The input will consist of a single string s (1 ≤ |s| ≤ 10<sup>5</sup>), with only the characters capital ‘B’ and ‘W’. The stones are arranged in a circle, so the first stone and the last stone are adjacent.</p>

### 출력 

 <p>Output 1 if it is possible for Ming to balance the stones with his rules. Otherwise, output 0.</p>

