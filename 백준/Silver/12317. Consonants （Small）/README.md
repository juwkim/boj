# [Silver V] Consonants (Small) - 12317 

[문제 링크](https://www.acmicpc.net/problem/12317) 

### 성능 요약

메모리: 115180 KB, 시간: 276 ms

### 분류

브루트포스 알고리즘, 구현

### 문제 설명

<p>In English, there are 26 letters that are either <strong>vowels</strong> or <strong>consonants</strong>. In this problem, we consider <strong>a, e, i, o,</strong> and <strong>u</strong> to be vowels, and the other 21 letters to be consonants.</p>

<p>A tribe living in the Greatest Colorful Jungle has a tradition of naming their members using English letters. But it is not easy to come up with a good name for a new member because it reflects the member's social status within the tribe. It is believed that the less common the name he or she is given, the more socially privileged he or she is.</p>

<p>The leader of the tribe is a professional linguist. He notices that hard-to-pronounce names are uncommon, and the reason is that they have too many <strong>consecutive consonants</strong>. Therefore, he announces that the social status of a member in the tribe is determined by its <strong>n</strong>-value, which is the number of substrings with at least <strong>n</strong> consecutive consonants in the name. For example, when <strong>n</strong> = 3, the name "quartz" has the <strong>n</strong>-value of 4 because the substrings <strong>quartz</strong>, <strong>uartz</strong>, <strong>artz</strong>, and <strong>rtz</strong> have at least 3 consecutive consonants each. A greater <strong>n</strong>-value means a greater social status in the tribe. Two substrings are considered different if they begin or end at a different point (even if they consist of the same letters), for instance "tsetse" contains 11 substrings with two consecutive consonants, even though some of them (like "<strong>tse</strong>tse" and "tse<strong>tse</strong>") contain the same letters.</p>

<p>All members in the tribe must have their names and <strong>n</strong> given by the leader. Although the leader is a linguist and able to ensure that the given names are meaningful, he is not good at calculating the <strong>n</strong>-values. Please help the leader determine the <strong>n</strong>-value of each name. Note that different names may have different values of <strong>n</strong> associated with them.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. The first line of each test case gives the name of a member as a string of length <strong>L</strong>, and an integer <strong>n</strong>. Each name consists of one or more lower-case English letters.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>0 < <strong>n</strong> ≤ <strong>L</strong>.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">L</strong><span style="line-height:1.6em"> ≤ 100.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the <strong>n</strong>-value of the member's name.</p>

