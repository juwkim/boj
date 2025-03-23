# [Silver IV] Selling Cells - 4717 

[문제 링크](https://www.acmicpc.net/problem/4717) 

### 성능 요약

메모리: 111620 KB, 시간: 208 ms

### 분류

브루트포스 알고리즘, 기하학, 수학, 수치해석

### 제출 일자

2025년 3월 24일 07:30:08

### 문제 설명

<p>Competition has been fierce among the cellphone providers in the town of Eastern WestField. Several companies have been running ads in which they each claim to provide more coverage to the town than do any of their competitors.</p>

<p>AetherTech Telecommunications suspects that they, in fact, really do cover a larger portion of the town than do their competitors. They would like to compute their actual coverage so they they can advertise the true amount.</p>

<p>The metropolitan area of Eastern WestField will be modeled as a circle around the town center. The area covered by each cell tower can also be modeled as a circle, centered on the location of the tower, indicating the area within which a the tower provides sufficient signal strength for a phone to connect (e.g., one bar on the average phone’s signal strength meter).</p>

<p>All cell towers to be considered will have their centers within the metropolitan area, though their area of coverage may extend beyond the border of the metropolitan area. The areas covered by different towers can overlap, though for economic reasons no two towers have been constructed so close to one another that the center of one would lie within the coverage area of the other.</p>

<p>Compute the fraction of the metropolitan area within which a cell phone would be covered by at least one tower.</p>

### 입력 

 <p>Input consists of multiple data sets. Each data set begins with a line containing a single integer N, 1 ≤ N ≤ 25. This line is followed by N lines, each containing three floating point numbers x, y, r. These give the (x,y) coordinates of the circle’s center and the radius of that circle, respectively.</p>

<p>The first circle in the list denotes the metropolitan area of Eastern Westfield. Each of the remaining N-1 circles describes a cell tower.</p>

<p>The final data set is followed by a line containing a zero.</p>

### 출력 

 <p>For each data set, compute the fraction of the metropolitan area covered by the cell towers (as a number in the range 0.00 . . . 1.00 and print a line containing that fraction as a real number presented to 2 decimal points precision.</p>

<p> </p>

