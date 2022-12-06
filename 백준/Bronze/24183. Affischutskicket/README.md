# [Bronze IV] Affischutskicket - 24183 

[문제 링크](https://www.acmicpc.net/problem/24183) 

### 성능 요약

메모리: 30864 KB, 시간: 76 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>VE OCH FASA! PostNord har för det $1337$:e året i rad höjt portot, vilket riskerar att bräcka Programmeringsolympiadens budget.</p>

<p>Varje år skickar PO ut affischer till ca $450$ gymnasieskolor. Ett utskick består av tre saker: </p>

<ul>
	<li>ett kuvert av C4-storlek ($229\text{ mm} \times 324\text{ mm}$)</li>
	<li>två affischer av A3-storlek ($297\text{ mm} \times 420\text{ mm}$)</li>
	<li>ett informationsblad av A4-storlek ($210\text{ mm} \times 297\text{ mm}$)</li>
</ul>

<p>Det är mycket viktigt att brevet väger högst $50$ gram, eftersom portot annars blir dubbelt så högt. För att klara denna magiska viktgräns kan PO styra över vilken sorts papper som används för de tre sakerna. Varje sort har en ytvikt (vikt per area) som typiskt anges i $\frac{\text{gram}}{\text{m}^2}$. Notera att kuvertet består av <strong>två sammanklistrade ark</strong> av C4-storlek, medan ytvikter och ovanstående mått gäller för <em>ett ark</em>.</p>

<p>Skriv ett program som räknar ut den totala vikten för ett brev.</p>

### 입력 

 <p>Indatan består av tre heltal mellan $50$ och $200$, ytvikterna i $\frac{\text{gram}}{\text{m}^2}$ för sorterna som används till kuvertet, affischerna respektive informationsbladet.</p>

### 출력 

 <p>Skriv ut ett enda decimaltal: vikten på ett fullständigt brevutskick i gram. Svaret ska anges med minst $3$ decimalers noggrannhet (d.v.s. vara inom $5 \cdot 10^{-4}$ från rätt svar).</p>

