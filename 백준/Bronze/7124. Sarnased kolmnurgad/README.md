# [Bronze I] Sarnased kolmnurgad - 7124 

[문제 링크](https://www.acmicpc.net/problem/7124) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

기하학, 피타고라스 정리

### 제출 일자

2024년 8월 12일 00:54:54

### 문제 설명

<p>Juku õpib koolis kolmnurkade sarnasust ja saab teada, et kolmnurgad on sarnased, kui nende vastavate nurkade suurused on võrdsed ja vastavate külgede pikkused võrdelised. Sarnased kolmnurgad võivad olla omavahel pööratud, peegeldatud ja nihutatud. Sarnaste kolmnurkade vastavate külgede pikkuste jagatist nimetatakse nende sarnasusteguriks.</p>

<p>Kodutööna saab ta hulga kolmnurki, mille sarnasustegureid on vaja määrata. Kuna 21. sajandil sobivad arvutamiseks rohkem arvutid kui inimesed, aita Jukul kirjutada programm, mis selle töö tema eest ära teeb.</p>

### 입력 

 <p>Tekstifaili esimesel real on kuus täisarvu lõigust $-10^9$ kuni $10^9$: esimese kolmnurga tippude x- ja y-koordinaadid. Teisel real on samuti kuus arvu: teise kolmnurga tippude koordinaadid. Tipud võivad olla antud nii päripäeva kui vastupäeva järjekorras. Antud punktid moodustavad alati kolmnurga (pole ühtelangevaid punkte ega sirgnurki).</p>

### 출력 

 <p>Kui kolmnurgad on sarnased, siis kirjutada tekstifaili täpselt üks reaalarv (täpsusega vähemalt $0{,}0001$), mis näitab, mitu korda on esimene kolmnurk suurem kui teine (kui esimene kolmnurk on väiksem, on ka vastus väiksem kui $1$). Kui kolmnurgad ei ole sarnased, kirjutada väljundfaili $-1$.</p>

