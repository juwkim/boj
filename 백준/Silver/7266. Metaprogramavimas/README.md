# [Silver II] Metaprogramavimas - 7266 

[문제 링크](https://www.acmicpc.net/problem/7266) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

많은 조건 분기, 구현, 수학

### 제출 일자

2025년 3월 24일 09:34:25

### 문제 설명

<p>Justas labai dažnai dalyvauja programavimo olimpiadose. Kadangi jis labai daug laiko praleidžia spręsdamas uždavinius, Justas užsimanė uždavinių sprendimą automatizuoti. Jis norėtų turėti programą, kuriai galėtų duoti uždavinio testus, ir ta programa jam surastų uždavinio sprendimą. Deja, Justas nežino, kaip tokią programą parašyti. Padėkite jam!</p>

<p>Justas jums duos sąrašą testų, ir jūs turėsite surasti sprendimą, kuris teisingai išspręstų visus tuos testus. Kiekvienas testas susideda iš dviejų skaičių – testo pradinio duomens ir testo rezultato. Visų testų pradiniai duomenys yra skirtingi.</p>

<p>Programavimo kalba, kuria Justas rašo uždavinių sprendimus, yra labai paprasta. Programos turi vieną kintamąjį, kuriame laikomas bet kokio dydžio neneigiamas sveikasis skaičius. Programai pradedant darbą, į šį kintamąjį įrašomas testo pradinis duomuo. Pati programa susideda iš komandų sąrašo:</p>

<ul>
	<li>add n – prie kintamojo prideda n. 0 ≤ n < 10<sup>9</sup>.</li>
	<li>multiply n – kintamąjį padaugina iš n. 0 ≤ n < 10<sup>9</sup>.</li>
	<li>print – išspausdina kintamojo reikšmę ir naujos eilutės simbolį.</li>
</ul>

<p>Pavyzdžiui, turime tokią programą:</p>

<pre>add 5
multiply 8
print</pre>

<p>Jei pradinis duomuo būtų 1, ši programa išspausdintų 48. Jei pradinis duomuo būtų 25, išspausdintų 240.</p>

<p>Justas nenori, kad jo sprendimai viršytų laiko ribojimą, todėl jums reikia surasti mažiausiai komandų turinčią programą, kuri teisingai išsprendžia visus Justo duotus testus.</p>

### 입력 

 <p>Pirmoje eilutėje yra skaičius N – uždaviniui skirtų testų skaičius. Kitose N eilučių yra po du skaičius a<sub>i</sub> ir b<sub>i</sub> – i-tojo testo pradinis duomuo ir reikiamas rezultatas. Visos ai reikšmės skirtingos.</p>

### 출력 

 <p>Pirmoje eilutėje išveskite vieną skaičių K – trumpiausią tinkamą programą sudarančių komandų skaičių. Tolesnėse K eilučių išspausdinkite programos komandas – po vieną komandą per eilutę. Jei yra kelios tokios programos, išveskite bet kurią.</p>

<p>Jei programa, kuri galėtų išspręsti visus testus, neegzistuoja, išveskite -1.</p>

