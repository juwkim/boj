# [Bronze I] Crushing Confections - 11343 

[문제 링크](https://www.acmicpc.net/problem/11343) 

### 성능 요약

메모리: 30840 KB, 시간: 328 ms

### 분류

구현(implementation)

### 문제 설명

<p>A popular app has players line up a set of three candies of the same color in a row in order to remove them from the screen and continue playing. The candies come in six colors: blue, yellow, green, orange, purple, and red. They are arranged in a two-dimensional grid with horizontal rows and vertical columns. Once a player has moved candies to complete and remove a set of candies, the game must automatically find and remove any remaining sets of three candies of the same color in a row.</p>

<p>Your program must find and display the location of a valid set of three candies of the same color in a row (or column) or display “no set found.” If there is more than one valid set, your program may display the location of any one of the valid sets. The rows are numbered from 1 starting at the top. The columns are numbered from 1 starting at the left.</p>

### 입력 

 <p>The input will start with a number representing the number of test cases. Each test case consists of one line containing two integers representing the number of rows and columns of the grid followed by a grid representing the colors of the candies.</p>

<p>The dimensions of the board will be at most 100 by 100.</p>

### 출력 

 <p>Your output should be three ordered pairs of integers representing row numbers and column numbers, respectively, of a valid set if there is a valid set found. If there is no valid set found, your output should consist of the message “no set found.”</p>

