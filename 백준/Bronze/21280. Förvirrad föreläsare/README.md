# [Bronze III] Förvirrad föreläsare - 21280 

[문제 링크](https://www.acmicpc.net/problem/21280) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>Bjarki undervisar på en kurs på universitetet, men är inte särskilt organiserad av sig. Särskilt förvirrad blir han av att antalet föreläsningar varierar från vecka till vecka.</p>

<p>Första veckan håller Bjarki sina $A$ schemalagda föreläsningar. Men varje vecka utom den första kommer han att förutsätta att schemat är likadant som det var föregående vecka. Andra veckan håller han alltså exakt $A$ föreläsningar igen. Därför kan det ibland hända att Bjarki håller lektion inför tomt klassrum och ibland att han inte dyker upp när han ska. I slutet av veckan får han dock ett argt brev av sin chef med vilka tider han skulle hållit föreläsningar och kommer istället att använda dessa tider veckan därpå. </p>

<p>Skriv ett program som, givet antalet schemalagda föreläsningar under $N$ veckor, skriver ut antalet föreläsningar Bjarki kommer hålla inför tomma klassrum samt antalet föreläsningar Bjarki inte dyker upp på.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 660px; height: 249px;"></p>

<p style="text-align: center;">Figur 1. Schemat i det första exemplet. F markerar schemalagda föreläsningar. En blå cirkel markerar att Bjarki håller lektionen inför tomt klassrum och en röd triangel markerar att han inte dyker upp. <strong>Förklaring:</strong> Första veckan har Bjarki alltid koll på vilka föreläsningar han ska hålla. Veckan därpå tror han att han bara ska hålla en föreläsning, och missar därför två stycken. Tredje veckan håller han tre föreläsningar, varav en inför tomt klassrum, och sista veckan missar han två föreläsningar. Totalt har han hållt 1 tom föreläsning och missat 4 föreläsningar.</p>

### 입력 

 <p>Först kommer talet $N$ på en egen rad, där $1\le N \le 9$. Därefter kommer $N$ heltal, antalet schemalagda föreläsningar under var och en av veckorna.</p>

<p>Det kan aldrig vara mer än 10 föreläsningar under en vecka och tiderna fylls alltid på från början av veckan utan luckor (se figuren ovan). </p>

### 출력 

 <p>Skriv ut antalet tomma föreläsningar Bjarki har hållt, ett mellanslagtecken, därefter antalet föreläsningar Bjarki har missat.</p>

