# [Bronze I] Historical TV Remote Control - 25871 

[문제 링크](https://www.acmicpc.net/problem/25871) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>As Dr. Orooji is getting older, he is becoming more attached to older items and has difficulty letting go of them (he claims they have historical value). For example, he still has the first table he got for the programming team! The situation is the same at home, e.g., there is a broken TV remote control but Dr. O still uses it, because he considers it an old item with historical value!</p>

<p>The old remote control has 12 buttons: digits 0-9, channel down, and channel up. There are no other buttons on the remote control. Some digits on the remote don’t work but channel up/down always works. So, to get to a particular channel, Dr. O sometimes has to use the channel up/down. For example, let’s assume digits 0 and 5 on the remote don’t work:</p>

<ul>
	<li>If Dr. O wants to watch channel 102, he would select 99 and then “channel up” 3 times.</li>
	<li>If he wants to watch channel 597, he would select 611 and then “channel down” 14 times.</li>
</ul>

<p>Given the digits that do not work and a target channel, determine how many times Dr. O needs to hit channel up or down. Dr. O, of course, wants to exert the least energy, hence he wants to hit the channel up/down the minimum number of times. Assume that Dr. O will enter a channel between 0 and 999 (inclusive) to start and that channel down has no effect at 0 and channel up has no effect at 999.</p>

### 입력 

 <p>The first input line contains an integer, n (1 ≤ n ≤ 9), indicating how many digits on the remote do not work. These broken digits are listed (in increasing order) on the same input line. The second input line provides the target channel (an integer between 1 and 999, inclusive).</p>

### 출력 

 <p>The output consists of a single integer, indicating how many times Dr. O needs to hit channel up/down. Note that, since one or more digits work, it is always possible to reach the target channel.</p>

