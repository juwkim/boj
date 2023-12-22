# [Bronze I] Даты - 29585 

[문제 링크](https://www.acmicpc.net/problem/29585) 

### 성능 요약

메모리: 196612 KB, 시간: 4572 ms

### 분류

구현

### 제출 일자

2023년 12월 22일 17:41:34

### 문제 설명

<p>Вася конструирует свой собственный автоматический электронный календарь, который будет отображать текущую дату в формате <<ДД.ММ.ГГГГ>>. Для этого ему нужно уметь отображать различные цифры. На данный момент его календарь умеет отображать <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> различных цифр. Поскольку добавление поддержки каждой новой цифры --- процесс очень трудоемкий, то Вася решил, что если его календарь будет отображать довольно большое количество дат, то он будет доволен. Поэтому на данный момент Васю крайне интересует следующий вопрос: сколько дней из данного промежутка его календарь будет отображать дату. </p>

<p>Например, если Васин календарь может отображать только цифры <code>0</code>, <code>2</code> и <code>9</code>, то он сможет отобразить дату <<второе февраля 2009 года>> и не сможет отобразить дату <<третье февраля 2009 года>>. </p>

<p>Стоит отметить, что программировать Вася умеет неплохо, поэтому он не забывает, что существует такое понятие, как високосный год, в котором в феврале 29 дней. Напомним, что год является високосным, если его номер кратен 4 и при этом не кратен 100, либо кратен 400.</p>

### 입력 

 <p>Первая строка входного файла состоит из одного целого числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>k</mi><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le k \le 10$</span></mjx-container>). Во второй строке входного файла перечислены через пробел <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> различных цифр, которые Васин календарь умеет отображать. Следующие две строки содержат описание первой и последней даты интересующего его промежутка в формате <<ДД.ММ.ГГГГ>>.</p>

### 출력 

 <p>В выходной файл выведите одно целое число --- количество дней в промежутке включая концы, в которые календарь может показать дату.</p>

