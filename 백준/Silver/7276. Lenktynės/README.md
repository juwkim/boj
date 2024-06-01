# [Silver IV] Lenktynės - 7276 

[문제 링크](https://www.acmicpc.net/problem/7276) 

### 성능 요약

메모리: 110820 KB, 시간: 144 ms

### 분류

자료 구조, 구현, 시뮬레이션

### 제출 일자

2024년 6월 2일 01:51:52

### 문제 설명

<p>Ralio lenktynėse dalyvavo N automobilių. Pasibaigus varžyboms, televizijos operatoriai nori sumontuoti visą nufilmuotą medžiagą. Svarbiausia – jie nori parodyti visus aplenkimus, kurie įvyko lenktynių metu. Tačiau bemontuodami medžiagą operatoriai susimaišė: kaip sužinoti, ar visus aplenkimus jie sumontavo teisinga tvarka?</p>

<p>Jums žinomos pradinės automobilių pozicijos, bei eilė automobilių aplenkimų. Parašykite programą, kuri nustatytų, ar duoti aplenkimai galėjo įvykti tokia tvarka.</p>

### 입력 

 <p>Pirmoje eilutėje įrašytas automobilių skaičius N, o antroje – automobilių numeriai, įrašyti tokia tvarka, kokia jie startavo (pirmasis startavęs automobilis įrašytas pirmas). Visi automobilių numeriai yra skirtingi sveikieji skaičiai nuo 1 iki N.</p>

<p>Tolimesnėje eilutėje įrašytas lenkimų skaičius L. Toliau pateikta L eilučių kuriose įrašyta po skaičių porą (a<sub>i</sub>, b<sub>i</sub>), žyminčią, kad automobilis a<sub>i</sub> aplenkė automobilį b<sub>i</sub>. Skaičių poros įrašytos tokia tvarka, kokia buvo sumontuota operatorių įraše. Galite būti tikri, kad lenktynių metu įvyko bent vienas lenkimas.</p>

### 출력 

 <p>Jei lenktynės galėjo vykti tokia eiga, kokia yra pateikta, pirmoje eilutėje išveskite žodį <code>TAIP</code>, o antroje – galutinę automobilių tvarką, tokiu pačiu formatu, kaip ir pradiniuose duomenyse.</p>

<p>Jei operatoriai padarė klaidą montuodami, pirmoje eilutėje išveskite žodį <code>NE</code>, o antroje numerį lenkimo, kuris yra neįmanomas (t.y. automobilis a<sub>i</sub> negalėjo aplenkti b<sub>i</sub> tuo metu).</p>

