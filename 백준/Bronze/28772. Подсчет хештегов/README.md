# [Bronze II] Подсчет хештегов - 28772 

[문제 링크](https://www.acmicpc.net/problem/28772) 

### 성능 요약

메모리: 117696 KB, 시간: 188 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2023년 12월 6일 10:25:41

### 문제 설명

<p>Дима разрабатывает новую модную соцсеть. В данный момент он хочет написать модуль, который будет обрабатывать текст и подсчитывать количество различных хештегов в нем.</p>

<p>Текст состоит из строчных английских букв, цифр, символов <<<code>#</code>>> и пробелов. Назовем словом несколько последовательных непробельных символов, ограниченных слева и справа пробелами или концом/началом текста. Слово является хештегом, если его длина хотя бы <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>, первый символ равен <<<code>#</code>>>, а все остальные --- нет.</p>

<p>Дима хочет вычислить количество различных хештегов, которые встречаются в тексте, вывести их, а также количество раз, которое встречается каждый из них.</p>

### 입력 

 <p>В единственной строке дан текст в формате, описанном выше. Длина текста не превышает <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100\,000$</span></mjx-container>. Текст может содержать несколько пробелов подряд, пробелы в начале или конце строки.</p>

### 출력 

 <p>В первой строке выведите целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество различных хештегов, которые встречаются в тексте. В следующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строках выведите хештег и количество раз, которое он встречается. Хештеги можно выводить в любом порядке.</p>

