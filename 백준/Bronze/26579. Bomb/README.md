# [Bronze I] Bomb - 26579 

[문제 링크](https://www.acmicpc.net/problem/26579) 

### 성능 요약

메모리: 114488 KB, 시간: 128 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Bomberman is having some trouble defeating his enemies, and he has asked you to help him figure out where to place his bomb in order to defeat the most enemies. In this scenario, bomberman's bombs destroy everything in the four cardinal directions to the edge of the map, except for stopping at walls that cannot be broken. Write a program that finds the best spot to place a bomb to destroy the most enemies.</p>

### 입력 

 <p>The first line will contain a single integer n that indicates the number of data sets that follow. Each data set will start with two integers, r c representing the number of rows and columns in each map, respectively. The next r lines will consist of c characters, representing the map. # denotes a wall, . is a blank space, and @ is an enemy. The bomb can only be placed in a blank space. Rows are numbered 0 to r-1 and columns are numbered 0 to c-1.</p>

### 출력 

 <p>Output the coordinate for the bomb, in the format r, c, where r is the row number and c is the column number. The bomb will explode outward in the four cardinal directions, destroying any enemy in its path. The explosion only stops in one direction when it reaches the end of the map or when it hits a wall, in which case any enemy past that wall is safe. Assume that there will always be at least one enemy that a bomb can hit, and there will never be more than one best placement.</p>

