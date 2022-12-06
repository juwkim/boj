# [Bronze II] Lamp - 9897 

[문제 링크](https://www.acmicpc.net/problem/9897) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>A building has a long corridor and <i>L</i> ceiling lamps labeled 1, 2, 3, ..., <i>L</i>. Each lamp has an individual switch that can turn the lamp on or off. The building manager hires <i>G</i> security guards (no two guards have the same name), whose job at night is to patrol the corridor and turn the lamps on and off. Each guard is assigned a subset of lamps. During one patrol round, a guard will walk along the corridor, and toggle the lamps assigned to him/her (that is, if a lamp is on, switch it off; if the lamp is off, switch it on). After a guard toggles each lamp assigned to him/her exactly once, the guard will take a break until his/her next patrol round. A guard may have more than one patrol round in one night. The order of patrol for the guards is dictated by a duty roster.</p>

<p>All lamps are off before the guards begin their patrol rounds, and there is only one guard on patrol at any time.</p>

<p>The assignment of lamps to a guard is specified by two positive integers, <i>a</i><sub>0</sub> and <i>d</i>. The subset of lamps the guard will toggle is</p>

<p style="text-align: center;">{<i>a</i><sub>0</sub>, <i>a</i><sub>0</sub> + <i>d</i>, <i>a</i><sub>0</sub> + 2<i>d</i>, ..., <i>a</i><sub>0</sub> + <i>kd</i>}</p>

<p>where <i>k</i> is the largest integer such that <i>a</i><sub>0</sub> + <i>kd</i> ≤ <i>L</i>.</p>

<p>Given the lamp assignment for each guard and the duty roster, find out how many lamps are on after all the guards have finished all of their patrol rounds.</p>

<p>Suppose we have 10 lamps, two security guards (Edi and Lou), and three patrol rounds. Edi's lamp assignment is (<i>a</i><sub>0</sub>, <i>d</i>) = (1, 4) and Lou's lamp assignment is (<i>a</i><sub>0</sub>, <i>d</i>) = (2, 3). The order of patrol is Edi, Lou, Edi.</p>

<p>After the first patrol round by Edi, lamps 1, 5, and 9 will be on. During the second patrol round, Lou toggles lamps 2, 5, and 8. Therefore, after the second patrol round, lamps 1, 2, 8, and 9 are on but lamp 5 has been turned off. On the third patrol round, Edi patrols again, and toggles lamps 1, 5, and 9. Consequently, after all the patrol rounds specified in the duty roster, the lamps that are on are 2, 5, and 8.</p>

<p>The number of lamps that are still on after the guards finish their patrol rounds is therefore 3.</p>

### 입력 

 <p>The first line in input consists of three positive integers, separated with a blank character. The first number <i>L</i> ≤ 1000 is the number of lamps. The second number <i>G</i> ≤ 10 is the number of security guards, and the third number <i>R</i> ≤ 50 is the total number of patrol rounds. The next <i>G</i> lines contain the names and lamp assignments of the guards. Each of these <i>G</i> lines consists of the name (exactly 3 English letters), <i>a</i><sub>0</sub> and <i>d</i>, (<i>a</i><sub>0</sub> ≤ <i>N</i>) separated with a blank character. The subsequent <i>R</i> lines specify the duty roster. Each line contains the name of a guard (guaranteed to have lamp assignment). The order of the guards appearing in the duty roster dictates the order of their patrol.</p>

### 출력 

 <p>The output contains one integer which is the number of lamps that are on after all guards finish all of their patrol rounds.</p>

