# [Silver II] Paradox Sort (Small) - 12220 

[문제 링크](https://www.acmicpc.net/problem/12220) 

### 성능 요약

메모리: 110576 KB, 시간: 4492 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 1월 9일 03:40:45

### 문제 설명

<p>Vlad likes candies. You have a bag of different candies, and you're going to let Vlad keep one of them. You choose an order for the candies, then give them to Vlad one at a time. For each candy Vlad receives (after the first one), he compares the candy he had to the one he was just given, keeps the one he likes more, and throws the other one away.</p>

<p>You would expect that for any order you choose, Vlad will always end up with his favorite candy. But this is not the case! He does not necessarily have a favorite candy. We know for any pair of candies which one he will prefer, but his choices do not necessarily correspond to a simple ranking. He may choose Orange when offered Orange and Lemon, Banana when offered Orange and Banana, and Lemon when offered Lemon and Banana!</p>

<p>There is a particular candy you want Vlad to end up with. Given Vlad's preferences for each pair of candies, determine if there is an ordering such that Vlad will end up with the right candy. If there is, find the lexicographically-smallest such ordering.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case will start with a line containing the integers <strong>N</strong> and <strong>A</strong>, separated by a space. <strong>N</strong> is the number of candies, and <strong>A</strong> is the number of the candy we want Vlad to finish with. The candies are numbered from 0 to <strong>N</strong>-1. The next <strong>N</strong> lines each contains <strong>N</strong> characters. Character j of line i will be 'Y' if Vlad prefers candy i to candy j, 'N' if Vlad prefers candy j to candy i, and '-' if i = j. Note that if i ≠ j, the jth character of the ith row must be different from the ith character of the jth row.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 10.</span></li>
</ul>

### 출력 

 <p>For each test case output "Case #x: ", where x is the case number, followed by either "IMPOSSIBLE" or a space-separated list of the lexicographically-smallest ordering of candies that leaves Vlad with <strong>A</strong>.</p>

