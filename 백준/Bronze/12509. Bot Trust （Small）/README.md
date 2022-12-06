# [Bronze I] Bot Trust (Small) - 12509 

[문제 링크](https://www.acmicpc.net/problem/12509) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>Blue and Orange are friendly robots. An evil computer mastermind has locked them up in separate hallways to test them, and then possibly give them cake.</p>

<p>Each hallway contains 100 buttons labeled with the positive integers {1, 2, ..., 100}. Button k is always k meters from the start of the hallway, and the robots both begin at button 1. Over the period of one second, a robot can walk one meter in either direction, or it can press the button at its position once, or it can stay at its position and not press the button. To complete the test, the robots need to push a certain sequence of buttons in a certain order. Both robots know the full sequence in advance. How fast can they complete it?</p>

<p>For example, let's consider the following button sequence:</p>

<p><code>   O 2, B 1, B 2, O 4</code></p>

<p>Here, <code>O 2</code> means button 2 in Orange's hallway, <code>B 1</code> means button 1 in Blue's hallway, and so on. The robots can push this sequence of buttons in 6 seconds using the strategy shown below:</p>

<pre>Time | Orange                  | Blue
-----+------------------+-----------------
  1      | Move to button 2 | Stay at button 1
  2     | Push button 2       | Stay at button 1
  3     | Move to button 3  | Push button 1
  4     | Move to button 4  | Move to button 2
  5     | Stay at button 4    | Push button 2
  6     | Push button 4       | Stay at button 2
</pre>

<p>Note that Blue has to wait until Orange has completely finished pushing <code>O 2</code> before it can start pushing <code>B 1</code>.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow.</p>

<p>Each test case consists of a single line beginning with a positive integer <strong>N</strong>, representing the number of buttons that need to be pressed. This is followed by <strong>N</strong> terms of the form "<strong>R</strong><sub>i</sub><strong>P</strong><sub>i</sub>" where <strong>R</strong><sub>i</sub> is a robot color (always 'O' or 'B'), and <strong>P</strong><sub>i</sub> is a button position.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>P</strong><sub>i</sub> ≤ 100 for all i.</li>
	<li>1 ≤ <strong>T</strong> ≤ 20.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the minimum number of seconds required for the robots to push the given buttons, in order.</p>

