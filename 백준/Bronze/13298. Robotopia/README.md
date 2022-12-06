# [Bronze I] Robotopia - 13298 

[문제 링크](https://www.acmicpc.net/problem/13298) 

### 성능 요약

메모리: 29284 KB, 시간: 600 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>In the wonderful land of Robotopia, life is better than ever. This is thanks to all the robots, who work hard together. Different types of robots come in different forms, that is, different numbers of arms and different numbers of legs. By day, when they are working, robots are grouped so they can be assigned to different tasks. But by night, it is your job to count how many robots there are of each type within each group. Robots are naughty and energetic; they don’t like to stand still and it is difficult to count them. After many exhausting attempts, you are finally able to count how many arms and how many legs there are in total.</p>

<p>We know each group consists of exactly two different types of robots, with at least one of each type in each group. We also know the number of arms and legs that each type of robot has. Can you find out how many robots of each type there are within each group?</p>

### 입력 

 <p>The first line contains an integer n (1 ≤ n ≤ 100). The following n lines each contain one test case. Each has six integers: l<sub>1</sub> a<sub>1</sub> l<sub>2</sub> a<sub>2</sub> l<sub>t</sub> a<sub>t</sub>, where l<sub>1</sub> and a<sub>1</sub> are the number of legs and arms (respectively) for the first type of robot, l<sub>2</sub> and a<sub>2</sub> are those for the second type, and l<sub>t</sub> and a<sub>t</sub> are the total number of observed legs and arms. All values are in the range [1, 10 000].</p>

### 출력 

 <p>For each test case output two positive integers denoting the number of each of the two types of robots. Give first the count for the first type listed. If the test case has no solution or multiple solutions, output “?” (a question mark).</p>

