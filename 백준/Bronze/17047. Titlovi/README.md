# [Bronze I] Titlovi - 17047 

[문제 링크](https://www.acmicpc.net/problem/17047) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

파싱(parsing), 문자열(string)

### 문제 설명

<p>In order to understand speech in foreign films, the translation of the spoken text is displayed at the bottom of the screen, colloquially called subtitles. In the digital world, subtitles are often written in .SRT files that consist of blocks of the following format:</p>

<pre>[Ordinal number of the block]
[Beginning time of the subtitles --> Ending time of the subtitles]
[Subtitle text in one or more lines]</pre>

<p>These blocks are separated by one blank line. The time is in the form of HH:MM:SS,TTT (note the colon and the comma), meaning hour:minute:second,millisecond. One second contains 1000 milliseconds. Here's an example of a .SRT file:</p>

<pre>1
00:00:01,600 --> 00:00:04,200
Good day!

2
00:00:05,900 --> 00:00:07,999
Good day to you too!
Here you go!

3
00:00:10,000 --> 00:00:14,000
May I please have ten garlic sausages?</pre>

<p>Sometimes subtitles are not fully synchronized with the associated movie, and appear for example two seconds too soon or too late. Because of that we want all the times in the appropriate .SRT file, or in some part of that file, to shift forward or backward for a specified number of (milli)seconds. Write a program which does that.</p>

### 입력 

 <p>Input data contains up to 30 lines that represent part of some .SRT file.</p>

<p>The first line begins with a block with the ordinal number X, followed by blocks with ordinal numbers X + 1, X + 2, ..., X + K, in the form described in the task statement.</p>

<p>Blocks are separated by a single blank line. The subtitles text within the block contains one or more non-empty lines containing the letters of the english alphabet and the punctuation marks<code>',.?!.</code> The line after the last block contains only the '#' sign that indicates the end of the observed part of the file and that character will not appear elsewhere.</p>

<p>The following (last) line contains the time in milliseconds (-10 000 ≤ T ≤ 10 000), which needs to be added to all subtitle blocks.</p>

### 출력 

 <p>Print part of the .SRT file given in the input data, whereby the time stamps (beginning and ending time of each block) should be increased by T milliseconds. Test samples will ensure that the required time stamps are not negative.</p>

