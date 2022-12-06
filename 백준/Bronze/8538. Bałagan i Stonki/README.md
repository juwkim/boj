# [Bronze I] Bałagan i Stonki - 8538 

[문제 링크](https://www.acmicpc.net/problem/8538) 

### 성능 요약

메모리: 34540 KB, 시간: 96 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string)

### 문제 설명

<p>Przewodniczący Stonkony chce się dowiedzieć z ilu członków składa się jego organizacja. Zarządził, aby wszyscy członkowie wpisali się na listę obecności. Stonki są mało inteligentne, więc część z nich wpisała się na listę wielokrotnie. Na domiar złego nie potrafią dobrze pisać: mylą się im małe i wielkie litery oraz często wpisują znak <code>-</code> (minus). Pomóż Przewodniczącemu dowiedzieć się, jak duża jest jego organizacja.</p>

<p>Mając daną listę z wpisami (jeden wpis w jednym wierszu) policz, ile różnych nazwisk się na niej znajduje. To samo nazwisko może się pojawić na liście wiele razy. Nazwiska składają się tylko z wielkich liter alfabetu angielskiego i mają co najwyżej 20 znaków. Swoje nazwisko stonka może zapisać:</p>

<ul>
	<li>zamieniając niektóre wielkie litery na małe,</li>
	<li>wstawiając w dowolne miejsce dowolnie dużo znaków <code>-</code> (minus).</li>
</ul>

<p><b>Przykład</b>: zapisy <code>A-b</code> oraz <code>--A-B-</code> przedstawiają to samo nazwisko.</p>

### 입력 

 <p>W pierwszym wierszu podana jest liczba wpisów <em>j</em>, 1 ≤ <em>j</em> ≤ 10000. W każdym z kolejnych <em>j</em> wierszy podany jest jeden wpis z listy (nie ma ograniczenia na długość tego wpisu, ale wiadomo, że co najwyżej 20 znaków jest różnych od <code>-</code>).</p>

### 출력 

 <p>W pierwszym i jedynym wierszu program powinien wypisać liczbę różnych nazwisk znajdujących się na liście.</p>

