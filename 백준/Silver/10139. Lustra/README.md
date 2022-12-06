# [Silver V] Lustra - 10139 

[문제 링크](https://www.acmicpc.net/problem/10139) 

### 성능 요약

메모리: 116408 KB, 시간: 944 ms

### 분류

정렬(sorting)

### 문제 설명

<p>Firma Bajtazara zajmuje się produkcją drewnianych szaf z lustrzanymi drzwiami. Firma koncentruje się na jakości wyrobów z drewna, a produkcję luster zleca podwykonawcom.</p>

<p>Właśnie zakończył się jeden z przetargów zorganizowanych przez firmę Bajtazara. Wzięło w nim udział <em>n</em> zakładów, z których każdy złożył pewną ofertę rozmiarów produkowanych luster. Wszystkie lustra mają prostokątny kształt. Oferta każdego z zakładów przedstawia minimalną i maksymalną szerokość oraz minimalną i maksymalną wysokość produkowanych luster. Przy produkcji szaf luster nie można obracać.</p>

<p>Bajtazar wie, że jeśli do przetargu stanął zakład, którego oferta majoryzuje oferty wszystkich pozostałych, tzn. żaden inny oferent nie ma w ofercie rozmiaru luster, którego nie produkowałby ów zakład, to taki zakład z pewnością wygra przetarg (jeśli w przetargu wystąpi wiele zakładów o majoryzującej ofercie, wygra ten, który zaproponuje najniższą cenę centymetra kwadratowego lustra). W przeciwnym razie ocena ofert będzie skomplikowana, a rozstrzygnięcie przetargu znacząco się opóźni. Licząc na uniknięcie jałowych dyskusji, Bajtazar poprosił Cię o napisanie programu, który stwierdzi, czy oferta któregoś z zakładów majoryzuje oferty pozostałych zakładów.</p>

### 입력 

 <p>Pierwszy wiersz wejścia zawiera jedną liczbę całkowitą <em>t</em> (1 ≤ <em>t</em> ≤ 10), oznaczającą liczbę przypadków testowych do rozważenia. Dalej następują opisy kolejnych przypadków testowych.</p>

<p>Pierwszy wiersz opisu zawiera jedną liczbę całkowitą <em>n</em> (2 ≤ <em>n</em> ≤ 100 000), oznaczającą liczbę zakładów produkcji luster, które złożyły oferty w przetargu organizowanym przez firmę Bajtazara. Każdy z kolejnych <em>n</em> wierszy zawiera po cztery liczby całkowite <em>w<sub>1</sub></em>, <em>w<sub>2</sub></em>, <em>h<sub>1</sub></em>, <em>h<sub>2</sub></em> (1 ≤ <em>w<sub>1</sub></em> ≤ <em>w<sub>2</sub></em> ≤ 10<sup>9</sup>, 1 ≤ <em>h<sub>1</sub></em> ≤ <em>h<sub>2</sub></em> ≤ 10<sup>9</sup>). Liczby te oznaczają, że dany zakład może wyprodukować lustra o dowolnej całkowitej szerokości <em>w</em> i wysokości <em>h</em> spełniających <em>w<sub>1</sub></em> ≤ <em>w</em> ≤ <em>w<sub>2</sub></em> oraz <em>h<sub>1</sub></em> ≤ <em>h</em> ≤ <em>h<sub>2</sub></em>.</p>

### 출력 

 <p>Twój program powinien wypisać na wyjście dokładnie <em>t</em> wierszy, zawierających odpowiedzi dla poszczególnych zestawów testowych. W <em>i</em>-tym z tych wierszy powinno znaleźć się jedno słowo <code>TAK</code> lub <code>NIE</code>, w zależności od tego, czy w przetargu wziął udział zakład, którego oferta majoryzuje oferty wszystkich pozostałych oferentów.</p>

