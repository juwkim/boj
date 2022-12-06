# [Bronze I] Noughts & Crosses - 7584 

[문제 링크](https://www.acmicpc.net/problem/7584) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Noughts and crosses is a simple game played by 2 people. The aim is to get a row of 3 of your own symbols (vertically, horizontally or diagonally) before your opponent can do so. For example: </p>

<p><img alt="" src="" style="height:126px; width:307px"></p>

<p>Game 1 shows X winning with a horizontal row. Game 2 shows O winning with a diagonal row. Game 3 is a draw as neither side has completed a row. </p>

### 입력 

 <p>In this problem you will be given one or more games to follow and must determine who has won. Each game occupies a single line and begins with a letter, X or O, which shows who takes the first turn. Input is terminated by a line which contains just the character # - this line should not be processed.</p>

<p>A number of turns follow the initial letter, on the same line, all separated from each other by a space. A turn is designated by one of the numbers from 1 to 9, numbers representing board squares as shown below:</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/7584/2.png" style="height:101px; line-height:20.8px; width:106px"></p>

<p>Game 1 above could have been represented as</p>

<pre>X 1 5 9 7 3 6 2 </pre>

### 출력 

 <p>For each game in the input, 1 line of output should be given. If there is a winner, the output should be an upper case X or an upper case O as appropriate. If there is no winner, the output should be the word Draw. </p>

