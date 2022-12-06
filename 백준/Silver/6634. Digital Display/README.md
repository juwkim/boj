# [Silver IV] Digital Display - 6634 

[문제 링크](https://www.acmicpc.net/problem/6634) 

### 성능 요약

메모리: 115388 KB, 시간: 256 ms

### 분류

구현(implementation), 런타임 전의 전처리(precomputation)

### 문제 설명

<p>There is a suspicion that some officers cheat when reporting exact time of various events. They antedate important documents and gain enormous profit by that. To eliminate such practices, ACM decided to install big digital clock on the wall of each office. Thank to this, everyone can easily see the current time and verify that it is correctly recorded on documents.</p>

<p>Your task is to write a firmware for this digital clock. Digits will be shown using the classical seven-segment display.</p>

### 입력 

 <p>On each line of the input, there are exactly five characters: two digits, a colon (“:”) and another two digits. These characters specify a time between 00:00 and 23:59, inclusive.</p>

<p>The last time is followed by a line containing the word “end”.</p>

### 출력 

 <p>For each input line, print a display consisting of seven rows of exactly 29 characters each. The only characters allowed are dashes (“-”) for horizontal segments, pipes (“|”) for vertical segments, plus signs (“+”) for corners, small latin letter “o” for the colon between hours and minutes, and spaces (“ ”).</p>

<p>The area for each digit is exactly 5 characters wide and there are two empty columns (spaces) between neighboring digit areas or between a digit area and the colon. Exact digit shapes and placements can be seen in Sample Output. </p>

<p>Always print two empty lines after each time displayed. Also, print the word “end” at the end of the output.</p>

<p>Notice In this problem, the meaning of evaluation system responses is a little bit different than usual. If you get a Presentation Error, it most probably means that you did not follow the output format exactly. Note that it does not necessarily imply that your answer is close to the correct one. On the other hand, a Wrong Answer will be issued if the format seems basically all-right but the contents of the display are not correct. If your output contains both errors, the decision between Wrong Answer and Presentation Error is solely at the discretion of the system. Therefore, you should never try to derive any important conclusions from the response.</p>

