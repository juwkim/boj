# [Silver III] Magic Trick - 7550 

[문제 링크](https://www.acmicpc.net/problem/7550) 

### 성능 요약

메모리: 166764 KB, 시간: 256 ms

### 분류

구현, 파싱, 시뮬레이션, 문자열

### 제출 일자

2024년 4월 17일 03:29:22

### 문제 설명

<p>Warning! This problem statement contains a serious spoiler. It shows the trick behind a magic trick. So if you still want to be amazed in case somebody shows this trick to you then do NOT read the rest of this problem statement. Stop reading... NOW!</p>

<p>Well, you’re still reading, so obviously you have no respect for magic tricks. Be ashamed, please. Ok, here’s what happens. The magician shows you a text with three paragraphs like this one:</p>

<pre>It was a horribly dark night.
The moon was shining, but not much.

A suspicious stranger entered the
bar and went straight to John Doe.

"I’m searching for aliens, can I
borrow your computer?", he said.</pre>

<p>He then asks you to secretly pick a word in the first paragraph. Then you shall do this:</p>

<ol>
	<li>Count the number of characters in your word (call that number X).</li>
	<li>From your word move on X words.</li>
</ol>

<p>Repeat these two steps until you reach the third paragraph. Then tell the magician that you’re done. After some hocus pocus he tells you the word you ended up with.</p>

<p>For our purposes, a “word” is defined as consecutive letters (A-Z,a-z). For example, “I’m” is regarded as two separate words.</p>

<p>For example, let’s say you choose “night” in the above example. It has 5 characters, so you move on five words: “The”, “moon”, “was”, “shining”, “but”. Our new word is “but”. You move on 3 words to “A”, then 1 to “suspicious”, then 10 to “Doe” and then 3 to “searching”. Now you tell the magician that you’re ready. He says that you’ve reached “searching”.</p>

<p>How can he know? Well, it doesn’t matter where you start in the first paragraph, you’ll always end up at “searching”. The magician needs new texts and asks you to help him to find all possible outcomes (in the above example, “searching” is the only one). Apart from words, a possible outcome is “-outside-”, which means it’s possible to jump behind the third paragraph. Also, he’s not interested if more than three outcomes are possible.</p>

### 입력 

 <p>The first line contains the number of scenarios. For each scenario, three lines are given, representing the three paragraphs. No line is longer than 100000 characters. Every paragraph will contain at least one word.</p>

### 출력 

 <p>The output for every scenario begins with a line containing “Scenario #i:”, where i is the number of the scenario starting at 1. Then print the possible outcomes (possibly including “-outside-”) in alphabetical/lexicographical order, one word per line. Write words in lower case. Don’t list outcomes more than once. If however there are more than three possible outcomes, then print “-too many-” and do *not* print any of them. Terminate the output for the scenario with a blank line.</p>

