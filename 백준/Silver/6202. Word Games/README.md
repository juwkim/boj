# [Silver V] Word Games - 6202 

[문제 링크](https://www.acmicpc.net/problem/6202) 

### 성능 요약

메모리: 118352 KB, 시간: 272 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>The cows are playing Scrabble but, sad to say, they do not have the vocabulary to play at the tournament level. Bessie wants your help for just the first move. Given her rack (a "rack" is a holder of Scrabble letters) of N (3 <= N <= 10) letters (which might or might not be unique and might include one or more blank "wild card" tiles) along with a scrabble dictionary of D (10 <= D <= 50000) words, print the words she might use (by searching the dictionary).</p>

<p>The 27 possible letters are upper-case 'A'..'Z' and the '#' symbol, which represents a "wildcard" and can stand for any letter. If two '#'s appear in one rack, each can represent a different letter when played.</p>

<p>The dictionary words can be read, one per line, from file whose name is 'scrbl.txt' (the file name is all lower case letters, unlike the file's contents). The letters in Bessie's rack can always be used to make at least one word. Each word in the dictionary is unique. Remember that you are running on Linux: each input line ends with a '\n' character; no 'return' characters are present.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, N and D.</li>
	<li>Line 2: N letters (with no intervening blanks) that are the letters in Bessie's Scrabble rack.</li>
</ul>

### 출력 

 <ul>
	<li>Lines 1..??: Each line contains a single word that appears in the scrbl.txt dictionary. Print the output in the order the words appear in the dictionary.</li>
</ul>

