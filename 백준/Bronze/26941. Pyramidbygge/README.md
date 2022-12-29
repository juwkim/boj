# [Bronze III] Pyramidbygge - 26941 

[문제 링크](https://www.acmicpc.net/problem/26941) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="width: 200px; height: 123px;"></p>

<p style="text-align: center;">Figure 1: Ett exempel på en pyramid av höjd 3 med 35 block.</p>

<p>När man ska inleda ett större projekt, exempelvis bygga en pyramid, är det bäst att tänka efter en gång extra. Du ska skriva ett program som beräknar hur hög pyramid man kan bygga om man har tillgång till ett visst antal stenblock.</p>

<p>Vi antar att pyramiden är kompakt, d.v.s. det finns inga hålrum inuti. Vidare byggs den enligt principen i figure 1. Varje lager är alltså kvadratiskt med en sidlängd som är två block mindre än det underliggande lagrets. Det översta lagret består alltid av ett ensamt block.</p>

<p>Det gör ingenting om det blir block över, men det får inte saknas ett enda block.</p>

### 입력 

 <p>Indata består av ett enda heltal $N$ ($1 \le N \le 100\,000\,000$): antal tillgängliga block.</p>

### 출력 

 <p>Programmet ska skriva ut en rad med ett heltal: höjden för den största pyramid som kan byggas med som högst $N$ block.</p>

