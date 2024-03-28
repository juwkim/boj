# [Bronze III] Закат - 29308 

[문제 링크](https://www.acmicpc.net/problem/29308) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

구현

### 제출 일자

2024년 3월 28일 18:16:26

### 문제 설명

<p>Долгие переговоры руководства ФК <<Закат>> увенчались успехом: Брюс Бэннер присоединился к команде. Как и положено звезде мирового футбола, он получал немаленькую зарплату.</p>

<p>Однако, одному из прежних игроков команды это не понравилось. Стало ясно, что не избежать волны требований увеличения заработка. После некоторого раздумья, великий тренер Чулано Спагетти нашел способ решить эту проблему.</p>

<p>Всего в команде <<Закат>> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> игроков. Некоторые из них имеют российское гражданство, все остальные --- легионеры. К требованиям легионеров тренер относится с осторожностью и предпочтет увеличить им зарплату, чтобы не упустить ценного игрока. А вот российских игроков тренер будет стимулировать снижать их запросы следующим действием: в ближайшем матче не выпускать на поле того игрока с российским гражданством, который потребует себе наибольшую зарплату. Теперь ваша задача определить, кто из команды не выйдет на поле, зная фамилии игроков, их гражданство и зарплату, которую они требуют.</p>

### 입력 

 <p>В первой строке задано число футболистов <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100$</span></mjx-container>). % n ≤ 100 Далее следуют <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк, содержащих описания футболистов. Каждое описание состоит из перечисленных через пробел зарплаты, требуемой этим игроком, его фамилии и гражданства. Фамилия и гражданство --- строки, содержащие только строчные и прописные латинские символы. Длина фамилии и гражданства не превышает 20 символов. У игроков, имеющих российское гражданство, в соответствующем параметре значится <<Russia>>. Зарплата, которую требует игрок --- положительное число, не превышающее <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^9$</span></mjx-container>. Гарантируется, что в команде есть хотя бы один игрок с российским гражданством.</p>

### 출력 

 <p>Выведите фамилию футболиста, который не выйдет на поле. Гарантируется, что такой игрок всегда один.</p>

