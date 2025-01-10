# [Silver II] Próg kwalifikacyjny - 26776 

[문제 링크](https://www.acmicpc.net/problem/26776) 

### 성능 요약

메모리: 147752 KB, 시간: 344 ms

### 분류

이분 탐색, 그리디 알고리즘, 누적 합, 정렬

### 제출 일자

2025년 1월 10일 13:42:54

### 문제 설명

<p>Bajtazar startuje w Bajtockiej Olimpiadzie Informatycznej Juniorów (BOIJ). Zasady tej olimpiady nieco różnią się od OIJ: do rozwiązania na pierwszym etapie jest pewna liczba zadań, a za każde z nich można uzyskać ustaloną liczbę punktów (być może różną dla różnych zadań), która jest przyznawana tylko, jeśli zadanie zostanie w pełni poprawnie rozwiązane. W innym przypadku rozwiązanie otrzymuje zawsze zero punktów.</p>

<p>Bajtazar jest dość leniwy, dlatego zamiast zabrać się do rozwiązywania zadań, zastanawia się ile zadań będzie wystarczające, żeby dostać się do drugiego etapu. Co roku, po zawodach, Komitet Główny BOIJ publikuje próg kwalifikacyjny do drugiego etapu zawodów. Każdy zawodnik, który będzie miał przynajmniej tyle punktów, ile wynosi próg, zostanie zakwalifikowany. Niestety, sytuację utrudnia fakt, że Bajtazar nie zna progu w trakcie zawodów. Każdej nocy jednak ma sen, w którym dowiaduje się ile wynosi wartość progu – co rano zastanawia się wtedy, ile zadań wystarczyłoby w takim wypadku zrobić. Napisałby program odpowiadający mu na to pytanie, jednak, no właśnie, jest trochę leniwy. Dlatego poprosił Cię o pomoc.</p>

<p>Napisz program, który wczyta wartości punktowe poszczególnych zadań oraz potencjalne progi kwalifikacyjne, dla każdego progu wyznaczy minimalną liczbę rozwiązanych zadań niezbędnych do przejścia do drugiego etapu i wypisze wyniki na standardowe wyjście.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 200 000), określająca liczbę zadań na pierwszym etapie zawodów. W drugim wierszu wejścia znajduje się ciąg N liczb naturalnych V<sub>i</sub> (1 ≤ V<sub>i</sub> ≤ 10<sup>9</sup>), pooddzielanych pojedynczymi odstępami – i-ta liczba określa liczbę punktów za poprawne rozwiązanie i-tego zadania.</p>

<p>W trzecim wierszu wejścia znajduje się jedna liczba naturalna Q (1 ≤ Q ≤ 200 000), określająca liczbę snów Bajtazara. W kolejnych Q wierszach znajduje się opis tych snów, po jednym w wierszu. Opis każdego snu składa się z jednej liczby naturalnej P<sub>i</sub>, 1 ≤ P<sub>i</sub> ≤ V<sub>1</sub> + V<sub>2</sub> + ··· + V<sub>N</sub>, określającej wyśniony próg do drugiego etapu zawodów podczas i-tego snu Bajtazara.</p>

### 출력 

 <p>Twój program powinien wypisać na wyjście dokładnie Q wierszy: po jednym dla każdego snu Bajtazara. W i-tym wierszu powinna się znaleźć jedna liczba naturalna – minimalna liczba zadań do rozwiązania, wystarczająca do kwalifikacji do drugiego etapu przy założeniu wyśnionego progu z i-tego snu.</p>

