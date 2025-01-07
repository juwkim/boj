# [Silver II] Similarity - 3312 

[문제 링크](https://www.acmicpc.net/problem/3312) 

### 성능 요약

메모리: 125188 KB, 시간: 312 ms

### 분류

구현, 문자열, 두 포인터

### 제출 일자

2025년 1월 8일 07:36:06

### 문제 설명

<p>Byteman works in a computational biology research team in Gdynia. He is a computer scientist, though, and his work is mainly concentrated on designing algorithms related to strings, patterns, texts etc. His current assignment is to prepare a tool for computing the similarity of a pattern and a text.</p>

<p>Given a pattern and a text, one can align them in many different ways, so that each letter of the pattern has a corresponding letter in the text. Here we only consider alignments without holes, in which the pattern is matched against a consecutive part of the text of length equal to the length of the pattern. For any such alignment, one can count the positions where the letter of the pattern is the same as the corresponding letter of the text. The sum of such numbers is called the similarity of the pattern and the text. The table below illustrates the computation of the similarity between an example pattern <code>abaab</code> and the text <code>aababacab</code>.</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/3312/1.png" style="height:171px; width:301px"></p>

<p>Byteman has already managed to implement the graphical interface of the tool. Could you help him in writing the piece of software responsible for computing the similarity?</p>

### 입력 

 <p>The standard input consists of two lines. The first line contains a non-empty string composed of small English letters — the pattern. The second line contains a non-empty string composed of small English letters — the text. You may assume that the length of the pattern does not exceed the length of the text. The text contains no more than 2 000 000 letters.</p>

<p>Additionally, in test cases worth 30 points the length of the text does not exceed 5 000.</p>

### 출력 

 <p>The only line of the standard output should contain the similarity of the given pattern and the text.</p>

