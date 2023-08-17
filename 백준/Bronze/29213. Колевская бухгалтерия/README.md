# [Bronze II] Колевская бухгалтерия - 29213 

[문제 링크](https://www.acmicpc.net/problem/29213) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

브루트포스 알고리즘

### 문제 설명

<p>Бухгалтерия в виде Зазу работала при Муфасе и будет работать при Симбе. Но когда Шрам запер Зазу в клетку, бухгалтерия ушла в вынужденный отпуск и потеряла все данные. И теперь Симба очень хочет их восстановить.</p>

<p>Бухгалтерия отвечала за количество антилоп и зебр в саванне. Кроме этого, она также считала количество останков животных. Одна единица останков образуется в результате поедания одной антилопы или зебры хищниками. Симба посчитал количество антилоп, зебр и останков в данный момент. Он точно знает, что с момента заточения Зазу не появилось ни одной новой зебры и ни одной новой антилопы, но некоторые зебры и антилопы могли быть съедены и превращены в останки. Кроме этого, Симба помнит, что в момент заточения Зазу антилоп было больше, чем зебр. Помогите ему посчитать количество различных наборов антилоп, зебр и останков, которые могли быть в момент заточения Зазу.</p>

### 입력 

 <p>В строке заданы три целых числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$c$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>≤</mo><msup><mn>10</mn><mn>3</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le a, b, c \le 10^3$</span></mjx-container>) --- текущее количество антилоп, зебр и останков соответственно.</p>

### 출력 

 <p>В единственной строке выведите одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> --- количество возможных троек этих чисел в момент заточения Зазу.</p>

