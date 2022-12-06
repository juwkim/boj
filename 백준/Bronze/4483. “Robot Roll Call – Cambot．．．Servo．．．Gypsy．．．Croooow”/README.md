# [Bronze I] “Robot Roll Call – Cambot...Servo...Gypsy...Croooow” - 4483 

[문제 링크](https://www.acmicpc.net/problem/4483) 

### 성능 요약

메모리: 29200 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Mystery Science Theater 3000 is about to start, which means it’s time for “Robot Roll Call”, where the name of each robot is called out, as per the list received from Earth. The expectation is that if a robot is there, it will respond by adding its name to a data stream which is then sent back to Earth. Unfortunately today, once the roll is received, communication with Earth is temporarily lost. In the meantime, the robots that are present for roll call have saved their names to the data stream. However, lots of other things are also being saved to this same stream. To help extract data later, any data placed in the stream is separated by whitespace. Once the communication problems are resolved, the contents of this stream are relayed to Earth.</p>

<p>Your task is as follows. Given a list of names for roll call, you must scan the accompanying data stream and determine if a given name is there. For each name that is in the roll call, report whether or not that name was in the data stream. For a name to be a match, it must appear <strong>EXACTLY</strong> as shown in the roll. This means a match is case-sensitive and sub-string matches are not allowed.</p>

### 입력 

 <p>The first entry in the file will be an integer value t (t > 0) that represents the number of test data sets the file contains. Following this entry, will be t test sets. Each test set will start with an integer n (0 < n < 26) representing the number of names in the roll. On the lines that follow will be n entries, one per line, containing the individual names in the roll. No name will have more than 25 characters. Names will only contain the characters A-Z, a-z, and 0-9. Names will be unique.</p>

<p>Following the names will be an integer d (0 < d < 100) representing the number of lines in the data stream. On each subsequent line will be the characters that make up the data stream. Each line of the data stream will contain at least one character and at most 100. Furthermore, the data on a given line will be separated by whitespace (space, tab, or combination of the two). Finally, any names from the roll that might occur as part of the data stream will be found on one line (a name will not be split across lines).</p>

### 출력 

 <p>Write the test set number (starting at 1) on a line of its own, followed by the names in the roll and whether or not a given name was found in the data stream. Each of these names should occur on a line of their own. Add a blank line to the end of each test case. Output format must be identical to the sample output shown below.</p>

