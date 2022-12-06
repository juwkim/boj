# [Bronze I] Postman Joe - 5105 

[문제 링크](https://www.acmicpc.net/problem/5105) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Postman Joe is a fitness fanatic. He has a single row of 20 houses on his delivery route, and sets himself a task every day that will require him to walk up and down the row several times. A typical task will look something like this:</p>

<p>3 U3 D2 U1 U6 D4 D5 U7 U9 D5 D3 U5 U4 D2 D5 U8</p>

<p>This means that Joe delivers firstly to house 3, moves 3 houses up the street and delivers to house 6, then moves 2 houses down the street and delivers to house 4, and so on. The houses are numbered sequentially from 1 to 20, house 1 being at the bottom of the street.</p>

<p>Not every house will necessarily receive a delivery each day, but Joe's instructions must never take him to the same house twice, nor take him beyond either end of the row of houses.</p>

<p>To solve this problem, you must write a program to help Joe. It must check that Joe has set himself a legal task and, if so, must report those houses which do not receive a delivery.</p>

### 입력 

 <p>Input will consist of a number of tasks that Joe has set, each on a single line. The last line will contain just a # character – that line should not be processed.</p>

<p>Each task represents the deliveries for a single day. Each line starts with a single integer S (1 <=S <= 20) being the first house to which Joe makes a delivery. This is followed by a sequence of letter-number pairs, each separated by a single space. The letter will be U or D, U meaning go up the street (increasing house number), D go down the street. The number will be a single digit integer, stating the number of houses to move.</p>

### 출력 

 <p>Output will consist of 1 line for each line of input. If the instructions for the task are legal (ie no house is visited twice, and Joe is not taken beyond either end of the street), output will be a list of houses that do not receive a delivery that day. The list will be in numerical order with a space between each house number. If all houses receive a delivery, output should be the word none.</p>

<p>If the instructions for a task are not legal, output should be the word illegal.</p>

