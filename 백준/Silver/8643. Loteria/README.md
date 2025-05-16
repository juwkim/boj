# [Silver I] Loteria - 8643 

[문제 링크](https://www.acmicpc.net/problem/8643) 

### 성능 요약

메모리: 111784 KB, 시간: 104 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 5월 17일 05:41:53

### 문제 설명

<p>Przedsiębiorstwo Bajtocki Lotek specjalizuje się w przeprowadzaniu gier liczbowych i loterii pieniężnych, wśród których największą popularnością cieszy się loteria o nazwie <i>Gra w litery</i>. Również Bajtazar postanowił spróbować szczęścia w grze.</p>

<p>Kupon do <i>Gry w litery</i> zawiera <em>n</em> pozycji. Na każdej z nich można zakreślić jedną z trzech liter: A, B lub C. Poniższy rysunek przedstawia przykładowe wypełnienie kuponu dla <em>n</em> = 10:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/bcb0012e-d022-4b06-8d69-b4b5a6494915/-/preview/" style="width: 250px; height: 76px;"></p>

<p>Losowanie zwycięzców przeprowadza się przy pomocy maszyny losującej, w której znajduje się 3<em>n</em> metalowych kulek trzech rodzajów: <em>n</em> kulek z literą A, <em>n</em> z literą B i <em>n</em> z literą C. W górnej części maszyny jest rozmieszczonych równomiernie <em>n</em> otworów o średnicy mniejszej niż średnica kulki. W pewnym momencie losowania włączany jest mechanizm pneumatyczny, który powoduje, że do każdego z otworów przyssana zostaje jedna kulka. Wypisując kolejno litery znajdujące się na wylosowanych kulkach, otrzymuje się ciąg złożony z <em>n</em> liter, stanowiący wynik losowania. Szczęśliwi właściciele kuponów, na których zakreślono taki właśnie ciąg liter, zdobywają nagrodę główną - milion bajtalarów do podziału. Na rysunku przedstawiono wynik losowania, przy którym powyższy kupon uzyskałby główną nagrodę.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e489327b-92ed-4ae8-87d7-d3f7f4676169/-/preview/" style="width: 300px; height: 46px;"></p>

<p>Bajtazar nabył kupon i zakreślił na nim <em>n</em> liter. Zanim jednak zdążył złożyć swój kupon w kolekturze, w mediach pojawił się przeciek, że losowanie w <i>Grze w litery</i> nie jest do końca uczciwe. Zbadano bowiem, że kulki tego samego rodzaju - czyli z tą samą literą - odpychają się i nigdy nie ustawią się przy sąsiednich otworach w trakcie losowania (np. układ kulek przedstawiony na powyższym rysunku nie byłby możliwy).</p>

<p>Bajtazar, dowiedziawszy się o tym, postanowił zmienić ciąg <em>n</em> liter, który wskazał, tak aby żadne dwie kolejne litery w ciągu nie były takie same. Żeby nie kusić losu, chciałby zmienić możliwie najmniej liter w swoim ciągu. Pomóż Bajtazarowi ustalić, ile liter musi zmienić.</p>

### 입력 

 <p>Pierwszy wiersz wejścia zawiera jedną liczbę całkowitą <em>n</em> (2 ≤ <em>n</em> ≤ 500 000). Drugi wiersz zawiera ciąg złożony z <em>n</em> znaków A, B i/lub C. W ciągu tym występuje co najmniej jedna para sąsiadujących ze sobą takich samych liter.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą dodatnią - minimalną liczbę liter w ciągu, które trzeba zmienić, tak aby żadne dwie takie same litery nie występowały w nim obok siebie.</p>

