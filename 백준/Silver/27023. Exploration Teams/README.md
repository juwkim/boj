# [Silver II] Exploration Teams - 27023 

[문제 링크](https://www.acmicpc.net/problem/27023) 

### 성능 요약

메모리: 111276 KB, 시간: 312 ms

### 분류

브루트포스 알고리즘, 비트마스킹

### 제출 일자

2025년 6월 15일 02:51:38

### 문제 설명

<p>The cows want to form an expeditionary team to explore the wooded area at the edge of Farmer John's territory.  Exploring turns out to be an activity that requires more skill than just standing in the pasture and grazing.</p>

<p>The team of C (1 ≤ C ≤ 20) cows numbered 1..C must include cows that are able to navigate through the woods without getting lost, fend off big nasty creatures, tell jokes to keep the morale high, etc.  At least one cow on the team must possess each of these A (1 ≤ A ≤ 20) special abilities numbered 1..A.  Some cows have only one ability, but many have multiple abilities; some cows are just freeloaders who are completely useless.</p>

<p>Given a list of all the cows and the abilities of each cow, compute the number of different exploration teams that the cows can form, such that the team as a whole has all the given abilities.</p>

### 입력 

 <ul>
	<li>Line 1: Two integers, C and A</li>
	<li>Lines 2..A+1: Each line contains a set of space-separated integers describing an ability.  Line 2 describes ability 1; line 3 describes ability 2; etc.  The first integer on each line, K (1 ≤ K ≤ C), is the number of cows with this ability. The following K integers represent the cows who have the ability.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: An integer representing the number of different exploration teams that the cows can form.</li>
</ul>

