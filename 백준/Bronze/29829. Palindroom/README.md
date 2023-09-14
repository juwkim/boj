# [Bronze II] Palindroom - 29829 

[문제 링크](https://www.acmicpc.net/problem/29829) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

애드 혹, 해 구성하기

### 문제 설명

<p>Jada nimetatakse palindroomiks, kui see on sama eest tahapoole ja tagant ettepoole lugedes. Näiteks jada 1, 2, 2, 1 on palindroom (sest see on ka tagurpidi lugedes 1, 2, 2, 1), aga jada 1, 2, 3, 4 ei ole (sest see on tagurpidi lugedes 4, 3, 2, 1).</p>

<p>Kirjutada programm, mis kontrollib, kas antud 4-elemendilisest arvujadast saab palindroomi, kui selles võib muuta maksimaalselt ühe elemendi väärtust.</p>

### 입력 

 <p>Ainsal real on neli tühikutega eraldatud täisarvu väärtustega <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>…</mo><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \ldots 9$</span></mjx-container>.</p>

### 출력 

 <p>Kui sisendis antud jada juba on palindroom või kui selle saab ühe elemendi muutmisega palindroomiks teha, trükkida väljundi esimesele reale sõna '\verb'JAH" ja teisele reale neli tühikutega eraldatud täisarvu: saadud palindroom. Kui võimalikke palindroome on mitu, väljastada ükskõik milline neist.</p>

<p>Kui sisendis antud jada maksimaalselt ühe elemendi muutmisega palindroomiks teha ei saa, trükkida väljundi ainsale reale sõna '\verb'EI".</p>

<p>NB! Väljundisse <strong>ei tohi</strong> väljastada ühtegi muud sõna või sümbolit (st väljund peaks olema kas '\verb'JAH" ja täpselt neli täisarvu või '\verb'EI" ja mitte midagi muud).</p>

