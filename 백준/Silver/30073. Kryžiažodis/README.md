# [Silver IV] Kryžiažodis - 30073 

[문제 링크](https://www.acmicpc.net/problem/30073) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵

### 제출 일자

2023년 12월 26일 03:06:58

### 문제 설명

<p><img alt="" src="https://upload.acmicpc.net/99a5a811-b38c-45ca-9b59-ef1273ca96af/-/preview/" style="width: 163px; height: 236px; float: right;">Brigita nusprendė sudaryti kryžiažodį savo jaunesniajam broliui, o kad užduotis nepasirodytų jam per sunki, kryžiažodis bus tik iš trijų žodžių. Tinkamas kryžiažodis tenkina šias taisykles:</p>

<ul>
	<li>Kryžiažodyje žodžiai rašomi eilute (horizontaliai) arba stulpeliu (vertikaliai)</li>
	<li>Jei du žodžiai kertasi (persidengia), jie kertasi ties lygiai viena raide</li>
	<li>Kiekvienas žodis kertasi su bent vienu kitu žodžiui, t.y. visi trys kryžiažodžio žodžiai susiję.</li>
	<li>Jei žodis kertasi su dviem kitais žodžiais, tai jis turi kirstis skirtingose vietose. Pavyzdžiui, žodis <code>KURMIS</code> su žodžiais <code>KAVA</code> ir <code>KELMAS</code> negali kirstis ties raide <code>K</code>.</li>
</ul>

<p>Padėkite Brigitai sudaryti kryžiažodį iš trijų pateiktų žodžių. Jei egzistuoja keli galimi sprendiniai, pateikite bet kurį.</p>

### 입력 

 <p>Trijose eilutėse įrašyta po vieną žodį, sudarytą iš didžiųjų lotyniškų raidžių. Žodžiai tokie, kad iš pateiktų žodžių visada bus galima sudaryti taisykles tenkinantį kryžiažodį.</p>

### 출력 

 <p>Atskirose eilutėse išveskite visų susikertančių žodžių poras ir raidžių numerius, kur jie kertasi: išveskite pirmąjį žodį ir raidės, kur jis kertasi su antruoju, numerį, tada antrąjį žodį ir raidės, kur jis kertasi su pirmuoju, numerį.</p>

<p>Pavyzdžiui, jei žodžiai <code>VANDUO</code> ir <code>PIENAS</code> kryžiažodyje kertasi ties raide <code>A</code>, tai išveskite: <code>VANDUO 2 PIENAS 5</code></p>

