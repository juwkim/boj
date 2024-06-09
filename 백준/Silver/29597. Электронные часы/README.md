# [Silver III] Электронные часы - 29597 

[문제 링크](https://www.acmicpc.net/problem/29597) 

### 성능 요약

메모리: 111604 KB, 시간: 176 ms

### 분류

브루트포스 알고리즘, 구현, 시뮬레이션

### 제출 일자

2024년 6월 10일 03:04:17

### 문제 설명

<p>Юный конструктор Федя решил сделать электронные часы, отображающие время четырьмя дисплеями, расположенными на табло (часы показывают только час и минуту текущего времени). Каждый дисплей Фединых часов отображает одну цифру и представляет собой прямоугольник размером <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>×</mo><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \times m$</span></mjx-container>, каждая клетка которого является светодиодом. Таким образом каждой цифре соответствует ее графическое изображение на дисплее.</p>

<p>Каждый светодиод может находиться в двух состояниях: включенном и выключенном. Для того, чтобы перевести диод из одного состояния в другое, требуется потратить один джоуль энергии. Поддержка диода в любом из состояний на сколь угодно долгое время не требует энергии. Например, если каждый дисплей Фединых часов имеет два диода, единице соответствует включенный первый диод и выключенный второй, двойке соответствует включенный второй диод и выключенный первый, то при переходе из единицы в двойку требуется потратить два джоуля энергии. А при переходе из двойки в тройку (если тройке соответствуют выключенные диоды) требуется потратить один джоуль энергии.</p>

<p>Для определения типа батарейки, которою необходимо поставить в часы, Федя попросил Вас рассчитать, сколько джоулей энергии тратит в сутки (начиная от перехода от 00:00 к 00:01 и заканчивая переходом от 23:59 к 00:00) табло его электронных часов. Помогите Феде найти эту величину.</p>

### 입력 

 <p>В первой строке входного файла задано два натуральных числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n, m \le 100$</span></mjx-container>). Следующие десять блоков содержат графические представления для цифр от нуля до девяти соответственно. Каждый блок состоит из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк, каждая из которых состоит из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> символов. Символ <<#>> соответствует включенному светодиоду, а символ <<.>> - выключенному.</p>

### 출력 

 <p>В выходной файл выведите количество джоулей энергии, которое тратит в сутки табло Фединых часов.</p>

