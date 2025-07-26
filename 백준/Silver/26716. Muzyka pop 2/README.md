# [Silver I] Muzyka pop 2 - 26716 

[문제 링크](https://www.acmicpc.net/problem/26716) 

### 성능 요약

메모리: 123672 KB, 시간: 120 ms

### 분류

수학, 그리디 알고리즘, 비트마스킹

### 제출 일자

2025년 7월 26일 21:19:59

### 문제 설명

<p>Jak być może pamiętacie, Mateusz uwielbia muzykę pop. Właśnie skomponował nowy utwór i pozostaje mu tylko ułożyć do niego odpowiednie zakończenie.</p>

<p>Mateusz chce, aby zakończenie jego utworu składało się z pewnego niepustego ciągu nut, gdzie każdą można opisać przez jej głośność, która to jest dodatnią liczbą całkowitą. Mateusz może używać nut o dowolnie dużych głośnościach, jednak zadaniem zakończenia jest stopniowe wygaszenie utworu – z tego względu głośności nut w zakończeniu muszą tworzyć ciąg ściśle malejący.</p>

<p>Jak pewnie wiecie lub pamiętacie, w muzyce pop ważne są dobre bity. Tym razem Mateusz stwierdził, że nuta o głośności x ma moc bitową równą liczbie zapalonych bitów w binarnym zapisie liczby x. Biorąc pod uwagę resztę utworu ustalił, że suma mocy bitowych nut w zakończeniu powinna być równa dokładnie n.</p>

<p>Pomóż mu i znajdź odpowiedni ciąg głośności nut. Można udowodnić, że zawsze istnieje co najmniej jeden taki ciąg, więc Twoim zadaniem jest znaleźć minimalny leksykograficznie.</p>

<p>Uwaga: Mówimy, że ciąg liczbowy A jest mniejszy leksykograficznie od ciągu liczbowego B, jeśli na pierwszej pozycji, na której te ciągi się różnią, A zawiera liczbę mniejszą od B. Jeśli taka pozycja nie istnieje, to A jest mniejszy leksykograficznie od B, jeśli A jest krótszy od B. Na przykład ciąg [1, 10000000] jest mniejszy leksykograficznie od ciągu [2, 2], ciąg [4, 2, 20, 30, 40] jest mniejszy leksykograficznie od ciągu [4, 2, 100, 1], a ciąg [5, 4, 3, 2] jest mniejszy leksykograficznie od ciągu [5, 4, 3, 2, 1].</p>

### 입력 

 <p>W jedynym wierszu standardowego wejścia znajduje się jedna liczba całkowita n (1 ≤ n ≤ 1 000 000), oznaczająca wymaganą sumę mocy bitowych nut w szukanym ciągu.</p>

### 출력 

 <p>W pierwszym wierszu standardowego wyjścia powinna znaleźć się jedna liczba całkowita k, oznaczająca długość szukanego ciągu.</p>

<p>W drugim wierszu standardowego wyjścia powinno znaleźć się k dodatnich liczb całkowitych – minimalny leksykograficznie, ściśle malejący ciąg, którego elementy mają sumarycznie zapalonych dokładnie n bitów w zapisie binarnym.</p>

