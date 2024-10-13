# [Silver V] Драфт НБА - 18099 

[문제 링크](https://www.acmicpc.net/problem/18099) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2024년 10월 13일 23:48:07

### 문제 설명

<p>Перед каждым сезоном НБА проходит драфт, то есть церемония выбора игроков командами.</p>

<p>Перед драфтом скаутские службы команд детально изучают потенциальных новичков. Одна из команд поручила вам написать программу для обработки собранных данных в соответствии с внутрикомандными стандартами.</p>

<p>Каждый из новичков до этого провёл как минимум один сезон в студенческих лигах, так что для каждого игрока известны пять основных целочисленных параметров:</p>

<ul>
	<li>Рост игрока --- ожидаемый диапазон от 190 до 220 см.</li>
	<li>Размах рук (иначе говоря, wingspan) --- ожидаемый диапазон от 200 до 250 см.</li>
	<li>Среднее количество очков за матч --- ожидаемый диапазон от 10 до 20.</li>
	<li>Среднее количество подборов за матч --- ожидаемый диапазон от 2 до 6.</li>
	<li>Среднее количество передач за матч --- ожидаемый диапазон от 3 до 7.</li>
</ul>

<p>Таким образом, каждый из параметров может оказаться ниже ожидаемого диапазона, в нижней половине ожидаемого диапазона, в верхней половине ожидаемого диапазона (середина входит в верхнюю половину) и выше ожидаемого диапазона.</p>

<p>Перед драфтом требуется распределить игроков по следующим категориям: </p>

<ul>
	<li>уникальный игрок (таких ещё называют <<единорогами>> --- unicorn) с сочетанием выдающихся физических данных и игровых навыков; </li>
	<li>игрок, достойный выбора в первом раунде; </li>
	<li>игрок, достойный выбора во втором раунде; </li>
	<li>игрок, которого не стоит выбирать вообще.</li>
</ul>

<p>Если у игрока три параметра выше ожидаемого диапазона, <strong>причём среди них обязательно есть рост или размах рук</strong>, то игрок считается <<единорогом>> (категория 0)</p>

<p>Игрока рекомендуется выбирать в первом раунде драфта (категория 1), если верно одно из следующих утверждений:</p>

<ul>
	<li>У игрока два параметра выше ожидаемого диапазона и ещё один --- как минимум в верхней половине ожидаемого диапазона.</li>
	<li>У игрока все параметры как минимум в ожидаемом диапазоне и не менее трёх --- как минимум в верхней половине.</li>
</ul>

<p>Игрока рекомендуется выбирать во втором раунде драфта (категория 2), если верно одно из следующих утверждений:</p>

<ul>
	<li>У игрока один параметр выше ожидаемого диапазона и ещё один --- как минимум вверхней половине ожидаемого диапазона.</li>
	<li>У игрока три параметра как минимум в верхней половине ожидаемого диапазона.</li>
</ul>

<p>В остальных случаях тратить выбор драфта на этого игрока не рекомендуется (категория 3).</p>

<p>Вам заданы параметры некоторых из 32 игроков текущего драфта (для объективности имена игроков не указаны). Ваша задача --- для каждого игрока определить категорию, под которую он подпадает для вашей команды на драфте.</p>

### 입력 

 <p>Первая строка входных данных содержит одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> --- количество игроков (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>32</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 32$</span></mjx-container>). Описание каждого игрока состоит из 5 целых чисел: роста <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn><mo>≤</mo><mi>h</mi><mo>≤</mo><mn>250</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$150 \le h \le 250$</span></mjx-container>), размаха рук <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$w$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c37"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn><mo>≤</mo><mi>w</mi><mo>≤</mo><mn>270</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$150 \le w \le 270$</span></mjx-container>), среднего количества очков <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> за матч (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>≤</mo><mi>s</mi><mo>≤</mo><mn>35</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5 \le s \le 35$</span></mjx-container>), среднего количества подборов <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$r$</span></mjx-container> за матч (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>r</mi><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le r \le 10$</span></mjx-container>), среднего количества передач <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container> за матч (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>p</mi><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le p \le 10$</span></mjx-container>). Каждое число задаётся в отдельной строке.</p>

### 출력 

 <p>Для каждого игрока в порядке их следования во входном файле выведите одно число --- категорию на драфте, в которую этот игрок попадает в соответствии с критериями вашей команды.</p>

