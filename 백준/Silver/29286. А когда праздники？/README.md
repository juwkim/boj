# [Silver V] А когда праздники? - 29286 

[문제 링크](https://www.acmicpc.net/problem/29286) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현

### 제출 일자

2024년 9월 3일 22:37:00

### 문제 설명

<p>Зебра Марти очень любит веселиться. К сожалению, у него на работе очень строгий начальник, поэтому веселиться получается только по праздникам.</p>

<p>На Мадагаскаре не празднуются такие праздники, как день России или международный женский день. Там вообще нет праздников с фиксированными датами. Все праздники отмечаются в даты вроде <<<em>первый понедельник января</em>>> или <<<em>последняя среда июля</em>>>. Более формально, праздничным может быть только либо первый день недели какого-то месяца, либо последний. День недели, как и месяц, могут быть любыми. Календарь на Мадагаскаре полностью совпадает с принятым в России календарем.</p>

<p>Каждый год Марти приходится довольно долго вычислять даты праздников. Он просит вас помочь ему и автоматизировать этот процесс.</p>

### 입력 

 <p>В первой строке дано число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c36"></mjx-c><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>168</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 168$</span></mjx-container>) --- количество праздников, даты которых хочет знать Марти.</p>

<p>Во второй строке сначала записано название дня недели, на который выпало первое января интересующего Марти года. Далее через пробел записано слово <<<code>yes</code>>>, если год високосный, и <<<code>no</code>>> в противном случае.</p>

<p>Далее идут <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк, описывающих праздники, даты которых хочет знать Марти. Первым словом каждой строки может быть либо <<<code>first</code>>>, либо <<<code>last</code>>> --- описание того, выпадает ли описываемый праздник на первый день недели в месяце или на последний соответственно. Далее через пробел следует название дня недели. Далее через пробел следует слово <<<code>of</code>>>, а после этого --- название месяца, в котором отмечается этот праздник.</p>

<p>Все буквы во входном файле строчные. Названия дней недели и месяцев совпадают с названиями, приведенными в таблицах ниже.</p>

### 출력 

 <p>Для каждого праздника выведите в отдельной строке одно число --- то, на какое число месяца этот праздник приходится в описанном году.</p>

