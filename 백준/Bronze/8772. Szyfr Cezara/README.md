# [Bronze II] Szyfr Cezara - 8772 

[문제 링크](https://www.acmicpc.net/problem/8772) 

### 성능 요약

메모리: 39596 KB, 시간: 292 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Hektor zapoznał się niedawno z metodą szyfrowania wiadomości nazywaną "szyfrem Cezara". To metoda opierająca się na pozycjach, jakie poszczególne litery zajmują w alfabecie. W zadaniu będziemy rozważać standardowy alfabet angielski złożony z 26 liter:</p>

<pre>a b c d e f g h i j k l m n o p q r s t u v w x y z</pre>

<p>Aby zaszyfrować wiadomość szyfrem Cezara, należy na początku wybrać liczbę z przedziału od 0 do 25 (chociaż liczba 0 będzie skutkować wyjątkowo nieskutecznym szyfrowaniem), którą nazwiemy <strong>K</strong>. Następnie należy każdą z liter wiadomości zastąpić literą położoną o <strong>K</strong> pozycji dalej w alfabecie. W przypadku, w którym litera położona o <strong>K</strong> pozycji dalej od zadanej wypada poza alfabet, należy uznać, że alfabet powtarza się w nieskończoność, tj. zaraz po literze "z" występuje ponownie "a", następnie "b", etc.</p>

<p>Przykładowo, dla <strong>K</strong> = 2, wiadomość "zoska" zostanie zaszyfrowana jako "bqumc".</p>

<p>Hektor przesłał Wiktorowi wiadomość zaszyfrowaną szyfrem Cezara, nie podając jednak jednak wartości <strong>K</strong>, której użył do szyfrowania. Zamiast tego, wraz z wiadomością przesłał Wiktorowi informację o tym, na jaką literę zaczynała się przesyłana wiadomość przed zaszyfrowaniem. Czy taka informacja wystarczy do odszyfrowania wiadomości?</p>

<p>Napisz program, który znając pierwszą literę pierwotnej wiadomości i jej wersję zaszyfrowaną opisanym wyżej szyfrem, odszyfruje wiadomość.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) opisująca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy. Opis każdego zestawu składa się z trzech linii.</p>

<p>Pierwsza linia opisu zestawu testowego zawiera liczbę naturalną <strong>N</strong> ( 1 <= <strong>N</strong> <= 1000000), oznaczającą liczbę liter zaszyfrowanej wiadomości.</p>

<p>W drugiej linii opisu zestawu znajduje się <strong>N</strong> małych liter alfabetu angielskiego, które stanowią zaszyfrowaną wiadomość od Hektora.</p>

<p>Trzecia linia opisu zestawu zawiera jedną małą literę alfabetu angielskiego - jest to pierwsza litera pierwotnej wiadomości Hektora.</p>

### 출력 

 <p>Dla każdego testu należy w osobnej linii wypisać odszyfrowaną wiadomość od Hektora.</p>

