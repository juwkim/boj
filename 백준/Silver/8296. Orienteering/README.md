# [Silver II] Orienteering - 8296 

[문제 링크](https://www.acmicpc.net/problem/8296) 

### 성능 요약

메모리: 124792 KB, 시간: 112 ms

### 분류

구현

### 제출 일자

2025년 1월 9일 19:59:07

### 문제 설명

<p>Byteman is organizing an orienteering competition. Participants will be given a map that indicates checkpoints, and they are to visit each one of them in a given order. By the traditions of Byteland, the route has to be a closed loop. An appropriate area has been found and the route planned accordingly. However, the starting point, which will be the first and the last to visit, and the race direction are yet to be chosen.</p>

<p>Byteman decided that every part of the race should not be more difficult than a previous one. He walked the entire way noting stage difficulty between every two consecutive checkpoints as positive integer numbers. The higher the number is, the more difficult the corresponding part of the route. Your task is to check whether there exist such starting point and race direction, that Byteman's constraint is satisfied.</p>

### 입력 

 <p>The first line of the standard input contains an integer <em>n</em> (2 ≤ <em>n</em> ≤ 100 000) denoting the number of all checkpoints on the route. The checkpoints are numbered from 1 to <em>n</em>. In the second line, there is a sequence of <em>n</em> integers <em>t<sub>i</sub></em> (1 ≤ <em>t<sub>i</sub></em> ≤ 1 000 000 000), in which <em>i</em>-th number describes difficulty of the stage between checkpoints <em>i</em> and <em>i</em> + 1, except for <em>t<sub>n</sub></em>, which denotes the difficulty of the stage between checkpoints <em>n</em> and 1.</p>

### 출력 

 <p>In the first line of the standard output your program should output "<code>TAK</code>" (meaning yes, without the quotes), if there is a starting point and race direction satisfying Byteman's condition, and "<code>NIE</code>" (meaning no) otherwise.</p>

