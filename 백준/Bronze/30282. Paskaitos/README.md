# [Bronze II] Paskaitos - 30282 

[문제 링크](https://www.acmicpc.net/problem/30282) 

### 성능 요약

메모리: 111508 KB, 시간: 132 ms

### 분류

구현

### 제출 일자

2024년 4월 23일 16:21:33

### 문제 설명

<p>Artūras šiemet baigė mokyklą ir labai džiaugiasi įstojęs į prestižinį universitetą. Pirmas darbas, kurį turėjo atlikti Artūras nuvykęs į universitetą – išsirinkti 10 pasirenkamųjų dalykų, kuriuos jis studijuos universitete pirmą semestrą.</p>

<p>Artūras pasirinko dešimt dalykų, tačiau vėliau susimąstė, ar nesidubliuos paskaitų laikai, t. y. ar neišsirinko jis tokių dalykų, kurių paskaitos vyksta tuo pačiu metu.</p>

<p>Jei tuo pačiu metu viena paskaita baigiasi, o kita prasideda (sutampa pabaigos ir pradžios laikas), tokios paskaitos laikomos nesidubliuojančiomis.</p>

<p>Padėkite Artūrui išsiaiškinti, ar jis galės lankyti visus pasirinktus dalykus.</p>

### 입력 

 <p>Pradinius duomenis sudaro 10 eilučių su informacija apie Artūro pasirinktus studijuoti dalykus.</p>

<p>Kiekvienoje eilutėje yra pateikiami penki skaičiai: savaitės dienos numeris s (1 – pirmadienis, 2 – antradienis, ..., 5 – penktadienis), paskaitos pradžios laikas (valanda h<sub>pr</sub> ir minutės m<sub>pr</sub>) ir pabaigos laikas (valanda h<sub>pb</sub> ir minutės m<sub>pb</sub>).</p>

### 출력 

 <p>Jeigu Artūras galės lankyti visas paskaitas, tuomet išveskite žodį <code>TAIP</code> bei bendrą paskaitų trukmę valandomis ir minutėmis.</p>

<p>Jeigu kurių nors pasirinktų paskaitų laikai dubliuosis, tuomet išveskite žodį <code>NE</code> bei dviejų dalykų, kurių užsiėmimai dubliuosis, numerius. Laikykite, kad pasirinkti dalykai sunumeruoti nuo 1 iki 10.</p>

<p>Jei galimi keli atsakymo variantai, išveskite bet kurį.</p>

