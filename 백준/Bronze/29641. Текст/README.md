# [Bronze II] Текст - 29641 

[문제 링크](https://www.acmicpc.net/problem/29641) 

### 성능 요약

메모리: 111356 KB, 시간: 120 ms

### 분류

문자열

### 제출 일자

2024년 5월 22일 11:21:30

### 문제 설명

<p>Давным-давно, в далекой-далекой галактике учились в одной школе два закадычных друга --- Вася и Петя. Они были верными товарищами, не раз выручавшими друг друга в трудную минуту из самых безвыходных ситуаций. Однако речь сейчас пойдет не об этом, а о редчайшем случае --- ссоре между двумя героями нашего повествования.</p>

<p>В конце седьмого класса Вася увлекся программированием и написал свой текстовый редактор. Естественно, Петя тут же захотел его испытать. Несложно представить насколько велико было его разочарование, когда обнаружилось, что Васина программа корректно работает только при использовании экрана с тем же разрешением, как и у него дома. Вася оправдывал это тем, что оптимальный вывод текста на экран --- штука сложная, поэтому универсальным образом сделать это невозможно. Петя же заявил, что хоть программист он и никудышный, но легко решит эту задачу.</p>

<p>К сожалению, программирует Петя действительно из рук вон плохо, поэтому он просит вас помочь ему в написании решения.</p>

<p>На вход дан текст. Назовем <em>словом</em> последовательность символов, ограниченную пробелами, началом или концом текста. Обратите внимание, что в данной задаче знаки препинания считаются частью слова. Требуется разбить текст на строки так, чтобы длина каждой из них была не более <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> символов, при этом их общее количество было минимальным. Порядок слов и сами слова менять запрещено.</p>

### 입력 

 <p>Первая строка входного файла содержит натуральное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> --- максимально допустимая длина строки (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>k</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le k \le 100$</span></mjx-container>). Вторая строка входного файла содержит текст, который необходимо вывести. Текст состоит из латинских букв, цифр, пробелов и символов <<,>> (запятая), <<.>> (точка), <<!>> (восклицательный знак) и <<?>> (вопросительный знак). Размер входного файла не превышает <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$50000$</span></mjx-container> байтов.</p>

### 출력 

 <p>Выведите заданный во входном файле текст так, чтобы длина каждой строки была не более <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> символов, а количество строк было минимально возможным. Гарантируется, что задача имеет решение. В случае если решение не единственно, выведите любое из них.</p>

<p>Слова в выходном файле должны быть отделены друг от друга пробелами и/или переводами строк.</p>

