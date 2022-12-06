# [Bronze II] Perfect Harmony (Small) - 12495 

[문제 링크](https://www.acmicpc.net/problem/12495) 

### 성능 요약

메모리: 28776 KB, 시간: 120 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Jeff is a part of the great Atlantean orchestra. Each player of the orchestra has already decided what sound will he play (for the sake of simplicity we assume each player plays only one sound). We say two sounds are in harmony if the frequency of any one of them divides the frequency of the other (that's a pretty restrictive idea of harmony, but the Atlanteans are known to be very conservative in music). Jeff knows that the notes played by other players are not necessarily in harmony with each other. He wants his own note to improve the symphony, so he wants to choose his note so that it is in harmony with the notes all the other players play.</p>

<p>Now, this sounds simple (as all the frequencies are positive integers, it would be enough for Jeff to play the note with frequency 1, or, from the other side, the Least Common Multiple of all the other notes), but unfortunately Jeff's instrument has only a limited range of notes available. Help Jeff find out if playing a note harmonious with all others is possible.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each test case is described by two lines. The first contains three numbers: <strong>N</strong>, <strong>L</strong> and <strong>H</strong>, denoting the number of other players, the lowest and the highest note Jeff's instrument can play. The second line contains <strong>N</strong> integers denoting the frequencies of notes played by the other players.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 40.</li>
	<li>1 ≤ <strong>N</strong> ≤ 100.</li>
	<li>1 ≤ L ≤ H ≤ 10000.</li>
	<li>All the frequencies are no larger than 10000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either the string "NO" (if Jeff cannot play an appropriate note), or a possible frequency. If there are multiple frequencies Jeff could play, output the lowest one.</p>

