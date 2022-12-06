# [Bronze I] Figure Skating - 20218 

[문제 링크](https://www.acmicpc.net/problem/20218) 

### 성능 요약

메모리: 29028 KB, 시간: 148 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Figure skating is a very popular sport at the Winter Olympics. It has been on the programme the longest of all winter sports, having even been included in the Summer Olympics before the split in 1924. Just like in gymnastics, each contestant executes a routine consisting of elements, which are individually scored by a jury. This subjective aspect to judging skill always leaves room for heated discussion, but a huge scandal in the 2002 Winter Olympics, with allegations that the game had been fixed, caused a transition to the new scoring system IJS. Points awarded to each element of the routine are known beforehand: A Lutz scores 0.60 points (but 2.10 for a double and 5.90 for a triple), a Salchow scores 0.40 (1.30 for double, 4.30 for triple), an Euler scores 0.50, et cetera. Then, points are added or subtracted by the jury based on execution. Consequently, a figure skater is able to estimate his or her score assuming average performance.</p>

<p>Olympics observers from the Bookmakers' Association for the Prevention of Cheating are tasked with assessing the objectivity of the jury. They will compare the predicted ranking of the contestants with the final outcome to determine who is the jury's favourite. The favourite is the contestant who rose the most places between the predicted and final scoreboard. Ties are broken by whoever ends up higher on the final scoreboard. However, if no one did better than predicted, this raises some red flags with the observers, which is declared "suspicious".</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>A line containing a single integer $n$ ($1 \leq n \leq 1000$), the number of contestants.</li>
	<li>$n$ lines, the $i$th of which contains the name of the contestant who places $i$th on the predicted scoreboard.</li>
	<li>$n$ lines, the $i$th of which contains the name of the contestant who places $i$th on the final scoreboard.</li>
</ul>

<p>Each name consists of at most $100$ lower-case and upper-case alphabetical characters. All names are unique, and occur on both scoreboards exactly once.</p>

### 출력 

 <p>If the scoreboards are suspicious, output "<code>suspicious</code>". Otherwise, output the name of the jury's favourite.</p>

