# [Bronze III] Игра в дженгу - 28790 

[문제 링크](https://www.acmicpc.net/problem/28790) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

애드 혹, 게임 이론

### 문제 설명

<p>Чтобы впечатлить Лорну Кэмпбелл, Джонни Инглиш не придумал ничего лучше, чем обыграть ее в шпионскую дженгу. </p>

<p>Дженга --- высокая башня из деревянных брусков. В каждом ряду стоит по три одинаковых прямоугольных бруска, образующих квадрат. Самый верхний ряд образуют бруски, стоящие поперек, ниже --- вдоль, ниже --- снова поперек и так далее. </p>

<p>В шпионской дженге игроки по очереди вынимают по одному бруску из ряда. При этом бруски из верхнего и нижнего ряда вынимать не разрешается. После того, как брусок вынут, он откладывается и в башню в дальнейшем не возвращается. Башня падает в том случае, если из ряда вынуты два соседних бруска (считаем, что башня не может упасть после неаккуратного хода, в силу того что игроки истинные профи). Тот, кто только что сделал ход и башня упала --- проиграл. </p>

<p>Итак, перед Джонни стоит башня из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> уровней, и очень умный противник, не желающий сдаваться. Выведите, кто выиграет, если первым начинает Джонни.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/dc2d2936-04e4-4a57-9aad-034d1afa6c28/-/preview/" style="width: 400px; height: 300px;"></p>

### 입력 

 <p>В единственной строке входных данных содержится целое положительное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- высота башни (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>7</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \leq n \leq 10^7$</span></mjx-container>).</p>

### 출력 

 <p>Выведите строку <code>Johnny</code>, если выиграет Джонни, иначе --- <code>Lorna</code></p>

