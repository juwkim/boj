# [Silver III] Призы - 19993 

[문제 링크](https://www.acmicpc.net/problem/19993) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

많은 조건 분기

### 제출 일자

2024년 2월 3일 08:40:52

### 문제 설명

<p>Организаторы Всероссийской командной олимпиады школьников по программированию всегда ответственно относятся ко всем этапам проведения соревнования. Недавно организаторам были доставлены футболки для участников олимпиады. Они были сложены в ящик, который является кубом со стороной в один метр. Ящик был поставлен в углу комнаты прямоугольной формы размером <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>×</mo><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m \times n$</span></mjx-container> метров. Чтобы никто случайно не забрал ящик, на его верхней грани красной краской написали слово <<ВКОШП>>.</p>

<p>Сегодня организаторам вдруг понадобилось переставить этот ящик в противоположный угол комнаты. Но, к сожалению, ящик оказался настолько тяжелым, что никто не мог сдвинуть его с места. Выяснилось, что все, что можно сделать с ящиком --- перекатить его через ребро нижней грани. Соответствующее ребро при этом остается на том же месте, а нижней становится другая смежная с этим ребром грань.</p>

<p>Перед организаторами олимпиады встала следующая задача. Им необходимо перекатить ящик из угла комнаты, в котором он стоит, в противоположный угол. При этом даже перекатывать ящик очень тяжело, поэтому организаторы решили минимизировать количество перекатываний ящика. </p>

<p>Но когда они уже собрались начать транспортировку, обнаружилась еще одна проблема. Красная надпись <<ВКОШП>> каждый раз, касаясь пола, оставляет на нем следы. Поэтому среди всех вариантов транспортировки, минимизирующих количество перекатываний, организаторы решили выбрать тот, при котором надпись <<ВКОШП>> окажется на нижней грани куба минимальное число раз.</p>

<p>Помогите организаторам --- посчитайте, сколько раз надпись <<ВКОШП>> коснется пола при оптимальном перекатывании куба с футболками.</p>

### 입력 

 <p>В первой строке задано два числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n, m \le 10^9$</span></mjx-container>) --- размеры комнаты в метрах.</p>

### 출력 

 <p>Выведите одно число --- сколько раз надпись <<ВКОШП>> окажется на нижней грани при оптимальном перемещении ящика.</p>

