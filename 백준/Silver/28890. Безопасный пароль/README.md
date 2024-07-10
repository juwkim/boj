# [Silver IV] Безопасный пароль - 28890 

[문제 링크](https://www.acmicpc.net/problem/28890) 

### 성능 요약

메모리: 112004 KB, 시간: 116 ms

### 분류

문자열

### 제출 일자

2024년 7월 11일 02:12:30

### 문제 설명

<p>Однажды Эркюль Пуаро решил изменить пароль от своего сейфа. <em>Паролем</em> он называет строку, состоящую из строчных латинских букв. Придумав новый пароль, Пуаро хочет убедиться, что его никто не сможет подобрать.</p>

<p>Мсье Бук подсказал ему, что <em>безопасным</em> называется пароль, который не содержит трех или более одинаковых символов подряд, а также никакой символ которого не встречается в ней чаще, чем в половине позиций.</p>

<p>Помогите Пуаро получить из придуманной им строки безопасный пароль при помощи минимального количества операций вида <<заменить <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>-й символ строки на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$c$</span></mjx-container>>>.</p>

### 입력 

 <p>Входные данные содержит единственную непустую строку, содержащую хотя бы два, но не более, чем <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$25$</span></mjx-container> символов, состоящую из строчных букв латинского алфавита.</p>

### 출력 

 <p>Выведите в единственной строке полученный безопасный пароль.</p>

