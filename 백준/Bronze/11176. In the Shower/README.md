# [Bronze III] In the Shower - 11176 

[문제 링크](https://www.acmicpc.net/problem/11176) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Your roommate recently gave you a somewhat passiveaggressive post-it note containing the question “how many empty shampoo bottles do we really need to keep in the shower?”. Passive-aggressive post-it notes generally start with a single number P, the number of passive-aggressive statements and/or questions. P lines then follow, each line containing a passive-aggressive statement or question. Whenever P is equal to 1 the line containing it is typically omitted, and the entire note will just be one passiveaggressive statement or question. This is by far the most common.</p>

<p>Somewhat frustated over your roommate’s inability to count, you decide to write a program that any of your roommates can run whenever they wonder how many empty shampoo bottles are required for a happy existence here in Sector 001. Of course, different roommates can (and probably will) have different definitions for “empty”, and therefore it is only fair that they should input this definition before getting an answer.</p>

### 입력 

 <p>The first line of input is T, the number of cases. T cases follow.</p>

<p>The first line of each case contains two numbers separated by a space: E, the number of attempts that must will be made at extracting visible amounts of shampoo before considering the bottle empty, and N, the number of candidate bottles.</p>

<p>Then follow N lines, each line with a single number describing how many attempts were needed for a particular bottle. If the number of attempts E is exceeded, we consider the bottle empty.</p>

<ul>
	<li>1 ≤ T ≤ 100</li>
	<li>1 ≤ E ≤ 1000</li>
	<li>1 ≤ N ≤ 10</li>
</ul>

### 출력 

 <p>Output a single line containing the number of empty shampoo bottles.</p>

