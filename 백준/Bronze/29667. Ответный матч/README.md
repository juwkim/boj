# [Bronze III] Ответный матч - 29667 

[문제 링크](https://www.acmicpc.net/problem/29667) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

사칙연산, 많은 조건 분기, 구현, 수학

### 문제 설명

<p>Две популярные футбольные команды A и Б решили выявить сильнейшего между собой. Для этого они решили провести двухматчевое противостояние --- сначала сыграть матч на поле А, затем на поле Б.</p>

<p>Противостояние выигрывает та команда, которая в сумме забьет больше голов, чем соперник. Если же команды забили одинаковое число мячей в ворота соперника, то победителем признается команда, забившая большее число голов в гостях (на стадионе соперника). Если же и эти величины совпадают, то команды исполняют серию пенальти.</p>

<p>Второй матч противостояния на поле Б на радио <<Слушаем внимательно>> комментировал ведущий Вася. Во время трансляции его слушатели регулярно интересовались не только текущим результатом матча, который Вася зачитывал с табло, но и возможностью такого исхода встречи, что будет исполнена серия пенальти (как самое захватывающее футбольное зрелище).</p>

<p>Математические способности Васи оставляли желать лучшего, и он попросил Вас написать программу, которая, зная результат первого матча и текущий счет на табло во время второго матча, поможет определить, смогут ли зрители наблюдать серию пенальти.</p>

### 입력 

 <p>Первая строка входного файла содержит результат матча А --- Б (на поле команды А) в формате <<<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container>:<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container>>>, где <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container> --- число мячей, забитых хозяевами поля, а <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container>, соответственно, гостями (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo><</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le a, b < 10$</span></mjx-container>). Вторая строка в том же формате содержит текущий счет на табло в матче Б --- А.</p>

### 출력 

 <p>В выходной файл выведите слово <<<code>YES</code>>>, если команды могут закончить встречу со счетом, после которого результат противостояния определиться в серии пенальти, иначе --- выведите слово <<<code>NO</code>>>.</p>

