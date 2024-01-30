# [Silver III] Gra - 8689 

[문제 링크](https://www.acmicpc.net/problem/8689) 

### 성능 요약

메모리: 218580 KB, 시간: 460 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 1월 30일 19:56:39

### 문제 설명

<p>Kolejny deszczowy dzień. Paweł i Gaweł znów byli zmuszeni do pozostania w domu. W związku z brakiem zajęć postanowili wymyślić jakąś grę.</p>

<p>Paweł wpadł na genialny pomysł. Na kartce papieru narysował <em>n</em> pól. Na każdym polu znajdowały się dwie liczby - pierwsza z nich była numerem pola (liczba naturalna od 1 do <em>n</em>, pola miały parami różne numery), a druga jego wartością (liczba całkowita od -1 000 do 1 000). Na polu numer 1 umieścił pionek. Zadaniem gracza było wykonywanie kolejnych ruchów, polegających na rzucie sześcienna kostką (z numerami od 1 do 6 napisanymi na ściankach) oraz przesuwaniu pionka o wskazaną liczbę oczek. Gra kończyła się, kiedy pionek stanął na pole o numerze <em>n</em>. Wynikiem, jaki uzyskał gracz, była suma wartości pól na jakich stał pionek.</p>

<p>Po rozegraniu kilku partii Paweł i Gaweł otrzymali kilka różnych wyników, jednak nie wiedzieli czy któryś z nich był największym możliwym do uzyskania. Zadzwonili więc do Ciebie, utalentowanego informatyka, abyś napisał program, który dla danej planszy obliczy maksymalny możliwy do uzyskania wynik.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>6</sup>) oznaczającą liczbę pól na planszy. Drugi wiersz zawiera <em>n</em> liczb całkowitych <em>w</em><sub>1</sub>, <em>w</em><sub>2</sub>, ..., <em>w<sub>i</sub></em> (-1 000 ≤ <em>w<sub>i</sub></em> ≤ 1 000), gdzie <em>w<sub>i</sub></em> oznacza wartość <em>i</em>-tego pola.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz standardowego wyjścia powinien zawierać jedną liczbę całkowitą, oznaczającą maksymalny możliwy do uzyskania wynik na danej planszy.</p>

