# [Bronze I] KIARA is a Recursive Acronym - 24993 

[문제 링크](https://www.acmicpc.net/problem/24993) 

### 성능 요약

메모리: 40144 KB, 시간: 292 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A recursive acronym is an acronym in which one of its letters stands for the acronym itself. For instance, the first word in the title of this problem is a recursive acronym of the full title. Another example is “BOB”, which is an acronym of “Beware of Bob”.</p>

<p>Given a list of words, you must decide whether there exists a word in the list which is a recursive acronym of a phrase that can be formed using words in the list. Since the first letter of any word can stand for the whole word, it is enough to decide whether there exists a word in the list which can be formed using the first letter of some words in the list.</p>

### 입력 

 <p>The first line contains a positive integer N indicating the number of words in the list. Each of the next N lines contains a non-empty string made of uppercase letters representing a word in the list. The sum of the lengths of all the strings is at most 10<sup>6</sup>.</p>

### 출력 

 <p>Output a single line with the uppercase letter “<code>Y</code>” if there exists a word in the list which is a recursive acronym of a phrase that can be formed using words in the list, and the uppercase letter “<code>N</code>” otherwise.</p>

