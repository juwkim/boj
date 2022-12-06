# [Platinum IV] 선분 교차 3 - 20149 

[문제 링크](https://www.acmicpc.net/problem/20149) 

### 성능 요약

메모리: 2056 KB, 시간: 0 ms

### 분류

많은 조건 분기(case_work), 기하학(geometry), 선분 교차 판정(line_intersection)

### 문제 설명

<p>2차원 좌표 평면 위의 두 선분 L<sub>1</sub>, L<sub>2</sub>가 주어졌을 때, 두 선분이 교차하는지 아닌지 구해보자. 한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차하는 것이다.</p>

<p>L<sub>1</sub>의 양 끝 점은 (x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>), L<sub>2</sub>의 양 끝 점은 (x<sub>3</sub>, y<sub>3</sub>), (x<sub>4</sub>, y<sub>4</sub>)이다.</p>

### 입력 

 <p>첫째 줄에 L<sub>1</sub>의 양 끝 점 x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>가, 둘째 줄에 L<sub>2</sub>의 양 끝 점 x<sub>3</sub>, y<sub>3</sub>, x<sub>4</sub>, y<sub>4</sub>가 주어진다.</p>

### 출력 

 <p>L<sub>1</sub>과 L<sub>2</sub>가 교차하면 첫째 줄에 1, 아니면 0을 출력한다.</p>

<p>두 선분이 한 점에서 교차하는 경우 둘째 줄에 교차하는 점의 x좌표와 y좌표를 공백으로 구분해 출력한다. 한 점에서 교차하지 않는 경우에는 둘째 줄을 출력하지 않는다.</p>

<p>좌표의 절대/상대 오차는 10<sup>-9</sup>까지 허용한다.</p>

