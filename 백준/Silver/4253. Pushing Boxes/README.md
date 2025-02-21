# [Silver II] Pushing Boxes - 4253 

[문제 링크](https://www.acmicpc.net/problem/4253) 

### 성능 요약

메모리: 111936 KB, 시간: 124 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 2월 21일 22:38:35

### 문제 설명

<p>Scrap cars in a junk yard are crushed in a device that pushes the car in from the sides, from the front and back, and from the top and bottom. The result is a compact little chunk of metal. In this problem you’re going to model a device that works in a similar manner, but doesn’t crush anything, only pushes boxes around in two dimensions. The boxes are all square with unit length on a side and are situated on the floor of a room. Each wall of the room can be programmed to move inward a certain amount, pushing any boxes it may bump into. Unlike the car-crusher, this device is sensitive and if it senses that boxes are stacked up against a wall and that it might crush them if pressed any farther, it will stop.</p>

<p>For example, suppose we have boxes arranged in a 12-by-16 room as shown below. The upper left-hand corners of the boxes (which is how we will locate them in this problem) are at coordinates (1,13) (box A below), (3,2), (6,2), (6,4), (6,6), (7,6) and (8,9) (box G), where the first coordinate indicates distance from the top wall and the second coordinate indicates distance from the left wall. </p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/pb1.png" style="height:209px; width:299px"></p>

<p>Suppose the top wall is programmed to move down 3 units (then retreats, as the walls always will) and then the right wall is programmed to move left 14 units. The first operation can be performed with no problem, but the second one can not be carried out without crushing some boxes. Therefore, the right wall will move only 13 units, the maximum distance it can move until boxes are packed tightly between it and the left wall. The boxes will then be in the configuration shown in the following figure. The locations of the boxes are (3,1), (3,2), (6,0), (6,1), (6,2), (7,2), (8,2).</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/pb2.png" style="height:207px; width:296px"></p>

### 입력 

 <p>There will be multiple data sets for this problem. The first line of each data set will be two integers giving the height and width of the room. (We’ll visualize the room as if on a piece of paper, as drawn above.) Each dimension will be no more than 20. The next line will contain an integer n (0 < n ≤ 10) followed by n pairs of integers, each pair giving the location of a box as the distances from the top and the left walls of the room. The following lines will be of the form direction m, where direction is either down, left, up, right, or done and m is a positive integer. For example, left 2 would mean to try to move the right wall 2 spaces to the left. The “direction” done indicates that you are finished pushing this set of boxes around. There will be no integer m following the direction done, of course. The data sets are followed by a line containing 0 0.</p>

### 출력 

 <p>For each data set you are to produce one line of output of the form:</p>

<pre>Data set d ends with boxes at locations (r<sub>1</sub>, c<sub>1</sub>) (r<sub>2</sub>, c<sub>2</sub>) . . . (r<sub>n</sub>, c<sub>n</sub>).</pre>

<p>where the (r<sub>i</sub>, c<sub>i</sub>) are the locations of the boxes given from top-to-bottom, left-to-right, (separated by one space) and d is the data set number (starting at 1).</p>

