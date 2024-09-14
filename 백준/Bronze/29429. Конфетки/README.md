# [Bronze I] Конфетки - 29429 

[문제 링크](https://www.acmicpc.net/problem/29429) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

문자열

### 제출 일자

2024년 9월 14일 21:48:22

### 문제 설명

<p>Арсений и Артём --- два брата. Как и все дети, они любят конфетки. Пока мама на работе, они решили определить, кто сколько конфет сегодня получит. У них есть специально для этого предназначенный набор карточек с цифрами. Они решили разделить их между собой и составить себе по числу. И вот они составили эти числа.</p>

<p>Наглость Арсения выше наглости Артёма, и он решил, что должен сегодня получить строго больше конфет, чем Артём. Ради этого он готов пойти на всё! Даже на подлое жульничество. А именно, он готов поменять местами несколько цифр в числах. Он боится, что его уличат в жульничестве, и поэтому, меняет только цифры, стоящие на одинаковых позициях (например, он может получить из чисел 123 и 456 числа 153 и 426, но не 523 и 416), так как иначе подмену легко заметить. Позиции в числе нумеруются слева направо (от старших к младшим разрядам).</p>

<p>Если числа разной длины, то он может менять цифры местами, только если обе позиции есть в числах. Например, он не может поменять третьи цифры в числах 123 и 23. Также, он хочет обменять как можно меньше цифр, так как чем больше обменов он сделает, тем проще будет заметить его жульничество. Помогите Арсению добиться своей цели.</p>

### 입력 

 <p>В первой строке задано целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container> --- которое составил Арсений. Во второй строке задано целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container> --- которое составил Артём. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq a, b \leq 10^9$</span></mjx-container>).</p>

<p>Числа записаны без ведущих нулей.</p>

### 출력 

 <p>Если Арсению никак не удастся получить больше конфет, чем Артёму, выведите <<<code>Bad luck</code>>>.</p>

<p>Иначе в первой строке выведите минимальное количество обменов, а во второй строке через пробел --- позиции, цифры в которых необходимо поменять.</p>

