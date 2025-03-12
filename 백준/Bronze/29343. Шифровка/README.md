# [Bronze I] Шифровка - 29343 

[문제 링크](https://www.acmicpc.net/problem/29343) 

### 성능 요약

메모리: 110032 KB, 시간: 96 ms

### 분류

구현, 문자열

### 제출 일자

2025년 3월 12일 18:46:07

### 문제 설명

<p>Лее Органе срочно нужна ваша помощь! Орден Джедаев недавно смог перехватить шифровку с планеты Татуин, предназначавшуюся, видимо, для Ордена Ситхов. В этой сводке должно содержаться очень много информации, в том числе и та, которая интересна Светлой Стороне. Однако данная шифровка может являться также и дезинформацией, чтобы запутать доблестных борцов со злом.</p>

<p>Однако, как сообщил перебежчик, достоверность послания зависит от числа <code>интересных</code> пар префиксов и суффиксов одинаковой длины. Префикс длины <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> может образовать <code>интересную</code> пару с суффиксом той же длины, если и префикс и суффикс содержат одинаковое, ненулевое количество гласных букв. Во всей вселенной звездных войн принято считать гласными следующие буквы: <code><<a>></code>, <code><<o>></code>, <code><<u>></code>, <code><<i>></code>, <code><<e>></code>.</p>

<p>К сожалению, наши друзья пока не знают зависимость между достоверностью шифровки и количеством пар суффиксов и префиксов. Скоро они выяснят эту зависимость, а пока Лея просит помочь ей посчитать количество <code>интересных</code> пар префиксов и суффиксов.</p>

### 입력 

 <p>Во входном файле в первой строке содержится целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>20000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 20000$</span></mjx-container>) --- длина зашифрованной строки. Вторая строка содержит саму шифровку, состоящую только из строчных и прописных букв латинского алфавита.</p>

### 출력 

 <p>В выходном файле выведите одно число: количество таких положительных чисел <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>, что префикс и суффикс длины <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> содержат одинаковое, ненулевое количество гласных букв.</p>

