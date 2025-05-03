# [Silver I] House Lawn - 16322 

[문제 링크](https://www.acmicpc.net/problem/16322) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 파싱, 문자열

### 제출 일자

2025년 5월 3일 16:30:23

### 문제 설명

<p>You have just bought a new house, and it has a huge, beautiful lawn. A lawn that needs cutting. Several times. Every week. The whole summer.</p>

<p>After pushing the lawnmower around the lawn during the hottest Saturday afternoon in history, you decided that there must be a better way. And then you saw the ads for the new robotic lawnmovers. But which one should you buy? They all have different cutting speeds, cutting times and recharge times, not to mention different prices!</p>

<p>According to the advertisement, a robotic lawnmover will spend all its time either cutting the lawn or recharging its battery. Starting from a full battery, it will cut the lawn at a given rate of c square meters per minute for a cutting time of t minutes, after which it has run out of battery. Once out of battery, it will immediately start recharging. After recharging for r minutes the battery is full again and it immediately starts cutting.</p>

<p>You decide that in order for your lawn to look sufficiently prim and proper, the lawnmower that you buy must be powerful enough to cut your whole lawn at least once a week on average. Formally, if we start the mower fully charged at the beginning of the week and run it for exactly T weeks, it needs to cut the whole lawn at least T times, for all positive integers T. But apart from this, you have no specific requirements, so among the ones that satisfy this requirement, you will simply go for the cheapest option. For the purposes of cutting your lawn, you may make the simplifying assumption that a week is always exactly 10 080 minutes long.</p>

### 입력 

 <p>The first line of input contains two integers ℓ and m (1 ≤ ℓ ≤ 10<sup>6</sup>, 1 ≤ m ≤ 100), the size of your lawn in square meters, and the number of lawnmowers to consider, respectively. Then follow m lines, each containing a string n and 4 integers p, c, t, and r, separated by commas, describing a lawnmower as follows:</p>

<ul>
	<li>n is the name of the lawnmower, a string of at most 60 printable characters (ASCII 32 to 126) excluding ‘,’, neither starting nor ending with a space,</li>
	<li>1 ≤ p ≤ 100 000 is the price of the lawnmover,</li>
	<li>1 ≤ c ≤ 100 is the cutting rate in square meters per minute,</li>
	<li>1 ≤ t ≤ 10 080 is the cutting time in minutes, and</li>
	<li>1 ≤ r ≤ 10 080 is the recharge time in minutes.</li>
</ul>

### 출력 

 <p>Output the name of the cheapest lawnmower capable of cutting your whole yard at least once a week on average. If several lawnmovers share the same lowest price, output all of their names, in the same order they were given in the input. If there is no such mower, output “<code>no such mower</code>”.</p>

