# [Bronze II] Wymiana żarówki - 8846 

[문제 링크](https://www.acmicpc.net/problem/8846) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>Jak wiadomo, do wymiany żarówki często wystarcza jedna osoba. Jeśli sufit jest za wysoko, potrzebujemy już pięciu ludzi: jeden stoi na stole trzymając żarówkę a reszta kręci stołem.</p>

<p>Jeśli sufit jest jeszcze wyżej, można pójść o krok dalej: jedna osoba trzyma żarówkę, cztery osoby trzymają stół, a dodatkowo każda z tych czterech osób także stoi na stole, utrzymywanym przez kolejne cztery osoby. Razem daje to 1 + 4 + 16 =  21 osób. Metodę tę można oczywiście rozszerzać w zależności od wysokości sufitu.</p>

<p>Oblicz, ile osób potrzebnych jest do zbudowania konstrukcji o zadanej wysokości. Ponieważ wynik może być bardzo duży, wystarczy, że podasz jego resztę z dzielenia przez 500000009.</p>

### 입력 

 <p>Na wejściu znajduje się dokładnie jedna liczba całkowita A (1<=A<=1000000), oznaczająca ilość poziomów konstrukcji, jaką musimy osiągnąć.</p>

### 출력 

 <p>Minimalna liczba osób potrzebna do wymiany żarówki, podana modulo 500000009 (zamiast liczby, należy wypisać jej resztę z dzielenia przez 500000009).</p>

