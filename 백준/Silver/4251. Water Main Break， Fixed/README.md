# [Silver II] Water Main Break, Fixed - 4251 

[문제 링크](https://www.acmicpc.net/problem/4251) 

### 성능 요약

메모리: 112208 KB, 시간: 1236 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2025년 2월 7일 06:31:48

### 문제 설명

<p>The reason that water main breaks cause so much water wastage is that it typically takes a while to fix them. And part of that is in turn that the crews capable of fixing a water break must get there first. This is particularly the case when there’s multiple breaks at once, and not enough crews to fix them all at the same time. Then, a decision needs to be made whether to first go to the far-away break that may be leaking more water, or fix a few nearby ones that one can get to quickly. That’s actually a non-trivial optimization problem, and — by sheer coincidence — one that you are asked to solve here.</p>

<p>We will give you a list of water main breaks. For each, you’ll be given its (x, y) coordinates, the time at which it starts flooding, and the rate at which water is flowing there. The repair crew starts at the origin at time 0, and can travel at a given speed v along straight lines. (There are no streets or obstacles in this problem.) Your goal is to find a sequence of visits to the locations that minimizes the total water that is lost. Notice that we assume here that the repair crews know the entire future of where the water main breaks will be. However, if a water main break will happen at a location at time 3, it doesn’t help the crew to arrive there at time 2.5 — they will have to wait until time 3 to fix it.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form: The first line contains an integer 1 ≤ n ≤ 10, the number of water main breaks, and the double v > 0, the speed of the repair crew’s truck.</p>

<p>Next come n lines, each describing one water main break with four doubles x<sub>i</sub>, y<sub>i</sub>, t<sub>i</sub>, r<sub>i</sub>. (x<sub>i</sub>, y<sub>i</sub>) with −1000.0 ≤ xi, y<sub>i</sub> ≤ 1000.0 is the location of the water main break, and 0 ≤ t<sub>i</sub> ≤ 1000.0 the time at which the pipe there broke. 0 ≤ r<sub>i</sub> ≤ 1000.0 is the rate at which water is flowing. Notice that we assume that once the repair crew reaches the location of a main break, they repair it instantaneously, and can start driving to the next location.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then output the minimum amount of water that is lost if the repair crew chooses the optimum way to visit the main break locations, rounded to two decimals. Remember that the crew starts at the origin (0, 0) at time 0.</p>

<p>Each data set should be followed by a blank line.</p>

