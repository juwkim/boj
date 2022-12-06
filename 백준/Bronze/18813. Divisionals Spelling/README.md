# [Bronze III] Divisionals Spelling - 18813 

[문제 링크](https://www.acmicpc.net/problem/18813) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Emilio’s team is competing at the South Pacific ICPC Divisional Finals. They have read the problems and immediately know all the solutions. Emilio finds simply winning the contest boring. Instead, he has convinced his team to spell out a word with their submissions. He has put together a list of n words that he would like to spell.</p>

<p>Each question in the contest is labelled with an uppercase letter. The first question is labelled “A”, the second is labelled “B”, and so on. A word is spelled by solving questions in a specific order. For example, if Emilio’s team wants to spell <code>LEAK</code>, the team first solves problem L, then problem E, then problem A, and finally problem K. The team may only solve each problem once, so they may not spell words with duplicated letters (for example, they cannot spell <code>EMILIO</code>). Which words can Emilio’s team spell?</p>

### 입력 

 <p>The first line contains two integers n (1 ≤ n ≤ 100), which is the number of words in Emilio’s list, and m (1 ≤ m ≤ 15), which is the number of questions in the contest.</p>

<p>The next n lines describe the words. Each of these lines contains a word with at least 1 and at most 15 uppercase letters. All the words are distinct.</p>

### 출력 

 <p>Display the number of words in the list that can be spelled.</p>

