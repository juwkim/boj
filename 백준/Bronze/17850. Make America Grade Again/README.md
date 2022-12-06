# [Bronze II] Make America Grade Again - 17850 

[문제 링크](https://www.acmicpc.net/problem/17850) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>The University of America is having an integrity issue. It turns out that grades in many of the science classes are not being based on any graded work but on such things as attendance, grooming habits and any snacks the students bring with them. The administration has decided to crack down on this. First, they confiscated all of the snacks. Then they insisted that all grades in science classes must be on graded work in four categories: labs, homeworks, projects and exams. They don’t care what percentage of the final grade is assigned to each of these as long as the total percentage assigned is 100%.</p>

<p>The professors at UA have grudgingly agreed to start grading their assignments, but they balk at the task of having to calculate final grades as well. They are asking you to write a program to calculate a student’s final grade. They will provide you with the following information: first, the percentage of each of the four categories; second, a list of (grudgingly) graded assignments each of which fits into one of the categories. Using this, they want you to calculate a final integer percentage grade.</p>

<p>For example, suppose the assigned percentages are labs - 20, homeworks - 20, projects - 25 and exams - 35 and the list of graded assignments is the following:</p>

<ul>
	<li>Lab 1: 15/20</li>
	<li>Hw 1: 65/70</li>
	<li>Hw 2: 27/35</li>
	<li>Exam 1: 88/100</li>
	<li>Proj 1: 50/50</li>
	<li>Hw 3: 61/65</li>
	<li>Exam 2: 79/100</li>
	<li>Lab 2: 17/20</li>
	<li>Hw 4: 51/60</li>
	<li>Exam 3: 141/150</li>
</ul>

<p>To calculate the final grade you first total up the fraction of points achieved in each category. For labs it’s 32/40 (there were two assignments each worth 20 and the student got a 15 on the first and a 17 on the second for a total of 32 points); for homeworks it’s 204/230; for projects it’s 50/50 and for exams it’s 308/350. You then multiply each of these fractions by the percentage assigned to each category: 20(32/40) + 20(204/230) + 25(50/50) + 35(308/350) = 89.539. Finally you truncate this to get the final grade of 89. Then you sit back and eat all the snacks you no longer need to bring to class.</p>

### 입력 

 <p>Input starts with five positive integers l h p e n, where the first four values are the percentages for labs, homeworks, projects and exams, respectively (always totaling to 100), and n (4 ≤ n ≤ 200) is the number of graded assignments. Following this are n lines each of the form cat i: r/s, where cat is either <code>Lab</code>, <code>Hw</code>, <code>Proj</code> or <code>Exam</code>, i is a positive integer, r is the number of points achieved for an assignment and s is the total possible points for the assignment. In each of these lines s is positive and 0 ≤ r ≤ s ≤ 1 000. There will always be at least one assignment in each of the four categories.</p>

### 출력 

 <p>Output the final truncated percentage grade.</p>

