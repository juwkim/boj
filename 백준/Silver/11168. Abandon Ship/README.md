# [Silver III] Abandon Ship - 11168 

[문제 링크](https://www.acmicpc.net/problem/11168) 

### 성능 요약

메모리: 112588 KB, 시간: 160 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 시뮬레이션

### 제출 일자

2025년 3월 12일 03:19:43

### 문제 설명

<p>As a Starph1337 Captain, you know that the list of tasks on a starship can be long. Even on the flagship of the International Planet of Federations, a lot of things need to be taken care of during battle: power needs to be diverted, matrices need to be re-inverted, and some day you might have to get to those well-decorated emergency escape pods. A brand new software program with the somewhat cumbersome and long yet completely informative name of CaptainsLogStardate41254.7TheseAreTheVoyagesOfTheStarship (Enterprise Edition) is under development. The first version should support giving orders during battle. There are three types of systems that should be supported:</p>

<ul>
	<li>Category I: Systems will simply go out of whack once in a while. When they do, recalibrate them!</li>
	<li>Category II: Systems will suddenly (and for no apparent reason) no longer be usable in their current state. Invert them, or re-invert them, as needed. While you take care of these systems, the engineers are grepping the source code for do_damage_to_self.</li>
	<li>Category III: Life-critical. Divert power to them if you can, or abandon ship! You have 20 units of extra power.</li>
</ul>

### 입력 

 <p>The first line of input will be T, the number of cases. T cases follow.</p>

<p>The first line of each case will be four numbers A, B, C, D, separated by spaces. The first three numbers will be the number of systems in Category I, II and III, respectively. The fourth number is the number of damaged systems.</p>

<p>After this line follow A lines with the names of Category I systems, B lines with the names of Category II systems, C lines with Category III systems, and then D lines with names of damaged systems (in the order they were damaged).</p>

<ul>
	<li>0 ≤ T ≤ 100</li>
	<li>0 ≤ A, B, C, D ≤ 100</li>
	<li>Each system name will start and end with a lowercase letter a - z.</li>
	<li>Each system name will consists of between 2 and 22 characters, and only lowercase letters a-z and spaces.</li>
</ul>

<p>Given a SYSTEM, the orders will be one of the following:</p>

<ul>
	<li>recalibrate SYSTEM</li>
	<li>invert SYSTEM</li>
	<li>re-invert SYSTEM</li>
	<li>divert all power to SYSTEM</li>
	<li>ABANDON SHIP. REPEAT. ALL HANDS ABANDON SHIP.</li>
</ul>

### 출력 

 <p>For each damage, output the correct order that should be given to your crew. Category I systems will always need to be recalibrated when they are damaged, hence, output <code>recalibrate [system name]</code>. Category II systems will need to be inverted the first time they are damaged, then re-inverted the next time, then inverted again, and so on. Output <code>invert [system name]</code> or <code>re-invert [system name]</code> as needed. Category III systems start with 100 units of power and will lose 10 units for each damage taken.</p>

<p>The ship has 20 units of extra power in total that can be diverted to these damaged systems. Output <code>divert all power to [system name]</code>. As long as the system is still alive, give the order to divert extra power (even if the 20 extra units has been diverted). Whenever you divert power, your crew will use as much as they need to get it back to 100 units. When a life-critical (Category III) system’s power is 10 units or less, give the order to abandon ship by outputting <code>ABANDON SHIP. REPEAT. ALL HANDS ABANDON SHIP.</code> to your crew and terminate the case (do not give further orders after this). All orders need to be in lower case except for the abandon ship order, which needs to be in upper case and with the punctuation exactly as written.</p>

