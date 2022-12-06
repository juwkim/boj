# [Bronze III] Papier kamień nożyczki - 8806 

[문제 링크](https://www.acmicpc.net/problem/8806) 

### 성능 요약

메모리: 121220 KB, 시간: 100 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Adam i Gosia grają w "Papier kamień nożyczki".</p>

<p>Gra polega na tym, że każdy z zawodników jednocześnie wybiera <em>papier</em>, <em>kamień</em> lub <em>nożyczki</em>.</p>

<ul>
	<li>Gracz, który wybrał <em>papier</em> wygrywa z tym, który wybrał <em>kamień</em>.</li>
	<li>Gracz, który wybrał <em>kamień</em> wygrywa z tym, który wybrał <em>nożyczki</em>.</li>
	<li>Gracz, który wybrał <em>nożyczki</em> wygrywa z tym, który wybrał <em>papier</em>.</li>
</ul>

<p>Jeśli oboje wybiorą ten sam ruch gra jest powtarzana do momentu wyłonienia zwycięzcy.</p>

<p>Wiedząc z jakim prawdopodobieństem każdy z graczy wybierze <em>papier</em>, <em>kamień</em> i <em>nożyczki</em> oblicz kto ma większe szanse wygrania pojedynku.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba zestawów testowych <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ).</p>

<p>Pierwsza linia pojedynczego zestawu testowego zawiera liczby <strong>X1 Y1 Z1</strong> ( 0 <= <strong>X1</strong>, <strong>Y1, Z1</strong> <= 1,  <strong>X1 + Y1 + Z1</strong> = 1) określające z jakim prawdopodobieństwem Adam wybierze <em>papier</em>, <em>kamień</em> i <em>nożyczki</em>. Druga linia zawiera liczby <strong>X2 Y2 Z2</strong> ( 0 <= <strong>X2</strong>, <strong>Y2, Z2</strong> </p>

<p><= 1,  <strong>X2 + Y2 + Z2</strong> = 1 ) określające z jakim prawdopodobieństwem Gosia wybierze <em>papier</em>, <em>kamień</em> i <em>nożyczki</em>.</p>

### 출력 

 <p>Dla każdego zestawu testowego należy wypisać:</p>

<ul>
	<li>"ADAM" jeśli Adam ma większe szanse na zwycięstwo</li>
	<li>"GOSIA" jeśli Gosia ma większe szansce na zwycięstwo</li>
	<li>"=" jesli Adam i Gosia mają równe szanse na zwycięstwo</li>
</ul>

