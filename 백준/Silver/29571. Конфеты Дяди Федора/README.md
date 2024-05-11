# [Silver IV] Конфеты Дяди Федора - 29571 

[문제 링크](https://www.acmicpc.net/problem/29571) 

### 성능 요약

메모리: 109240 KB, 시간: 120 ms

### 분류

두 포인터

### 제출 일자

2024년 5월 12일 05:15:06

### 문제 설명

<p>В погожий субботний день жители села Простоквашино по традиции собрались на чаепитии у Дяди Федора. На этот раз Дядя Федор открыл ящик с заморскими шарообразными шоколадными конфетами, а Почтальон Печкин в силу своей аккуратности построил из всех конфет пирамидку в форме правильного тетраэдра.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d51f77f2-5624-4d45-ab55-1eefb8dd8c55/-/preview/" style="width: 161px; height: 150px;"></p>

<p>Каждый слой пирамидки представляет собой правильный треугольник, выложенный из конфет, причем сторона его содержит на одну конфету меньше, чем сторона предыдущего слоя. Например, так выглядят третий и четвертый сверху слои пирамидки.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/2e9ee6a9-6e05-4748-b1df-41f87fd8bccf/-/preview/" style="width: 283px; height: 155px;"></p>

<p>Галчонку Хватайке очень не понравилось распределение конфет по слоям (верхний слой состоит из одной конфеты, а последний может состоять, к примеру, из десяти!), и он решил немного исправить ситуацию. Приведя всех в заблуждение и ослабив бдительность фразой <<Кто там?>>, он целиком съел несколько верхних слоев пирамидки.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/df40d0c5-d3c4-4bc7-b513-2224ba0b5c6b/-/preview/" style="width: 161px; height: 121px;"></p>

<p>Этот поступок заметили и начали ловить заметно растолстевшего галчонка. Разумеется, в суете стол опрокинули, и все конфеты рассыпались по полу.</p>

<p>Операцию по поиску и сбору конфет провели Шарик и Матроскин, которые нашли <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> конфет, и заинтересовались, не потерялись ли еще конфеты. Так как никто не помнит, сколько конфет было, да и анализ внешности и состояния Хватайки ничего не дал, будем считать, что конфеты не потерялись, если их можно сложить в усеченную правильную пирамидку, то есть пирамидку без нескольких верхних слоев. Помогите жителям Простоквашино понять, потерялись ли столь ценные заморские конфетки!</p>

### 입력 

 <p>Входной файл содержит единственное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le n \le 10^9$</span></mjx-container>) --- количество найденных конфет.</p>

### 출력 

 <p>Если из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> конфет можно сложить усеченную пирамидку, то выведите в выходной файл слово <code>YES</code>, иначе --- выведите слово <code>NO</code>.</p>

