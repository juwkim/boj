# [Silver V] Numerically Speaking - 6420 

[문제 링크](https://www.acmicpc.net/problem/6420) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>A developer of crossword puzzles (and other similar word games) has decided to develop a mapping between every possible word with from one to twenty characters and unique integers. The mapping is very simple, with the ordering being done first by the length of the word, and then alphabetically. Part of the list is shown below.</p>

<p> </p>

<pre>    a          1
    b          2
    ...
    z          26
    aa         27
    ab         28
    ...
    snowfall   157,118,051,752
    ...
</pre>

<p>Your job in this problem is to develop a program which can translate, bidirectionally, between the unique word numbers and the corresponding words.</p>

<p> </p>

### 입력 

 <p>Input to the program is a list of words and numbers, one per line starting in column one, followed by a line containing a single asterisk in column one. A number will consist only of decimal digits (0 through 9) followed immediately by the end of line (that is, there will be no commas in input numbers). A word will consist of between one and twenty lowercase alphabetic characters (a through z).</p>

### 출력 

 <p>The output is to contain a single line for each word or number in the input data. This line is to contain the word starting in column one, followed by an appropriate number of blanks, and the corresponding word number starting in column 23. Word numbers that have more than three digits must be separated by commas at thousands, millions, and so forth.</p>

