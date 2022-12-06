# [Bronze II] Analysis of Advanced Analytics - 15155 

[문제 링크](https://www.acmicpc.net/problem/15155) 

### 성능 요약

메모리: 29200 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>James is purchasing lecture notebooks for his upcoming course: Analysis of Advanced Analytics. James knows exactly how many pages are needed for each day during the semester. On the first day, he starts writing his notes at the beginning of the first notebook. On the second day, he checks if there are enough pages left in the first notebook to write all of the notes for the second day. If there are enough pages left, he will write the notes in the first notebook. If there are not enough pages left, he will start a new notebook and write all of his notes for that lecture in the new notebook. He continues this process, checking every day if there is enough room left in the current notebook to write the notes for that day. If there is enough room, he will continue writing in that notebook and if there is not enough room, he will start a new notebook.</p>

<p>Each notebook contains the same number of pages. Given the lengths of the notes for each day during the entire semester, how many notebooks should James buy to contain all of the notes for the semester?</p>

### 입력 

 <p>The input consists of two lines. The first line contains two integers n (1 ≤ n ≤ 1 000), which is the number of days in the semester, and k (1 ≤ k ≤ 1 000), which is the number of pages in each notebook.</p>

<p>The second line contains n integers a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>n</sub> (1 ≤ a<sub>i</sub> ≤ k), where a<sub>i</sub> is the number of pages needed for the i th day in the semester.</p>

### 출력 

 <p>Display the number of notebooks that James needs for the entire semester.</p>

