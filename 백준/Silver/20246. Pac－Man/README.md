# [Silver IV] Pac-Man - 20246 

[문제 링크](https://www.acmicpc.net/problem/20246) 

### 성능 요약

메모리: 113248 KB, 시간: 116 ms

### 분류

구성적(constructive)

### 문제 설명

<p>Pac-Man is a maze-chase video game developed in 1980s. The player controls the character “Pac-Man” to eat dots in a maze while avoiding enemy characters “ghosts.” All characters may move in four directions: up, down, left, right. The game ends when one of the following two conditions is met:</p>

<ol>
	<li>Pac-Man eats all dots in the maze. In this case, the player wins.</li>
	<li>A ghost catches Pac-Man. In this case, the player loses.</li>
</ol>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">Figure 1: Pac-Man gameplay (image from <a href="https://en.wikipedia.org/wiki/File:Pac-man.png">Wikipedia</a>)</p>

<p>Adam is learning how to create games with modern programming tools. To practice the skills, he tries to reproduce the Pac-Man game with some modification. In Adam’s game, the playable character is a “ghost,” and the enemy character is “Pac-Man.” Since he changes the roles of the ghost and Pac-Man, he also changes the ending conditions of the game.</p>

<ol>
	<li>Pac-Man eats all dots in the maze. In this case, the player loses.</li>
	<li>The ghost controlled by the player catches Pac-Man. In this case, the player wins.</li>
</ol>

<p>Adam has almost developed the first full functioning version of his game. He wants to test his game and creates a simple stage for testing. The maze of the stage is based on a 10-by-10 grid. We label the cell at the intersection of row r and column c with (r, c). In this problem, rows and columns are numbered from 0 to 9. Each grid cell contains exact one dot. The exterior boundary of the grid are walls. No characters may move to the area outside of the grid. Inside the grid, there are no walls or obstacles. All characters may move freely from a cell to any cell adjacent to it. Note that two grid cells (r<sub>1</sub>, c<sub>1</sub>) and (r<sub>2</sub>, c<sub>2</sub>) are adjacent to each other if and only if |r<sub>1</sub> − r<sub>2</sub>| + |c<sub>1</sub> − c<sub>2</sub>| = 1.</p>

<p>Adam has to prepare the movements of Pac-Man for the testing. He needs a set of Pac-Man’s trajectories with diversity, but any trajectory must satisfy the following requirements.</p>

<ul>
	<li>Pac-Man eats all dots in the maze if it follows the trajectory.</li>
	<li>Pac-Man moves at most 10000 steps.</li>
</ul>

<p>Adam needs your help to generate a trajectory starting at cell (x, y). Please write a program to generate a trajectory of Pac-Man satisfying all requirements above and starting at cell (x, y).</p>

### 입력 

 <p>The input has exactly one line which consists of two space-separated integers x and y. You are asked to generate a trajectory starting at cell (x, y).</p>

### 출력 

 <p>You must output a requested trajectory in the following format: The trajectory is represented by m + 1 lines where m is the number of steps of the trajectory. The i-th line contains two integers r<sub>i</sub> and c<sub>i</sub> separated by exactly one space. The trajectory starts at the cell (r<sub>1</sub>, c<sub>1</sub>), and Pac-Man will be in cell (r<sub>i</sub>, c<sub>i</sub>) after moving i − 1 steps along the trajectory for 1 < i ≤ m + 1.</p>

<p>If there are multiple solutions, then you may output any of them.</p>

