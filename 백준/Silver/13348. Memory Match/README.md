# [Silver I] Memory Match - 13348 

[문제 링크](https://www.acmicpc.net/problem/13348) 

### 성능 요약

메모리: 110068 KB, 시간: 112 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2025년 4월 21일 16:51:59

### 문제 설명

<p>You are playing the game “Memory Match”.</p>

<p>This game revolves around a set of N picture cards. The cards are organized in pairs: there are N/2 different pictures, each picture occurring on exactly two cards.</p>

<p>At the beginning of the game, the cards are shuffled and laid face down on the table. Players then take turns in guessing a pair of cards with the same picture. Each turn consists of picking a face-down card and turning it over to reveal its picture, then picking another face-down card and turning that card over as well. If the pictures on the two turned cards are identical, the cards remain face-up, the player scores a point and may take another turn. If the pictures are different, both cards are turned face-down again and the turn goes to the next player.</p>

<p>It is now your turn! Given a description of all previous actions in the game, pick as many matching pairs as possible.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13348/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-10-10%20%EC%98%A4%ED%9B%84%204.05.17.png" style="height:91px; width:500px"><br>
Figure 1: Illustration of the first example input. Only cards 3 and 6 have been matched correctly, all other cards are face-down. How many pairs can you score?</p>

### 입력 

 <p>The first line contains an even integer N, the number of cards on the table (2 ≤ N ≤ 1000).</p>

<p>The second line contains an integer K, the number of turns played thus far in the game (0 ≤ K ≤ 1000).</p>

<p>The following K lines each describe a turn. A turn is described by integers C<sub>1</sub> and C<sub>2 </sub>followed by words P<sub>1</sub> and P<sub>2</sub>. The numbers C<sub>1</sub> and C<sub>2</sub> refer to card positions on the table (1 ≤ C<sub>1</sub>, C<sub>2</sub> ≤ N and C<sub>1</sub> ≠ C<sub>2</sub>). The words describe the pictures on the two selected cards. Each word consists of between 1 and 20 lowercase letters in range ‘a’ . . . ‘z’. If P<sub>1</sub> = P<sub>2</sub>, the two cards stay face-up and the corresponding positions C<sub>1</sub> and C<sub>2</sub> may not be chosen again.</p>

<p>The input is such that at least two cards are still in face-down position.</p>

### 출력 

 <p>Output one line with an integer S, the number of matching pairs you can score with certainty.</p>

