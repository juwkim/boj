# [Silver I] Music Notes - 6010 

[문제 링크](https://www.acmicpc.net/problem/6010) 

### 성능 요약

메모리: 112860 KB, 시간: 148 ms

### 분류

이분 탐색, 누적 합

### 제출 일자

2025년 4월 8일 19:47:20

### 문제 설명

<p>FJ is going to teach his cows how to play a song. The song consists of N (1 <= N <= 50,000) notes, and the i-th note lasts for B_i (1 <= B_i <= 10,000) beats (thus no song is longer than 500,000,000 beats). The cows will begin playing the song at time 0; thus, they will play note 1 from time 0 through just before time B_1, note 2 from time B_1 through just before time B_1 + B_2, etc.</p>

<p>However, recently the cows have lost interest in the song, as they feel that it is too long and boring. Thus, to make sure his cows are paying attention, he asks them Q (1 <= Q <= 50,000) questions of the form, "In the interval from time T through just before time T+1, which note should you be playing?" The cows need your help to answer these questions which are supplied as T_i (0 <= T_i <= end_of_song).</p>

<p>Consider this song with three notes of durations 2, 1, and 3 beats:</p>

<pre>Beat:   0    1    2    3    4    5    6    ...
        |----|----|----|----|----|----|--- ...
        1111111111     :              :
                  22222:              :
                       333333333333333:</pre>

<p>Here is a set of five queries along with the resulting answer:</p>

<pre>   Query    Note
     2        2
     3        3
     4        3
     0        1
     1        1</pre>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and Q</li>
	<li>Lines 2..N+1: Line i+1 contains the single integer: B_i</li>
	<li>Lines N+2..N+Q+1: Line N+i+1 contains a single integer: T_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..Q: For each query, print a single integer that is the index of the note that the cows should be playing.</li>
</ul>

<p> </p>

