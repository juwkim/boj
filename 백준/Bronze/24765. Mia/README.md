# [Bronze II] Mia - 24765 

[문제 링크](https://www.acmicpc.net/problem/24765) 

### 성능 요약

메모리: 30840 KB, 시간: 180 ms

### 분류

많은 조건 분기(case_work), 구현(implementation)

### 문제 설명

<p>Mia is a dice game for two players. Each roll consist of two dice. Mia involves bluffing about what a player has rolled, but in this problem we focus only on its scoring rules. Unlike most other dice games, the score of a roll is not simply the sum of the dice.</p>

<p>Instead, a roll is scored as follows:</p>

<ul>
	<li>Mia (12 or 21) is always highest.</li>
	<li>Next come doubles (11, 22, and so on). Ties are broken by value, with 66 being highest.</li>
	<li>All remaining rolls are sorted such that the highest number comes first, which results in a two-digit number. The value of the roll is the value of that number, e.g. 3 and 4 becomes 43.</li>
</ul>

### 입력 

 <p>The input will contain multiple test cases. Each test case contains on a single line four integer numbers s<sub>0</sub> s<sub>1</sub> r<sub>0</sub> r<sub>1</sub> where s<sub>0</sub> s<sub>1</sub> represent the dice rolled by player 1 and r<sub>0</sub> r<sub>1</sub> represents the dice rolled by player 2. The input will be terminated by a line containing 4 zeros.</p>

### 출력 

 <p>For each test case, output which player won, or whether there was a tie, using exactly the format shown below.</p>

