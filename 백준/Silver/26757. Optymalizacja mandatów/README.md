# [Silver I] Optymalizacja mandatów - 26757 

[문제 링크](https://www.acmicpc.net/problem/26757) 

### 성능 요약

메모리: 318492 KB, 시간: 2268 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 6월 20일 19:07:19

### 문제 설명

<p>Chyba nikt nie lubi być łapany na przekroczeniu prędkości – co gorsza, w Bajtocji kary są bardzo surowe, a system ich przydzielania dość skomplikowany.</p>

<p>Każde takie wykroczenie rejestrowane jest jako para (K<sub>i</sub>, R<sub>i</sub>), gdzie liczba K<sub>i</sub> oznacza, o ile przekroczona została dopuszczalna prędkość, a R<sub>i</sub> – numer służbowy policjanta, który nałożył mandat. Kwota mandatu to sklejenie cyfr liczb K<sub>i</sub> oraz R<sub>i</sub>. Na przykład: jeśli K<sub>i</sub> = 12, a R<sub>i</sub> = 5 432, to kwota wynosi aż 125 432.</p>

<p>Bajtazar otrzymał właśnie N mandatów do zapłacenia. Patrząc na łączną ich kwotę poprzysiągł sobie, że nigdy więcej nie dociśnie gazu w swoim Alfa Bitteo. Aby jednak móc zachować swój samochód i przez najbliższy rok jeść cokolwiek poza keczupem, będzie musiał dokonać pewnej optymalizacji.</p>

<p>Płacone mandaty są kontrolowane przez dwa różne wydziały skarbowe – Wydział Ewidencji Prędkości sprawdza tylko, czy wśród zapłaconych mandatów obecne są wszystkie wartości prędkości K<sub>i</sub>, a Wydział Ewidencji Policjantów – czy zgadzają się numery służbowe R<sub>i</sub>. Nikt jednak sprawdza, w jakiej kolejności (i w jakich parach) mandaty zostały zapłacone. To oczywiście może wpływać na sumaryczną kwotę do zapłacenia – uczciwy, lecz sprytny pirat drogowy (taki jak Bajtazar) może „posklejać” ze sobą liczby K<sub>i</sub> oraz R<sub>i</sub> inaczej niż oryginalnie, tak aby łączna kwota była jak najmniejsza. Czy możesz mu pomóc?</p>

<p>Napisz program, który wczyta wartości przekroczeń prędkości K<sub>i</sub> oraz numery służbowe R<sub>i</sub>, obliczy najmniejszą możliwą sumaryczną kwotę mandatów przy najlepszym przypisaniu jednych numerów do drugich, i wypisze wynik na standardowe wyjście.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 1 000 000) określająca liczbę mandatów Bajtazara. W drugim wierszu wejścia znajduje się ciąg N liczb naturalnych K<sub>i</sub> (1 ≤ K<sub>i</sub> ≤ 100 000): wartości przekroczeń prędkości. W trzecim (ostatnim) wierszu wejścia znajduje się ciąg N liczb naturalnych R<sub>i</sub> (1 ≤ R<sub>i</sub> ≤ 100 000): numery służbowe policjantów, którzy przyłapali Bajtazara na nieostrożnej jeździe.</p>

### 출력 

 <p>W pierwszym (jedynym) wierszu wyjścia należy wypisać jedną liczbę naturalną – minimalna kwota do zapłacenia przy optymalnym przypisaniu wartości prędkości do numerów służbowych zgodnie z zasadami opisanymi powyżej.</p>

