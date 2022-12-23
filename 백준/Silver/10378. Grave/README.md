# [Silver IV] Grave - 10378 

[문제 링크](https://www.acmicpc.net/problem/10378) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

기하학(geometry)

### 문제 설명

<p>Gerard develops a Halloween computer game. The game is played on a rectangular graveyard with a rectangular chapel in it. During the game, the player places new rectangular graves on the graveyard. The grave should completely fit inside graveyard territory and should not overlap with the chapel. The grave may touch borders of the graveyard or the chapel.</p>

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/grave.png" style="height:225px; width:282px"></p>

<p>Gerard asked you to write a program that determines whether it is possible to place a new grave of given size or there is no enough space for it.</p>

### 입력 

 <p>The first line of the input file contains two pairs of integers: x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub> (−10<sup>9</sup> ≤ x<sub>1</sub> < x<sub>2</sub> ≤ 10<sup>9</sup>; −10<sup>9</sup> ≤ y<sub>1</sub> < y<sub>2</sub> ≤ 10<sup>9</sup>) — coordinates of bottom left and top right corners of the graveyard. The second line also contains two pairs of integers x<sub>3</sub>, y<sub>3</sub>, x<sub>4</sub>, y<sub>4</sub> (x<sub>1</sub> < x<sub>3</sub> < x<sub>4</sub> < x<sub>2</sub>; y<sub>1</sub> < y<sub>3</sub> < y<sub>4</sub> < y<sub>2</sub>) — coordinates of bottom left and top right corners of the chapel.</p>

<p>The third line contains two integers w, h — width and height of the new grave (1 ≤ w, h ≤ 10<sup>9</sup>). Side with length w should be placed along OX axis, side with length h — along OY axis.</p>

### 출력 

 <p>The only line of the output file should contain single word: “Yes”, if it is possible to place the new grave, or “No”, if there is not enough space for it.</p>

