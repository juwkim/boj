# [Silver I] SLOVA - 25139 

[문제 링크](https://www.acmicpc.net/problem/25139) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

조합론, 구현, 수학, 문자열

### 제출 일자

2025년 8월 15일 20:40:42

### 문제 설명

<p>Mirko je kupio <strong>leksikografski</strong> uzlazno sortiran popis svih riječi duljine točno N koje se sastoje od prvih N slova <strong>engleske abecede</strong> u kojima se <strong>svako od tih slova pojavljuje točno jednom</strong>. Popis je složen tako da je u N redaka zapisana po jedna riječ. Npr. za N je 3 popis izgleda ovako {abc, acb, bac, bca, cab, cba}. Za razliku od prošlog zadatka, budući da se radi o engleskoj abecedi, u ovom zadatku znakovi L, N, i J nemaju poseban značaj.</p>

<p>Podsjetimo se da su dvije riječi leksikografski uzlazno sortirane ako riječ koja je zapisana prije počinje sa slovom koje je prije u abecedi od slova s kojim počinje druga riječ, a ako su prva slova jednaka, tada se gleda odnos drugog slova u riječi, itd.</p>

<p>Udaljenost dviju riječi definiramo kao <strong>razliku njihovih pozicija na popisu</strong>. Tako su riječi <strong>acb</strong> i <strong>bca</strong> udaljene 2, dok su riječi cba i abc udaljene za 5.</p>

<p>Za zadane dvije riječi s popisa, odredi <strong>njihovu udaljenost</strong>.</p>

### 입력 

 <p>U prvom retku nalazi se prirodan broj N (1 ≤ N ≤ 26), broj korištenih slova. Sljedeća dva retka sadrže po dvije riječi s popisa, riječ A i riječ B. Budući da su s popisa, obje riječi su duljine N, sastavljene su od prvih N malih slova engleske abecede i svako slovo se pojavljuje točno jednom. Ulazni podaci bit će takvi da će rješenje za njih uvijek biti manje od 2<sup>64</sup>.</p>

### 출력 

 <p>Ispiši traženu udaljenost između riječi A i B.</p>

