# [Silver V] Ekscentrična enkripcija - 25131 

[문제 링크](https://www.acmicpc.net/problem/25131) 

### 성능 요약

메모리: 114820 KB, 시간: 116 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Gospodin Malnar jučer je održao predavanje o Cezarovoj šifri te zaključio da bi bila pogodna za šifriranje njegovih tajnih poruka. No, kako se ipak radi o Gospodinu Malnaru, odlučio ju je malo unaprijediti te stvorio takozvanu <em>Malnarovu šifru</em>. Ključ se sastoji od tri broja $a$, $b$, $c$ ($0 ≤ a, b, c < 26$). Za zadanu riječ engleske abecede S, Gospodin Malnar prvo slovo ciklički pomakne za $a$, drugo za $b$, treće za $c$, i ponovno četvrto za $a$, peto za $b$ te tako dokgod nije šifrirao cijelu riječ te time dobio novu riječ T.</p>

<p>Ciklički pomak za jedno mjesto pretvara slovo $a$ u slovo $b$, slovo $b$ u slovo $c$ i sve do slova z koje pretvara u slovo $a$. Ciklički pomak za neki drugi prirodan broj primjena je cikličkog pomaka za jedan taj broj puta, odnosno ciklički pomak za $0$ ne mijenja ni jedan znak.</p>

<p>Sada Gospodina Malnara zanima za par riječi S i T postoji li ključ takav da se šifriranjem riječi S Malnarovom šifrom dobije riječ T. U slučaju da postoji takav ključ, moli vas da ispišete neki.</p>

### 입력 

 <p>U prvom retku nalazi se riječ $S$ ($3 ≤ |S| ≤ 3 · 10^5$).</p>

<p>U drugom retku nalazi se riječ $T$ ($3 ≤ |T| ≤ 3 · 10^5$).</p>

### 출력 

 <p>Potrebno je ispisati tri broja $a$, $b$, $c$ ako postoji takav ključ, odnosno $-1$ ako ne postoji. Ako postoji više točnih ključeva, moguće je ispisati bilo koji.</p>

