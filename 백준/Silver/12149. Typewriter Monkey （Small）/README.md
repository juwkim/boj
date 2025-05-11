# [Silver I] Typewriter Monkey (Small) - 12149 

[문제 링크](https://www.acmicpc.net/problem/12149) 

### 성능 요약

메모리: 114820 KB, 시간: 2036 ms

### 분류

브루트포스 알고리즘, 문자열

### 제출 일자

2025년 5월 12일 02:28:25

### 문제 설명

<p>Your publishing house has decided to use monkeys randomly typing at keyboards to write great works of literature. You are the supervisor for one monkey with a keyboard containing <strong>K</strong> keys, each of which is labeled with an uppercase English letter. (There may be multiple keys displaying the same letter.) The monkey will start with an empty string and repeat the following <strong>S</strong> times: choose a key from its keyboard uniformly at random and press it, adding a copy of that key's letter to the right end of the string. The final resulting string will have length <strong>S</strong>.<br>
<br>
You have a <em>target word</em> of length <strong>L</strong> that you are hoping the monkey will type. (The target word will not necessarily be a real English word.) This target word may even appear multiple times in what the monkey types. (Overlapping instances count too -- for example, if "ABA" is the target word and the monkey types "ABABA", that contains two instances of the target.)<br>
<br>
You plan to pay the monkey one banana for each instance of the target word that it types. When you go to inspect the monkey's work, you will bring along the minimum number of bananas that you need to <em>ensure</em> that you will always have enough bananas to pay the monkey, no matter what it has typed. Then, you will pay the monkey one banana for each instance of the target word that it <em>actually</em> typed. You will keep the remaining bananas that you brought with you.<br>
<br>
What is the expected number of bananas that you will get to keep?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each consists of three lines. The first contains three space-separated positive integers: <strong>K</strong>, <strong>L</strong>, and <strong>S</strong>. The second contains a string of <strong>K</strong> uppercase English letters representing the monkey's keyboard. The third contains a string of <strong>L</strong> uppercase English letters representing the target word.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>K</strong> ≤ 7.</li>
	<li>1 ≤ <strong>L</strong> ≤ <strong>S</strong> ≤ 7.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where y is the expected number of bananas you will get to keep after paying the monkey.</p>

<p>y will be considered correct if it is within an absolute or relative error of 10<sup>-6</sup> of the correct answer.</p>

