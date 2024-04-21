# [Silver III] Netiquette - 4628 

[문제 링크](https://www.acmicpc.net/problem/4628) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현, 문자열

### 제출 일자

2024년 4월 21일 14:26:16

### 문제 설명

<p>Mr. Manners teaches netiquette ("net etiquette", particularly as it applies to email) at the local community college. There are many different aspects to proper netiquette, including courtesy, correct spelling, and correct grammar. Through experience Mr. Manners has found that his college's email system does a good job of catching most spelling and grammatical errors, and he's also found that most of his students are courteous. So there are four violations of netiquette that Mr. Manners pays careful attention to, and he's devised a quick way to test for them. A message is suspicious if it contains any of the following:</p>

<ol>
	<li>two adjacent uppercase letters,<br>
	(because you might be SHOUTING)</li>
	<li>a digit adjacent to a letter,<br>
	(because you might be l33t, d00d)</li>
	<li>an isolated character other than a, A, or I,<br>
	(because u r probably abbreviating words; the spell checker doesn't catch this for some reason)</li>
	<li>two adjacent punctuation marks, unless one of them is a double quote (the character ").<br>
	(because you might be using an emoticon :-)</li>
</ol>

<p>For this problem, all characters in an email message are printable ASCII characters with codes in the range 32..126 (inclusive). A punctuation mark is any character other than a letter, digit, or space. Two characters are adjacent if they are right next to each other, with no characters in between. An isolated character is one whose only adjacent characters (if any) are spaces. Your job is to write a program that can tell if a one-line email message is suspicious.</p>

### 입력 

 <p>The input consists of one or more email messages, followed by a line containing only # that signals the end of the input. Each message is on a line by itself, does not begin or end with a space, and does not contain consecutive spaces. End-of-line characters occur at the end of every line (of course), but they are not considered to be part of the message. A message will contain 1..80 characters.</p>

### 출력 

 <p>For each message, output suspicious if it meets one or more of the four criteria defined above, and output OK otherwise. In the examples below, the second email meets all four criteria, and the fourth and sixth emails meet one criterion each.</p>

