# [Silver III] Conference - 8373 

[문제 링크](https://www.acmicpc.net/problem/8373) 

### 성능 요약

메모리: 110536 KB, 시간: 268 ms

### 분류

그리디 알고리즘, 구현, 수학

### 제출 일자

2024년 10월 11일 12:17:11

### 문제 설명

<p>In Bytetown preparations for the annual Great Bitonic Conference are taking place. There are going to be <em>m</em> presentations which - according to the tradition - must take place at exactly the same time. All presentations are organized in identical rooms. Each room can hold up to <em>k</em> persons. There are enough rooms to hold all participants of the conference. If there are more than <em>k</em> attendance of a presentation, organizers have to book more than one room for it (to be exact, for <em>n</em> participants there are ⌈<em>n</em> / <em>k</em>⌉<sup>1</sup> rooms required).</p>

<p>Organizers of the conference would like to maximize their income - the amount of money obtained from selling tickets, decreased by the cost of renting rooms should be as great as possible. The cost of renting one room for <em>k</em> people is equal to <em>s</em>. A single ticket for the <em>i</em>-th presentation costs <em>c<sub>i</sub></em>. The prices of tickets were selected in such way that it is profitable to rent a room for ⌊<em>k</em> / 2⌋ people (it is also possible - however not required - that it is profitable to rent a room for a smaller number of people), meaning that in this case the profit is non-negative. Organizers may cancel some reservations, so that their income is maximized. You implemented the original version of registration system, so it is your job to perform the cancellation process.</p>

<p>Write a program which:</p>

<ul>
	<li>reads from the standard input the prices of tickets, the size of a room, the cost of renting a room and the list of reservations,</li>
	<li>calculates maximal profit from the conference, that can be obtained by potentially cancelling some of the reserved tickets,</li>
	<li>writes the result to the standard output.</li>
</ul>

<p><sup>1</sup>Symbol ⌈<em>x</em>⌉ represents the smallest integer not smaller than <em>x</em>. Analogically, ⌊<em>x</em>⌋ represents the greatest integer not grater than <em>x</em>.</p>

### 입력 

 <p>In the first line of the standard input there are four integers: <em>m</em>, <em>l</em>, <em>k</em> and <em>s</em> (1 ≤ <em>m</em> ≤ 100, 2 ≤ <em>l</em> ≤ 1 000 000, 2 ≤ <em>k</em> ≤ 400, 1 ≤ <em>s</em> ≤ 1 000), separated by single spaces. They represent: the number of presentations, the number of reservations, the size of a single room and the cost of renting a single room. The second line contains exactly <em>m</em> numbers <em>c<sub>i</sub></em> (<em>c<sub>i</sub></em> · ⌊<em>k</em> / 2⌋ ≥ <em>s</em>, <em>c<sub>i</sub></em> ≤ <em>s</em>), separated by single spaces (the lower limit on the value of <em>c<sub>i</sub></em> is due to profitability of renting a room for ⌊<em>k</em> / 2⌋ participants of a conference). They represent prices of tickets for the presentations (numbered from 1 to <em>m</em>). Following <em>l</em> lines contain descriptions of reservations. Each reservation is represented by two integers <em>p<sub>i</sub></em> and <em>r<sub>i</sub></em> (1 ≤ <em>p<sub>i</sub></em> ≤ <em>m</em>, 1 ≤ <em>r<sub>i</sub></em> ≤ 1 000), separated by a single space. They represent the number of a presentation and the number of tickets booked for this presentation. It is allowed to cancel any number of tickets within the same reservation, not only the whole reservation.</p>

### 출력 

 <p>The first and only line of standard output should contain exactly one integer - the total income that can be obtained.</p>

