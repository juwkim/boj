# [Silver III] Polynesiaglot (Small2) - 12038 

[문제 링크](https://www.acmicpc.net/problem/12038) 

### 성능 요약

메모리: 28776 KB, 시간: 92 ms

### 분류

조합론(combinatorics), 다이나믹 프로그래밍(dp), 수학(math)

### 문제 설명

<p>Ursula is a big fan of constructing artificial languages. Today, she is starting to work on a language inspired by real Polynesian languages. The only rules she has established are:</p>

<ul>
	<li>All words consist of letters. Letters are either consonants or vowels.</li>
	<li>Any consonant in a word must be immediately followed by a vowel.</li>
</ul>

<p>For example, in a language in which <em>a</em> is the only vowel and <em>h</em> is the only consonant, <em>a</em>, <em>aa</em>, <em>aha</em>, <em>aaha</em>, and <em>haha</em> are valid words, whereas <em>h</em>, <em>ahh</em>, <em>ahah</em>, and <em>ahha</em> are not. Note that the rule about consonants disallows ending a word in a consonant as well as following a consonant with another consonant.</p>

<p>If Ursula's new language has <strong>C</strong> different consonants and <strong>V</strong> different vowels available to use, then how many different valid words of length <strong>L</strong> are there in her language? Since the output can be a really big number, we only ask you to output the remainder of dividing the result by the prime 10<sup>9</sup>+7 (1000000007).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each consists of one line with three integers <strong>C</strong>, <strong>V</strong>, and <strong>L</strong>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>C</strong> ≤ 50.</li>
	<li>1 ≤ <strong>V</strong> ≤ 50.</li>
	<li>1 ≤ <strong>L</strong> ≤ 15.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of different valid words of length <strong>L</strong> in the language, modulo the prime 10<sup>9</sup>+7 (1000000007).</p>

