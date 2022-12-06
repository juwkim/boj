# [Silver V] Languages - 9512 

[문제 링크](https://www.acmicpc.net/problem/9512) 

### 성능 요약

메모리: 2412 KB, 시간: 92 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>The Enterprise has encountered a planet that at one point had been inhabited. The only remnant from the prior civilization is a set of texts that was found. Using a small set of keywords found in various different languages, the Enterprise team is trying to determine what type of beings inhabited the planet.</p>

### 입력 

 <p>The first line of input will be N (1 ≤ N ≤ 100), the number of different known languages. The next N lines contain, in order, the name of the language, followed by one or more words in that language, separated with spaces. Following that will be a blank line. After that will be a series of lines, each in one language, for which you are to determine the appropriate language.</p>

<p>Words consist of uninterrupted strings of upper or lowercase ASCII letters, apostrophes, or hyphens, as do the names of languages. No words will appear in more than one language.</p>

<p>No line will be longer than 256 characters. There will be at most 1000 lines of sample text.</p>

<p>Every sample text will contain at least one keyword from one of the languages. No sample text will contain keywords from multiple languages. The sample text may contain additional punctuation (commas, periods, exclamation points, semicolons, question marks, and parentheses) and spaces, all of which serve as delimiters separating keywords. Sample text may contain words that are not keywords for any specific language.</p>

<p>Keywords should be matched in a case-insensitive manner.</p>

### 출력 

 <p>For each line of sample text that follows the blank line separating the defined languages, print a single line that identifies the language with which the sample text is associated.</p>

