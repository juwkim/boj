# [Silver III] Pamięć doskonała - 8784 

[문제 링크](https://www.acmicpc.net/problem/8784) 

### 성능 요약

메모리: 268380 KB, 시간: 720 ms

### 분류

사칙연산, 해 구성하기, 수학

### 제출 일자

2024년 2월 5일 09:29:30

### 문제 설명

<p>Hektor z Wiktorem mają nowe, fascynujące hobby - zapamiętywanie długich ciągów liczb całkowitych. Każdy z chłopców wyspecjalizował się w zapamiętywaniu konkretnego rodzaju ciągów. Hektor najbardziej lubi palindromy, tj. ciągi które na odpowiadających sobie przeciwnych pozycjach (pierwsza z ostatnią, druga z przedostatnią, etc.) mają te same liczby. Wiktor natomiast jest specjalistą od antypalindromów, tj. ciągów, które na odpowiadających sobie przeciwnych pozycjach (pierwsza z ostatnią, druga z przedostatnią, etc.) mają przeciwne (tj. sumujące się do zera) liczby.</p>

<p>Ostatnio chłopcy zaczęli zastanawiać się nad tym, jakie możliwości otwiera przed nimi połączenie ich zdolności. Gdyby tak potrafili rozkładać dowolny ciąg liczb całkowitych na sumę palindromu i antypalindromu, każdy z nich mógłby zapamiętać ciąg swojego ulubionego rodzaju, a razem bez trudu potrafiliby odtworzyć początkowy ciąg!</p>

<p>Dla zadanego ciągu liczb całkowitych <strong>S</strong> o parzystej długości <strong>N </strong>oblicz dwa ciągi <strong>P</strong> i <strong>A</strong>, każdy długości <strong>N</strong>, takie, że <strong>P</strong> jest palindromem, <strong>A</strong> jest antypalindromem, a po wysumowaniu elementów <strong>P</strong> i <strong>A</strong> na odpowiadających sobie pozycjach, otrzymujemy ciąg <strong>S</strong>.</p>

### 입력 

 <p>W pierwszej linii znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) opisująca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>W pierwszej linii opisu zestawu znajduje się jedna niezerowa parzysta liczba naturalna <strong>N</strong> ( 1 <= <strong>N</strong> <= 1000000 ) oznaczająca długość ciągu <strong>S</strong>.</p>

<p>W drugiej linii opisu zestawu znajduje się <strong>N</strong> liczb całkowitych <strong>s<sub>i</sub></strong> ( -1000000 <= <strong>s<sub>i</sub></strong> <= 1000000 ) opisujących kolejne elementy ciągu <strong>S</strong>.</p>

### 출력 

 <p>Dla każdego zestawu:</p>

<ul>
	<li>Jeśli zadany ciąg <strong>S</strong> da się rozłożyć na sumę opisanych w treści ciągów <strong>P</strong> i <strong>A</strong>, należy wypisać w pierwszej linii ciąg <strong>P</strong> (oddzielając poszczególne elementy spacjami), a w drugiej linii ciąg <strong>A</strong>.</li>
	<li>W przeciwnym wypadku należy w jedynej linii wypisać słowo "NIE".</li>
</ul>

