# [Bronze III] The King - 9806 

[문제 링크](https://www.acmicpc.net/problem/9806) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>Once upon a time in a country far away lived a king and he had a big kingdom. He was a very clever king but he had one weakness -- he could count only up to three.</p>

<p>Nevertheless, he did not consider this to be a really great drawback, since he had a lot of wizards who could count up to one hundred (and some of them, people said, even up to one thousand), so it was all right. But one day the grief came to the kingdom as the outnumbering barbarians started to approach from all sides. And the king then had to make the most important decision in his life. He had to choose which of his sons to make generals that he would send to the borders of the country to lead the army.</p>

<p>However, the king knew that though some of his sons were clever, just like he was, some of them were quite stupid and could only lower army spirits with their wrong decisions. More precisely, he knew about each of his sons his mental potential -- an integer number ranging from minus three to three (remember, that the king could count only up to three). He also knew that the chance of his army defeating barbarians was proportional to the sum of some powers of mental potentials of those of his sons that he would make generals (the power exponent was a positive integer number, the same for all his sons and not exceeding three either). Thus he had to choose such a combination of his sons to lead</p>

<p>the army, that this sum would be maximal possible.</p>

<p>However, the king himself could not make all apropriate calculations since, for example, the second power of the number not exceeding three (which is its square) could be greater than three, and therefore he asked you, his most intellegent wizard, to solve this problem.</p>

### 입력 

 <p>The first line of the input file contains the number of the sons of the king (integer number less or equal to one hundred). The second line contains the positive integer number not exceeding three, the exponent in the formula used to calculate the chance of defeating barbarians. The third line contains the list of mental potentials of king’s sons -- all integer numbers, not greater than three by their absolute value.</p>

### 출력 

 <p>Output the only number -- the maximal possible chance of defeating barbarians measured as the sum described.</p>

