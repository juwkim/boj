# [Bronze I] Mahershalalhashbaz, Nebuchadnezzar, and Billy Bob Benjamin Go to the Regionals - 4070 

[문제 링크](https://www.acmicpc.net/problem/4070) 

### 성능 요약

메모리: 115592 KB, 시간: 140 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>The Association for Computing Machinery (ACM) is considering new rules for its regional programming contests, in part to solve some software problems. For instance, the program that prints out the badges for each team was designed so that the same font size is used to print all badges for that team. However, this means that if one member of the team has a very long name, then a very small font will be used to print all of the team’s badges, and this wouldn’t look very nice for someone with an extremely short name like “AL”.</p>

<p>The initial solution proposed by the ACM was to put a limit on the length of contestants’ names. Someone pointed out that this would discriminate against teams from certain regions where bigger names are more common (for instance, children in the home towns of well-known actors are more likely to be named after that actor – imagine how many children in Oakland, California have been named after the actor Mahershalalhashbaz Ali since he became one of the stars of the television series The 4400).</p>

<p>As a compromise, the ACM decided to change the rule to require that “no team member’s name can have length more than two away from the average length of all the team member’s names.” Using this rule, a team consisting of “MAHERSHALALHASHBAZ”, “AL”, and “BILL” would be disqualified (average name length is 8, so AL and BILL are not within 2). However, “MAHERSHALALHASHBAZ”, “NEBUCHADNEZZAR”, and “BILLYBOBBENJAMIN” would be okay (average name length is 16, and all team member names have length within 2 of this number).</p>

<p>Given the names of n students, determine whether or not they can be placed into teams of k members each so that each team meets the requirements of the new ACM rule.</p>

### 입력 

 <p>Input will consist of multiple test cases. Each test case begins with a line consisting of two positive integers n and k, where n ≤ 1000, k ≤ 8, and n is divisible by k. Following this are n lines, each containing a single name consisting only of upper case letters with no embedded, leading, or trailing blanks. These are the names of the n students who need to be organized into teams of size k each. No name will exceed 80 characters. The last test case is followed by a line containing two zeros.</p>

### 출력 

 <p>For each test case, output the case number (starting at 1) followed by either the word “yes” (meaning that it is possible to organize the students into teams of size k so that no student on that team has a name whose length is greater than distance 2 from the average name lengths of the members on that team), or “no” if it is not possible. Use the format shown in the sample output. Insert a blank line between cases.</p>

