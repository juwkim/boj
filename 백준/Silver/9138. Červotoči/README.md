# [Silver V] Červotoči - 9138 

[문제 링크](https://www.acmicpc.net/problem/9138) 

### 성능 요약

메모리: 116868 KB, 시간: 256 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Do stolů ve školce se pustili červotoči a začali v nich vyhlodávat chodbičky. Aby bylo možno správně nadávkovat ochranný prostředek, je třeba zjistit, kolik dřeva již sežral nejžravější červotoč (když by totiž červotoč sežral příliš velkou dávku ochranného prostředku, mohl by zmutovat a stát se ještě nebezpečnějším). Protože každý červotoč má charakteristický způsob tunelování, můžeme snadno zjistit, kterou chodbičku vyhlodal který červotoč.</p>

### 입력 

 <p>Vstup se skládá z několika bloků. Každý blok vyjma posledního začíná třemi čísly <var>R</var>, <var>S</var> a <var>C</var>, kde 1 ≤ <var>R</var>,<var>S</var> ≤ 250, 1 ≤ <var>C</var> ≤ 26. Poslední blok začíná třemi nulami a nemá být dále zpracováván. V bloku pak následuje <var>C</var> řádek se jmény červotočů. Jméno každého červotoče začíná velkým písmenem, za kterým následuje nejvýše šedesát malých písmen. Předpokládejte, že počáteční písmena jmen různých červotočů jsou různá. Za jmény v bloku následuje <var>R</var> řádek popisujících prožraný stůl. Na každém řádku je <var>S</var> znaků. Každý ze znaků je buď <code>*</code> (značí, že tato část stolu dosud nebyla zkonzumována), nebo počáteční písmeno jména některého z červotočů (značí, že červotoč, jehož jméno začíná na příslušné písmeno, sežral tuto část stolu). Ne každý červotoč musí sežrat nějakou část stolu. Oblast vyhlodaná jedním červotočem je souvislá (červotoč umí hlodat v osmi směrech).</p>

### 출력 

 <p>Na výstup má váš program pro každý blok na vstupu vypsat text "<code>Nejzravejsi cervotoc je XXXX.</code>", kde <code>XXXX</code> bude nahrazeno jménem červotoče, který sežral nejvíce částí stolu. Můžete předpokládat, že takovýto červotoč bude určen jednoznačně.</p>

