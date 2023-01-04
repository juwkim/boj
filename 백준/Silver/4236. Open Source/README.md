# [Silver IV] Open Source - 4236 

[문제 링크](https://www.acmicpc.net/problem/4236) 

### 성능 요약

메모리: 118652 KB, 시간: 188 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 정렬(sorting)

### 문제 설명

<p>At an open-source fair held at a major university, leaders of open-source projects put sign-up sheets on the wall, with the project name at the top in capital letters for identification.</p>

<p>Students then signed up for projects using their userids. A userid is a string of lower-case letters and numbers starting with a letter.</p>

<p>The organizer then took all the sheets off the wall and typed in the information.</p>

<p>Your job is to summarize the number of students who have signed up for each project. Some students were overly enthusiastic and put their name down several times for the same project. That's okay, but they should only count once. Students were asked to commit to a single project, so any student who has signed up for more than one project should not count for any project.</p>

<p>There are at most 10,000 students at the university, and at most 100 projects were advertised.</p>

### 입력 

 <p>The input contains several test cases, each one ending with a line that starts with the digit 1. The last test case is followed by a line starting with the digit 0.</p>

<p>Each test case consists of one or more project sheets. A project sheet consists of a line containing the project name in capital letters, followed by the userids of students, one per line.</p>

### 출력 

 <p>For each test case, output a summary of each project sheet. The summary is one line with the name of the project followed by the number of students who signed up. These lines should be printed in decreasing order of number of signups. If two or more projects have the same number of signups, they should be listed in alphabetical order.</p>

