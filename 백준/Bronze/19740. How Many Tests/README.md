# [Bronze I] How Many Tests - 19740 

[문제 링크](https://www.acmicpc.net/problem/19740) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

파싱(parsing), 문자열(string)

### 문제 설명

<p>When judges prepare tests for the programming contest problem, they number tests from $1$ to $n$.</p>

<p>It is convenient if the files with tests are shown in their correct order, from $1$ to $n$. But file managers sort files by their names as strings, so if the name of the test file is equal to its number, the file order is not correct, for example <<<code>10</code>>> goes before <<<code>2</code>>>.  </p>

<p>To avoid such problem, file names are prepended with leading zeroes. Judges use minimal possible number of leading zeroes to make names of all files have the same length. For example, if the problem has $10$ tests, the names of the files with tests are <<<code>01</code>>>, <<<code>02</code>>>, <<<code>03</code>>>, <<<code>04</code>>>, <<<code>05</code>>>, <<<code>06</code>>>, <<<code>07</code>>>, <<<code>08</code>>>, <<<code>09</code>>> and <<<code>10</code>>>.</p>

<p>Andrew is an experienced judge, so he always uses the described way to name the files with tests. Recently he has found some files with tests of some ancient problem at his old hard drive. Unfortunately, the drive is damaged, so some tests are missing. Help Andrew to find out how many tests could be there in the problem. He wants to know the minimal and the maximal possible number of tests.</p>

### 입력 

 <p>The first line of input contains an integer $k$  --- the number of files ($1 \le k \le 1000$). The following $k$ lines contain file names. All these lines are non-empty, have equal length that doesn't exceed $9$. File names are distinct, they only contain digits. No file name contains only zeroes.</p>

### 출력 

 <p>Output two integers: the minimal and the maximal number of tests that the problem could have.</p>

