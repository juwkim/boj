# [Bronze I] PAPRIKA - 10701 

[문제 링크](https://www.acmicpc.net/problem/10701) 

### 성능 요약

메모리: 30840 KB, 시간: 112 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Young Marin is working as an assistant chef in a popular restaurant called Plavi 9 where the daily offer includes, among other things, stuffed peppers. Every assistant chef knows that the peppers are stuffed when they are young, so he decided to prepare the meal using only peppers not older than X days. Marin will serve all the other peppers fresh, as an appetizer. Luckily, as Croatia entered the EU, there is a new law enforced. The law states that every pepper has to have its ID card at any moment. Marin can easily determine the age of a pepper by looking at its ID card.</p>

<p>It is less known that peppers have, besides official documents, their own life purposes and ambitions. More precisely, every pepper knows from an early age whether they want to be served as a fresh or stuffed pepper when they grow up. Bearing that in mind, you are aware of the problems N peppers are facing while waiting in line to be filled. The life purpose of some peppers is to be a part of the dish, but they are too old, and some peppers want to be served fresh, but will be filled.</p>

<p>Because the peppers aren’t aware of Marin’s number X, they have decided to rectify the injustice using the following strategy. The first pepper tries to switch its ID card with second pepper, then the second pepper tries to switch its ID card with the third pepper and so on until the end of the line. Two peppers will switch their ID cards if the pepper that has a larger number on the ID card it’s currently holding wants to become a filled pepper, and the one with the smaller number doesn’t. The peppers will not switch ID cards if they have equal numbers on them.</p>

<p>Your task is to determine the number of peppers that will have their life purpose completed.</p>

### 입력 

 <p>The first line of input contains two integers N and X (1 ≤ N, X ≤ 1 000) from the task.</p>

<p>Each of the following N lines contains two integers a (1 ≤ a ≤ 1 000) and b (0 ≤ b ≤ 1) that describe the peppers in the order which they’re waiting in line to be filled.</p>

<p>The number a is printed on the ID card of a pepper and represents its age in days, and number b represents it’s life purpose (0 if pepper wants to be served fresh or 1 if it wants to be served as a filled pepper).</p>

### 출력 

 <p>The first and only line of output must contain the number of peppers that will have their life purpose completed.</p>

