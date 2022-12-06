# [Bronze III] Breaking Branches - 17783 

[문제 링크](https://www.acmicpc.net/problem/17783) 

### 성능 요약

메모리: 121220 KB, 시간: 100 ms

### 분류

게임 이론(game_theory), 수학(math)

### 문제 설명

<p>Your parents decided that it would be “fun” to spend the entire Sunday walking near the Mookerheide close to Nijmegen.</p>

<p>Although you can pass the time by solving programming problems in your head, your siblings do not have the same luxury. After a short while, your younger sister Alice and your big brother Bob find themselves hopelessly bored. Together, they try to figure out if they can pass the time with a game (a problem that would later be referred to as the Bob and Alice Pastime Conundrum). Finally, they come up with the following simple game.</p>

<p>They find a single branch of length n that will be the main object of the game. Alternatingly, Alice and Bob choose a piece of branch and break it into two parts, in such a way that both parts have integer lengths. The last player who is able to break one of the pieces wins. Alice gets to start, as she is the younger of the two.</p>

<p>Of course, you already have the game figured out in your head. Assuming Bob plays optimally, can Alice win the game? And if so, what move should she make first?</p>

### 입력 

 <ul>
	<li>A line containing a single integer 2 ≤ n ≤ 10<sup>9</sup>, the length of the branch.</li>
</ul>

### 출력 

 <ul>
	<li>On the first line print the name of the person who wins, Alice or Bob.</li>
	<li>If Alice can win, print the length of a piece of branch Alice can break off as a winning move. This should be an integer between 1 and n − 1, inclusive.</li>
</ul>

<p>If there are multiple valid solutions, you may output any one of them.</p>

