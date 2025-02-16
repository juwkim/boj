# [Silver II] Countries - 3369 

[문제 링크](https://www.acmicpc.net/problem/3369) 

### 성능 요약

메모리: 111276 KB, 시간: 128 ms

### 분류

그래프 이론, 구현

### 제출 일자

2025년 2월 16일 16:01:10

### 문제 설명

<p>This problem considers how mighty countries arise from humble beginnings. Consider a two-dimensional map of the area. On this map there are n cities. Each city i is in a distinct location with coordinates (x<sub>i</sub>, y<sub>i</sub>) on the map. The city has also a number s<sub>i</sub> of soldiers in it under the command of a general.</p>

<p>The influence city i exerts to another location (x, y) is computed as s<sub>i</sub> divided by the squared distance between it and (x, y). It is as if the mass of soldiers in city i exerted a gravitational pull to all map locations around it. City i is threatened by another city j if the influence exerted by city j on the location (x<sub>i</sub>, y<sub>i</sub>) of city i exceeds its number of soldiers s<sub>i</sub>: then city j can dispatch enough soldiers to overpower all the soldiers defending city i. If city i is not threatened by any other city j, then its grateful citizens elect its invincible general as their king, and turn their city into the capital of his kingdom.</p>

<p>On the other hand, if some city j threatening city i exerts strictly more influence on its location (x<sub>i</sub>, y<sub>i</sub>) than any other city k, then the citizens of city i have no choice: city i must surrender to city j. Henceforth city i must obey the same capital as city j obeys; however, the s<sub>i</sub> soldiers in city i do not join the army of city j or the capital. Otherwise city i is saved by mutual distrust of the equally threatening cities j and k: If one of them would attack and overpower city i, then the other would in turn attack and overpower the battle-weary first attackers. However, the citizens of city i can no longer elect its general as their king, because he has failed in his duty to keep the city safe from threats. Thus they must turn their city into the capital of a democracy instead.</p>

<p>Your task is to write a program, which takes the information about the cities on the map as inputs, and outputs for each city i one of the three outcomes:</p>

<ul>
	<li>It is the capital of a kindgom.</li>
	<li>It is the capital of a democracy.</li>
	<li>It obeys city j as its capital.</li>
</ul>

### 입력 

 <p>The first line consists of one integer 1 ≤ n ≤ 1000, the number of cities. The following n lines give the information on the n cities, each city as its own line. Line i + 1 gives the information on city i as the three integers x<sub>i</sub>, y<sub>i</sub>, s<sub>i</sub> which are separated by single space characters. All these numbers are in range 0 ≤ x<sub>i</sub>, y<sub>i</sub>, s<sub>i</sub> ≤ 1000.</p>

### 출력 

 <p>The output consists of n lines, where line i consists of the outcome for city i:</p>

<ul>
	<li>The character <code>K</code> if city i is the capital of a kingdom.</li>
	<li>The character <code>D</code> if city i is the capital of a democracy.</li>
	<li>The number 1 ≤ j ≤ n of the city which city i obeys as its capital if city i had to surrender.</li>
</ul>

