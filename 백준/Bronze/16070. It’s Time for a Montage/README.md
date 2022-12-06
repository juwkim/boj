# [Bronze I] It’s Time for a Montage - 16070 

[문제 링크](https://www.acmicpc.net/problem/16070) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>The heroes of your favorite action TV show are preparing for the final confrontation with the villains. Fundamentally, there are two rivals who will fight each other: a very important main hero who wants to save the universe and an equally important main villain who wants to destroy it. However, through countless recursive spin-offs, they may have slightly less important sidekicks (a hero and a villain who are rivals themselves), who in turn may also have their own (even less important) sidekicks, and so on. Note that there is an equal number of heroes and villains, and each rival pair has at most one sidekick pair.</p>

<p>Initially, every character will fight their rival, with the winner being determined by who has the higher Power Level. If a hero and their corresponding villain have the same Power Level, their battle will be determined by their sidekicks’ battle, as the winning sidekick can help as a sort of tiebreaker. (If rivals of equal Power Level do not have sidekicks, the hero character will win with the help of random passersby.) However, whenever a battle is won by either side, there is nothing the sidekicks can do about it – this is because the people behind the show believe some fans might get upset if a character were to get defeated by a bunch of less important characters, so they would lose regardless of the Power Levels.</p>

<p>After the battles between rivals (and possible tiebreakers) are done, the most important character remaining will defeat the rest of the opposing side and determine the fate of the universe. Fortunately, the heroes can ensure victory through hard, rigorous training. For each day they spend training, the Power Level of each hero increases by 1, while the villains’ Power Levels remain constant.</p>

<p>But you already knew all this. The question plaguing your mind is how long the training is going to take.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with an integer n (1 ≤ n ≤ 1 000), giving the number of rival pairs.</li>
	<li>one line with n integers h<sub>1</sub>, . . . , h<sub>n</sub> (1 ≤ h<sub>i</sub> ≤ 1 000 for each i), the i-th value giving the Power Level of the i-th most important hero.</li>
	<li>one line with n integers v<sub>1</sub>, . . . , v<sub>n</sub> (1 ≤ v<sub>i</sub> ≤ 1 000 for each i), the i-th value giving the Power Level of the i-th most important villain.</li>
</ul>

### 출력 

 <p>Output a single integer, the minimum number of days the heroes need to spend training in order for their side to win.</p>

