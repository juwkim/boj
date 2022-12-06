# [Silver IV] Run Bajtocja - 8608 

[문제 링크](https://www.acmicpc.net/problem/8608) 

### 성능 요약

메모리: 120812 KB, 시간: 792 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 유클리드 호제법(euclidean), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Król Bajtocji dba o dobrą kondycję fizyczną swoich poddanych. Dlatego regularnie w stolicy organizowana jest masowa impreza sportowa - "Run Bajtocja". Mieszkańcy kraju licznie stają na linii startu, aby wystartować do biegu. Biegacze nie mają do pokonania określonego dystansu, tylko rozpocząwszy bieg razem ze wspólnego startu, biegają po trasie będącej pętlą o długości 1 km do czasu, aż znowu wszyscy spotkają się razem w punkcie startu. Każdy z biegaczy chciałby wiedzieć, ile kilometrów przebiegł w czasie wyścigu. Jednak ponieważ wyścig ten potrafi trwać bardzo długo, zawodnicy często zapominają ze zmęczenia, ile dokładnie przebiegli okrążeń, mimo że każdy z nich przebiega jedno okrążenie w stałym, znanym czasie.</p>

<p>Twoim zadaniem jest pomóc im dowiedzieć się, ile kilometrów przebiegli.</p>

<p>Napisz program, który:</p>

<ul>
	<li>dla każdego z zawodników wczyta ze standardowego wejścia czas, jaki potrzebuje on do przebycia jednego okrążenia,</li>
	<li>dla każdego zawodnika obliczy, ile kilometrów przebiegł on w czasie wyścigu,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba całkowita $n$ ($1 ≤ n ≤ 100\,000$), oznaczająca liczbę zawodników. W każdym z następnych $n$ wierszy znajduje się jedna liczba całkowita $t_i$ ($1 ≤ t_i ≤ 500$, oznaczająca czas wyrażony w sekundach, w jakim zawodnik o numerze $i$ przebiega jedno okrążenie.</p>

### 출력 

 <p>Twój program powinien wypisać na standardowe wyjście $n$ wierszy. W $i$-tym z nich powinna znaleźć się jedna liczba całkowita $d_i$ oznaczająca dystans przebyty przez $i$-tego zawodnika.</p>

