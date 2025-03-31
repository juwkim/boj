# [Silver II] Mathemagicians - 17890 

[문제 링크](https://www.acmicpc.net/problem/17890) 

### 성능 요약

메모리: 110776 KB, 시간: 100 ms

### 분류

애드 혹, 많은 조건 분기, 구현, 문자열

### 제출 일자

2025년 3월 31일 14:17:47

### 문제 설명

<p>There are n mathemagicians standing in a circle. Each mathemagician wears either a blue hat or a red hat. A mathemagician can cast a color change charm which changes the color of their hat to the same color as the hat of the mathemagician directly to the left or to the right of them (the caster of the spell may choose which one of them). Note that mathemagicians are polite people and do not like interrupting each other, so only one mathemagician at a time may perform mathemagic.</p>

<p>The mathemagicians are not happy with their current hat configuration, so they would like to use the color change charm repeatedly to enter another hat configuration. Time isn’t an issue because they can conjure cookies to eat.</p>

### 입력 

 <p>The first line contains an integer n (3 ≤ n ≤ 105 ), the number of mathemagicians. The next contains a string of length n. If the ith mathemagician wears a blue hat in the beginning, the ith character of the string is ‘B’, otherwise the ith character is ‘R’. Finally, the third line contains a string of length n. If the ith mathemagician would like to wear a blue hat in the end, the ith character of the string is ‘B’, otherwise the ith character is ‘R’.</p>

<p>It is guaranteed that not every mathemagician is happy with their hat color in the beginning.</p>

### 출력 

 <p>Output “yes” if it is possible for the mathemagicians to achieve the desired hat configuration after a finite number of color change charms, otherwise output “no”.</p>

