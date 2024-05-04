# [Silver III] Rangers in the Bus - 16245 

[문제 링크](https://www.acmicpc.net/problem/16245) 

### 성능 요약

메모리: 160188 KB, 시간: 348 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 시뮬레이션, 트리를 사용한 집합과 맵

### 제출 일자

2024년 5월 4일 16:11:32

### 문제 설명

<p>Space Rangers are going to a secret meeting by a bus.</p>

<p>The Main Villain is watching the bus that he thinks the rangers are using. The bus has n rows of seats, each row has two seats: one to the left of the passage, one to the right. Rows are numbered from 1 to n, starting from the front of the bus. There were k passengers that entered the bus at the first stop, the villain knows the order they entered, and who took which seat. Initially all seats were free.</p>

<p>He knows the way rangers choose the seat when they enter the bus:</p>

<ul>
	<li>Red Ranger likes front seats. When he enters the bus he always chooses the free seat in the minimal row. If both seats are free, he chooses the left one.</li>
	<li>Blue Ranger also likes front seats. But unlike the Red Ranger, he chooses the right seat if both seats in the minimal possible row are free.</li>
	<li>Black Ranger likes back seats. He always chooses the free seat in the maximal row. If both seats in that row are free, he chooses the left one.</li>
	<li>Yellow Ranger also likes back seats, but chooses the right one if possible.</li>
	<li>Pink Ranger has no preferences and just chooses any seat.</li>
</ul>

<p>For each ranger the villain wants to know who of the k passengers could be that ranger. Note that some rangers could take another bus.</p>

### 입력 

 <p>The first line of input contains two integers: n and k — the number of rows and the number of passangers (1 ≤ n ≤ 10<sup>9</sup>, 1 ≤ k ≤ min(2·10<sup>5</sup>, 2n)).</p>

<p>The following k lines describe passengers in order they entered the bus.</p>

<p>The i-th of these lines contains integers x<sub>i</sub> and y<sub>i</sub> — the row that the i-th passenger chose and the seat in that row (1 ≤ x<sub>i</sub> ≤ n, 1 ≤ y<sub>i</sub> ≤ 2), xi is the row number, y<sub>i</sub> = 1 means that the passenger took the left seat, y<sub>i</sub> = 2 — the right seat.</p>

<p>Seats for different passengers are distinct.</p>

### 출력 

 <p>The first line must contain s<sub>1</sub> — the number of passengers that could be Red Ranger, followed by a space and s<sub>1</sub> space separated integers, the numbers of there passengers in order they entered the bus (the passengers are numbered from 1 to k in order they entered the bus).</p>

<p>The following four lines must contain the same information about Blue Ranger, Black Ranger, Yellow Ranger, and Pink Ranger, correspondingly.</p>

