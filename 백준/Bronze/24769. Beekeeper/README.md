# [Bronze II] Beekeeper - 24769 

[문제 링크](https://www.acmicpc.net/problem/24769) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>It’s Bill the beekeeper again. In this problem, we learn that didn't choose his career for the best reason. Bill chose to be a beekeeper because he really, really likes the look of the double e's in the word "beekeeper". Your task is to help identify other words Bill will really like.</p>

<p>Bill's affinity for a word is determined by how many pairs of double vowels it has, where vowels are the letters {a,e,i,o,u,y}. Given a list of words, find the word that has the most pairs of double vowels, as it will be Bill's favorite word.</p>

<p>Notes:</p>

<ul>
	<li>It is guaranteed that there will be a unique correct answer. That is, one word in the list will have strictly more pairs of vowels than all other words in the list.</li>
	<li>No word in the input will have three or more of the same vowel consecutively, because that would just be too much for poor Bill.</li>
</ul>

### 입력 

 <p>The first line of each case contains N, the number of words in that case (0 < N ≤ 1000). The next N lines will contain the words that make up that case. Each word will contain only lowercase English letters <code>[a-z]</code>, and no word will be longer than 80 characters. Words will not necessarily be actual English words, but they will contain at least one letter. The input will be terminated by a line containing a single zero.</p>

### 출력 

 <p>For each case, print Bill's favorite word. Each output should be printed on its own line.</p>

