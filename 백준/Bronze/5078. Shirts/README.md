# [Bronze I] Shirts - 5078 

[문제 링크](https://www.acmicpc.net/problem/5078) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>Jane and Tim are getting married. They are so compatible because they keep their shirts in their wardrobes in the same colour and size order. Jane has bought her own house so Tim will be moving in after they are married. His shirts will need to be merged in with hers, sorted by size then colour.</p>

<p>If you do a good job, they will make your solution available to other newly weds that are known to have similar habits, so you will be given more than one set of data to test.</p>

### 입력 

 <p>Input consists of a number of scenarios. A scenario begins with a single number, W (0 < W <= 30) on a line of its own being the number of shirts belonging to the wife. If this number is 0, then it signals the end of input.</p>

<p>The number is followed by W lines, each line being two upper case letters. The letters represent the size and colour of a shirt. Sizes are S, M and L. Colours are B for Blue, K for blacK, N for browN, O for Orange, P for Purple, R for Red and W for White.</p>

<p>The next line is another single number, H (0 < H <= 30) on a line of its own being the number of shirts belonging to the husband.</p>

<p>The number is followed by H lines to represent the husband's shirts using the same two letter codes as for the wife.</p>

### 출력 

 <p>Output consists of a single line for each scenario. The line contains all of the shirts from the input, separated by single spaces. The shirts are sorted firstly by size (small before medium before large) then by colour (alphabetical order of the representative letter).</p>

