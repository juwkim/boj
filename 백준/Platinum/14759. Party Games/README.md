# [Platinum III] Party Games - 14759 

[문제 링크](https://www.acmicpc.net/problem/14759) 

### 성능 요약

메모리: 30840 KB, 시간: 172 ms

### 분류

문자열(string)

### 문제 설명

<p>You've been invited to a party. The host wants to divide the guests into 2 teams for party games, with exactly the same number of guests on each team. She wants to be able to tell which guest is on which team as she greets them as they arrive, and as easily as possible, without having to take the time to look up each guest's name on a list. Being a good computer scientist, you have an idea: give her a single string, and all she has to do is determine whether the guest's name is alphabetically less than or greater than that string.</p>

<p>Given the unique names of n party guests (n is even), find the shortest possible string S such that exactly half the names are less than or equal to S, and exactly half are greater than S. If there’s more than one string of the shortest length, output the one that comes first alphabetically.</p>

### 입력 

 <p>There will be multiple test cases in the input. Each test case will begin with an even integer n (2≤n≤1,000) on its own line. On the next n lines will be names, one per line. Each name will be a single word consisting only of capital letters, and will be at least one letter and no longer than 30 letters. All of the names in a test case will be unique. The input will end with a 0 on its own line.</p>

### 출력 

 <p>For each case, output the alphabetically first of all of the shortest possible strings that your host could use to separate her guests. Output this string using all upper case letters. Do not output any spaces. Do not put a blank line between outputs.</p>

