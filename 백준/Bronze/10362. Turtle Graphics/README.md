# [Bronze I] Turtle Graphics - 10362 

[문제 링크](https://www.acmicpc.net/problem/10362) 

### 성능 요약

메모리: 28776 KB, 시간: 84 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966. It involved the Turtle, originally a robotic creature that moved around on the floor. It can be directed by typing commands into the computer. The command ‘F’ (forward) causes the turtle to move forward one step, ‘R’ (right) rotates the turtle 90 degrees clockwise while leaving it in the same place on the floor, and ‘L’ (left) rotates the turtle 90 degree anticlockwise and leaving it in the same location.</p>

<p>When the turtle moves forward it will leave a trail. We will represent the trail with character 'x'.</p>

<p>For example, the command </p>

<p>FFFRFFFFLFFFRFFFFF</p>

<p>will create the pattern below</p>

<pre>y 0...............................
  9...............................
  8.........xxxxxx...............
  7.........x.....................
  6.........x.....................
  5.....xxxxx.....................
  4.....x.........................
  3.....x.........................
  2.....o.........................
  1...............................
  0...............................
   0123456789012345678901234567890 x
</pre>

<p>with assumption that the initial direction of the turtle is facing to the North (the y-axis) and the initial location of the turtle is marked as 'o'. The maximum size of the drawing area is 64x64 with the origin coordinate (0, 0) at the lower left corner. You may safely assume that the path of the turtle never exceed the drawing area.</p>

### 입력 

 <p>First line of the input contains T the number of test cases (1 ≤ T ≤ 50). Each test case consists of two lines. The first line of each test case contains a pair of integer, x and y (0 ≤ x, y < 64) which represents the starting point of the path. The second line contains a string with no more than 128 characters. Each character of the string is either ‘F’, ‘R’ or ‘L’ which represents a computer command for the turtle in order.</p>

### 출력 

 <p>For each case, output in a line "Case #X: x y n" (without quotes) where X is the case number starting from 1. x and y represents the final location of the turtle and n is the number of locations in which the turtle visits more than once.</p>

