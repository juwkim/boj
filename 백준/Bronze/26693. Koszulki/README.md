# [Bronze I] Koszulki - 26693 

[문제 링크](https://www.acmicpc.net/problem/26693) 

### 성능 요약

메모리: 115012 KB, 시간: 152 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Gotowi na walkę o koszulki Potyczek Algorytmicznych 2021? Zazwyczaj rozdajemy je uczestnikom, którzy uplasowali się na miejscach od 1 do 256 w rankingu dywizji B+C, w którym zawodników porównujemy, przede wszystkim patrząc na sumę punktów zdobytych za zadania z dywizji B oraz dywizji C, a przy remisie bierzemy pod uwagę również dokładny rozkład punktów za poszczególne zadania.</p>

<p>Czasem jesteśmy w stanie zrobić wyjątek i rozdać nawet więcej niż 256 koszulek, gdyż chcielibyśmy spełnić dodatkowy warunek mówiący, że jeśli uczestnik A zdobył co najmniej tyle punktów co uczestnik B i uczestnik B otrzyma koszulkę, to uczestnik A również ją dostanie, bez względu na dokładny rozkład punktów.</p>

<p>W praktyce nie zawsze można spełnić wspomniany dodatkowy warunek, gdyż mogłoby to oznaczać, że musielibyśmy rozdać o wiele więcej koszulek niż planowaliśmy. Jest to jeden z powodów, dla którego zachęcamy zawodników, by starali się zdobywać punkty, gdzie tylko się da, wysyłając również rozwiązania o nieoptymalnej złożoności czasowej (które często mogą liczyć na częściową liczbę punktów, nawet jeśli nie zaznaczono tego wyraźnie w treści). Wygładza to ranking oraz uszczęśliwia wszystkich zainteresowanych (a szczególnie organizatorów).</p>

<p>Gdyby w Potyczkach wzięło udział n uczestników, organizatorzy chcieliby rozdać co najmniej k koszulek, a uczestnicy zdobyliby kolejno a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, . . . , a<sub>n</sub> punktów, to ile koszulek musieliby co najmniej rozdać organizatorzy, aby spełnić również dodatkowy warunek?</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajdują się dwie liczby całkowite n i k (1 ≤ k ≤ n ≤ 2000), oznaczające odpowiednio liczbę uczestników oraz minimalną liczbę koszulek, które chcą rozdać organizatorzy.</p>

<p>Drugi wiersz zawiera ciąg n liczb całkowitych a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, . . . , a<sub>n</sub> (1 ≤ a<sub>i</sub> ≤ 120), gdzie ai oznacza liczbę punktów zdobytych przez i-tego zawodnika.</p>

### 출력 

 <p>Na wyjściu powinna znaleźć się jedna liczba całkowita, oznaczająca minimalną liczbę koszulek, które muszą rozdać organizatorzy, aby spełnić dodatkowy warunek.</p>

