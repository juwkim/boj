# [Silver IV] Drzewko - 8680 

[문제 링크](https://www.acmicpc.net/problem/8680) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

비트마스킹(bitmask), 수학(math), 트리(trees)

### 문제 설명

<p>Mamy dane drzewko binarne o wysokości <em>h</em> (jak na rysunku):</p>

<p style="text-align: center;"><img alt="" src=""><br>
 </p>

<p>Każda krawędź może być zamknięta bądź otwarta. Początkowo otwarte są wszystkie lewe krawędzie (zaznaczone linią przerywaną). Adrianek zrzuca po kolei <em>n</em> piłeczek, poczynając od wierzchołka startowego, który jest korzeniem drzewa. Każda piłeczka zawsze leci przez otwartą krawędź, a następnie zmienia ją na zamkniętą oraz otwiera sąsiednią krawędź (gdy otwarta jest lewa krawędź, to zamykamy lewą i otwieramy prawą, a gdy otwarta jest prawa, to zamykamy prawą i otwieramy lewą).</p>

<p>Adrianek zastanawia się, do którego wierzchołka (ponumerowanego od 0 do 2<em><sup>h</sup></em> - 1) spadnie <em>n</em>-ta piłeczka.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera dwie liczby całkowite <em>n</em>, <em>h</em> (1 ≤ <em>n</em> ≤ 10<sup>8</sup>, 0 ≤ <em>h</em> ≤ 30), oznaczające odpowiednio liczbę piłeczek zrzucanych przez Adrianka oraz wysokość drzewka binarnego.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz standardowego wyjścia powinien zawierać jedną liczbę całkowitą, równą numerze wierzchołka, do którego spadnie <em>n</em>-ta piłeczka.</p>

