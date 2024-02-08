# [Silver III] Exam Redistribution - 13932 

[문제 링크](https://www.acmicpc.net/problem/13932) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 2월 9일 02:27:02

### 문제 설명

<p>Linda is giving an exam. When the exam is over, Linda will redistribute the exams among the students for a peer review, so they may grade each other’s answers and assign preliminary scores.</p>

<p>The students are split up in several rooms of varying sizes. Linda has devised the following scheme for redistributing the exams:</p>

<ol>
	<li>Linda visits the first room, picks up all exams written there, and places them in a pile.</li>
	<li>In each subsequent room Linda takes exams from the top of her pile and randomly distributes them to the students in the room. She then picks up all exams written in that room and adds them to the bottom of her pile.</li>
	<li>After having visited each room exactly once, Linda returns to the first room, and distributes the remaining exams from her pile there.</li>
</ol>

<p>Naturally, it is imperative that no student receives their own exam to review, and that Linda does not run out of exams in her pile while doing the redistribution (i.e., that when entering a room after the first one, Linda’s pile contains at least as many exams as there are students in the room). Whether or not this is the case depends on the order in which the rooms are visited. We say that an ordering of the rooms is safe if Linda will not run out of exams in her pile when visiting rooms in that order, and that there is no chance that any student receives their own exam to review.</p>

<p>Can you find a safe order in which to visit the rooms (or determine that no safe order exists)?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line containing an integer n (2 ≤ n ≤ 30), the number of rooms.</li>
	<li>one line containing n integers s<sub>1</sub>, . . . , s<sub>n</sub> (1 ≤ s<sub>i</sub> ≤ 100 for each i), where si is the number of students in room i.</li>
</ul>

### 출력 

 <p>If it is impossible to redistribute the exams safely, output “impossible”. Otherwise, output a safe order in which to visit the rooms. If there are multiple safe orders, you may give any of them.</p>

