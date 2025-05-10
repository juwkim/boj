# [Silver I] Frame by Frame - 11342 

[문제 링크](https://www.acmicpc.net/problem/11342) 

### 성능 요약

메모리: 110908 KB, 시간: 116 ms

### 분류

구현

### 제출 일자

2025년 5월 11일 03:53:56

### 문제 설명

<p>In this problem you will have to decide the final score of a game of bowling. A game of bowling has 10 frames. The tenth frame works in a slightly different way than the first 9.</p>

<p>For the first 9 frames, each will consist of 1 or 2 rolls. You will be presented with 10 pins. If you hit all 10 pins in the first roll you make a “strike”, and the frame is over. Otherwise you have a second roll to hit the remaining pins. If you hit all remaining pins you score a “spare”; otherwise you have an “open frame”. The number of points an open frame gives is simply the total number of pins you hit. A spare gives 10 points plus the number of pins hit on your next roll (in the next frame). A strike gives 10 points plus the number of pins hit on the next two rolls (in the next frame, or possibly the next two frames if you hit a strike in the next roll).</p>

<p>The last frame consists of 2 or 3 rolls. The way it works can be explained as:</p>

<ul>
	<li>10 pins are presented</li>
	<li>If you hit all 10 pins, you score a strike (10 points), and 10 pins are presented again:
	<ul>
		<li>If you hit all 10 pins again, you score a new strike, and 10 pins are presented again, for the last time.
		<ul>
			<li>If you hit 10 pins again, you score one more strike. (1)</li>
			<li>If you hit fewer than 10 pins, you score that number of pins. (2)</li>
		</ul>
		</li>
		<li>If you hit fewer than 10 pins, you score that number of points and the remaining pins are presented.
		<ul>
			<li>If you hit all remaining pins, you score a spare (10 points). (3)</li>
			<li>If you hit fewer than that, you score that many pins. (4)</li>
		</ul>
		</li>
	</ul>
	</li>
	<li>If you hit fewer than 10 pins on the first roll, the remaining pins are presented.
	<ul>
		<li>If you hit all remaining pins, you score a spare and 10 pins are presented again.
		<ul>
			<li>If you hit all 10 pins on the third roll, you score a strike. (5)</li>
			<li>If you hit fewer than 10 pins, you score as many points as pins hit. (6)</li>
		</ul>
		</li>
		<li>If you hit fewer than the remaining pins, you score the number of pins hit in both rolls. (7)</li>
	</ul>
	</li>
</ul>

<p>Note that the number of points in the last frame is the total number of pins hit in all rolls.</p>

<p>Your job is to compute the total score for a game of bowling given the scores for each of ten frames. A strike is represented by an “X”, a spare is represented by the number of pins hit in the first roll followed by a slash (“/”) and an open frame is represented by 2 numbers: the number of pins hit in each roll. Similarly, the tenth frame is represented either as: (1) “X X X”, or (2) “X X a”, or (3) “X a /” or (4) “X a b” or (5) “a / X” or (6) “a / b” or (7) “a b”, where a and b are numbers.</p>

### 입력 

 <p>Your program must read the notated scores for each of a set of games (preceded by the number of games) and compute the total scores. Note that the frames are not delimited in any way---it’s your job to figure out if a frame has one, two, or three rolls.</p>

### 출력 

 <p>Print the total scores.</p>

