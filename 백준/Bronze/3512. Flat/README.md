# [Bronze III] Flat - 3512 

[문제 링크](https://www.acmicpc.net/problem/3512) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>You are one of the developers of software for a real estate agency. One of the functions you are to implement is calculating different kinds of statistics for flats the agency is selling. Each flat consists of different types of rooms: bedroom, bathroom, kitchen, balcony and others.</p>

<p>The cost of the flat is equal to the product of reduced total area and the cost of one square metre. Reduced total area is the total area of all rooms except for balconies plus one half of balconies total area.</p>

<p>You will be given some information about the area of each room in the flat and the cost of one square metre. You are to calculate the following values for the flat:</p>

<ul>
	<li>the total area of all rooms;</li>
	<li>the total area of all bedrooms;</li>
	<li>the cost of the flat.</li>
</ul>

### 입력 

 <p>The first line of the input file contains two integer numbers n (1 ≤ n ≤ 10) and c (1 ≤ c ≤ 100 000) — number of rooms in the flat and the cost of one square metre, respectively.</p>

<p>Each of the following n lines contains an integer number a<sub>i</sub> (1 ≤ ai ≤ 100) and a word t<sub>i</sub> — the area of i-th room and its type, respectively. Word t<sub>i</sub> is one of the following: “bedroom”, “bathroom”, “kitchen”, “balcony”, “other”.</p>

### 출력 

 <p>The first line of the output file should contain one integer number — the total area of all rooms of the flat. The second line of the output file should contain one integer number — the total area of bedrooms of the flat. The third line of the output file should contain one real number — the cost of the flat with precision not worse than 10<sup>−6</sup>.</p>

