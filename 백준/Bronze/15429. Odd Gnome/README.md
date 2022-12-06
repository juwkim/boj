# [Bronze III] Odd Gnome - 15429 

[문제 링크](https://www.acmicpc.net/problem/15429) 

### 성능 요약

메모리: 28776 KB, 시간: 84 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>According to the legend of Wizardry and Witchcraft, gnomes live in burrows underground, known as gnome holes. There they dig up and eat the roots of plants, creating little heaps of earth around gardens, causing considerable damage to them.</p>

<p>Mrs. W, very annoyed by the damage, has to regularly de-gnome her garden by throwing the gnomes over the fence. It is a lot of work to throw them one by one because there are so many. Fortunately, the species is so devoted to their kings that each group always follows its king no matter what. In other words, if she were to throw just the king over the fence, all the other gnomes in that group would leave.</p>

<p>So how does Mrs. W identify the king in a group of gnomes? She knows that gnomes travel in a certain order, and the king, being special, is always the only gnome who does not follow that order.</p>

<p>Here are some helpful tips about gnome groups:</p>

<ul>
	<li>There is exactly one king in a group.</li>
	<li>Except for the king, gnomes arrange themselves in strictly increasing ID order.</li>
	<li>The king is always the only gnome out of that order.</li>
	<li>The king is never the first nor the last in the group, because kings like to hide themselves.</li>
</ul>

<p>Help Mrs. W by finding all the kings!</p>

### 입력 

 <p>The input starts with an integer n, where 1 ≤ n ≤ 100, representing the number of gnome groups. Each of the n following lines contains one group of gnomes, starting with an integer g, where 3 ≤ g ≤ 1 000, representing the number of gnomes in that group. Following on the same line are g space-separated integers, representing the gnome ordering. Within each group all the integers (including the king) are unique and in the range [0, 10 000]. Excluding the king, each integer is exactly one more than the integer preceding it.</p>

### 출력 

 <p>For each group, output the king’s position in the group (where the first gnome in line is number one).</p>

