# [Silver II] Bomboni - 14146 

[문제 링크](https://www.acmicpc.net/problem/14146) 

### 성능 요약

메모리: 141832 KB, 시간: 272 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2025년 2월 17일 06:04:05

### 문제 설명

<p>Ivica je pozvao sve svoje prijatelje na veliku zabavu. Svi znaju da nijedno pravo druženje ne može proći bez megapopularnih i nezamjenjivih PEZ bombona.</p>

<p>Ivica se boji da će tih slatkiša biti premalo, pa ne želi kupiti manje od A bombona. Isto tako, ima dovoljno novaca za najviše B bombona. Budući da se neće svi prijatelji odazvati, Ivica ne zna točan broj sudionika zabave. Stoga želi kupiti količinu bombona koju može ravnopravno podijeliti na najviše moguće načina. Podjela bombona je ravnopravna ako svaki od prijatelja dobije jednako mnogo bombona i ako pri tome svi kupljeni bomboni budu podijeljeni. Na primjer, ukoliko Ivica kupi 6 bombona, moći će ih ravnopravno podijeliti na 4 načina: { 1+1+1+1+1+1, 2+2+2, 3+3, 6 }.</p>

<p>Napišite program koji će pomoći Ivici odlučiti koliko bombona treba kupiti. </p>

### 입력 

 <p>U prvom i jedinom retku ulaza nalaze se dva prirodna broja A i B, 1 ≤ A ≤ B ≤ 2 000 000, odvojena jednim razmakom. </p>

### 출력 

 <p>Označimo sa M maksimalni broj načina na koje Ivica može ravnopravno podijeliti kupljene bombone. Neka je S skup svih brojeva X u intervalu [A, B] takvih da ako Ivica kupi X bombona, onda ih može ravnopravno podijeliti na M načina; neka je N broj elemenata skupa S.</p>

<p>U prvi redak izlaza ispišite brojeve M i N odvojene razmakom. U svaki od idućih N redaka ispišite po jedan element skupa X; elementi trebaju biti ispisani uzlazno po veličini. </p>

