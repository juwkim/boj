# [Silver III] Miasta - 8677 

[문제 링크](https://www.acmicpc.net/problem/8677) 

### 성능 요약

메모리: 216392 KB, 시간: 388 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 1월 30일 22:57:43

### 문제 설명

<p>Wzdłuż rzeki znajduje się <em>n</em> miast. Pomiędzy każdą parą sąsiednich miast wybudowana jest droga, niestety nie zawsze dwukierunkowa, dlatego nie zawsze da się dojechać z każdego miasta do wszystkich innych. Znając, które drogi są wybudowane, chcielibyśmy wiedzieć dla każdego miasta, do ilu innych miast da się z niego dojechać.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>6</sup>), oznaczającą liczbę miast.</p>

<p>W kolejnym wierszu znajduje się <em>n</em> - 1 liczb całkowitych <em>d</em><sub>1</sub>, <em>d</em><sub>2</sub>, ..., <em>d</em><sub><em>n</em>-1</sub> (0 ≤ <em>d<sub>i</sub></em> ≤ 2), gdzie <em>d<sub>i</sub></em> oznacza połączenie pomiędzy miastem <em>i</em>-tym, a <em>i</em>+1-wszym. Jeśli:</p>

<ul>
	<li><em>d<sub>i</sub></em> = 0, to z miasta <em>i</em>-tego biegnie jednokierunkowa droga do miasta <em>i</em>+1-wszego,</li>
	<li><em>d<sub>i</sub></em> = 1, to z miasta <em>i</em>+1-wszego biegnie jednokierunkowa droga do miasta <em>i</em>-tego,</li>
	<li><em>d<sub>i</sub></em> = 2, to miasta <em>i</em>-te i <em>i</em>+1-wsze połączone są drogą dwukierunkową.</li>
</ul>

### 출력 

 <p>W pierwszym i jedynym wierszu wyjścia powinno znajdować się <em>n</em> liczb całkowitych <em>w</em><sub>1</sub>, <em>w</em><sub>2</sub>, ..., <em>w<sub>n</sub></em>, gdzie <em>w<sub>i</sub></em> oznacza liczbę miast, do których da się dojechać z miasta <em>i</em>-tego.</p>

