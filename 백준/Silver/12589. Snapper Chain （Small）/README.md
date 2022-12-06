# [Silver V] Snapper Chain (Small) - 12589 

[문제 링크](https://www.acmicpc.net/problem/12589) 

### 성능 요약

메모리: 117216 KB, 시간: 676 ms

### 분류

비트마스킹(bitmask), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>The <em>Snapper</em> is a clever little device that, on one side, plugs its input plug into an output socket, and, on the other side, exposes an output socket for plugging in a light or other device.</p>

<p>When a <em>Snapper</em> is in the ON state and is receiving power from its input plug, then the device connected to its output socket is receiving power as well. When you snap your fingers -- making a clicking sound -- any <em>Snapper</em> receiving power at the time of the snap toggles between the ON and OFF states.</p>

<p>In hopes of destroying the universe by means of a singularity, I have purchased <strong>N</strong><em>Snapper</em> devices and chained them together by plugging the first one into a power socket, the second one into the first one, and so on. The light is plugged into the <strong>N</strong>th <em>Snapper</em>.</p>

<p>Initially, all the <em>Snapper</em>s are in the OFF state, so only the first one is receiving power from the socket, and the light is off. I snap my fingers once, which toggles the first <em>Snapper</em> into the ON state and gives power to the second one. I snap my fingers again, which toggles both <em>Snapper</em>s and then promptly cuts power off from the second one, leaving it in the ON state, but with no power. I snap my fingers the third time, which toggles the first <em>Snapper</em>again and gives power to the second one. Now both <em>Snapper</em>s are in the ON state, and if my light is plugged into the second <em>Snapper</em> it will be <em>on</em>.</p>

<p>I keep doing this for hours. Will the light be <em>on</em> or <em>off</em> after I have snapped my fingers <strong>K</strong>times? The light is <em>on</em> if and only if it's receiving power from the <em>Snapper</em> it's plugged into.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each one contains two integers, <strong>N</strong> and <strong>K</strong>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 10,000.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10;</li>
	<li>0 ≤ <strong>K</strong> ≤ 100;</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "ON" or "OFF", indicating the state of the light bulb.</p>

