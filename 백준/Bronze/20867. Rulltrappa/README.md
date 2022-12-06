# [Bronze IV] Rulltrappa - 20867 

[문제 링크](https://www.acmicpc.net/problem/20867) 

### 성능 요약

메모리: 30864 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Paulina Osqulda (Osqulda är en studentikos benämning på teknologer som studerar vid Kungliga Tekniska högskolan i Stockholm, se <a href="https://sv.wikipedia.org/wiki/Osquar_och_Osqulda">https://sv.wikipedia.org/wiki/Osquar_och_Osqulda</a>.) pluggar på KTH i Stockholm, och åker varje morgon till skolan via tunnelbanan. När hon kommer fram till sin tunnelbanestation måste hon åka upp längs en rulltrappa för att komma ut.</p>

<p>I rulltrappan bildas det ofta två olika köer. På den högra sidan av trappan ställer sig folk som vill stå still i rulltrappan, medan man ställer sig på den vänstra sidan om man föredrar att gå i rulltrappan (för att komma upp snabbare).</p>

<p>Paulina har märkt att det oftast bildas en <em>jättelång</em> kö till den vänstra sidan av rulltrappan, eftersom alla är så stressade till jobbet och vill kunna gå snabbt upp för rulltrappan. På sista tiden har hon funderat på om det kanske rentav skulle gå snabbare att istället välja den högra kön, eftersom kön där ofta är kortare.</p>

<p>Rulltrappan är totalt $M$ trappsteg lång. Om man står i rulltrappan färdas man $S$ trappsteg per sekund uppåt i rulltrappan. Om man istället går i rulltrappan färdas man $G$ trappsteg per sekund uppåt.</p>

<p>Totalt kan $A$ personer per sekund börja gå i rulltrappan ur den vänstra kön, medan $B$ personer per sekund kan ställa sig på rulltrappan ur den högra kön. Detta betyder att i början av förloppet går en person på rulltrappan. Innan en ny person går på rulltrappan måste denna vänta $\frac{1}{A}$ (resp $\frac{1}{B}$ sekunder) för att kunna gå på rulltrappan.</p>

<p>Den vänstra kön är för närvarande $L$ personer lång, och den högra är $R$ personer lång.</p>

<p>Hjälp Paulina avgöra vilken kö hon ska ställa sig i, för att så snabbt som möjligt nå rulltrappans topp.</p>

### 입력 

 <p>Den första raden i indatat består av heltalen $M, S, G$ som är beskrivna i uppgiften. Det gäller att $30 \le M \le 200$, $1 \le S \le G \le M$.</p>

<p>Nästa rad innehåller decimaltalen $A, B$ som är beskrivna i uppgiften. Det gäller att $0.1 \le A, B \le 1$.</p>

<p>Den sista raden innehåller heltalen $L, R$ som är beskrivna i uppgiften. Det gäller att $0 \le L, R \le 100$.</p>

### 출력 

 <p>Skriv ut <code>latmask</code> om det snabbaste alternativet är att välja den högra kön och stå i rulltrappan, eller <code>friskus</code> om det snabbaste alternativet är att välja den vänstra kön och gå i rulltrappan.</p>

<p>Det är garanterat att tiden det tar för Paulina att åka upp för rulltrappan skiljer sig med minst 1 sekund mellan de två köerna, så du behöver aldrig bry dig om fallet när båda alternativen är lika snabba.</p>

