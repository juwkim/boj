# [Bronze I] Important Test - 13040 

[문제 링크](https://www.acmicpc.net/problem/13040) 

### 성능 요약

메모리: 30840 KB, 시간: 168 ms

### 분류

Empty

### 문제 설명

<p>Nick is going to take an important test soon, so he has decided to prepare. Test has n possible variants, the i-th of them has m<sub>i</sub> tasks numbered from 1 to m<sub>i</sub>. For each task of each variant Nick has estimated the time t<sub>ij</sub> minutes that it would take him to solve it and write down.</p>

<p>The tasks in the test must be solved in order they appear in the test, one after another. The test must be submitted until deadline of t minutes. Nick thinks he could secretly copy some solutions from his notes, but he doesn't want to risk much. So he would copy at most one solution. Copying of any solution would take t<sub>0</sub> minutes.</p>

<p>Now Nick would like to find out for each variant what is the maximal number of tasks he could write down if he gets this variant.</p>

### 입력 

 <p>The first line of input contains three integers: n, t and t<sub>0</sub> (1 ≤ n ≤ 100, 1 ≤ t ≤ 10 000, 1 ≤ t<sub>0</sub> ≤ 100) — the number of variants, the length of the test, and the time needed to secretly copy the solution from the notes.</p>

<p>The following n lines describe variants. The first integer m<sub>i</sub> (1 ≤ m<sub>i</sub> ≤ 100) is the number of tasks in the i-th variant. It is followed by mi integers t<sub>ij</sub> (1 ≤ t<sub>ij</sub> ≤ 100) — time needed for tasks.</p>

### 출력 

 <p>For each variant print one integer: the number of tasks Nick can write down if he gets this variant.</p>

<p> </p>

