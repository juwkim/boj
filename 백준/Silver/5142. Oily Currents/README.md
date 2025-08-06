# [Silver I] Oily Currents - 5142 

[문제 링크](https://www.acmicpc.net/problem/5142) 

### 성능 요약

메모리: 120076 KB, 시간: 168 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 8월 7일 02:45:52

### 문제 설명

<p>One major problem with something like an oil spill is that the oil doesn’t just stay where it comes from. If we just had a big cloud of oil forming right above the ruptured oil well itself, while still being a big problem, it would be much easier to clean up. But instead, the oil spreads both under the water and on top, due to wind, waves, and currents. Once it is covering hundreds of square miles, it becomes much harder to clean. Here, we will use a simple model to calculate the area that will find itself covered by oil due to currents. For simplicity, we will focus only on two dimensions and a bounded region; any oil leaving that region is assumed to never return to it.</p>

<p>You will be given the information on currents in the following form: for a 2-dimensional grid, each location will tell you the strength (0–4) and direction (N,S,E,W) of the current. For instance, 2N means that once the current square gets contaminated with oil, within one time step, the two squares immediately to the north of this square will also be contaminated. You will also be given the coordiantes of the square where the oil spread starts, and the duration t to simulate. Your task is to output the map of the oil spread after those t steps.</p>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line contains five integers x,y,x0,y0,t. 1 ≤ x,y ≤ 100 are the width and height of the map. 1 ≤ x0 ≤ x, 1 ≤ y0 ≤ y are the coordinates of the square where the oil spill starts. 0 ≤ t ≤ 100 is the duration you are to simulate.</p>

<p>This is followed by y lines, each consisting of 2x characters. The characters in columns 2j − 1 and 2j of line i describe the current at position (j,i). The first one (a digit between 0 and 4) is the strength, and the second one (N, S, E, or W) is the direction of the current.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then output the map after t steps of the oil spill. The map should consist of y lines of x characters each. The jth character of line i should be a dot (‘.’) if the square was not reached by the oil, and an ‘X’ if it was reached. Each data set should be followed by a blank line.</p>

