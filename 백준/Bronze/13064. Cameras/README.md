# [Bronze II] Cameras - 13064 

[문제 링크](https://www.acmicpc.net/problem/13064) 

### 성능 요약

메모리: 29200 KB, 시간: 92 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>In a crowded city, a network of traffic cameras are installed on all crosses and capture the image of the cars that pass the red lights. The law enforcement department requires a software system to process all the captured numbers, and issue a ticket for all the cars that violate the law. An image processing module has already preprocessed the video recordings and generated a file containing the recorded car numbers. You are requested to write the ticketing module. The problem is that the image processing module is not perfect, and some car numbers are wrong.</p>

<p>A true car number should meet all of the following requirements:</p>

<ul>
	<li>It is 8 characters long.</li>
	<li>The two leftmost characters are identical digits between 1 to 9, which indicate in which city the car number is issued.</li>
	<li>The following two characters are two digits between 1 to 9.</li>
	<li>The following character is a capital English letter.</li>
	<li>The three rightmost characters are also digits between 1 to 9.</li>
</ul>

### 입력 

 <p>The first line of input contains the number of captured car numbers (n) that are reported by the image processing module. In each of the next n lines, there are exactly 8 numerical or English alphabetical characters, showing one inferred car number. You can assume 1 ≤ n ≤ 1000.</p>

### 출력 

 <p>You should report the car numbers that have violated the law, one in each line, in the same order that they appear in the input. If the same car number has violated the law multiple times, all of the violation cases should be reported. The wrong car numbers, which do not meet one or more of the above requirements, should not be listed in the output. </p>

