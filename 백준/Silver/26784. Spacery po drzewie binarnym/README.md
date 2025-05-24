# [Silver I] Spacery po drzewie binarnym - 26784 

[문제 링크](https://www.acmicpc.net/problem/26784) 

### 성능 요약

메모리: 111548 KB, 시간: 192 ms

### 분류

최소 공통 조상, 수학, 트리

### 제출 일자

2025년 5월 25일 02:12:07

### 문제 설명

<p>Przypomnijmy jak wygląda drzewo binarne. Węzły tego drzewa będziemy numerowali kolejnymi liczbami naturalnymi od 1, idąc kolejnymi poziomami od góry do dołu poczynając od korzenia (wierzchołka na samej górze), a na każdym poziomie od lewej do prawej:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b47946e7-1262-4f05-8d3e-303f8a3f94c5/-/preview/" style="width: 443px; height: 254px;"></p>

<p style="text-align: center;">Drzewo binarne narysowane do węzła nr 18. Zwróć uwagę, że drzewo ma więcej niż 18 węzłów.</p>

<p>W tym zadaniu będziemy rozpatrywali najkrótsze ścieżki pomiędzy dwoma węzłami. Przykładowo, najkrótsza ścieżka między węzłami numer 8 oraz 5 ma trzy krawędzie i przebiega przez węzły 4 oraz 2.</p>

<p>Napisz program, który wczyta zapytania dotyczące ścieżek pomiędzy dwoma węzłami drzewa, dla każdego z nich wyznaczy długość najkrótszej ścieżki między tymi węzłami i wypisze wyniki na standardowe wyjście.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna Q (1 ≤ Q ≤ 100 000), określająca liczbę zapytań. W kolejnych Q wierszach znajdują się zapytania, po jednym w wierszu. Opis każdego zapytania składa się z dwóch liczb naturalnych A<sub>i</sub> oraz B<sub>i</sub> (1 ≤ A<sub>i</sub>, B<sub>i</sub> ≤ 10<sup>18</sup>), oddzielonych pojedynczym odstępem i określających numery węzłów, dla których należy wyznaczyć ścieżkę.</p>

### 출력 

 <p>Twój program powinien wypisać na wyjście Q wierszy. W i-tym z nich powinna się znaleźć liczba całkowita – liczba krawędzi, które należy pokonać, aby przedostać się w drzewie z węzła o numerze A<sub>i</sub> do węzła B<sub>i</sub>.</p>

