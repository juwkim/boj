# [Bronze II] Hanging Out on the Terrace - 17930 

[문제 링크](https://www.acmicpc.net/problem/17930) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>The HiQ office in Stockholm has a pretty awesome rooftop terrace, often used in company parties and events such as programming competitions.</p>

<p>Unfortunately, fire safety rules limit the number of people who can be on the terrace at any one point in time -- at most $L$ people. During a party, people come and go to the terrace, but it is pretty annoying to keep track of the number of people who are currently on the terrace. Furthermore, people often enter the terrace in groups. If a group of people wish to enter the terrace, but their addition would exceed the fire safety limit, the group will instead go and play ping pong inside.</p>

<p>Your task is to write a program that determines, given the sizes of the groups which attempted to enter the terrace during a party and when people left the terrace, how many times a group was denied entry to the terrace.</p>

### 입력 

 <p>The first line of input contains the fire safety limit $1 \le L \le 200$ and the number of events $0 \le x \le 100$.</p>

<p>The next $x$ lines contains the events. An event starts with one of the words "enter" or "leave", depending on whether the event describes a group attempting to enter the terrace or some set of people leaving it.<br>
This is followed by an integer $1 \le p \le 200$ -- the number of people entering/leaving at this time.</p>

<p>The number of people who leave the terrace will never exceed the number of people currently on the terrace.</p>

### 출력 

 <p>Output the number of groups who were not allowed to enter the terrace during the party.</p>

