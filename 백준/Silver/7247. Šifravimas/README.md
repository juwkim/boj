# [Silver IV] Šifravimas - 7247 

[문제 링크](https://www.acmicpc.net/problem/7247) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘, 구현, 수학, 문자열

### 제출 일자

2023년 12월 26일 01:31:54

### 문제 설명

<p>Ignas ir Simonas kartu susidomėjo klasikine kriptografija ir nusprendė šifruoti vienas kitam žinučių tekstus. Jų sutartas šifravimo procesas toks:</p>

<ul>
	<li>Žinutėse naudoti tik šiuos simbolius ir juos sunumeruoti nuo 1 iki 29:
	<ul>
		<li>naudoti didžiąsias lotyniškas raides: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, sunumeruoti nuo 1 iki 26 abėcėlės tvarka;</li>
		<li>naudoti pabraukimo ženklą „ _ “ vietoje tarpo – numeris 27;</li>
		<li>naudoti kablelį „ , “ ir tašką „ . “ – numeriai 28 ir 29, atitinkamai.</li>
	</ul>
	</li>
	<li>Žinutę šifruojame po simbolį:
	<ol>
		<li>Simbolio numeris keliamas kubu, tada paimama liekana dalinant iš 29 ir prie gaunamos liekanos pridedamas 1.</li>
		<li>Randame naują simbolį, kuris atitinka pirmame punkte gautą skaičių. Tai bus mūsų užšifruotas simbolis.</li>
	</ol>
	</li>
	<li>Taip tęsiame su visais žinutės simboliais.</li>
</ul>

<p>Paprastumo delei pateiksime atitinkamą lentelę su simbolių numeriais.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9e551a43-9d7b-4f17-b781-a2909d44f7bf/-/preview/" style="width: 459px; height: 320px;"></p>

<p>Pavyzdžiui, tekstas „<code>GERI_ORAI.</code>“ pagal Igno ir Simono algoritmą bus užšifruotas kaip „<code>YJDEVLDBEA</code>“. Tai lengva patikrinti. Imkime pirmąją raidę <code>G</code>:</p>

<ul>
	<li>raidės <code>G</code> numeris yra 7,</li>
	<li>kurio kubas yra 7<sup>3</sup> = 343,</li>
	<li>kurio dalybos iš 29 liekana yra 24,</li>
	<li>prie kurio pridėjus 1 gausime 25,</li>
	<li>o numerį 25 turi raidė <code>Y</code>.</li>
</ul>

<p>Taigi, šifruodami <code>G</code> gauname <code>Y</code>. Analogiškai galime patikrinti ir kitų simbolių šifravimą.</p>

<p>Taškas „ <code>.</code> “, kurio numeris yra 29, užšifruojamas raide <code>A</code>. 29<sup>3</sup> dalijasi iš 29 ir todėl liekana bus 0, o pridėjus 1, turėsime 1, t.y. raidę <code>A</code>.</p>

<p>Vyresnis Igno brolis pastebėjo, kad toks šifravimo algoritmas, deja, labai lengvai „sulaužomas“, nes pagal šifruotą tekstą galima greitai atstatyti pradinį, t.y. jį dešifruoti.</p>

<p>Parašykite programą, kuri dešifruoja teksto eilutę, užšifruotą pagal Igno ir Simono algoritmą.</p>

### 입력 

 <p>Pirmoje duomenų eilutėje pateikta šifruoto teksto eilutė.</p>

### 출력 

 <p>Pateikite dešifruoto teksto eilutę.<span style="display: none;"> </span></p>

