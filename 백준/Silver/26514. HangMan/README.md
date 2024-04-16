# [Silver III] HangMan - 26514 

[문제 링크](https://www.acmicpc.net/problem/26514) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현

### 제출 일자

2024년 4월 17일 05:12:53

### 문제 설명

<p>In the classic blackboard game HangMan you are given a word and attempt to guess the word by choosing a series of letters. In this program, you must determine if the provided letters are contained in the word prior to a body figure being drawn. One body part is added for each letter not contained in the word. The body figure below consists of the head shown by the letter "O", two body parts "|", 2 arms shown by equal signs "=", 2 hands shown by asterisks "*", and legs shown using a forward slash "/"and a back slash "\", 9 parts in all, drawn in order, top to bottom - from left to right, as shown below. Once all the letters of the word are found, the game ends and no further letters are read. The game also ends once the figure is completed. If no body parts are drawn, print the word “SAFE”.</p>

<pre>  O
*=|=*
  |
 / \
</pre>

### 입력 

 <p>The first line contains a single positive integer, k, indicating the number of data sets. Each data set is on one line, and consists of a single word S (all capital letters), an integer N, followed by N distinct capital letters.</p>

### 출력 

 <p>The word and resulting hangman figure, according to the series of guesses provided by the letters. The body parts MUST align as shown, with the "*" on the left edge of the screen, and all other parts aligned accordingly. Exactly one blank line must follow each output.</p>

