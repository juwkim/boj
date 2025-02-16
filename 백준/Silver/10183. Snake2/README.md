# [Silver II] Snake2 - 10183 

[문제 링크](https://www.acmicpc.net/problem/10183) 

### 성능 요약

메모리: 113500 KB, 시간: 112 ms

### 분류

자료 구조, 덱, 구현, 시뮬레이션

### 제출 일자

2025년 2월 16일 17:44:28

### 문제 설명

<p>Many people have played the snake game (a few years ago Nokia phones came with snake on it, sometimes when watching YouTube videos you could pause the video and press the left arrow to start the game…). Let’s simulate that game!</p>

<p>For this program, you will be given a matrix (15x15) of spaces and letters. The snake will initially consist of 3 contiguous ‘X’ characters, and the food pellets are represented by the ‘F’ character. The object of the game is to eat food pellets and grow, without hitting the boundary (stay within the size of the matrix).</p>

<p>For this program, you need to keep track of how the snake grows, how many pellets it eats, and whether the game ends or not. The game will end if either the snake goes outside the playing area OR it runs into itself.</p>

<p>The input will be a string of 20 of the characters “UDLRO” standing for Up, Down, Left, Right, and Onward…continue in the same direction. For each input, determine either how many food pellets are eaten, or if it is game over (by leaving the matrix). The game will restart with the same board configuration of snake and pellets. The snake will start to move to the RIGHT at the beginning of the game, and the snake will be horizontal.</p>

<p>Here is an example of the snake moving with the following input string:</p>

<pre>UROOOUOOLOOOOOUOOOOO
12345678901234567890</pre>

<p>The first 5 moves made are in bold below (12345). On the 8th move, the snake would eat the pellet! Then, you would turn left and continue to eat the next pellet straight ahead (move 14).</p>

<pre>0                   X
9                   X
8                   X
7                   X
6           --->    X
5F32109F            54321098
       7                   7
       6                   6
   12345               12345
 XXX    F                   F</pre>

<p>Due to eating two pellets, the snake would be 5 X’s long and be continuing upwards</p>

### 입력 

 <p>The first 15 lines consists of the matrix (15x15 characters). The next line will consist of the number of data sets. Each data set will consist of a line of 20 characters (UDLRO).</p>

### 출력 

 <p>For each data set, print out “N pellets” or “GAME OVER”. Then print out the final game board. Separate games with a blank line.</p>

