# [Silver I] ... albo psikus! - 26755 

[문제 링크](https://www.acmicpc.net/problem/26755) 

### 성능 요약

메모리: 215536 KB, 시간: 300 ms

### 분류

조합론, 수학, 누적 합

### 제출 일자

2025년 8월 3일 21:34:29

### 문제 설명

<p>W Bajtocji panuje pewna tradycja, nieznana w innych zakątkach świata – na początku jesieni dzieci przebierają się w straszne kostiumy i chodzą od domu do domu, zbierając cukierki od mieszkańców.</p>

<p>Bajtek i Bitosia także planują wybrać się na zbieranie cukierków. Mieszkają oni przy bardzo długiej ulicy, która zawiera N domów mieszczących się po tej samej stronie drogi i ponumerowanych kolejno od 1 do N. Odwiedzali już tę ulicę wcześniej i wiedzą, dla każdego i = 1,2,...,N, że gdy odwiedzą i-ty dom, dostaną dokładnie Ci cukierków.</p>

<p>Jako że co roku wybuchały między nimi kłótnie o ostatniego cukierka, Bajtek i Bitosia postawili tym razem koniecznie zebrać parzystą liczbę cukierków. Ich planowana strategia to wybrać pewne dwa numery domów L i R, po czym odwiedzić wszystkie domy pomiędzy nimi, czyli L, L +1, ..., R−1, R. W ten sposób zbiorą dokładnie C<sub>L</sub> +C<sub>L+1</sub> +...+ C<sub>R−1</sub> +C<sub>R</sub>. cukierków.</p>

<p>Na ile różnych sposobów Bajtek i Bitosia mogą wybrać domy L i R tak aby zebrać parzystą liczbę cukierków?</p>

### 입력 

 <p>W pierwszym wierszu wejścia dana jest liczba N (1 ≤ N ≤ 1 000 000), oznaczająca liczbę domów przy ulicy. W kolejnym wierszu dane jest N liczb C<sub>1</sub>, C<sub>2</sub>, ..., C<sub>N</sub> (1 ≤ C<sub>i</sub> ≤ 10<sup>9</sup> dla 1 ≤ i ≤ N), gdzie C<sub>i</sub> oznacza liczbę cukierków, które dzieci mogą zebrać odwiedzając dom o numerze i.</p>

### 출력 

 <p>Wypisz jeden wiersz, zawierający liczbę możliwych par numerów domów (L,R), dla których dzieci zbiorą parzystą liczbę cukierków.</p>

