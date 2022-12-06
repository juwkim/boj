# [Bronze I] Letter Replacement - 5093 

[문제 링크](https://www.acmicpc.net/problem/5093) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Mr Sythe is teaching an ESL class about repeated letters in English words. As an exercise, he gets his students to replace all the repeated letters in a word with symbols.</p>

<p>The symbols used are as follows:</p>

<ul>
	<li>* is used to replace the first repeated letter (the first letter encountered which has occurred before)</li>
	<li>? for the second repeated letter</li>
	<li>/ for the third repeated letter</li>
	<li>+ for the fourth repeated letter</li>
	<li>! for the fifth repeated letter.</li>
</ul>

<p>No word that Mr Sythe uses has more than 5 repeated letters.</p>

<p>So, for example, the word Reindeer would become Reind**? because e is repeated twice and r is repeated once. The repeated e comes before the repeated r, hence the allocation of * to e and ? to r. Note that the first letter in the word is an upper case R, but this is treated as the same letter as the lower case r. </p>

### 입력 

 <p>In this problem, you will write a program to help Mr Sythe mark the exercise by giving him a list of correct answers. Input will consist of a list of words, one per line. Each word begins with an upper case letter and contains no more than 10 letters. The last line contains just a # - do not process this line.</p>

### 출력 

 <p>Output will be one word for each line of input each on a separate line. The output word must be the input word with repeated letters replaced as indicated by Mr Sythe's rules.</p>

