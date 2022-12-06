# [Silver IV] Wlazł kotek na płotek - 8819 

[문제 링크](https://www.acmicpc.net/problem/8819) 

### 성능 요약

메모리: 32952 KB, 시간: 948 ms

### 분류

브루트포스 알고리즘(bruteforcing), 유클리드 호제법(euclidean), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Wlazł kotek na płotek i skacze.</p>

<p>Płotek składa się z <strong>N</strong> sztachetek rozmieszczonych równomiernie na planie okręgu. Kotek skacze po płotku co <strong>K</strong> sztachetek ( czyli dla <strong>N</strong> = 8 i <strong>K</strong> = 3 kotek skacze kolejno na sztachetki: 1, 4, 7, 2, ... ). Kotek skacze tak długo, jak długo staje na sztachetkach, których jeszcze nie odwiedzał. Kiedy tylko dotrze do sztachetki na którą kiedyś już skoczył, od razu schodzi z płotka.</p>

<p>Znając liczbę sztachetek <strong>N</strong> wyznacz wszystkie możliwe <strong>K</strong> ( 1 <= <strong>K</strong> <= <strong>N</strong> ) dla których kotek skacząc w opisany wyżej sposób odwiedza wszystkie sztachetki w płocie.</p>

### 입력 

 <p>W pierwsze linii znajduje się liczba zestawów testowych <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10). Następnie podawane są opisy kolejnych zestawów.</p>

<p>W jedynej linii zestawu znajduje się opisana w treści liczba naturalna <strong>N</strong> ( 1 <= <strong>N</strong> <strong> </strong><= 1000000 ).</p>

### 출력 

 <p>Dla każdego zestawu w osobnej linii wypisz wszystkie możliwe wartości <strong>K</strong> ( zgodnie z opisem w treści ) w kolejności rosnącej, oddzielając kolejne liczby spacjami.</p>

