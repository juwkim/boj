# [Silver IV] Rhyming Slang - 13527 

[문제 링크](https://www.acmicpc.net/problem/13527) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

구현

### 문제 설명

<p>Rhyming slang involves replacing a common word with a phrase of two or three words, the last of which rhymes with the original word. For example,</p>

<ul>
	<li>replacing the word “stairs” with the rhyming phrase “apples and pears”,</li>
	<li>or replacing “rotten” with the phrase “bales of cotton”.</li>
</ul>

<p>English has such a wide variety of spellings and pronunciations that for any non-native speaker telling what rhymes isn’t always easy. Perhaps you can help?</p>

<p>Typically, two words rhyme (or can be forced to rhyme) if both of their endings can be found on the same list of word endings that sound the same.</p>

<p>Given a common word, a number of lists, each containing word endings that sound the same, and a number of phrases, determine if those phrases could be rhyming slang.</p>

### 입력 

 <ul>
	<li>One line containing the single common word S (1 ≤ |S| ≤ 20).</li>
	<li>One line containing an integer E (1 ≤ E ≤ 10), the number of lists of word endings that sound the same.</li>
	<li>E lines, each no more than 100 characters long. Each a list of space-separated word endings.</li>
	<li>One line containing an integer P (1 ≤ P ≤ 10), the number of phrases to test.</li>
	<li>P lines, each no more than 100 characters long, containing a phrase p<sub>i</sub> of two or three words that might rhyme with the common word.</li>
</ul>

<p>All words and letters will be in lower case. The common word’s ending will appear in at least one ending list.</p>

### 출력 

 <ul>
	<li>P lines, each consisting of either:
	<ul>
		<li>’YES’: The phrase p<sub>i</sub> rhymes with the common word.</li>
		<li>’NO’: The phrase p<sub>i</sub> does not rhyme with the common word.</li>
	</ul>
	</li>
</ul>

