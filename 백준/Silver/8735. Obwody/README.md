# [Silver V] Obwody - 8735 

[문제 링크](https://www.acmicpc.net/problem/8735) 

### 성능 요약

메모리: 191824 KB, 시간: 1300 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Jaś na urodziny dostał komplet magicznych elektrycznych kabelków. Każdy kabelek składa się z drutu oraz bateryjki. <em>i</em>-ty drut może wytrzymać napięcie <em>d<sub>i</sub></em> woltów, a <em>i</em>-ta bateryjka ma napięcie <em>b<sub>i</sub></em> woltów.</p>

<p>Jasio buduje z kabelków obwody: wybiera druty, skręca je razem tworząc grubszy drut i robi z niego kółko. W kółku napięcie jest sumą napięć wszystkich bateryjek, a skręcony drut może wytrzymać napięcie będące sumą napięć, które mogą wytrzymać poszczególne druty.</p>

<p>Jaś buduje obwód tak, aby zrobione kółko nie przepaliło się. Z ilu maksymalnie kabelków może się ono składać?</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba całkowita <em>n</em> (1 ≤ <em>n</em> ≤ 500 000), oznaczająca liczę drutów. W <em>n</em> następnych linijkach pary liczb <em>d<sub>i</sub></em>, <em>b<sub>i</sub></em> opisujące kolejne druty (0 ≤ <em>d<sub>i</sub></em>, <em>b<sub>i</sub></em> ≤ 10<sup>6</sup>).</p>

### 출력 

 <p>W jedynej linijce powinna znaleźć się liczba całkowita oznaczająca maksymalna liczbę drutów tworzących kółko.</p>

