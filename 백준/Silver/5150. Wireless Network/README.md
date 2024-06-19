# [Silver III] Wireless Network - 5150 

[문제 링크](https://www.acmicpc.net/problem/5150) 

### 성능 요약

메모리: 110608 KB, 시간: 180 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 6월 19일 16:25:05

### 문제 설명

<p>One amenity that is being added to buses and trains in order to attract or retain ridership is wireless networks. This way, commuters can get work done, or waste as much time browsing the Internet as they do at home. Of course, as more and more riders use the service, there is less and less bandwidth available for any one person, making the service somewhat less attractive. Wouldn’t it be nice if, before downloading a big file, you knew who would enter and leave a bus when, so you could calculate exactly how much bandwidth you will get over the course of your ride?</p>

<p>You should write a program to help you compute this. You will be given the following data:</p>

<ol>
	<li>The bus line: how many stops there are, and how many seconds between each stop.</li>
	<li>The wireless network: The total bandwidth available is 1 Megabyte per second. For each seat i on the bus, you will be given the proportion ai of the wireless bandwidth it will command. If S is the set of all occupied seats, then seat i ∈ S will get bandwidth a<sub>i</sub>/Σ<sub>j∈S</sub>a<sub>j</sub>. All bandwidths ai for different seats will be different. <br>
	As an example, assume that there are three seats with proportions 3, 2, 1. If the first two seats are occupied, then the person in the first seat gets 3/5 = 60% of the bandwidth, and the other person 2/5 = 40%. If all three seats are occupied, the first person gets 3/6 = 50%, the second person 2/6 = 33.333%, and the third person 1/6 = 16.667%.</li>
	<li>The passengers: at which stations they get on or off the bus (including yourself). Passengers exiting at a station will always get off before anyone entering at that station will get on. Passengers will always take the best (in terms of proportion) available seat when they get on the bus, but will not change seats later if a better seat becomes available. If there is no more space on the bus, the passenger cannot get on. (This may include you.) If multiple passengers get on at the same station, they will try to get on in the order in which our input lists them.</li>
</ol>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line contains four integers n,m,p,y. n is the number of bus stops (2 ≤ n ≤ 100), m the number of seats on the bus (1 ≤ m ≤ 100), and p the number of passengers. 1 ≤ y ≤ p is your number as a passenger.</p>

<p>This is followed by a line with n − 1 integers, giving the time (in seconds) from station i to i + 1. The next line contains m non-negative integers, giving the proportion a<sub>i</sub> of the bandwidth that seat i commands.</p>

<p>This is followed by p lines, each describing one passenger j, by giving two integers, the station s<sub>j</sub> where the passenger gets on, and the station t<sub>j</sub> > s<sub>j</sub> where he gets off. The passengers will be sorted by non-decreasing start stations.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, on a separate line, output the total bandwidth in megabytes you obtained, rounded to two decimals. Each data set should be followed by an empty line.</p>

