# [Gold V] Tetris (Large) - 12197 

[문제 링크](https://www.acmicpc.net/problem/12197) 

### 성능 요약

메모리: 113052 KB, 시간: 368 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 3월 20일 21:04:22

### 문제 설명

<p>Tetris is a famous video game that almost everyone has played it. In this problem, you need to simulate a simplified version of it.</p>

<p>In our version, the game is played in a <b>W</b> by <b>H</b> field with gravity. At the beginning, the field is empty. Then the tetrominos start to fall from above top of the field to bottom of the field, one by one. Each tetromino will stop as soon as it touches some other tetrominos or bottom of the field.</p>

<p>One interesting feature of the game is called "line clearing". A line will be cleared as soon as it is filled by tetrominos. More than one line may be cleared at a time. For example:</p>

<pre><code>  |..............|      |..............|      |..............|
  |.............o|      |..............|      |..............|
  |.............o|      |..............|      |..............|
  |.............o|      |..............|      |..............|
  |.............o|      |..............|      |..............|
  |..xx..........| -->  |..xx..........| -->  |..............|
  |xxxxxxxxxxxxx.|      |xxxxxxxxxxxxxo|      |..............|
  |xxxxxxxxxxxxx.|      |xxxxxxxxxxxxxo|      |..xx..........|
  |xx..xxxxxxxxx.|      |xx..xxxxxxxxxo|      |xx..xxxxxxxxxo|
  |xxxxxxxxxxx...|      |xxxxxxxxxxx..o|      |xxxxxxxxxxx..o|
  ----------------      ----------------      ----------------

  Falling               Stopped               Cleared 2 lines
</code></pre>

<p>Note that in this simplified version, the "floating" tetromino blocks won't continue to fall after lines are cleared. This is why the top-most two squares will keep in such position. Consequently, cascade clearing won't happen, even though it would happen in the original version of Tetris.</p>

<p>The game ends when all the given tetrominos are placed, or the current tetromino cannot be placed due to the height limit of the field is reached.</p>

<p>In this problem, each tetromino will has its type, rotation and falling position told by the input. They will start to fall from the <b>above</b> of the field. Your goal is to simulate and get the final result of each play.</p>

### 입력 

 <p>We have 7 types of tetromino:</p>

<pre><code>1   2   3   4   5   6   7

x    x  x    x  xx  x    x
xx  xx  x    x  xx  x   xxx
 x  x   xx  xx      x
                    x
</code></pre>

<p>Rotation of a tetromino is represented by a number <b>r</b>. <b>r</b> can be 0, 1, 2 or 3. Rotation is counterclockwise. For example:</p>

<pre><code>r=0   r=1  r=2   r=3

  x     x   xxx   x
 xxx   xx    x    xx
        x         x

 x     xx   x     xx
 xx   xx    xx   xx
  x          x
</code></pre>

<p>The horizontal falling position is represented by a number <b>x</b>. It is the coordinate of the lower left square of a tetromino's bounding box. Here <b>x</b> starts from 0.</p>

<p>The first line of the input gives the number of test cases, <b>T</b>. For each test case, the first line of input has 3 integers, <b>W, H, N</b>. <b>W</b> is the width, <b>H</b> is the height and <b>N</b> is the number of blocks that are going to fall.</p>

<p>Then <b>N</b> lines below, each line has 3 integers, <b>t<sub>i</sub>, r<sub>i</sub>, x<sub>i</sub></b>. <b>t<sub>i</sub></b> tells the tetromino type. <b>r<sub>i</sub></b> is the rotation of this tetromino. <b>x<sub>i</sub></b> is the horizontal falling position of this tetromino. It is guaranteed that <b>x<sub>i</sub></b> will make the tetromino inside the field, horizontally.</p>

### 출력 

 <p>For each test case, first output one line containing "Case #i:", where <b>i</b> is the test case number (starting from 1). And then, if the game ends before the <b>N</b> blocks, output "Game Over!"(without quotes). Otherwise, output the game field's final state, which should have <b>H</b> lines, each has <b>W</b> characters. Each character can be '.' or 'x'.</p>

