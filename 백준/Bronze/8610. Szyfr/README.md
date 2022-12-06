# [Bronze II] Szyfr - 8610 

[문제 링크](https://www.acmicpc.net/problem/8610) 

### 성능 요약

메모리: 48756 KB, 시간: 548 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Jaś otrzymał sekretną wiadomość. Jest ona ciągiem wielkich liter alfabetu łacińskiego (który składa się z liter: <code>ABCDEFGHIJKLMNOPQRSTUVWXYZ</code>). Wie, że do jej zakodowania użyto szyfru Cezara. Jest to szyfr przesuwający kolejne litery wiadomości o określoną, stałą liczbę znaków w alfabecie. Litery z końca alfabetu stają się wówczas literami z jego początku. Dla przykładu, w wyniku zaszyfrowania wiadomości</p>

<p align="center"><code>ABCEGIKMOQSUVWXYZ</code></p>

<p>szyfrem Cezara z przesunięciem $4$, otrzymuje się wiadomość</p>

<p align="center"><code>EFGIKMOQSUWYZABCD</code></p>

<p>Jaś chciałby odszyfrować wiadomość. Nie wie niestety, jakiego dokonano w niej przesunięcia. Wielkie doświadczenie językowe Jasia pozwala mu jednak przewidzieć, jaka litera występowała najczęściej w oryginalnym tekście. Szczęście, które mu zawsze towarzyszy, sprawiło także, że taka litera jest tylko jedna - tzn. nie ma dwóch takich liter w oryginalnym tekście, które jednocześnie występowałyby największą liczbę razy.</p>

<p>Pomóż Jasiowi złamać szyfr, czyli odtworzyć oryginalną wiadomość.</p>

### 입력 

 <p>W pierwszym wierszu standardowego wejścia znajdują się: liczba całkowita $n$ ($1 ≤ n ≤ 1\,000\,000$) oznaczająca długość wiadomości oraz znak $c$ - wielka litera alfabetu łacińskiego występująca najczęściej w oryginalnej wiadomości; $n$ i $c$ są oddzielone pojedynczym odstępem. W drugim wierszu wejścia znajduje się zakodowana wiadomość, składająca się z $n$ wielkich liter alfabetu łacińskiego, bez jakichkolwiek odstępów.</p>

### 출력 

 <p>Program powinien wypisać na standardowe wyjście jeden wiersz, zawierający odszyfrowaną oryginalną wiadomość. Możesz założyć, że jednoznaczne odtworzenie tej wiadomości będzie zawsze możliwe.</p>

