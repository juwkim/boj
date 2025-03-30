# [Silver II] Genijalac - 25157 

[문제 링크](https://www.acmicpc.net/problem/25157) 

### 성능 요약

메모리: 110892 KB, 시간: 104 ms

### 분류

구현, 정렬

### 제출 일자

2025년 3월 30일 10:53:51

### 문제 설명

<p>Dok je s Ljepoticom Nicol sastavljao namještaj, Genijalac Ronald je razmišljao: „Ako zvijezde mogu pjevati, ako zvijezde mogu plesati, zašto zvijezde ne bi mogle kodirati?” Prionuo je poslu i osmislio pravila showa „Zvijezde kodiraju“.</p>

<p>U showu sudjeluje N zvijezda označenih brojevima od 1 do N. Show tj. zadatak je podijeljen na četiri dijela koji se nastavljaju jedan na drugi.</p>

<p>Dio 1.</p>

<p>Nakon što zvijezde predstave svoje programerske vještine, publika u studiju glasa za neku od njih. Zvijezda s najvećim brojem dobivenih glasova postaje pobjednik prvog dijela showa. Ako više zvijezda ima isti, a najveći broj glasova, pobjednik je ona s najmanjom oznakom.</p>

<p>U prvi redak izlaza ispiši oznaku pobjednika prvog dijela showa.</p>

<p>Dio 2.</p>

<p>U drugom dijelu glasovi publike pretvaraju se u bodove. Zvijezda (jedna ili više njih) s najvećim brojem glasova publike dobiva N bodova, zvijezda (jedna ili više njih) sa sljedećim najvećim brojem glasova publike dobiva N - 1 bodova i tako redom sve dok svakoj zvijezdi ne pretvorimo glasove u bodove.</p>

<p>U drugi redak ispiši najmanji broj bodova koji je dodijeljen nekoj zvijezdi.</p>

<p>Dio 3.</p>

<p>U trećem dijelu zvijezde dodatno ocjenjuje K članova žirija označenih brojevima od 1 do K. Svaki član žirija svakoj zvijezdi dodjeljuje između 1 i N glasova, dodijelivši svaki broj glasova točno jednom. Glasovi članova žirija se za svakog pojedinog natjecatelja zbrajaju. Nakon zbrajanja, glasovi se pretvaraju u bodove na isti način objašnjen u drugom dijelu. Zbrajanjem bodova iz drugog i trećeg dijela dobije se ukupan broj bodova koji pojedina zvijezda ima na kraju showa. Zvijezda s najvećim brojem ukupnih bodova postaje pobjednik cijelog showa. Ako više zvijezda ima isti najveći broj bodova, pobjednik je ona među njima s najmanjom oznakom.</p>

<p>Ispiši oznaku pobjednika showa.</p>

<p>Dio 4.</p>

<p>Službena ljestvica poretka dobije se sortiranjem zvijezda prema ukupnom broju bodova koje imaju (od većeg broja prema manjem). Zvijezde s istim brojem bodova sortiraju se prema vrijednosti njihove oznake (od manje prema većoj). U četvrtom dijelu određuje se koji je član žirija najbolje procijenio službenu ljestvicu poretka. Preciznije rečeno, to je onaj član žirija kod kojeg je minimalan zbroj apsolutnih vrijednosti razlike pozicije i-te zvijezde na službenoj ljestvici poretka i pozicije i-te zvijezde na ljestvici poretka kada bi se gledali samo glasovi tog člana žirija. Ako više članova žirija ima isti minimalan zbroj traženih razlika, tada za onoga među njima koji ima najmanju oznaku kažemo da je najbolje procijenio pobjednika.</p>

<p>Ispiši oznaku člana žirija s najboljom procjenom.</p>

### 입력 

 <p>U prvom retku nalazi se prirodan broj N (2 ≤ N ≤ 100), broj zvijezda iz teksta zadatka.</p>

<p>U sljedećih N redaka nalazi se po jedan prirodan broj P<sub>i</sub> (1 ≤ P<sub>i</sub> ≤ 1000, i=1..N), ukupan broj glasova publike koji je dobila zvijezda s oznakom i.</p>

<p>U sljedećem retku nalazi se prirodan broj K (1 ≤ K ≤ 100), broj članova žirija iz teksta zadatka.</p>

<p>U sljedećih K redaka nalazi se po N različitih prirodnih brojeva Z<sub>ij</sub> (1 ≤ Z<sub>ij</sub> ≤ N, i=1..K, j=1..N) odvojenih razmakom, broj glasova koje je član žirija s oznakom i dodijelio zvijezdi s oznakom j.</p>

### 출력 

 <p>U prvi redak treba ispisati prirodan broj, rješenje prvog dijela zadatka.</p>

<p>U drugi redak treba ispisati prirodan broj, rješenje drugog dijela zadatka.</p>

<p>U treći redak treba ispisati prirodan broj, rješenje trećeg dijela zadatka.</p>

<p>U četvrti redak treba ispisati prirodan broj, rješenje četvrtog dijela zadatka.</p>

