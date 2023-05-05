# [Silver IV] Haiku Review - 4676 

[문제 링크](https://www.acmicpc.net/problem/4676) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현, 문자열

### 문제 설명

<p><br>
Haiku is an ancient form of Japanese poetry. A haiku is a three-line poem with seventeen syllables, where the first line must contain five syllables, the second line must contain seven syllables, and the third line must contain five syllables. The lines do not have to rhyme. Here is an example, where slashes separate the lines:</p>

<blockquote>
<p>Computer programs/The bugs try to eat my code/I must not let them.</p>
</blockquote>

<p>You must write a program that will review a haiku and check that each line contains the correct number of syllables.</p>

<p>The input contains one or more lines, each of which contains a single haiku. A haiku will contain at least three words, and words will be separated by either a single space or a slash (‘/’). Slashes also separate the three lines of a haiku, so each haiku will contain exactly two slashes. (The three lines of the haiku will be contained within one physical line of the file.) A haiku will contain only lowercase letters (‘a’–‘z’), forward slashes (‘/’), and spaces, and will be no more than 200 characters long (not counting the end-of-line characters).</p>

<p>The haiku ‘e/o/i’ signals the end of the input.</p>

<p>Each haiku is guaranteed to contain three lines, and each line will contain at least one word. Your job is to determine whether each line has the correct number of syllables (5/7/5). For the purposes of this problem, every contiguous sequence of one or more vowels counts as one syllable, where the vowels are a, e, i, o, u, and y. Every word will contain at least one syllable.</p>

<p>(Note that this method of counting syllables does not always agree with English conventions. In the second example below, your program must consider the word ‘code’ to have two syllables because the ‘o’ and the ‘e’ are not consecutive. However, in English the ‘e’ is silent and so ‘code’ actually has only one syllable.)</p>

### 입력 

 <p>For each haiku, output a single line that contains ‘1’ if the first line has the wrong number of syllables, ‘2’ if the second line has the wrong number of syllables, ‘3’ if the third line has the wrong number of syllables, or ‘Y’ if all three lines have the correct number of syllables.</p>

### 출력 

 <p>If the haiku is not correct, you must output the number of the first line that has the wrong number of syllables.</p>

