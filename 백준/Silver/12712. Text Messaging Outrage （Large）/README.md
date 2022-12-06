# [Silver IV] Text Messaging Outrage (Large) - 12712 

[문제 링크](https://www.acmicpc.net/problem/12712) 

### 성능 요약

메모리: 114488 KB, 시간: 132 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Professor Loony, a dear friend of mine, stormed into my office. His face was red and he looked very angry. The first thing that came out of his mouth was "Damn those phone manufacturers. I was trying to send a text message, and it took me more than ten minutes to type a one-line message." I tried to calm him down. "But what is wrong? Why did it take you so long?" He continued, "Don't you see?! Their placement of the letters is so messed up? Why is 's' the 4th letter on its key? and 'e'? Why is it not the first letter on its key? I have to press '7' FOUR times to type an 's'? This is lunacy!"</p>

<p>"Calm down, my friend," I said, "This scheme has been in use for so long, even before text messaging was invented. They had to keep it that way."</p>

<p>"That's not an excuse," his face growing redder and redder. "It is time to change all this. It was a stupid idea to start with. And while we are at it, how come they only put letters on 8 keys? Why not use all 12? And why do they have to be consecutive?"</p>

<p>"Umm... I... don't... know," I replied.</p>

<p>"Ok, that's it. Those people are clearly incompetent. I am sure someone can come up with a better scheme."</p>

<p>He was one of <em>those</em> people, I could see. People who complain about the problem, but never actually try to solve it. </p>

<p>In this problem, you are required to come up with the best letter placement of keys to minimize the number of key presses required to type a message. You will be given the number of keys, the maximum number of letters we can put on every key, the total number of letters in the alphabet, and the frequency of every letter in the message. Letters can be placed anywhere on the keys and in any order. Each letter can only appear on one key. Also, the alphabet can have more than 26 letters (it is not English).</p>

<p>For reference, the current phone keypad looks like this</p>

<pre>key 2: abc
key 3: def
key 4: ghi
key 5: jkl
key 6: mno
key 7: pqrs
key 8: tuv
key 9: wxyz
</pre>

<p>The first press of a key types the first letter. Each subsequent press advances to the next letter. For example, to type the word "snow", you need to press "7" four times, followed by "6" twice, followed by "6" three times, followed by "9" once. The total number of key presses is 10.</p>

### 입력 

 <p>The first line in the input file contains the number of test cases <strong>N</strong>. This is followed by <strong>N</strong>cases. Each case consists of two lines. On the first line we have the maximum number of letters to place on a key (<strong>P</strong>), the number of keys available (<strong>K</strong>) and the number of letters in our alphabet (<strong>L</strong>) all separated by single spaces. The second line has <strong>L</strong> non-negative integers. Each number represents the frequency of a certain letter. The first number is how many times the first letter is used, the second number is how many times the second letter is used, and so on.</p>

<p>Limits</p>

<ul>
	<li><strong>P</strong> * <strong>K</strong> ≥ <strong>L</strong> </li>
	<li>0 ≤ The frequency of each letter ≤ 1 000 000</li>
	<li>1 ≤ <strong>N</strong> ≤ 100</li>
	<li>1 ≤ <strong>P</strong> ≤ 1 000</li>
	<li>1 ≤ <strong>K</strong> ≤ 1 000</li>
	<li>1 ≤ <strong>L</strong> ≤ 1 000</li>
</ul>

### 출력 

 <p>For each case, you should output the following</p>

<pre>Case #x: [minimum number of keypad presses]
</pre>

<p>indicating the number of keypad presses to type the message for the optimal layout.</p>

