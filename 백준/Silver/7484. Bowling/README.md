# [Silver V] Bowling - 7484 

[문제 링크](https://www.acmicpc.net/problem/7484) 

### 성능 요약

메모리: 115696 KB, 시간: 212 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>It is well known that programmers enjoy bowling. Bowling is a competitive sport in which a player (the ―bowler‖) rolls a bowling ball down a wooden or synthetic lane with the objective of scoring points by knocking down as many pins as possible.</p>

<p>Scoring is part of bowling which beginners find hard to understand. Fortunately it is not as hard as it seems.</p>

<p>As most bowling centers have a scoring computer, you do not usually have to score yourself. One day, when it all breaks down, or you are needed to correct a mistake, an understanding of the scoring rules becomes important.</p>

<p>The most difficult part of bowling scoring is when a strike or spare is scored, as the score on the scorecard does not get updated immediately.</p>

<p>A game consists of ten frames, which start with a full rack of ten pins. In each frame, you have two deliveries of your ball, in which you need to knock down as many of ten pins as you can.</p>

<p>If you knock down all the pins on your first ball, it is called a strike. The score doesn't get added immediatelly because for a strike you get the values of your next two balls as a bonus. For example, if you score a strike in the first frame, then 7 and 1 in the second frame, you would score 18 (10+7+1) for the first frame, and 8 for the second frame, making a total of 26 after two frames.</p>

<p>If you knock down some of the pins on the first ball, and knocked down the remainder of the pins in the second ball, it is known as a spare. Again, the score doesn't get added immediatelly because for a spare you get the value of your next ball as a bonus. For example, if you score a spare in the first frame, say 6 and 4, then get 8 and 1 in the second frame, you would score 18 (6+4+8) for the first frame, and 9 for the second frame, making a total of 27 after two frames.</p>

<p>When it comes to the final frame, it is slightly different. In the final frame, you get extra balls if you strike or spare, to allow bonus points. If you strike in the first delivery you have the opportunity to strike in the remaining two and have three deliveries in total. If you scored strikes in each of your final three deliveries, the score for the final frame would be 30 (10+10+10). If you spare the final frame, you get the third delivery as a bonus. So, a spare, 9 and 1, followed by a strike would equal 20 (9+1+10).</p>

<p>You have to write a program which will calculate the score the player gets for the game given the information about the pins knocked down after each delivery of the ball.</p>

### 입력 

 <p>The first line of the input contains number t <= 1000 – the amount of test cases. Then the description of each of t test cases follow one per line. Each test case consists of several integers 0 <= a <= 10 – the amount of pins knocked down after each delivery of the ball. Each test case describes a full game for one player. All the games in the input file are correct.</p>

### 출력 

 <p>For each test case output the number of points the player gets in a game on a separate line.</p>

