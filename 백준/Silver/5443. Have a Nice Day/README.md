# [Silver IV] Have a Nice Day - 5443 

[문제 링크](https://www.acmicpc.net/problem/5443) 

### 성능 요약

메모리: 118552 KB, 시간: 244 ms

### 분류

브루트포스 알고리즘, 구현, 파싱, 시뮬레이션, 문자열

### 문제 설명

<p>Rumour has it that the P versus N P question has been solved: the two classes are not equal. This implies that many well-known problems, such as the Traveling Salesman Problem, will remain difficult forever. It can be considered a waste of time to search for polynomial time solutions: essentially only brute-force approaches can solve them. Nothing you can do about that.</p>

<p>In view of the international crisis, the new Dutch government has therefore announced that on certain days it is not allowed to work on these hard problems anymore. Instead, one must concentrate on easier issues. These days are called nice. Of course, the algorithm to decide whether a given date is nice or not should itself be easy. So far politicians could not find such an algorithm. Can you?</p>

<p>A date day month year is written down using the digits 0,. . . ,9. A date is called nice if the digits occurring in it occur an equal number of times, and if it can be split. A date can be split if its four number set can be divided into two disjoint subsets with equal sum; the four numbers are the day, the month, the left part of the year (the number represented by its first and second digit; for 1957 this is 19) and the right part of the year (the number represented by its third and fourth digit; for 2000 this is 0). For example, 16 5 4928 is nice, because all digits occur exactly once and 16 + 5 + 28 = 49.</p>

### 입력 

 <p>The first line of the input contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line with three integers D, M and Y separated by single spaces, satisfying 1 ≤ D ≤ 31, 1 ≤ M ≤ 12 and 1000 ≤ Y ≤ 9999: the day, month and year of a valid date, respectively. There are no leading zeros; e.g., June is represented as 6 and not as 06.</li>
</ul>

### 출력 

 <p>For every test case in the input, the output should contain the string "yes" or "no": the fact whether the date is nice or not.</p>

