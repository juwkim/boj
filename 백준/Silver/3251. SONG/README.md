# [Silver IV] SONG - 3251 

[문제 링크](https://www.acmicpc.net/problem/3251) 

### 성능 요약

메모리: 108080 KB, 시간: 124 ms

### 분류

문자열

### 제출 일자

2023년 10월 26일 06:29:48

### 문제 설명

<p>A song consists of one or more verses, and each verse consists of four lines. Each line consists of one or more words separated by single blank character, and finally, each word consists of one or more letters (a-z, A-Z).</p>

<p>We define the last syllable of a word to be the sequence of letters from the last vowel (inclusively) to the end of the word. If a word has no vowel, then the last syllable is the word itself.</p>

<p>We say that two lines rhyme if they have same last syllables (ignoring the letter case). Verse can have perfect rhyme, even rhyme, cross rhyme, shell rhyme or there can be no rhyme at all (free rhyme).</p>

<p>Verse has a perfect rhyme if all lines in a verse mutually rhyme (a a a a).</p>

<p>If verse does not have a perfect rhyme then we say that it has:</p>

<ul>
	<li>even rhyme: if the first and second line rhyme and also third and fourth line rhyme (a a b b).</li>
	<li>cross rhyme: if the first and third line rhyme and also second and fourth line rhyme (a b a b).</li>
	<li>shell rhyme: if the first and fourth line rhyme and also second and third line rhyme (a b b a).</li>
</ul>

<p>Write a program that will determine the rhyme for each verse in a song. </p>

### 입력 

 <p>The first line of the input file contains an integer N, the number of verses in the song, 1 ≤ N ≤ 5.</p>

<p>The following 4N lines of the input file contain the lines of the song. Maximal length of each line is 50.</p>

### 출력 

 <p>Output file should have N lines. For each verse in a song there should a single line containing one of the words 'perfect', 'even', 'cross', 'shell' or 'free' describing the rhyme in that verse.</p>

