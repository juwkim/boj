# [Silver IV] Загадка древних Ассасинов - 28987 

[문제 링크](https://www.acmicpc.net/problem/28987) 

### 성능 요약

메모리: 121252 KB, 시간: 144 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 1월 17일 16:49:27

### 문제 설명

<p>Древние ассасины часто прятали свои секреты за загадками, которые могут решить только истинные ассасины.</p>

<p>Так например, чтобы открыть комнату с реликвиями испанского братства времен Агилара де Нерха, нужно из набора цифр составить наибольшее возможное число, которое будет делится на три без остатка. При этом, число может начинаться с ведущих нулей, и при равных значениях большим считается более длинное. Например, <<00021>> считается большим, чем <<021>>.</p>

<p>Каллум Линч нашел исходный набор цифр, из которых нужно составить ключ, но он оказался довольно длинным. Ваша задача помочь ему по данному набору цифр найти наибольшее число, состоящее из этих цифр, которое делится на три без остатка.</p>

### 입력 

 <p>В единственной строке входного файла находится строка, состоящая из цифр от <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> до <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container> --- набор цифр, из которых предлагается собрать решение загадки. Длина строки не меньше трех и не превосходит <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^5$</span></mjx-container>.</p>

### 출력 

 <p>В выходной файл выведите наибольшее число, которое можно составить из данных цифр, чтобы оно делилось на три без остатка.</p>

