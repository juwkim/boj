# [Silver II] Прибытие Таноса - 28918 

[문제 링크](https://www.acmicpc.net/problem/28918) 

### 성능 요약

메모리: 117092 KB, 시간: 188 ms

### 분류

백트래킹, 브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵

### 제출 일자

2025년 3월 15일 01:22:34

### 문제 설명

<p>Когда Халк прибыл на Землю, он сообщил Доктору Стрэнджу время прибытия на землю Таноса. Однако, Доктор не уверен, что после такого падения Халк правильно запомнил эту дату. Однако он уверен, что набор цифр, который сказал Халк, точно верный. Теперь ему нужно понять, в какие даты может прибыть Танос.</p>

<p>Помогите ему. По дате, которую сообщил Халк, посчитайте все возможные корректные даты, которые можно получить из нее перестановкой цифр. Дата называется корректной, если ee год положительный, месяц не больше <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$12$</span></mjx-container>, а номер дня не больше количества дней в этом месяце. В високосном году в феврале на один день больше --- <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>29</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$29$</span></mjx-container> дней вместо <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$28$</span></mjx-container>. Год называется високосным, если его номер делится на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$400$</span></mjx-container>, или если его номер делится на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>, но не делится на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>.</p>

### 입력 

 <p>В первой строке входных данных задана дата в формате <strong>ГГГГ ММ ДД</strong>. Гарантируется, что это корректная дата с учeтом високосных годов.</p>

### 출력 

 <p>В первой строке выведите количество дат, которые можно получить перестановкой цифр из исходный даты. Далее, по одной в строке, выведите сами эти даты в таком же формате, в порядке от самой ранней до самой поздней.</p>

