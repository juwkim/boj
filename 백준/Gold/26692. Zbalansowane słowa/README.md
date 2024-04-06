# [Gold I] Zbalansowane słowa - 26692 

[문제 링크](https://www.acmicpc.net/problem/26692) 

### 성능 요약

메모리: 234144 KB, 시간: 468 ms

### 분류

조합론, 자료 구조, 해시를 사용한 집합과 맵, 수학

### 제출 일자

2024년 2월 3일 02:34:29

### 문제 설명

<p>Wszędzie najważniejsza jest równowaga. Jest ona szczególnie ważna przy organizacji konkursów programistycznych i mamy nadzieję, że jury tegorocznych Potyczek Algorytmicznych dobrze o tym wie.</p>

<p>Powiemy, że słowo jest zbalansowane, jeśli każda litera, która w nim występuje, występuje w nim tyle samo razy. Np. słowa <code>w</code>, <code>mama</code>, <code>potyczki</code> i <code>aabbcbcccbaa</code> są zbalansowane, podczas gdy słowa <code>oko</code>, <code>algorytmistrz</code> i <code>abcba</code> nie są. Mając dane długie słowo składające się jedynie ze znaków <code>a</code>, <code>b</code> oraz <code>c</code>, policz, ile jego niepustych podsłów (czyli spójnych przedziałów liter) jest zbalansowanych.</p>

<p>Uwaga: Dwa takie same słowa, występujące jako podsłowa na różnych pozycjach, liczymy wielokrotnie. Np. w słowie oko zbalansowanymi podsłowami są <code>o</code>, <code>k</code>, <code>o</code>, <code>ok</code> oraz <code>ko</code>.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się niepuste słowo, o długości nieprzekraczającej 300 000, składające się jedynie ze znaków <code>a</code>, <code>b</code> oraz <code>c</code>.</p>

### 출력 

 <p>Na wyjściu powinna znaleźć się jedna liczba całkowita, oznaczająca liczbę zbalansowanych podsłów wejściowego słowa.</p>

