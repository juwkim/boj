# [Bronze I] Футбольный чемпионат - 29621 

[문제 링크](https://www.acmicpc.net/problem/29621) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

정렬

### 제출 일자

2024년 5월 17일 16:08:38

### 문제 설명

<p>Вася --- ярый футбольный фанат. Недавно он узнал, что матч с участием его любимой команды будет последним в чемпионате, и результаты всех остальных матчей будут известны до его окончания.</p>

<p>Естественно, Вася хочет рассчитать, на каком месте в турнирной таблице окажется его команда в зависимости от результата матча. Несмотря на то, что задача не так сложна, Вася боится не справиться с волнением, поэтому попросил вас написать программу, вычисляющую это за него.</p>

<p>Имейте в виду, что победившая команда получает <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> очка, а проигравшая --- <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>. В случае ничейного исхода матча, обе команды получают по одному очку.</p>

### 입력 

 <p>Первая строка входного файла содержит натуральное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество команд, участвующих в чемпионате (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 20$</span></mjx-container>). Вторая строка входного файла содержит название команды, за которую болеет Вася, а третья --- название второго участника последнего матча. Далее следует описание турнирной таблицы к окончанию всех матчей, кроме последнего. Каждая из последующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк содержит название команды и количество очков. Все названия состоят из заглавных латинских букв и их длина не превышает двадцати символов.</p>

### 출력 

 <p>В выходной файл выведите три числа разделенные пробелом --- положение команды, за которую болеет Вася в случае ее победы в последнем матче, ничьей и поражении соответственно. Учтите, что при равенстве очков более высокое место имеет команда с лексикографически меньшим названием.</p>

