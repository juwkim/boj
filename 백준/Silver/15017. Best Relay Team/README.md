# [Silver IV] Best Relay Team - 15017 

[문제 링크](https://www.acmicpc.net/problem/15017) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>You are the coach of the national athletics team and need to select which sprinters should represent your country in the 4 × 100 m relay in the upcoming championships.</p>

<p>As the name of the event implies, such a sprint relay consist of 4 legs, 100 meters each. One would think that the best team would simply consist of the 4 fastest 100 m runners in the nation, but there is an important detail to take into account: flying start. In the 2nd, 3rd and 4th leg, the runner is already running when the baton is handed over. This means that some runners – those that have a slow acceleration phase – can perform relatively better in a relay if they are on the 2nd, 3rd or 4th leg.</p>

<p>You have a pool of runners to choose from. Given how fast each runner in the pool is, decide which four runners should represent your national team and which leg they should run. You are given two times for each runner – the time the runner would run the 1st leg, and the time the runner would run any of the other legs. A runner in a team can only run one leg.</p>

### 입력 

 <p>The first line of input contains an integer n, the number of runners to choose from (4 ≤ n ≤ 500). Then follow n lines describing the runners. The i’th of these lines contains the name of the i’th runner, the time a<sub>i</sub> for the runner to run the 1st leg, and the time b<sub>i</sub> for the runner to run any of the other legs (8 ≤ b<sub>i</sub> ≤ a<sub>i</sub> < 20). The names consist of between 2 and 20 (inclusive) uppercase letters ‘A’-‘Z’, and no two runners have the same name. The times are given in seconds with exactly two digits after the decimal point.</p>

### 출력 

 <p>First, output a line containing the time of the best team. The precise formatting of the time is not important. Then output four lines containing the names of the runners in that team. The first of these lines should contain the runner you have picked for the 1st leg, the second line the runner you have picked for the 2nd leg, and so on. Any solution that results in the fastest team is acceptable.</p>

