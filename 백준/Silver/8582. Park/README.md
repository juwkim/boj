# [Silver V] Park - 8582 

[문제 링크](https://www.acmicpc.net/problem/8582) 

### 성능 요약

메모리: 212400 KB, 시간: 1480 ms

### 분류

다이나믹 프로그래밍(dp), 구현(implementation)

### 문제 설명

<p>Bajtocki Park Narodowy słynie z długiego (choć niezbyt szerokiego) pasma górskiego, rozciągającego się przez cały park z zachodu na wschód. Co roku przyjeżdżają do niego tłumy turystów, którzy często nie są zbyt rozgarnięci. Dlatego zarząd parku postanowił przygotować mapę całego pasma, podzieloną na fragmenty równej długości. Przy każdym punkcie podziału zarząd zamierza umieścić wysokość tego punktu oraz dwie inne liczby: wysokość najwyższego punktu podziału na zachód od niego oraz na wschód od niego.</p>

<p>Cała mapa jest już właściwie gotowa. Pozostaje jedynie obliczyć maksymalne wysokości na zachód i na wschód od każdego punktu podziału. Zarząd parku poprosił Cię o napisanie programu, który wyznaczy te wartości.</p>

### 입력 

 <p>W pierwszym wierszu standardowego wejścia znajduje się jedna liczba całkowita $n$ ($1 ≤ n ≤ 1\,000\,000$) oznaczająca długość pasma górskiego. W każdym z następnych $n$ wierszy znajduje się po jednej liczbie całkowitej $w_i$ ($1≤ w_i ≤ 1\,000\,000\,000$) oznaczającej wysokość $i$-tego punktu podziału. Punkty te podane są w kolejności z zachodu na wschód.</p>

### 출력 

 <p>Twój program powinien wypisać na standardowe wyjście dokładnie $n$ wierszy, odpowiadających kolejnym punktom podziału (w kolejności z zachodu na wschód). W każdym z tych wierszy powinny znaleźć się dwie liczby całkowite $a_i$ oraz $b_i$ oddzielone pojedynczym odstępem - wysokość najwyższego punktu podziału na zachód od punktu $i$ oraz na wschód od niego. W przypadku, gdy na zachód od punktu $i$ nie ma szczytu wyższego niż $w_i$, przyjmujemy $a_i = w_i$. Podobnie, jeśli na wschód od punktu $i$ nie ma szczytu wyższego niż $w_i$, to przyjmujemy $b_i = w_i$.</p>

