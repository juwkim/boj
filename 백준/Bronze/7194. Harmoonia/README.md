# [Bronze II] Harmoonia - 7194 

[문제 링크](https://www.acmicpc.net/problem/7194) 

### 성능 요약

메모리: 227480 KB, 시간: 476 ms

### 분류

구현

### 제출 일자

2024년 8월 17일 01:04:36

### 문제 설명

<p>Klassikalise harmooniateooria kohaselt tuleks mitmehäälset seadet kirjutades vältida niinimetatud paralleelkvinte, see tähendab olukorda, kus kahe hääle vaheline kaugus pooltoonides annab jagamisel kaheteistkümnega jäägi seitse, seejärel mõlemas hääles helikõrgus muutub ning nende vaheline kaugus pooltoonides annab jälle kaheteistkümnega jagades jäägi seitse.<sup>1</sup></p>

<p>Paralleelkvindid esinevad ainult siis, kui mõlemas hääles helikõrgus muutub. See tähendab, et kui kahel järjestikusel noodil annab kahe hääle vaheline kaugus 12-ga jagades jäägi 7, kuid kas ühes või kummaski hääles helikõrgus ei muutu, siis ei ole tegemist paralleelkvintidega.</p>

<p>Kirjutada programm, mis tuvastab kahehäälses seades paralleelkvintide olemasolu.</p>

<p>Helikõrgusi esitatakse sisendfailis täisarvudena. Arv 0 tähistab esimese oktavi C nooti ning positiivne täisarv k sellest k pooltooni võrra kõrgemat ja negatiivne täisarv vastavalt madalamat heli. Näiteks arv 4 vastab esimese oktavi E noodile ja arv −3 väikse oktavi A noodile.<sup>2</sup></p>

<hr>
<p><sup>1</sup> Märkus muusikateooriast rohkem huvitatuile: vahel loetakse paralleelkvintideks mitte ainult kaht järjestikust puhast kvinti, vaid ka näiteks järjestikuseid puhast ja vähendatud kvinti (vastavalt seitse ja kuus pooltooni); selles ülesandes loeme paralleelkvintideks vaid kaht järjestikust puhast kvinti.</p>

<p><sup>2</sup> Ülesande lahendamiseks ei ole oluline nootide nimetusi mõista.</p>

### 입력 

 <p>Tekstifaili esimesel real on täisarv N (0 ≤ N ≤ 1 000 000) — kummaski hääles esinevate nootide arv. Järgmisel N real on igauhel kaks tühikuga eraldatud täisarvu A<sub>i</sub> ja B<sub>i</sub>, vastavalt esimeses ja teises hääles kõlavate nootide helikõrgused (−100 ≤ B<sub>i</sub> ≤ A<sub>i</sub> ≤ 100, i ∈ 1 . . . N). Ühel real antud noodid kõlavad samaaegselt ning järjestikustel ridadel olevad noodid kõlavad vahetult üksteise järel.</p>

### 출력 

 <p>Kui seades paralleelkvinte ei esine, väljastada tekstifaili ainsale reale sõna <code>POLE</code>. Kui seades esinevad paralleelkvindid M eri noodipaari vahel, väljastada faili M rida, igaühele täisarv i — ühe paralleelkvindi esimese noodi järjekorranumber (1 ≤ i < N). Järjekorranumbrid väljastada kasvavas järjekorras.</p>

