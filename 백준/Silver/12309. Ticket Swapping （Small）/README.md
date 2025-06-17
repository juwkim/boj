# [Silver I] Ticket Swapping (Small) - 12309 

[문제 링크](https://www.acmicpc.net/problem/12309) 

### 성능 요약

메모리: 110908 KB, 시간: 104 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐

### 제출 일자

2025년 6월 18일 02:32:39

### 문제 설명

<p>The city has built its first subway line, with a grand total of <strong>N</strong> stations, and introduced a new way of paying for travel. Instead of just paying for one ticket and making an arbitrary journey, the price you pay is now based on <em>entry cards</em>.</p>

<p>When entering the subway, each passenger collects an <em>entry card</em>, which specifies the station the passenger entered at. When leaving the subway, the passenger has to give up the entry card, and is charged depending on the distance (in stations traveled) between the entry station specified on the entry card, and the exit station on which the entry card is surrendered. The payment depends on the distance between these stations as follows:</p>

<ul>
	<li>if they are the same station, you don't pay;</li>
	<li>if they are adjacent stations, you pay <strong>N</strong> pounds;</li>
	<li>if the distance is two stations, you pay <strong>2N - 1</strong>: a charge <strong>N</strong> for the first stop and <strong>N - 1</strong> for the second;</li>
	<li>the third station costs <strong>N-2</strong> (so you pay <strong>3N - 3</strong> for a three-station-long trip), the fourth stop <strong>N-3</strong>, and the <em>i</em>th stop <strong>N + 1-<em>i</em></strong>;</li>
	<li>thus, if you travel from one end of the subway to the other (a distance of <strong>N</strong>-1 stations), you pay 2 pounds for the last station traveled, and a grand total of (<strong>N</strong><sup>2</sup> + <strong>N</strong> - 2) / 2 in total.</li>
</ul>

<p> </p>

<p>After introducing this system the city noticed their gains are not as big as they expected. They figured out this might be due to people swapping their entry cards — so, for instance, if one person enters at station <strong>A</strong>, travels two stations to <strong>B</strong> and exits, while another person enters at <strong>B</strong>, travels three stations to <strong>C</strong> and exits, they would normally pay (in total) <strong>2N - 1 + 3N - 3 = 5N - 4</strong>. But if the two people swapped their entry cards at station <strong>B</strong>, then the first one would travel for free (as he would surrender an entry card specifying the station <strong>B</strong> while exiting a station <strong>B</strong>, and so register a distance of zero); while the second person will exit at station <strong>C</strong> and surrender an entry card specifying station <strong>A</strong>, which is 5 stations away, and pays <strong>5N - 10</strong>, at a net loss of six pounds to the city!</p>

<p>The city now wants to learn how much they can possibly lose if this practice becomes widespread. We will consider only one direction (from station 1 to station <strong>N</strong>, passing through all the stations in order) of the subway, and only one train on this line. We assume a passenger travelling from <strong>o</strong> to <strong>e</strong> obtains an entry card at <strong>o</strong>, can swap her entry card any number of times with any other passengers anywhere between <strong>o</strong> and <strong>e</strong>, including swapping with people who leave at <strong>o</strong> or those who enter at <strong>e</strong>, and then exit the train at <strong>e</strong> with some entry card (it is necessary to surrender some entry card to exit the subway). We also assume the passenger will not exit the train in the meantime (that is, will not surrender the currently held card and obtain a new one).</p>

<p>You are given a map of traffic (specifying how many passengers travel this train from which station to which), and you should calculate the city's financial loss, assuming passengers swap their cards to maximize this loss.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case contains the number <strong>N</strong> of stops (the stops are numbered 1 to <strong>N</strong>), and the number <strong>M</strong> of origin-endpoint pairs given. The next <strong>M</strong> lines contain three numbers each: the origin stop <strong>o</strong><strong><sub>i</sub></strong>, the end stop <strong>e</strong><strong><sub>i</sub></strong> and <strong>p</strong><strong><sub>i</sub></strong>: the number of passengers that make this journey.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 20.</li>
	<li>1 ≤ <strong>o</strong><strong><sub>i</sub></strong> < <strong>e</strong><strong><sub>i</sub></strong> ≤ <strong>N</strong></li>
	<li><span style="line-height:1.6em">2 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 100.</span></li>
	<li>1 ≤ <strong>M</strong> ≤ 100.</li>
	<li>1 ≤ <strong>p</strong><strong><sub>i</sub></strong> ≤ 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the total loss the city can observe due to ticket swapping, modulo 1000002013.</p>

