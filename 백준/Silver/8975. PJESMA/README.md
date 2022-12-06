# [Silver V] PJESMA - 8975 

[문제 링크](https://www.acmicpc.net/problem/8975) 

### 성능 요약

메모리: 115612 KB, 시간: 140 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>"Guess the song" is a popular game among young programmers in Croatia. It is a game of skill, wisdom and patience. The game host plays a song so that all players hear it. The players' goal is to guess the title of the song as fast as possible. </p>

<p>Mirko may not be much of a programmer, but he is a world class song-guesser. Mirko always guesses the song at the moment when at least half of the words in the title of the song have been said in the lyrics. All words in the song title are unique (no word will occur two or more times). </p>

<p>Write a program that, given the song title and its lyrics, determines at which point during the song (after how many words) Mirko guesses the title. </p>

### 입력 

 <p>The first line contains an integer N, 1 ≤ N ≤ 50, the number of words in the song title. </p>

<p>Each of the following N lines contains one word in the song title. </p>

<p>The next line contains an integer M, 1 ≤ M ≤ 10 000, the number of words in the lyrics. </p>

<p>Each of the following M lines contains one word of the lyrics. </p>

<p>All words in the title and lyrics will consist of between 1 and 15 lowercase English letters. </p>

<p>Note: the test data will be such that Mirko will always guess the song title from the lyrics. </p>

### 출력 

 <p>Output the number of words in the song lyrics after which Mirko guesses the title. </p>

