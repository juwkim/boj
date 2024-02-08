# [Silver III] Maze 7 - 22312 

[문제 링크](https://www.acmicpc.net/problem/22312) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2024년 2월 9일 05:19:25

### 문제 설명

<p>In southern Ontario, many corn farmers create cornstalk mazes like the one shown. The mazes are created in the fall, after the grain has been harvested. There is still time for you to help design the best maze ever for 2010.</p>

<p>A field is covered with corn stalks except for a few obstacles (trees, buildings and the like) where corn cannot grow. The stalks, which are extremely tall, form the walls of the maze. Pathways are created on a square grid by crushing 1m square areas of stalks. One grid square on the edge is the entrance, and one grid square is the core of the maze.</p>

<p>Jack visits a corn maze every year, and has become adept at finding his way quickly from the entrance to the core. You are designing a new maze, and your job is to determine which stalks to crush, so as to maximize the number of squares Jack must visit.</p>

<p>The grader will determine which square is the entrance (the only one on the perimeter) and which square is the core (the one that Jack must walk farthest to reach).</p>

<p>A map of the rectangular field is represented as text; for example, a 6m by 10m field with eight trees might be represented as:</p>

<pre>##X#######
###X######
####X##X##
##########
##XXXX####
##########
</pre>

<p>The symbol # represents a square with standing cornstalks, and X represents a square with an obstacle (such as a tree) that cannot be crushed to form a pathway.</p>

<p>The field is transformed into a maze by crushing squares occupied by corn. One crushed square (the entrance) must be on the edge of the field. The other crushed squares must be in the interior. The objective is to maximize the shortest path from the entrance to the core, measured by the number of crushed squares that Jack must pass through, including the entrance and the core. It is possible to pass from one square to another only if both are crushed and they share an edge.</p>

<p>In your submission, the crushed squares should be identified by periods (.). Exactly one of the crushed squares should be on the perimeter. For example:</p>

<pre>#.X#######
#.#X#...##
#...X#.X.#
#.#......#
#.XXXX##.#
##########
</pre>

<p>Below, for illustration purposes only, we mark the entrance <code>E</code>, the core <code>C</code> and remainder of the path using <code>+</code>. The path length is 12.</p>

<pre>#EX#######
#+#X#C+.##
#+++X#+X.#
#.#++++..#
#.XXXX##.#
##########
</pre>

<p>The folder <code>/home/ioi2010-contestant/maze</code> contains several text files named <code>field1.txt</code> <code>field2.txt</code> etc. containing maps of cornfields. You are to copy them to files named <code>maze1.txt</code> <code>maze2.txt</code> etc., and transform them into valid mazes by replacing some of the # symbols by periods.</p>

<p> </p>

<p>The file <a href="https://upload.acmicpc.net/5637893d-e01d-4cf8-99df-18f89d0e339a/">field7.txt</a> represents a field of size 20x20. Create a maze for this field named <code>maze7.txt</code> that has a shortest path from the entrance to the core of length P. Your score for this subtask will be the minimum of 11 and 10<sup>P/33</sup>.</p>

### 입력 

 Empty

### 출력 

 Empty

