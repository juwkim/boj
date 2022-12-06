# [Silver V] Hay Points - 4351 

[문제 링크](https://www.acmicpc.net/problem/4351) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string)

### 문제 설명

<p>Each employee of a bureaucracy has a job description - a few paragraphs that describe the responsibilities of the job. The employee's job description, combined with other factors, such as seniority, is used to determine his or her salary.</p>

<p>The Hay Point system frees the Human Resources department from having to make an intelligent judgement as to the value of the employee; the job description is merely scanned for words and phrases that indicate responsibility. In particular, job descriptions that indicate control over a large budget or management over a large number of people yield high Hay Point scores.</p>

<p>You are to implement a simplified Hay Point system. You will be given a Hay Point dictionary and a number of job descriptions. For each job description you are to compute the salary associated with the job, according to the system.</p>

### 입력 

 <p>The first line of input contains 2 positive integers: m <= 1000, the number of words in the Hay Point dictionary, and n <= 100, the number of job descriptions. m lines follow; each contains a word (a string of up to 16 lower-case letters) and a dollar value (a real number between 0 and 1,000,000). Following the dictionary are the n job descriptions. Each job description consists of one or more lines of text; for your convenience the text has been converted to lower case and has no characters other than letters, numbers, and spaces. Each job description is terminated by a line containing a period.</p>

### 출력 

 <p>For each job description, output the corresponding salary computed as the sum of the Hay Point values for all words that appear in the description. Words that do not appear in the dictionary have a value of 0.</p>

