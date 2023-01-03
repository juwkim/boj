# [Silver IV] Mountain Watching - 6053 

[문제 링크](https://www.acmicpc.net/problem/6053) 

### 성능 요약

메모리: 115632 KB, 시간: 268 ms

### 분류

애드 혹(ad_hoc)

### 문제 설명

<p>One day, Bessie was gazing off into the distance at the beautiful  Wisconsin mountains when she wondered to herself: which is the widest one?</p>

<p>She decided to take N (1 <= N <= 10,000) height measurements H_i (1 <= H_i <= 1,000,000,000) sequentially along the horizon using her new Acme Long Distance Geoaltimeter. </p>

<p>A mountain is defined to be a consecutive sequence of H_i values which increases (or stays the same) and then decreases (or stays the same), e.g., 2, 3, 3, 5, 4, 4, 1. It is possible for a mountain on the edge of her field of vision only to increase or only to decrease in height, as well.</p>

<p>The width of a mountain is the number of measurements it encompasses. Help Bessie identify the widest mountain.</p>

<p>Here's a simple example of a typical horizon:</p>

<pre>           *******                   *
          *********                 ***
          **********               *****
          ***********           *********               *
*      *****************       ***********             *** *
**    *******************     *************   * *     *******      *
**********************************************************************
?ddsssuussuussssssddddssddssssuuuuuuuuddddddssududssssuuudduddsssssuds
3211112333677777776543332111112344456765432111212111112343232111111211
aaaaa                     cccccccccccccccccccc eeeeeee    ggggggggg
  bbbbbbbbbbbbbbbbbbbbbbbbbbbb             ddddd ffffffffff  hhhhhhhhh</pre>

<p>The mountains are marked 'a', 'b', etc.  Obviously, mountain b is widest with width 28.</p>

<p>Hint: Sometimes it's easiest to find a mountain's width by knowing where its highest parts are.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains a single integer: H_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single line with a single integer that is the width of the widest mountain.</li>
</ul>

<p> </p>

