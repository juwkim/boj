# [Silver IV] Deli Deli - 6513 

[문제 링크](https://www.acmicpc.net/problem/6513) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

많은 조건 분기(case_work), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 문자열(string)

### 문제 설명

<p>Mrs. Deli is running the delicatessen store "Deli Deli".
Last year Mrs. Deli has decided to expand her business and build up an
online store. She has hired a programmer who has implemented the
online store.
</p>
<p>
Recently some of her new online customers complained about the
electronic bills. The programmer had forgotten to use the plural form
in case that an item is purchased multiple times. Unfortunaly the
programmer of Mrs. Deli is on holiday and now it is your task to
implement this feature for Mrs. Deli. Here is a description how
to make the plural form:
</p>
<ol>
<li>If the word is in the list of irregular words replace it with the
given plural. </li>
<li>Else if the word ends in a consonant followed by "y", replace "y" with "ies".</li>
<li>Else if the word ends in "o", "s", "ch", "sh" or "x", append "es" to the word.</li>
<li>Else append "s" to the word.</li>
</ol>

### 입력 

 <p>The first line of the input file consists of two integers
L and N (<i>0 ≤ L ≤ 20</i>, <i>1 ≤ N ≤ 100</i>).
The following L lines contain
the description of the irregular words and their plural form.
Each line consists of two words separated by a space character,
where the first word is the singular, the second word the plural
form of some irregular word.
After the list of irregular words, the following
N lines contain one word each, which you have to
make plural. You may assume that each word consists of at most
20 lowercase letters from the english alphabet ('a' to 'z').
</p>

### 출력 

 <p>Print N lines of output, where the i<sup>th</sup>
line is the plural form of the i<sup>th</sup> input word.
</p>

