# [Bronze II] Dangerous Dive - 13627 

[문제 링크](https://www.acmicpc.net/problem/13627) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>The recent earthquake in Nlogonia did not affect too much the buildings in the capital, which was at the epicenter of the quake. But the scientists found that it affected the dike wall, which now has a significant structural failure in its underground part that, if not repaired quickly, can cause the collapse of the dike, with the consequent flooding the whole capital.</p>

<p>The repair must be done by divers, at a large depth, under extremely difficult and dangerous conditions. But since the survival of the city is at stake, its residents came out in large numbers to volunteer for this dangerous mission.</p>

<p>As is traditional in dangerous missions, each diver received at the start of his/her mission a small card with an identification number. At the end of their mission, the volunteers returned the nameplate, placing it in a repository.</p>

<p>The dike is safe again, but unfortunately it seems that some volunteers did not return from their missions. You were hired for the grueling task of, given the plates placed in the repository, determine which volunteers lost their lives to save the city</p>

### 입력 

 <p>The input is composed of two lines. The first line contains two integers N and R, indicating respectively the number of volunteers that went to the mission and the number of volunteers that returned from the mission. Volunteers are identified by numbers from 1 to N. The second line contains R integers, indicating the volunteers which returned from the mission (at least one volunteer returned).</p>

<p>Restrictions</p>

<p>1 ≤ R ≤ N ≤ 10<sup>4</sup></p>

### 출력 

 <p>Your program must produce a single line containing the identifiers of the volunteers who did not return from their missions, in ascending order of their identifications. Leave a blank space after each identifier (notice that, therefore, there must be a blank space after the last identifier in the line). If every volunteer returned, the line must contain a single character ‘*’ (asterisc).</p>

