# [Bronze III] Taikinys - 30349 

[문제 링크](https://www.acmicpc.net/problem/30349) 

### 성능 요약

메모리: 109240 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘, 구현, 수학

### 제출 일자

2024년 9월 27일 22:02:53

### 문제 설명

<p>Už stačiakampės šaudymo angos stovi stačiakampio formos taikinys. Abu stačiakampiai sudalinti į 1 × 1 dydžio langelius.</p>

<p>Tiesė, einanti per apatinius kairiuosius stačiakampių kampus, yra statmena jų plokštumoms, bei apatinės abiejų stačiakampių kraštinės yra lygiagrečios.</p>

<p>Susitarsime, kad abiejų stačiakampių apatinio kairiojo langelio koordinatės yra (0, 0).</p>

<p>omas gali paleisti strėlę iš bet kurio angos langelio (X<sub>p</sub>, Y<sub>p</sub>). Deja, vėjas nupūs strėlę į šoną per (X, Y) langelių. T. y. iššovus iš langelio (X<sub>p</sub>, Y<sub>p</sub>), strėlė pataikys į langelį (X<sub>p</sub> + X, Y<sub>p</sub> + Y ).</p>

<p>Reikia pataikyti strėlę į taikinio langelį (0, 0). Jeigu strėlė pataiko į taikinio langelį (T<sub>X</sub>, T<sub>Y</sub>), yra skaičiuojami baudos taškai B = T<sub>X</sub> + T<sub>Y</sub>.</p>

<p>Įmanoma, kad strėlė apskritai nepataikys į taikinį.</p>

<p>Padėkite Adomui suskaičiuoti, ar jis gali apskritai pataikyti į taikinį ir jei taip – kiek mažiausiai baudos taškų jis gali gauti.</p>

### 입력 

 <p>Pirmoje eilutėje pateiktas angos plotis M ir aukštis N. Antroje eilutėje pateiktas taikinio plotis A ir aukštis B. Trečioje eilutėje yra vėjo poslinkį nusakantys skaičiai X ir Y . Visi pateikti skaičiai yra sveikieji.</p>

### 출력 

 <p>Rezultatas yra vienas sveikasis skaičius – minimali galima baudos vertė, kurią Adomas galėtų gauti paleidęs strėlę iš šaudymo angos.</p>

<p>Jeigu dėl vėjo neįmanoma pataikyti į taikinį, išveskite žodį <code>NEPATAIKYS</code>.</p>

