# [Silver V] Ballot Analyzing Device - 9444 

[문제 링크](https://www.acmicpc.net/problem/9444) 

### 성능 요약

메모리: 34904 KB, 시간: 136 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Election committee of Flatland is preparing for presidential elections. To minimize human factor in ballot counting they decided to develop an automated Ballot Analyzing Device (BAD).</p>

<p>There are n candidates running for president. The ballot contains one square field for each candidate. The voter must mark exactly one of the fields. If no field is marked or there are two or more marked fields, the ballot is invalid. Each voter puts his/her ballot to a special scanner in BAD. The scanner analyzes marks on the ballot and creates a special voting string of n characters: ‘X’ for marked field and ‘.’ for unmarked one. Now voting strings must be analyzed to get the report. Your task is to develop a report generator for BAD.</p>

<p>Given voting strings for all ballots, your program must print the voting report. Candidates in the report must be arranged in order of decreasing number of votes. If two candidates have the same number of votes, they must have the same order as in a voting ballot. For each candidate calculate his/her result in percent (if the candidate received p votes, the result in percent is 100p/m). The last line of the report must indicate the percentage of the invalid ballots.</p>

### 입력 

 <p>The first line contains two integers n and m — the number of candidates and the number of ballots (2 ≤ n ≤ 10; 1 ≤ m ≤ 1000). The following n lines contain last names of candidates. Each name is a string of at most 100 English letters. There is no candidate named “Invalid”.</p>

<p>Then m lines follow, each of them contains one voting string.</p>

### 출력 

 <p>Print n+ 1 lines. First print results for candidates in percent. For each candidate print his/her last name followed by a space and then his/her result in percent and a percent sign ‘%’. The last line must specify the percentage of invalid ballots: a word “Invalid” followed by a space, the percentage of invalid ballots and a percent sign.</p>

<p>Round all numbers to exactly two digits after the decimal point. If the number is exactly in the middle of two representable numbers, output the greater one (e.g. output “12.35” for 12.345).</p>

