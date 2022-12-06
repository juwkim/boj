# [Silver V] Flight Turbulence - 17848 

[문제 링크](https://www.acmicpc.net/problem/17848) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 구현(implementation)

### 문제 설명

<p>Fly-By-Night Airlines is a low budget carrier specializing in late night/early morning flights. Things are run a little looser on this airline as was apparent a few nights ago. The flight from Ypsilanti, MI to Walla Walla, WA was completely sold out and all of the passengers were eagerly waiting to board the plane. Sensing their eagerness and looking for a little fun, the flight crew decided to open the gates and let the passengers rush to any seat they wanted, regardless of their seat assignment. The passengers were a little leery of this until the flight crew sweetened the deal with the promise of free peanuts for everyone. After a mad dash through the gates and one minor trampling injury all of the passengers had found a seat and were eagerly awaiting their peanuts.</p>

<p>Well, almost all. Wouldn’t you know it, one passenger wasn’t too happy with the seat he ended up with and decided he wanted his pre-assigned seat, peanuts be damned. When he threatened to call the FAA the flight crew relented and let him have his originally assigned seat, displacing the passenger in that seat. Well now, of course, THAT passenger wanted HER original seat. This dislodged another passenger who also wanted his original seat and so on. Eventually one of the dislodged passengers ended up in the seat initially vacated and things quieted down. Needless to say, the price of peanuts skyrocketed on that flight.</p>

<p>Some of the flight crew wanted to try this again on some other flights, but they were concerned if a similar situation might arise. They would like you to write a simulation program that would determine how many people would have to move if one person suddenly insisted on sitting in his/her assigned seat.</p>

### 입력 

 <p>Input starts with a line containing two positive integers n m where n ≤ 200 is the number of passengers and m ≤ n is the current seat of a passenger who wants to sit in his/her assigned seat. The next line contains n integers. The value of the i<sup>th</sup> of these integers indicates the assigned seat for the passenger who is currently sitting in seat i. All assigned seat numbers are unique and in the range 1 . . . n.</p>

### 출력 

 <p>Output the number of passengers that must change seats.</p>

