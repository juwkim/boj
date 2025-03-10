# [Bronze I] Жребий Крижановского - 21466 

[문제 링크](https://www.acmicpc.net/problem/21466) 

### 성능 요약

메모리: 114172 KB, 시간: 124 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 3월 10일 23:00:44

### 문제 설명

<p>Петя играет с друзьями в игру, которую иногда называют <<Жребий Крижановского>>. Правила игры следующие: в каждом туре каждый игрок загадывает произвольное натуральное число. После этого игрок, загадавший минимальное число, которое не повторяется, выигрывает в этом туре, причем его выигрыш равен этому числу. Например, если играют 6 человек и были загаданы числа 3, 2, 1, 1, 4 и 2, то выиграл первый игрок, причем его выигрыш равен 3. Если все загаданные числа повторяются, то тур считается ничейным и никто баллов не получает.</p>

<p>Общий выигрыш игрока за игру равен сумме баллов за все сыгранные туры.</p>

<p>Петя с друзьями при игре просто называют по очереди загаданные ими числа, а потом определяют, кто выиграл, и подсчитывают баллы. Однако при таком формате игры в принципе можно сжульничать, не загадывая число заранее, а, уже зная числа, названные предыдущими игроками, выбрать себе оптимальное <<загаданное>> число. Этим и пользуется Петя. Он называет число последним и старается выбрать число так, чтобы максимизировать свой выигрыш.</p>

<p>Идет последний тур игры. Известны очки всех игроков перед этим туром и названные игроками числа. Выясните, какое число следует назвать Пете, чтобы по результатам игры у как можно большего числа игроков количество баллов было меньше чем у него. Если таких чисел несколько, то Петя хочет назвать минимальное возможное.</p>

### 입력 

 <p>Первая строка входного файла содержит число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество игроков (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le n \le 100$</span></mjx-container>). Вторая строка содержит <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> чисел --- баллы игроков перед последним туром (неотрицательные целые числа, не большие 100). Баллы перечислены в том порядке, в котором игроки обычно называют числа (то есть Петины баллы указаны последними). Третья строка содержит <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n - 1$</span></mjx-container> число --- числа, названные игроками в последнем туре (числа не превышают 100), в том порядке, в котором они их называли.</p>

### 출력 

 <p>Выведите в выходной файл число, которое следует назвать Пете.</p>

