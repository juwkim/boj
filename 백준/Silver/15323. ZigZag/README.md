# [Silver III] ZigZag - 15323 

[문제 링크](https://www.acmicpc.net/problem/15323) 

### 성능 요약

메모리: 119012 KB, 시간: 268 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 정렬, 문자열, 트리를 사용한 집합과 맵

### 제출 일자

2024년 1월 28일 20:17:01

### 문제 설명

<p>Zig and Zag are playing a word game. Zig says one letter, and Zag says a word that starts with that letter. However, the word needs to be from the allowed word list and such that Zag already said it the least amount of times. If the word choice is ambiguous, then Zag will choose the one that is lexicographically smaller (sooner in the alphabet). For each Zig’s letter, it will be possible to choose a word.</p>

<p>Let there be a list consisting of exactly K distinct words and an array of N letters that Zig has given. Write a program that will, based on the input, output an array of N words that Zag said during the game.</p>

### 입력 

 <p>The first line of input contains positive integers K (1 ≤ K ≤ 100 000) and N (1 ≤ N ≤ 100 000) from the task.</p>

<p>Each of the following K lines contains a single word consisting of lowercase letters of the English alphabet not longer than 21 characters.</p>

<p>Each of the following N lines contains a single lowercase letter of the English alphabet.</p>

### 출력 

 <p>You must output N lines, each containing a single word from the task.</p>

