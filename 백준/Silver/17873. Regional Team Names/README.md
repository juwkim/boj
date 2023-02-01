# [Silver V] Regional Team Names - 17873 

[문제 링크](https://www.acmicpc.net/problem/17873) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

문자열(string)

### 문제 설명

<p>A certain ICPC regional contest has specific requirements for the names of the competing teams. One of the reasons this is done is so spectators can determine which school each team is from. The requirements for a team name are specified on the website for the region as shown here:</p>

<ul>
	<li>Each team name must consist of the institution name (greater than 1 character but less than or equal to 8 characters) followed by a hyphen (-) followed by a team name (greater than 0 characters but less than or equal to 24 characters). Please note that spaces are counted as characters.</li>
	<li>Format: INSTITUTION-TEAMNAME INSTITUTION = University name or abbreviation. 1 < length(INSTITUTION ) <= 8. TEAMNAME = Your team name. 1 <= length(TEAMNAME) <= 24.</li>
</ul>

<p>Write a program that determines if a supplied string is a valid team name for this region.</p>

### 입력 

 <p>The input consists of a single line containing a string of characters at least one character long and no more than 80 characters long. The input string will not have any leading or trailing spaces. The INSTITUTION may not contain hyphens (obviously). The TEAMNAME, however, may contain hyphens.</p>

### 출력 

 <p>The single output line consists of the word YES if the string represents a valid team name for the region or NO if the string does not represent a valid team name for the region.</p>

