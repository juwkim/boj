# [Silver V] Skattkartan - 20861 

[문제 링크](https://www.acmicpc.net/problem/20861) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Paulina gillar Japan, jättemycket. Under en semester i Tokyo besöker hon en nöjespark där det finns en stor labyrint. För att navigera i labyrinten får Paulina en skattkarta som hon följer.</p>

<p>På skattkartan är varje ruta markerad med pilar för att visa åt vilket håll man ska gå från den rutan.</p>

<p>Paulina börjar alltid i den ruta som befinner sig längst upp till vänster på skattkartan, och följer därefter pilarna. I labyrinten finns det två olika mål: en bit smaskig laxsushi, samt en läskig samuraj. Det kan också hända att skattkartan leder runt Paulina i en oändlig cykel av rutor så hon aldrig når ett mål.</p>

<p>Kan du hjälpa Paulina att avgöra vilket mål hon når, eller om hon kommer gå runt i all oändlighet.</p>

### 입력 

 <p>Indatan börjar med en rad som innehåller antalet rader $R$ ($1 \le R \le 100$) i skattkartan. Därefter följer en rad som innehåller antalet kolumner $C$ ($1 \le C \le 100$) i skattkartan. Slutligen följer $R$ rader som alla innehåller $C$ tecken vardera -- själva skattkartan.</p>

<p>Följande tecken förekommer i skattkartan:</p>

<ul>
	<li>"<code><</code>" -- ruta med vänsterpil,</li>
	<li>"<code>></code>" -- ruta med högerpil,</li>
	<li>"<code>v</code>" -- ruta med nedåtpil,</li>
	<li>"$\wedge$" -- ruta med uppåtpil,</li>
	<li>"<code>A</code>" -- rutan sushin befinner sig på,</li>
	<li>"<code>B</code>" -- rutan samurajen befinner sig på.</li>
</ul>

<p>Paulina börjar på den första rutan i den första raden av skattkartan. Skattkartan är konstruerad så att Paulina aldrig kommer lämna labyrinten när hon följer pilarna.</p>

### 출력 

 <p>Ditt program ska skriva ut en enda rad med texten </p>

<ul>
	<li>"<code>sushi</code>" om hon når sushin genom att följa pilarna,</li>
	<li>"<code>samuraj</code>" om hon når samurajen genom att följa pilarna,</li>
	<li>"<code>cykel</code>" om hon kommer springa runt i all oändlighet genom att följa pilarna.</li>
</ul>

