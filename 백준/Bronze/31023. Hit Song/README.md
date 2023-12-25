# [Bronze I] Hit Song - 31023 

[문제 링크](https://www.acmicpc.net/problem/31023) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

문자열

### 제출 일자

2023년 12월 26일 01:13:28

### 문제 설명

<p>Everyone can generally recognize when they hear a hit song. It's melodic, the words are easy to follow, and is auditorily pleasant.</p>

<p>Your job is to determine if a song will be a hit song based on its lyrics. Because the general population has lost their ideals of quality due of oversaturation of media, the threshold for deciding if a song will be a hit or not will be if the song uses words that most people find appealing at least 75% of the time.</p>

### 입력 

 <p>The first line of input contains the number of test cases <code>N</code> (<code>1 <= N <= 100</code>).</p>

<p>Each test case begins with a line containing <code>P</code> (<code>1 <= P <= 100</code>), indicating the number of pleasant words. The following <code>P</code> lines each contain a pleasant word. The following line contains a number <code>L</code> (<code>1 <= L <= 100</code>), indicating the number of lines in a song. The following <code>L</code> lines each contain a line of the song you are analyzing. A word is a sequence of 1 or more ASCII letters. Words are separated by (and may be preceded by or followed by) other (non-letter) printable ASCII characters (using ASCII values 32-126). No input line will exceed 100 characters. Ignore case when comparing words.</p>

### 출력 

 <p>For each test case, if the song reaches the 75% threshold of pleasantness, output <code>It's a hit!</code>, otherwise output <code>Delete immediately!</code> . Output a single line after each case.</p>

