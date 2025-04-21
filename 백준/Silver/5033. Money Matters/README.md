# [Silver I] Money Matters - 5033 

[문제 링크](https://www.acmicpc.net/problem/5033) 

### 성능 요약

메모리: 112592 KB, 시간: 136 ms

### 분류

너비 우선 탐색, 자료 구조, 깊이 우선 탐색, 분리 집합, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 21일 15:08:54

### 문제 설명

<p>Our sad tale begins with a tight clique of friends. Together they went on a trip to the picturesque country of Molvania. During their stay, various events which are too horrible to mention occurred. The net result was that the last evening of the trip ended with a momentous exchange of “I never want to see you again!”s. A quick calculation tells you it may have been said almost 50 million times!</p>

<p>Back home in Scandinavia, our group of ex-friends realize that they haven’t split the costs incurred during the trip evenly. Some people may be out several thousand crowns. Settling the debts turns out to be a bit more problematic than it ought to be, as many in the group no longer wish to speak to one another, and even less to give each other money.</p>

<p>Naturally, you want to help out, so you ask each person to tell you how much money she owes or is owed, and whom she is still friends with. Given this information, you’re sure you can figure out if it’s possible for everyone to get even, and with money only being given between persons who are still friends.</p>

### 입력 

 <p>The first line contains two integers, n (2 ≤ n ≤ 10000), and m (0 ≤ m ≤ 50000), the number of friends and the number of remaining friendships. Then n lines follow, each containing an integer o (−10000 ≤ o ≤ 10000) indicating how much each person owes (or is owed if o < 0). The sum of these values is zero. After this comes m lines giving the remaining friendships, each line containing two integers x, y (0 ≤ x < y ≤ n − 1) indicating that persons x and y are still friends.</p>

### 출력 

 <p>Your output should consist of a single line saying “POSSIBLE” or “IMPOSSIBLE”.</p>

