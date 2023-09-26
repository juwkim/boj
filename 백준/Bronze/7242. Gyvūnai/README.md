# [Bronze II] Gyvūnai - 7242 

[문제 링크](https://www.acmicpc.net/problem/7242) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

구현, 수학

### 문제 설명

<p>Lukas domisi gamta ir žino, kuriuo paros metu kokie žvėrys ir paukščiai yra aktyvūs. Jis organizuoja žygį su bendraklasiais ir nori pamatyti N gyvūnų. Gyvūną galima pamatyti tik tuo dienos (nuo 9:00 iki 20:59) laiku, kai jis yra aktyvus. Žygeiviai nori visus gyvūnus stebėti vienu metu, t.y. tokiu metu, kai visi gyvūnai yra aktyvūs.</p>

<p>Padėkite Lukui nuspręsti, kada geriausia vykti į žygį, kad jie pamatytų visus norimus gyvūnus.</p>

<p>Kiekvienam gyvūnui duotas dienos laiko intervalas, kada tas gyvūnas yra aktyvus, t. y. kada jį galima stebėti. Nustatykite, ar yra laikas, kai visi N gyvūnų yra aktyvūs ir raskite ilgiausią tokį laiko intervalą. Jeigu du intervalai yra tokie, kad vienas prasideda lygiai tuo pačiu laiku, kai baigėsi kitas, laikoma, kad intervalai nesikerta.</p>

### 입력 

 <p>Pirmoje pradinių duomenų eilutėje pateiktas gyvūnų, kuriuos nori stebėti mokiniai, skaičius N.</p>

<p>Kiekvienoje tolesnių N eilučių pateikta po keturis skaičius, nusakančius gyvūno aktyvumo periodą dienoje valandomis ir minutėmis: h<sub>nuo</sub>, min<sub>nuo</sub>, h<sub>iki</sub>, min<sub>iki</sub>.</p>

<p>Kiekvienas pateiktas intervalas yra netrumpesnis nei 1 minutė.</p>

### 출력 

 <p>Jei yra dienos laikas, kai visi gyvūnai yra aktyvūs, tuomet pirmoje eilutėje išveskite <code>TAIP</code>, o antroje – ilgiausią laiko intervalą, nuo kada anksčiausiai ir iki kada vėliausiai galima pamatyti visus gyvūnus. Laiko intervalą sudaro keturi skaičiai tokiu pat formatu kaip pradiniuose duomenyse.</p>

<p>Jei bendro laiko, kada gyvūnai būtų aktyvūs, nėra, išveskite <code>NE</code>.</p>

