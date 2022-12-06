# [Bronze I] Memory - 10228 

[문제 링크](https://www.acmicpc.net/problem/10228) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

구현(implementation)

### 문제 설명

<p><img alt="" src="" style="width: 267px; height: 220px; float: right;">A game called <i>Memory</i> is played using 50 cards. Each card has one of the letters from A to Y (ASCII 65 to 89) printed on the face, so that each letter appears on exactly two cards. The cards are shuffled into some random order and dealt face down on the table.</p>

<p>Jack plays the game by turning two cards face up so the letters are visible. For each of the 25 letters Jack gets a candy from his mother the first time he sees both copies of the letter on the two face up cards. For example, the first time Jack turns over both cards that contain the letter M, he gets a candy. Regardless of whether the letters were equal or not, Jack then turns both cards face down again. The process is repeated until Jack receives 25 candies – one for each letter.</p>

<p>You are to implement a procedure <b>play</b> that plays the game. Your implementation should call the procedure <b>faceup(C)</b> which is implemented by the grader. <b>C</b> is a number between 1 and 50 denoting a particular card you wish to be turned face up. The card must not currently be face up. <b>faceup(C)</b> returns the character that is printed on the card <b>C</b>.</p>

<p>After every second call to faceup, the grader automatically turns both cards face down again.</p>

<p>Your procedure <b>play</b> may only terminate once Jack has received all 25 candies. It is allowed to make calls to <b>faceup(C)</b> even after the moment when Jack gets the last candy.</p>

### 입력 

 Empty

### 출력 

 Empty

