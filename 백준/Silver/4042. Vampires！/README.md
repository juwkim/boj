# [Silver I] Vampires! - 4042 

[문제 링크](https://www.acmicpc.net/problem/4042) 

### 성능 요약

메모리: 2356 KB, 시간: 4 ms

### 분류

구현

### 제출 일자

2025년 6월 15일 21:42:55

### 문제 설명

<p>The big media gimmick these days seems to be vampires. Vampire movies, vampire television shows, vampire books, vampire dolls, vampire cereal, vampire lipstick, vampire bunnies – kids and teenagers and even some adults spend lots of time and money on vampire-related stuff. Surprisingly, nowadays vampires are often the good guys. Obviously, the ACM Programming Contest had better have a vampire problem in order to be considered culturally relevant.</p>

<p>As eveyone knows, vampires are allergic to garlic, sunlight, crosses, wooden stakes, and the Internal Revenue Service. But curiously they spend a good part of their time smashing mirrors. Why? Well, mirrors can’t hurt vampires physically, but it’s embarrassing to be unable to cast a reflection. Mirrors hurt vampire’s feelings. This problem is about trying to help them avoid mirrors.</p>

<p>In a room full of vampires and ordinary mortals there are a number of mirrors. Each mirror has one of four orientations – north, south, east, or west (the orientation indicates which side of the mirror reflects). A vampire is in danger of embarrassment if he or she is in a direct horizontal or vertical line with the reflecting side of a mirror, unless there are intervening objects (mortals or other mirrors). For example, in the following room layout</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/vam.png" style="height:209px; width:233px"></p>

<p>vampire V<sub>2</sub> is exposed to a south-facing mirror and both vampires V<sub>1</sub> and V<sub>2</sub> are exposed to a west-facing mirror (note that a vampire can’t protect another vampire from embarrassment since neither one casts a reflection.) Your job is to notify each vampire of the directions in which there is danger of experiencing ENR (embarrassing non-reflectivity).</p>

### 입력 

 <p>Each test case begins with three integers v o m, indicating the number of vampires, ordinary mortals, and mirrors in the room. Each of the following v lines contains a pair of integers x,y, 0 ≤ x,y ≤ 100, giving the grid square of a vampire (x = 0 corresponds to the westernmost side of the grid and y = 0 corresponds to the southernmost side). Each of the following o lines contains the grid square of an ordinary mortal in the same format. Each of the following m lines contains a letter (either N, S, E, or W) indicating the orientation of a mirror, followed by four integers x<sub>1</sub> y<sub>1</sub> x<sub>2</sub> y<sub>2</sub> indicating the start and end squares of the mirror (same bounds as above). Mirrors can be of any positive length, have a thickness of 1 grid square, and will always be aligned along either the east-west or north-south axis. Each grid square contains no more than 1 vampire, mortal, or mirror section. The last test case is followed by a line containing 0 0 0.</p>

### 출력 

 <p>For each test case print the case number followed by one line for each vampire that is in danger of embarrassment. On each of these lines, print the vampire’s number (vampires are numbered from 1 to v in order of appearance in the input) followed by a list of directions to avoid. For instance, if a vampire is exposed to a south-facing mirror and an east-facing mirror, he/she is exposed in the directions north and west. Directions should be printed in alphabetical order (e.g., north west, not west north). If no vampires are suffering from embarrassment, output the word none. Imitate the sample output.</p>

