# [Silver V] Hostel Nights - 5091 

[문제 링크](https://www.acmicpc.net/problem/5091) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

구현

### 제출 일자

2024년 6월 22일 19:27:29

### 문제 설명

<p>Students staying in a hostel on the first floor have a reputation for being a bit too noisy. The warder decides to investigate reports of noisiness over the course of 5 nights of a week. Other students are not willing to dob in their floor-mates directly but will help him eliminate some rooms where the students were not noisy. They are eliminated through being either odd or even, because they are a multiple of some number n, or because the inhabitant’s name starts with a particular letter.</p>

<p>Over the 5 nights the warden manages to form 3 variables from various other students’ help. At the end of 5 nights he will be able to work out who the noisiest students are. There is at least one as this floor is notorious.</p>

### 입력 

 <p>Input begins with a single integer, W, being the number of weeks worth of data (each week being 5 nights). The data for each week begins with 20 lines, each showing a room number and the name of a student, separated by a space. Rooms are numbered from 101 to 120. A student is represented by a single name.</p>

<p>This names list is followed by 5 lines each representing one night of the week. Each line consists of a letter, a number and another letter, each of which is separated by a space. The first letter is E or O to indicate whether even (E) or odd (O) numbered rooms may be eliminated. The number is used to eliminate all rooms that are a multiple of that number. The second letter may be used to eliminate any students whose name begins with that letter.</p>

### 출력 

 <p>Output for each week consists of the week number, where the first week is 1, followed by a list of the noisiest students; that is those who have not been eliminated on the greatest number of nights. Names are output in room number order, one per line.</p>

