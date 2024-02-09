# [Silver III] HAN - 11810 

[문제 링크](https://www.acmicpc.net/problem/11810) 

### 성능 요약

메모리: 111648 KB, 시간: 224 ms

### 분류

구현

### 제출 일자

2024년 2월 9일 23:22:31

### 문제 설명

<p>Han didn’t want to study solo so he invited his friend Dominik to come over. After an eventful evening that will be remembered for a record number of solved tasks from the field of electronics, Dominik went home. To his surprise, the police stopped him thinking he was drunk. It is known that in these situations sobriety is proven by solving a series of carefully crafted tasks that test a man’s cognitive abilities. If we can trust Dominik, the conversation went something like this:</p>

<ul>
	<li>Policeman: Something easy to begin with. . . What is the complexity of bubble sort?</li>
	<li>Dominik: That is really easy, O(n<sup>2</sup>).</li>
	<li>Policeman: Say the English alphabet in reverse.</li>
	<li>Dominik: Trivial, zyxwvutsrqponmlkjihgfedcba</li>
	<li>Policeman: You learned that by heart. Now imagine that all the letters of the English alphabet from ‘a’ to ‘z’ are respectively written clockwise in a circle. Begin with the letter ‘a’ and say the letters clockwise. After each spoken letter, I can tell you to continue saying the alphabet in reverse order or I can ask you how many times so far you’ve said a certain letter. Are you ready? 3, 2, 1, Go!</li>
	<li>Dominik: Um... a, b, c...</li>
</ul>

<p>Write a programme that solves Dominik’s problem</p>

### 입력 

 <p>The first line of input contains the integer Q (1 ≤ Q ≤ 100 000), the number of policeman’s orders. Each of the following Q lines contains one of the policeman’s order in the form of “SMJER n” (Croatian for direction) or “UPIT n x” (Croatian for query). The order in the form “SMJER n” means that, after the nth spoken letter, Dominik must start saying the alphabet in reverse, whereas the order in the form “UPIT n x” means that Dominik must say how many times so far he’s said the letter x in the first n spoken letters.</p>

<p>The policeman’s order will be given chronologically in the input, or, the numbers n (1 ≤ n ≤ 10<sup>9</sup>) from the orders will be strictly ascending. The character x from the order in the form of “UPIT n x” is a lowercase letter of the English alphabet.</p>

### 출력 

 <p>For each order in the form of “UPIT n x”, output how many times Dominik has said the letter x in the first n spoken letters. The answer to each query needs to be written in a separate line, and the queries need to be answered in the order given in the input.</p>

