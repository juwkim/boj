# [Silver II] Лягушонок Билли - 19798 

[문제 링크](https://www.acmicpc.net/problem/19798) 

### 성능 요약

메모리: 126796 KB, 시간: 136 ms

### 분류

그리디 알고리즘, 정렬, 두 포인터

### 제출 일자

2025년 1월 9일 03:55:43

### 문제 설명

<p>Лягушонок Билли сидел на камне и любовался на закат, когда понял, что проголодался. Он огляделся и с удивлением обнаружил, что в ручье около него копошатся мошки. Ручей представляет собой прямую, на которой расположен и камень, на котором сидит Билли. Лягушонок был очень голоден, и потому захотел съесть всех мошек. У Билли очень длинный язык, поэтому он может, не спрыгивая с камня, съесть любую мошку (но только одну за раз).</p>

<p>Однако высовывать язык на большие расстояния не так-то просто, лягушонок на каждый сантиметр высунутого языка тратит одну единицу энергии. Каждый раз, когда Билли съедает мошку из какой-то точки происходит следующее: все мошки, сидящие слева от съеденной мошки, и все мошки, сидящие справа от нее в ужасе отпрыгивают от места событий на один сантиметр вдоль ручья. Мошки, которые сидят в той же точке, что и съеденная, настолько шокированы этим событием, что не двигаются.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/671ed13d-7f45-48ab-9d08-e050398a21c2/-/preview/" style="width: 426px; height: 155px;"></p>

<p>Если мошка в какой-то момент времени прыгает на камень, где сидит Билли, то Билли тут же съедает ее не тратя энергии. При этом другие мошки не перемещаются.</p>

<p>Лягушонок Билли хочет понять --- какое минимальное количество единиц энергии ему потребуется для того, чтобы съесть всех мошек. Помогите ему это выяснить.</p>

### 입력 

 <p>В первой строке входного файла задано одно натуральное числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn><mrow data-mjx-texclass="ORD"><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle></mrow><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100{\,}000$</span></mjx-container>) --- количество мошек. Во второй строке входного файла задано <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> натуральных чисел --- расстояния каждой из мошек до камня. Известно, что все мошки находятся на одной прямой по одну сторону от камня. Расстояния даны в порядке неубывания. Расстояния не превышают <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^9$</span></mjx-container>.</p>

### 출력 

 <p>Выведите одно число --- минимальное количество единиц энергии, которое потребуется Билли, чтобы съесть всех мошек.</p>

