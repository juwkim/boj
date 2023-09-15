# [Bronze II] Nonogramm - 7168 

[문제 링크](https://www.acmicpc.net/problem/7168) 

### 성능 요약

메모리: 115472 KB, 시간: 136 ms

### 분류

구현

### 문제 설명

<p>Nonogramm on mõistatus, mille lahendaja peab taastama ruudustikus mustadest ja valgetest ruutudest moodustatud kujundi. Ruudustiku iga rea ees on arvud, mis näitavad järjestikustest mustadest ruutudest koosnevate ja valgete ruutudega eraldatud plokkide pikkusi ja nende järjekorda. Samamoodi ka veergude kohal. Igal real ja igas veerus peavad näidatud pikkustega mustad plokid olema näidatud järjekorras ja kahe musta ploki vahel peab alati olema vähemalt uks valge ruut.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/95324ff3-b69e-4a8a-a3df-b47cc265db17/-/preview/" style="width: 137px; height: 119px;"></p>

<p>Kirjutada programm, mis aitab mõistatuse koostajal antud kujundile vastavad ridade ja veergude kirjeldused leida.</p>

### 입력 

 <p>Tekstifaili esimesel real on kaks täisarvu, ruudustiku ridade arv N (1 ≤ N ≤ 100) ja veergude arv M (1 ≤ M ≤ 100). Järgmisel N real on igaühel täpselt M märki, kus punkt tähistab valget ja trellimärk musta ruutu.</p>

### 출력 

 <p>Tekstifaili väljastada täpselt N +M rida. Esimesele N reale väljastada ruudustiku ridade ees olevad arvud: ruudustiku esimese rea ees olevad arvud faili reale 1, teise rea ees olevad arvud faili reale 2 j.n.e. Järgmisele M reale väljastada veergude kohal olevad arvud: vasakpoolseima veeru kohal olevad arvud faili reale N + 1, vasakult teise veeru kohal olevad arvud faili reale N + 2 j.n.e. Kui ruudustiku mõnes reas või veerus pole ühtki musta ruutu, siis väljastada faili vastavale reale arv 0.</p>

