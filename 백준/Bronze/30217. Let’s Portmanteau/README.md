# [Bronze II] Let’s Portmanteau - 30217 

[문제 링크](https://www.acmicpc.net/problem/30217) 

### 성능 요약

메모리: 113112 KB, 시간: 124 ms

### 분류

구현, 문자열

### 문제 설명

<p>From “yourdictionary.com”: Portmanteau, pronounced “port-man-tow,” refers to a new word made from two words and their meanings. For example, the portmanteau brunch refers to a combined meal of breakfast and lunch, and spork is a mix between a spoon and a fork.</p>

<p>You are to combine two words using a simplified approach.</p>

<p>Rules for combining:</p>

<ol>
	<li>Get the first letter of the first word regardless of what (vowel or consonant) it is. Then, starting from the second letter of the first word, get letters moving right until you reach a vowel. If no vowels while moving right, all letters will be taken. If there is a vowel moving right, let’s call it v<sub>1</sub>.</li>
	<li>Get the last letter of the second word regardless of what (vowel or consonant) it is. Then, starting from the letter next to the last letter of the second word, get letters moving left until you reach a vowel. If no vowels while moving left, all letters will be taken. If there is a vowel moving left, let’s call it v<sub>2</sub>.</li>
	<li>Combine the two words by listing the letters taken from the first word (Step 1), followed by a vowel (let’s call it the merging vowel), followed by the letters taken from the second word (Step 2). The merging vowel is as follows:
	<ol>
		<li>If the second word has a vowel while moving left (i.e., v<sub>2</sub> exists), v<sub>2</sub> is the merging vowel.</li>
		<li>If the second word does not have a vowel while moving left (i.e., v<sub>2</sub> does not exist) but the first word has a vowel while moving right (i.e., v<sub>1</sub> exists), v<sub>1</sub> is the merging vowel.</li>
		<li>If v<sub>1</sub> and v<sub>2</sub> don’t exist (i.e., neither word has a vowel while moving right/left), use the letter “o” as the merging vowel.</li>
	</ol>
	</li>
</ol>

<p>Assume the vowels are “aeiou”.</p>

### 입력 

 <p>There are two input lines: the first line provides the first word and the second line provides the second word. Assume that each word starts in column 1, is at least 4 letters and at most 20 letters, and contains only lowercase letters.</p>

### 출력 

 <p>Print the combined word on one output line.</p>

