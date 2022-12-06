# [Silver V] Pole Position - 5725 

[문제 링크](https://www.acmicpc.net/problem/5725) 

### 성능 요약

메모리: 115184 KB, 시간: 160 ms

### 분류

구현(implementation)

### 문제 설명

<p>In car races, there is always a high pole next to the finish line of the track. Before the race starts, the pole is used to display the starting grid. The number of the first car in the grid is displayed at the top of the pole, the number of the car in second place is shown below that, and so on.</p>

<p>During the race, the pole is used to display the current position of each car: the car that is winning the race has its number displayed at the top of the pole, followed by the car that is in second place, and so on.</p>

<p>Besides showing the current position of a car, the pole is also used to display the number of positions the cars have won or lost, relative to the starting grid. This is done by showing, side by side to the car number, an integer number. A positive value v beside a car number in the pole means that car has won v positions relative to the starting grid. A negative value v means that car has lost v positions relative to the starting grid. A zero beside a car number in the pole means the car has neither won nor lost any positions relative to the starting grid (the car is in the same position it started).</p>

<p style="text-align: center;"><img alt="" src="" style="height:177px; width:195px"></p>

<p>We are in the middle of the Swedish Grand Prix, the last race of the World Championship. The race director, Dr. Shoo Makra, is getting worried: there have been some complaints that the software that controls the pole position system is defective, showing information that does not reflect the true race order.</p>

<p>Dr. Shoo Makra devised a way to check whether the pole system is working properly. Given the information currently displayed in the pole, he wants to reconstruct the starting grid of the race. If it is possible to reconstruct a valid starting grid, he plans to check it against the real starting grid. On the other hand, if it is not possible to reconstruct a valid starting grid, the pole system is indeed defective.</p>

<p>Can you help Dr. Shoo Makra?</p>

### 입력 

 <p>The input contains several test cases. The first line of a test case contains one integer N indicating the number of cars in the race (2 ≤ N ≤ 10<sup>3</sup>). Each of the next N lines contains two integers C and P, separated by one space, representing respectively a car number (1 ≤ C ≤ 10<sup>4</sup>) and the number of positions that car has won or lost relative to the starting grid (−10<sup>6</sup> ≤ P ≤ 10<sup>6</sup>), according to the pole system. All cars in a race have different numbers.</p>

<p>The end of input is indicated by a line containing only one zero.</p>

<p>The input must be read from standard input.</p>

### 출력 

 <p>For each test case in the input, your program must print a single line, containing the reconstructed starting grid, with car numbers separated by single spaces. If it is not possible to reconstruct a valid starting grid, the line must contain only the value -1.</p>

<p>The output must be written to standard output.</p>

