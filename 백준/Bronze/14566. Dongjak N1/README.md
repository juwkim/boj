# [Bronze I] Dongjak N1 - 14566 

[문제 링크](https://www.acmicpc.net/problem/14566) 

### 성능 요약

메모리: 114328 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 정렬(sorting)

### 문제 설명

<p>You are the president of the company that runs the Chung Ang University shuttle bus. Students were able to use the bus to easily move the classroom. One day, the school expanded the campus by purchasing all the buildings in Heukseok - dong with your tuition. Because of this, you, the president of the shuttle bus operating company, must create a new line of buses to operate within the newly expanded campus.</p>

<p>Coincidentally, because of the president who wants to be tidy, the road that the newly built in campus are just two-line straight roads. There are no other roads. There are n stops on the campus roads.</p>

<p>For bus route development, you have numbered each of the n stops with an integer of A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>, ..., A<sub>n-1</sub>, A<sub>n</sub>.</p>

<p>To move from one stop to another stop, you must go to the bus by all means. You want to design the bus route with less cost. However, if you do not leave a reasonable number of stops, students will be dissatisfied in your design. In this case, they will blame you, and you will be fired :). So, you decided to find the nearest stop among the n stops and merge them into one.</p>

<p>You majored in computer science and have decided to use n integers to number the bus stops. We decided to solve this problem by creating a program that finds the distance between two stops closest to the distance and calculates the number of pairs of two stops with this distance.</p>

### 입력 

 <p>In the first line, the number of stops (2 ≤ n ≤ 5000) is given.</p>

<p>In the second line, the coordinates A<sub>1</sub>, ..., A<sub>n</sub> (0 ≤ A<sub>i</sub> ≤ 32,800,000) of each stop are given. There is no duplicate of each number.</p>

### 출력 

 <p>Two integers are output, the first integer is the minimum distance and the second integer is the number of pairs of two stops with this distance.</p>

