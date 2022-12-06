# [Silver V] Sortowanie biżuterii - 8633 

[문제 링크](https://www.acmicpc.net/problem/8633) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

정렬(sorting), 문자열(string)

### 문제 설명

<p>Małgosia odziedziczyła po wujku kolekcję drogocennej biżuterii. Zastała w skarbcu artystyczny nieład i postanowiła go uporządkować. Wskład biżuterii wchodzą kolie składające się z cennych i rzadkich kamieni szlachetnych. Żadne dwa z nich nie są jednakowe. Pomóż Małgosi uporządkować drogocenny zbiór.</p>

<p>Opracuj program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia opisy biżuterii,</li>
	<li>uporządkuje je według rosnącej długości, a te, które są równej długości uporządkuje leksykograficznie,</li>
	<li>posortowane łańcuchy wypisze na standardowe wyjście.</li>
</ul>

<p>Łańcuchy o równej długości powinny być uporządkowane leksykograficznie-spośród dwóch różnych łańcuchów równej długości mniejszy jest ten, który ma mniejszy znak na pierwszej różniącej się pozycji.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się liczba łańcuchów do analizy $N$ ($N \le 150$), a w kolejnych $N$ wierszach znajdują się opisy poszczególnych elementów biżuterii. Opis każdego z nich składa się z niepustego łańcucha małych liter alfabetu łacińskiego ('a'..'z') odpowiadających użytym kamieniom, o długości nie przekraczającej $200$ znaków.</p>

### 출력 

 <p>W kolejnych wierszach wypisz kolejno uporządkowane rosnąco łańcuchy, po jednym w każdym wierszu.</p>

