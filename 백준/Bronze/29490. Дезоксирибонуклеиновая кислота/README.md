# [Bronze I] Дезоксирибонуклеиновая кислота - 29490 

[문제 링크](https://www.acmicpc.net/problem/29490) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

문자열

### 제출 일자

2025년 3월 13일 22:39:03

### 문제 설명

<p>Дезоксирибонуклеиновая кислота (ДНК) --- один из двух типов нуклеиновых кислот, обеспечивающих хранение, передачу из поколения в поколение и реализацию генетической программы развития и функционирования живых организмов.</p>

<p>ДНК представляет собой пару полимерных молекул-цепей, каждое из звеньев которых является нуклеотидом одного из четырех видов: аденин (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>), тимин (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>), гуанин (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$G$</span></mjx-container>), или цитозин (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>). На каждой из цепочек задано направление, причем для двух цепочек из одного ДНК направления всегда противоположны. Получается, что напротив первого нуклеотида одной цепочки находится последний нуклеотид другой, напротив второго --- предпоследний и т.д.</p>

<p>Молекула ДНК устроена таким образом, что всегда соблюдается <em>принцип комплементарности</em>. Суть его состоит в том, что напротив аденина всегда находится тимин, и наоборот. Аналогичным образом гуанин соответствует цитозину. К примеру, цепочка AGC <em>комплементарна</em> цепочке GCT.</p>

<p>В одной суперсекретной лаборатории у Миши целиком прочитали его ДНК, но отдали запись <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> только одной из двух цепочек. Помогите Мише узнать, есть ли у него ген супермена, который записывается в ДНК подстрокой <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$t$</span></mjx-container>. Не забудьте, что этот ген может быть записан и на той цепочке Мишиного ДНК, которую он не получил из секретной лаборатории!</p>

### 입력 

 <p>В первой строке входного файла находится строка <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> длиной не более 200 символов. Во второй строке входного файла находится строка <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$t$</span></mjx-container> длиной не более 20 символов. Обе строки состоят из букв <<ATGC>>.</p>

### 출력 

 <p>В выходной файл выведите <<Yes>>, если у Миши есть ген супермена, и <<No>> если его нет.</p>

