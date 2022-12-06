# [Silver V] Maya Calendar - 7369 

[문제 링크](https://www.acmicpc.net/problem/7369) 

### 성능 요약

메모리: 115268 KB, 시간: 188 ms

### 분류

구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>During his last sabbatical, professor M. A. Ya made a surprising discovery about the old Maya calendar. From an old knotted message, professor discovered that the Maya civilization used a 365 day long year, called Haab, which had 19 months. Each of the first 18 months was 20 days long, and the names of the months were pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu. Instead of having names, the days of the months were denoted by numbers starting from 0 to 19. The last month of Haab was called uayet and had 5 days denoted by numbers 0, 1, 2, 3, 4. The Maya believed that this month was unlucky, the court of justice was not in session, the trade stopped, people did not even sweep the floor.</p>

<p>For religious purposes, the Maya used another calendar in which the year was called Tzolkin (holly year). The year was divided into thirteen periods, each 20 days long. Each day was denoted by a pair consisting of a number and the name of the day. They used 20 names: imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau and 13 numbers; both in cycles.</p>

<p>Notice that each day has an unambiguous description. For example, at the beginning of the year the days were described as follows:</p>

<p>1 imix, 2 ik, 3 akbal, 4 kan, 5 chicchan, 6 cimi, 7 manik, 8 lamat, 9 muluk, 10 ok, 11 chuen, 12 eb, 13 ben, 1 ix, 2 mem, 3 cib, 4 caban, 5 eznab, 6 canac, 7 ahau, and again in the next period 8 imix, 9 ik, 10 akbal...</p>

<p>Years (both Haab and Tzolkin) were denoted by numbers 0, 1, ..., where the number 0 was the beginning of the world. Thus, the first day was:</p>

<p>Haab: 0. pop 0</p>

<p>Tzolkin: 1 imix 0</p>

<p>Help professor M. A. Ya and write a program for him to convert the dates from the Haab calendar to the Tzolkin calendar.</p>

### 입력 

 <p>The date in Haab is given in the following format:</p>

<p>NumberOfTheDay. Month Year</p>

<p>The first line of the input file contains the number of the input dates in the file. The next n lines contain n dates in the Haab calendar format, each in separate line. The year is smaller then 5000.</p>

<p> </p>

### 출력 

 <p>The date in Tzolkin should be in the following format:</p>

<p>Number NameOfTheDay Year</p>

<p>The first line of the output file contains the number of the output dates. In the next n lines, there are dates in the Tzolkin calendar format, in the order corresponding to the input dates.</p>

