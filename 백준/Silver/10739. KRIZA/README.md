# [Silver I] KRIZA - 10739 

[문제 링크](https://www.acmicpc.net/problem/10739) 

### 성능 요약

메모리: 123888 KB, 시간: 112 ms

### 분류

수학

### 제출 일자

2025년 5월 4일 08:16:05

### 문제 설명

<p>The state of the economy is bad, the crysis is striking the country and people are losing their jobs. However, Sisyphus, the main hero of this task, has found himself a new job. Starting next monday, Sisyphus will be an assistant locksmith in a hotel. Naturally, first he needs to demonstrate his locksmithing abilities to the head locksmith.</p>

<p>This is why the head locksmith has given Sisyphus N keys on a big round pendant, blindfolded him and led him into a big room. That room contains N locked doors, denoted with numbers from 1 to N. Each of the keys on the pendant unlocks precisely one door.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images3/kriza.png" style="height:198px; width:214px"></p>

<p>Sisyphus’ job is to unlock and lock each door again. He does this in a way that he moves along the wall, not changing direction, until he reaches a door. When he reaches a door, he tries unlocking it using the first (leftmost) key. In the case when the key doesn’t unlock the door, Sisyphus moves it to the other (right) side of pendant and repeats this procedure until he finds the right key. His work is done when he goes through all the doors. The first door Sisyphus unlocked is denoted with 1, the next with 2, the one after with 3 and so on...</p>

<p>What Sisyphus doesn’t know is that the head locksmith is, in fact, testing his endurance so he led him into a circular room. Therefore, Sisyphus will, after unlocking and locking the last door, go unlocking and locking the first door again. Because he’s a hardworking and persistent fellow, Sisyphus has been doing this job for hours and hours without saying a single word. Only after the Kth successful unlocking and locking of a door he spoke: "If only I knew how many times so far I’ve put a wrong key in a door’s lock!" Your task is to answer his question!</p>

### 입력 

 <p>The first line of input contains the integers N (1 ≤ N ≤ 10<sup>5</sup>) and K (1 ≤ K ≤ 10<sup>9</sup>) from the task.</p>

<p>The ith of the following N lines contains the integer vi (1 ≤ vi ≤ N) which denotes that the ith key on the pendant (from left to right) unlocks the door vi.</p>

### 출력 

 <p>The first and only line of output must contain an integer representing the answer to Sisyphus’ question.</p>

