# [Bronze III] Microwave Mishap - 25830 

[문제 링크](https://www.acmicpc.net/problem/25830) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Donald is very hungry. He grabs a TV dinner, puts it in the microwave, and enters 02:15 to cook it for 2 minutes and 15 seconds. Unknown to Donald, microwave takes these values as hours and minutes, i.e., microwave takes 02:15 as 2 hours and 15 minutes (not 2 minutes and 15 seconds). We need to tell Donald how much extra (i.e., the additional time) his food will be cooking. That is, we need to tell Donald that his food will cook 2 hours, 12 minutes, and 45 seconds more (longer) than what he was expecting!</p>

<p>Given the initial time in the form of MM:SS, where the input is actually taken as HH:MM, determine how much extra the food will be in the microwave. Provide this info in the form of HH:MM:SS.</p>

### 입력 

 <p>Input will consist of a single line in the form of MM:SS, representing what Donald has entered. MM and SS will be in the range of 00 and 59 (inclusive), but they both will not be 00 at the same time, i.e., the total time will be positive, i.e., input will not be 00:00.</p>

### 출력 

 <p>Output should contain a single line in the form of HH:MM:SS, indicating the additional time the food will cook in the microwave. Note that you need to print two digits for each part. Also note that MM and SS must be in the range of 00 to 59.</p>

