# [Silver III] Irregular Expressions (Large) - 12522 

[문제 링크](https://www.acmicpc.net/problem/12522) 

### 성능 요약

메모리: 110836 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘, 문자열

### 제출 일자

2024년 3월 17일 09:20:47

### 문제 설명

<p>You are competing at the 2011 World Witch and Warlock Tournament. In this round of the competition, the Head Witch challenges all contestants to test their spell deflection skills. Contestants stand in a circle, and the Head Witch stands in the center and starts casting spells. The contestants then have to cast counter-spells as quickly as possible. Any contestant who is too slow risks being turned into a toad or petrified.</p>

<p>Each spell that the Head Witch casts consists of three words -- the start, the middle and the end. Each word consists of one or more syllables. The start word is always the same as the end word and consists of at least two syllables. A syllable consists of any number of letters, including exactly one vowel. There are 5 vowels: 'a', 'e', 'i', 'o' and 'u'. All other letters are considered to be consonants, including the letter 'y'.</p>

<p>Examples of valid syllables are "ab", "ra", "cad", "o" and "shabbr". Strings like "ero" and "grrgh" are not valid syllables.</p>

<p>To make things more difficult, the Head Witch speaks very fast, so you cannot easily figure out where one word ends and another one begins. What's worse, she sometimes says some useless gibberish before and after the spell in order to confuse the contestants, or she may not even cast any spell at all and say something completely unrelated instead.</p>

<p>For example, she may say "abracadabra", which is a valid spell because it consists of the words "abra", "cad" and "abra", with the start word and the end word being the same. The word "abra" consists of two syllables -- "ab" and "ra". The word "cad" consists of one syllable -- "cad". (Alternatively, "abra" could also be interpreted as "a-bra" or "abr-a".)</p>

<p>The Head Witch might also say "kajabbamajabbajab", which contains the spell "jabba ma jabba". Or she might say "frufrumfuffle", which is gibberish and does not contain any spells.</p>

<p>For each expression that the Head Witch says, you want to determine quickly whether the expression contains a spell or not. Your molecular integrity depends on it! Fortunately, you have managed to conjure up a computer. Now all you need to do is determine which of the Witch's expressions contain spells.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each one contains an expression, consisting of one or more lower case English letters and no spaces.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>At most 100 characters in each expression.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "Spell!" or "Nothing." (be careful with spelling and punctuation).</p>

