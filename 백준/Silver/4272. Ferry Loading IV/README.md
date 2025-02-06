# [Silver II] Ferry Loading IV - 4272 

[문제 링크](https://www.acmicpc.net/problem/4272) 

### 성능 요약

메모리: 112008 KB, 시간: 128 ms

### 분류

많은 조건 분기, 자료 구조, 그리디 알고리즘, 구현, 큐, 시뮬레이션, 두 포인터

### 제출 일자

2025년 2월 7일 08:45:09

### 문제 설명

<p>Before bridges were common, ferries were used to transport cars across rivers. River ferries, unlike their larger cousins, run on a guide line and are powered by the river's current. Cars drive onto the ferry from one end, the ferry crosses the river, and the cars exit from the other end of the ferry.</p>

<p>There is an l-meter-long ferry that crosses the river. A car may arrive at either river bank to be transported by the ferry to the opposite bank. The ferry travels continuously back and forth between the banks so long as it is carrying a car or there is at least one car waiting at either bank. Whenever the ferry arrives at one of the banks, it unloads its cargo and loads up cars that are waiting to cross as long as they fit on its deck. The cars are loaded in the order of their arrival; ferry's deck accommodates only one lane of cars. The ferry is initially on the left bank where it broke and it took quite some time to fix it. In the meantime, lines of cars formed on both banks that await to cross the river.</p>

### 입력 

 <p>The first line of input contains c, the number of test cases. Each test case begins with l, m. m lines follow describing the cars that arrive in this order to be transported. Each line gives the length of a car (in centimeters), and the bank at which the car arrives ("left" or "right").</p>

### 출력 

 <p>For each test case, output one line giving the number of times the ferry has to cross the river in order to serve all waiting cars.</p>

