# [Silver II] Sniegas - 30343 

[문제 링크](https://www.acmicpc.net/problem/30343) 

### 성능 요약

메모리: 113524 KB, 시간: 120 ms

### 분류

구현, 누적 합

### 제출 일자

2025년 8월 7일 00:39:41

### 문제 설명

<p>Naktį daug snigo, todėl Jonas su draugais nusprendė pažaisti sniego mūšį. Kiekvienas užėmė tam tikrą poziciją ir mūšis tuoj prasidės.</p>

<p>Mūšio lauką aprašo N sveikųjų skaičių v<sub>i</sub>, kurie žymi sniego pusnių aukščius. Kuo v<sub>i</sub> yra didesnis, tuo i-oji pusnis yra aukštesnė.</p>

<p>Metęs sniego gniūžtę iš pozicijos A, Jonas gali pataikyti į draugą, esantį pozicijoje B, jeigu tarp jo ir draugo nėra pusnių, aukštesnių už min(v<sub>A</sub>, v<sub>B</sub>).</p>

<p>Žemiau pateiktame pavyzdyje Jonas (pozicija 5, aukštis 5) gali pataikyti į Mantą (pozicija 2, aukštis 4), bet negali pataikyti į Astą (pozicija 7, aukštis 2).</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/622e91e4-db79-4569-b8aa-2e8641b87008/-/preview/" style="width: 310px; height: 195px;"></p>

<p>Žinodami, kaip atrodo sniego mūšio laukas, kur yra Jono bei jo draugų pozicijos, apskaičiuokite, į kelis draugus Jonas gali pataikyti mesdamas sniego gniūžtes.</p>

### 입력 

 <p>Pirmoje eilutėje pateikti trys sveikieji skaičiai: mūšio lauko dydis N, Jono draugų skaičius M (neskaičiuojant Jono) ir Jono pozicija A.</p>

<p>Antroje eilutėje yra N sveikųjų skaičių v<sub>i</sub>, nusakančių atitinkamų pusnių aukščius.</p>

<p>Trečioje eilutėje yra M skirtingų sveikųjų skaičių B<sub>i</sub>, nusakančių Jono draugų pozicijas didėjimo tvarka.</p>

### 출력 

 <p>Išveskite vieną skaičių – į kelis draugus Jonas gali pataikyti mesdamas sniego gniūžtes.</p>

