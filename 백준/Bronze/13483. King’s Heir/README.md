# [Bronze I] King’s Heir - 13483 

[문제 링크](https://www.acmicpc.net/problem/13483) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>The king is dead, long live the king! After the sudden death of the king Fert XIII the people of the Flatland Kingdom are going to welcome the new king. Unfortunately, there is a problem, Fert has too many sons.</p>

<p>Actually, he has n sons and he loved each new son more than all of his previous sons. Well, probably he just stopped loving his sons because of their bad behavior. Anyway, after the new son was born Fert made the new testament that declared that the newly born son would be the heir.</p>

<p>However, there is a problem. Only the king’s son who is at least 18 years old at the moment of the king’s death can become a new king. Now the ministers of the government are trying to find the correct new king, but they seem to fail. Help them!</p>

### 입력 

 <p>The first line of the input contains three integers: d, m and y — the day, the month and the year of the king’s death, d is from 1 to 31, m is from 1 to 12, y is from 1 to 9999. It is guaranteed that there exists day d in month m, all months have the same number of days in Flatland as in our country, except that Flatland calendar doesn’t have leap years, so February (month 2) always has 28 days.</p>

<p>The second line contains n (1 ≤ n ≤ 100) — the number of king’s sons. The following n lines contain three integers each d<sub>i</sub>, m<sub>i </sub>and y<sub>i</sub> and specify the birth dates of king’s sons. All dates are correct and no son is born after or on the day of king’s death. The king had no twins, so no two sons were born on the same date.</p>

### 출력 

 <p>Output one integer — the number of the son that would become the king, or −1 if none of them is at least 18 years old. The sons are numbered from 1 to n in order they are described in the input. The youngest son who is at least 18 years old at the moment of the king’s death would become the king. If the son has his 18th birthday exactly on the day of the king’s death, he can become a king.</p>

