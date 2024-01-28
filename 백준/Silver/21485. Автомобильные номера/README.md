# [Silver III] Автомобильные номера - 21485 

[문제 링크](https://www.acmicpc.net/problem/21485) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2024년 1월 29일 07:22:59

### 문제 설명

<p>При расследовании дорожно-транспортных происшествий часто возникают проблемы с розыском автомобилей, водители которых покинули место происшествия.</p>

<p>Получение свидетельских показаний --- непростая работа. Ситуация осложняется тем, что очень часто свидетели могут только приблизительно вспомнить номер автомобиля. При этом с большой вероятностью опрашиваемый может перепутать порядок цифр или букв в номере.</p>

<p>По полученному от свидетеля происшествия номеру, подсчитайте, сколько различных номеров может получиться из него перестановкой букв и/или цифр, а также выведите все такие номера.</p>

<p>Напомним, что автомобильные номера в России состоят из трех букв и трех цифр, упорядоченных следующим образом: буква, три цифры, затем две буквы. Фрагмент номера, который идентифицирует регион, в котором зарегистрирован автомобиль, мы будем игнорировать.</p>

<p>В номере могут использоваться следующие буквы: <<<code>A</code>>>, <<<code>B</code>>>, <<<code>C</code>>>, <<<code>E</code>>>, <<<code>H</code>>>, <<<code>K</code>>>, <<<code>M</code>>>, <<<code>O</code>>>, <<<code>P</code>>>, <<<code>T</code>>>, <<<code>X</code>>>, <<<code>Y</code>>> (эти буквы имеют схожие по написанию аналоги как в русском, так и в латинском алфавите). В этой задаче во входном файле будут использоваться буквы латинского алфавита.</p>

### 입력 

 <p>Входной файл содержит одну строку, которая представляет собой корректный автомобильный номер.</p>

### 출력 

 <p>В первой строке выходного файла выведите число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> --- количество номеров, которые могут получиться из заданного перестановкой букв и/или цифр.</p>

<p>В последующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> строках выведите все такие номера в произвольном порядке.</p>

