# [Bronze I] Hurtownia - 8620 

[문제 링크](https://www.acmicpc.net/problem/8620) 

### 성능 요약

메모리: 30840 KB, 시간: 972 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation)

### 문제 설명

<p>Szef Twojego kolegi, który pracuje w hurtowni, dzisiaj zachorował, a oto kontrola stoi u drzwi! Potrzebuje on więc możliwie szybko poznać liczbę pudeł poszczególnych towarów, jakie są aktualnie przechowywane w hurtowni. Korzystając z okazji, że odwiedziłeś go w pracy, Twój kolega poprosił Cię, żebyś pomógł mu to policzyć.</p>

<p>Na szczęście nie musisz liczyć pudeł ręcznie, gdyż chorujący szef zostawił swoje notatki, w których skrupulatnie notował każdy transport towarów, zarówno przywożonych, jak i wywożonych z hurtowni. Zapiski te leżą teraz przed Tobą - wszystkie od samego początku pracy hurtowni.</p>

<p>Oblicz, ile jest w tym momencie pudeł na składzie.</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia spis transportów magazynowanych pudeł,</li>
	<li>wyznaczy aktualną liczbę pudeł każdego z rodzajów towaru na składzie,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>Pierwszy wiersz wejścia zawiera jedną liczbę całkowitą $n$ ($1 ≤ n ≤ 1\,000\,000$), oznaczającą liczbę zapisków w notatkach. W każdym z kolejnych $n$ wierszy znajduje się pojedynczy zapis, dotyczący jednego transportu i składający się kolejno z:</p>

<ul>
	<li>rodzaju towaru, którego ten zapis dotyczy (poszczególne towary są oznaczone wielkimi literami alfabetu angielskiego od $A$ do $Z$);</li>
	<li>pojedynczego odstępu;</li>
	<li>znaku "$+$" lub "$-$" ("$+$" oznacza, że pudła zostały przywiezione do hurtowni, zaś "$-$" - że zostały z niej wywiezione);</li>
	<li>pojedynczej dodatniej liczby całkowitej, nie większej niż $2\,000$ i oznaczającej liczbę pudeł, które zostały przetransportowane.</li>
</ul>

<p>Zakładamy, że przed pierwszym transportem magazyn był pusty. Możesz też założyć, że nigdy w hurtowni nie było ujemnej liczby pudeł żadnego towaru.</p>

### 출력 

 <p>Wyjście powinno zawierać po jednym wierszu dla każdego rodzaju towaru, który pojawił się na wejściu. Każdy taki wiersz powinien zawierać nazwę towaru (oznaczoną za pomocą pojedynczej wielkiej litery) i oddzieloną od niej pojedynczym odstępem liczbę pudeł tego towaru, które znajdują się aktualnie w hurtowni. Towary na wyjściu powinny być wymienione w kolejności alfabetycznej.</p>

