# [Silver I] Dancers - 7494 

[문제 링크](https://www.acmicpc.net/problem/7494) 

### 성능 요약

메모리: 110964 KB, 시간: 144 ms

### 분류

기하학, 구현, 시뮬레이션, 정렬

### 제출 일자

2025년 6월 25일 02:09:51

### 문제 설명

<p>Alex missed the ballroom dance competition that he wanted to attend. So now he wants to know the pairs of dancers whose dancing he missed. He had several photos from the competition, so he chose one where all dancers are clearly visible and wrote down the coordinates of all <strong>N</strong> dancers (<strong>N</strong> is even).</p>

<p>Then Alex determined the pairs of dancers by the following algorithm: from not yet paired dancers he chooses two closest (to each other) dancers and assumes that they dance together as a pair. Should he find several pairs of dancers with the same minimum distance between dancers, he chooses lexicographically smallest pair (Alex enumerated dancers by integer numbers from <strong>1</strong> to <strong>N</strong>, dancers are ordered inside a pair, one with lower number goes first). You are asked to help Alex to determine pairs of dancers.</p>

### 입력 

 <p>The first line of input contains even integer <strong>N</strong> (<strong>2</strong> ≤ <strong>N</strong> ≤ <strong>300</strong>). Each <strong>i</strong>-th line of the next <strong>N</strong> lines contains two integers — <strong>x</strong> and <strong>y</strong> coordinates of <strong>i</strong>-th dancer. All coordinates are less than <strong>10</strong><sup><strong>8</strong> </sup>by absolute value.</p>

### 출력 

 <p>You should output <strong>N</strong>/<strong>2</strong> lines. Each line must contain numbers of dancers in the corresponding pair. The first number in a line should be less than the second. Lines must be sorted in the lexicographically ascending order.</p>

