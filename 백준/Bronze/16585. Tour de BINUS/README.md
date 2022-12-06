# [Bronze II] Tour de BINUS - 16585 

[문제 링크](https://www.acmicpc.net/problem/16585) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>BINUS University has N rooms to be used as lecture classes. These N rooms are numbered from 1 to N and arranged in a straight line, where the 1<sup>st</sup> room is the left-most room, and the Nth room is the right-most room.</p>

<p>On one fine afternoon, Ayu and Budi, two BINUS’ alumni, visit their lovely alma mater and walk around the campus. At that particular time, there might be a lecture in each class where Ai students attend the lecture in the i<sup>th</sup> room.</p>

<p>Ayu starts her walk from the x<sup>th</sup> room and walk in one direction to the first or last room (depends on the direction). While she walks, she counts the total number of students in all the rooms she passed. For example, if she starts from the 5<sup>th</sup> room and going left, then she will count the total number of students in the 5<sup>th</sup>, 4<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, and 1<sup>st</sup> room. If she is going right, then she will count the total number of students from the 5<sup>th</sup> room up to the Nth room. Budi also does a similar thing as Ayu, however, instead of counting the total number of students, Budi only counts the number of rooms which are not being used (empty rooms) at that time, i.e. when A<sub>i</sub> = 0.</p>

<p>Given array A (representing the number of students in each room), Ayu’s starting point (x<sub>1</sub>), Ayu’s direction, Budi’s starting point (x<sub>2</sub>), and Budi’s direction, compute the total number of students in Ayu’s walk and the total number of empty rooms in Budi’s walk.</p>

### 입력 

 <p>Input begins with an integer N (1 ≤ N ≤ 100) representing the number of rooms. The second line contains N integers: A<sub>i</sub> (0 ≤ A<sub>i</sub> ≤ 60) representing the number of students in the i<sup>th</sup> room. If A<sub>i</sub> = 0, then it means the room is not being used (empty). The third line contains an integer x<sub>1</sub> (1 ≤ x<sub>1</sub> ≤ N) and a string d<sub>1</sub>, representing Ayu’s walk from the x<sub>1</sub><sup>th</sup> room in d<sub>1</sub>’s direction. The fourth line contains an integer x<sub>2</sub> (1 ≤ x<sub>2</sub> ≤ N) and a string d<sub>2</sub>, representing Budi’s walk from the x<sub>2</sub><sup>th</sup> room in d<sub>2</sub>’s direction. It is guaranteed that d<sub>1</sub> and d<sub>2</sub> will be either “left” or “right” (without quotes).</p>

### 출력 

 <p>Output in a line two integers (separated by a single space) representing the total number of students in Ayu’s walk and the total number of empty rooms in Budi’s walk, respectively.</p>

