# [Bronze III] Mult! - 24408 

[문제 링크](https://www.acmicpc.net/problem/24408) 

### 성능 요약

메모리: 30840 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Nora Mainder has a game she plays with her students to help them learn multiplication. She calls out a sequence of numbers and the students have to determine when she names a whole number multiple of the first number. When a student recognizes such a multiple, he or she must call out “Mult!”, ending this round of the game. Then a new round begins with a new initial number. Fortunately her students are very bright and never fail to recognize a multiple, so they all cry out at once—a “multitude” of shouts.</p>

<p>For instance, if she calls out “$8$, $3$, $12$, $6$, $24$,” her students all yell “Mult!” when she reaches $24$ because it is a multiple of the first number, $8$. If she begins a second round of the game with the sequence “$14$, $12$, $9$, $70$,” the class will call out “Mult!” when she reaches $70$, a multiple of the first number, $14$.</p>

<p>Given a sequence of numbers called out by Nora during several rounds of the game, identify which numbers ought to produce a shout of “Mult!”</p>

### 입력 

 <p>The first line of input contains an integer $n$, $2 ≤ n ≤ 1\,000$, the length of the number sequence. The following $n$ lines contains the sequence, one number per line. All numbers in the sequence are positive integers less than or equal to $100$. The sequence is guaranteed to contain at least one complete round of the game (but may end with an incomplete round).</p>

### 출력 

 <p>Print all of the sequence elements that will cause the class to shout “Mult!” Each value should be printed on a separate line.</p>

