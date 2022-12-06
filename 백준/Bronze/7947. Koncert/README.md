# [Bronze III] Koncert - 7947 

[문제 링크](https://www.acmicpc.net/problem/7947) 

### 성능 요약

메모리: 29200 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Ekipa realizująca koncert znanej gwiazdy muzyki pop stanęła przed nie lada problemem. Gwiazda zażyczyła sobie bowiem, aby podczas trwania koncertu została oświetlona na precyzyjnie określony i niebanalny kolor. Technicy ekipy używają do oświetlenia gwiazdy 10 reflektorów, które jednocześnie oświetlają ją z różnych kierunków w precyzyjnie dobranych kolorach, aby efekt kompozycyjny całej sceny był zachowany. Musisz pomóc technikom określić jaki kolor zostanie uzyskany w centralnym miejscu, w którym znajduje się gwiazda.</p>

### 입력 

 <p>Pierwsza linia wejścia zawiera małą liczbę całkowitą z – liczbę zestawów danych występujących kolejno po sobie. Opis jednego zestawu jest następujący:</p>

<p>Składa się on z 10 linii, każda złożona z trzech liczb całkowitych r, g, b oddzielonych spacjami (0 ≤ r, g, b ≤ 255) oznaczającymi odpowiednio zawartość trzech podstawowych barw światła w kolejnych reflektorach. Przyjmujemy, że kolor światła oświetlający gwiazdę będzie prostym uśrednieniem kolorów pochodzących od wszystkich 10 używanych reflektorów.</p>

### 출력 

 <p>Dla każdego zestawu danych wypisz trzy liczby całkowite r, g, b stanowiące opis trzech składowych koloru światła padającego na gwiazdę, będące uśrednieniem światła padającego z reflektorów. Podaj wynik uwzględniając zaokrąglenie matematyczne do najbliższej liczby całkowitej, tzn. cyfry od 1 do 4 w dół, natomiast od 5 do 9 w górę.</p>

