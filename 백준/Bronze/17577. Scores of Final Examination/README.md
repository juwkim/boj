# [Bronze II] Scores of Final Examination - 17577 

[문제 링크](https://www.acmicpc.net/problem/17577) 

### 성능 요약

메모리: 30308 KB, 시간: 144 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>I am a junior high school teacher. The final examination has just finished, and I have all the students' scores of all the subjects. I want to know the highest total score among the students, but it is not an easy task as the student scores are listed separately for each subject. I would like to ask you, an excellent programmer, to help me by writing a program that finds the total score of a student with the highest total score.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>
<!-- end en only -->

<pre><i>n m</i>
<i>p</i><sub>1,1</sub> <i>p</i><sub>1,2</sub> … <i>p</i><sub>1,<i>n</i></sub>
<i>p</i><sub>2,1</sub> <i>p</i><sub>2,2</sub> … <i>p</i><sub>2,<i>n</i></sub>
…
<i>p</i><sub><i>m</i>,1</sub> <i>p</i><sub><i>m</i>,2</sub> … <i>p</i><sub><i>m,n</i></sub></pre>

<p>The first line of a dataset has two integers <i>n</i> and <i>m</i>. <i>n</i> is the number of students (1 ≤ <i>n</i> ≤ 1000). <i>m</i> is the number of subjects (1 ≤ <i>m</i> ≤ 50). Each of the following <i>m</i> lines gives <i>n</i> students' scores of a subject. <i>p</i><sub><i>j,k</i></sub> is an integer representing the <i>k</i>-th student's score of the subject <i>j</i> (1 ≤ <i>j</i> ≤ <i>m</i> and 1 ≤ <i>k</i> ≤ <i>n</i>). It satisfies 0 ≤ <i>p</i><sub><i>j,k</i></sub> ≤ 1000.</p>

<p>The end of the input is indicated by a line containing two zeros. The number of datasets does not exceed 100.</p>

### 출력 

 <p>For each dataset, output the total score of a student with the highest total score. The total score <i>s</i><sub><i>k</i></sub> of the student <i>k</i> is defined by <i>s</i><sub><i>k</i></sub> = <i>p</i><sub>1,<i>k</i></sub> + … + <i>p</i><sub><i>m,k</i></sub>.</p>

