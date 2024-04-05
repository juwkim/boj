# [Silver III] The Killer Word (Small) - 12505 

[문제 링크](https://www.acmicpc.net/problem/12505) 

### 성능 요약

메모리: 112776 KB, 시간: 284 ms

### 분류

구현, 문자열

### 제출 일자

2024년 4월 6일 02:27:35

### 문제 설명

<p>You are playing Hangman with your friend Sean. And while you have heard that Sean is very good at taking candy from a baby, he is not as good at this game. Can you take advantage of Sean's imperfect strategy, and make him lose as badly as possible?</p>

<pre> +--+
 |    O
 |   / | \       Mystery word: _ a _ a _ a _
 |    /  \
 |
+-+---+
</pre>

<p>Hangman is played as follows:</p>

<ul>
	<li>There is a dictionary <strong>D</strong> of all valid words, which both you and Sean know. A word consists only of the characters <code>a</code> - <code>z</code>. In particular, there are no spaces.</li>
	<li>You begin by choosing any word from <strong>D</strong>, and writing it down on a blackboard with each letter replaced by a blank: <code>_</code>.</li>
	<li>On his turn, Sean can choose any letter and ask you if it is in the word. If it is, you reveal <em>all</em> locations of that letter. Otherwise, Sean loses a point.</li>
	<li>Once all letters in the word have been revealed, the round ends.</li>
	<li>The round never ends early, no matter how many points Sean loses.</li>
</ul>

<p>Sean uses a very simple strategy. He makes a list <strong>L</strong> of the 26 letters in some order, and goes through the list one letter at a time. If there is at least one word in <strong>D</strong> that (a) has the letter he is thinking of, and (b) is consistent with what you have written down so far <em>and the result of all of Sean's previous guesses</em>, then Sean guesses that letter. Otherwise, he skips it. No matter what, Sean then moves on to the next letter in his list.</p>

<p>Given Sean's list, what word should you choose to make Sean lose as many as points as possible? If several choices are equally good, you should choose the one that appears first in <strong>D</strong>.</p>

<h3>Example</h3>

<p>Suppose Sean decides to guess the letters in alphabetical order (i.e., <strong>L</strong> = "abcdefghijklmnopqrstuvwxyz"), and <strong>D</strong> contains the words <code>banana</code>, <code>caravan</code>, and<code>pajamas</code>. If you choose <code>pajamas</code>, the game would play out as follows:</p>

<ul>
	<li>You begin by writing 7 blanks <code>_ _ _ _ _ _ _</code> on the blackboard. Based on the number of blanks, Sean knows immediately that the word is either <code>caravan</code> or <code>pajamas</code>.</li>
	<li>Sean begins by guessing <code>a</code> since it is first in <strong>L</strong>, and you reveal all locations of the letter <code>a</code> on the blackboard: <code>_ a _ a _ a _</code>.</li>
	<li>Sean skips <code>b</code> even though it is used in <code>banana</code>. Sean already knows that is not your word. </li>
	<li>He then guesses <code>c</code> because it appears in <code>caravan</code>. It does not appear in the word you actually chose though, so Sean loses a point and nothing more is revealed.</li>
	<li>By process of elimination, Sean now knows your word has to be <code>pajamas</code>, so he proceeds to guess <code>j</code>, <code>m</code>, <code>p</code>, and <code>s</code> in order, without losing any more points.</li>
</ul>

<p>So Sean loses one point if you choose <code>pajamas</code>. He would have gotten either of the other words without losing any points.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with a line containing integers <strong>N</strong> and <strong>M</strong>, representing the number of words in the dictionary and the number of lists to consider.</p>

<p>The next <strong>N</strong> lines contain the words in the dictionary, one per line: <strong>D</strong><sub>1</sub>, <strong>D</strong><sub>2</sub>, ..., <strong>D<sub>N</sub></strong>. Each word is an arbitrary sequence of characters <code>a</code> - <code>z</code>.</p>

<p>The final <strong>M</strong> lines contain all of the lists Sean will use, one per line: <strong>L</strong><sub>1</sub>, <strong>L</strong><sub>2</sub>, ..., <strong>L<sub>M</sub></strong>. Each list is exactly 26 letters long, containing each letter exactly once. Sean will use these lists to guess letters as described above.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 10.</li>
	<li>Each word in <strong>D</strong> will have between 1 and 10 characters inclusive.</li>
	<li>No two words in <strong>D</strong> will be the same within a single test case.</li>
	<li>1 ≤ <strong>N</strong> ≤ 100.</li>
	<li>1 ≤ <strong>M</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: <strong>w</strong><sub>1</sub> <strong>w</strong><sub>2</sub> ... <strong>w</strong><sub><strong>M</strong></sub>", where x is the case number (starting from 1) and <strong>w</strong><sub>i</sub> is the word you should choose if Sean guesses the letters in order <strong>L</strong><sub>i</sub>. If multiple words cause Sean to lose the same number of points, you should choose the option that appears first in the dictionary.</p>

