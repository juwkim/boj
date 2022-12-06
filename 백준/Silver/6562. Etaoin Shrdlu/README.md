# [Silver V] Etaoin Shrdlu - 6562 

[문제 링크](https://www.acmicpc.net/problem/6562) 

### 성능 요약

메모리: 116188 KB, 시간: 168 ms

### 분류

Empty

### 문제 설명

<p>The relative frequency of characters in natural language texts is very important for cryptography. However, the statistics vary for different languages. Here are the top 9 characters sorted by their relative frequencies for several common languages:</p>

<pre>English: ETAOINSHR
German:  ENIRSATUD
French:  EAISTNRUL
Spanish: EAOSNRILD
Italian: EAIONLRTS
Finnish: AITNESLOK
</pre>

<p>Just as important as the relative frequencies of single characters are those of pairs of characters, so called digrams. Given several text samples, calculate the digrams with the top relative frequencies.</p>

### 입력 

 <p>The input contains several test cases. Each starts with a number <em>n</em> on a separate line, denoting the number of lines of the test case. The input is terminated by <em>n=0</em>. Otherwise, <em>1<=n<=64</em>, and there follow <em>n</em> lines, each with a maximal length of <em>80</em> characters. The concatenation of these <em>n</em> lines, where the end-of-line characters are omitted, gives the text sample you have to examine. The text sample will contain printable ASCII characters only.</p>

### 출력 

 <p>For each test case generate 5 lines containing the top 5 digrams together with their absolute and relative frequencies. Output the latter rounded to a precision of 6 decimal places. If two digrams should have the same frequency, sort them in (ASCII) lexicographical order. Output a blank line after each test case.</p>

