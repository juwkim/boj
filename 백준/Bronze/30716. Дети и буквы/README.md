# [Bronze II] Дети и буквы - 30716 

[문제 링크](https://www.acmicpc.net/problem/30716) 

### 성능 요약

메모리: 112972 KB, 시간: 164 ms

### 분류

애드 혹, 문자열

### 제출 일자

2023년 12월 10일 21:43:54

### 문제 설명

<p>Алиса и Боб хотят пройти через турникет в метро. У них есть полоска, на которой в ряд написаны <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строчных букв латинского алфавита. Для того, чтобы пройти через турникет, каждый должен приложить к нему бумажку с кодовым словом. Турникет сканирует слово, записанное на бумажке и открывается, позволяя пройти одному человеку. Чтобы запретить человеку ездить по одному билету несколько раз, турникет не откроется если приложить к нему бумажку со словом, которое турникет сканировал до этого.</p>

<p>Алиса и Боб пришли в метро к открытию, поэтому через турникет еще никто не проходил, и он пропустит человека с любым текстом на билете. Детям разрешено вырезать ровно по одному непустому билету из полоски, причем билеты должны состоять из подряд идущих букв полоски и <strong>не должны пересекаться</strong>. Также, чтобы никто из детей не считал себя обделeнным, билеты, которые они вырежут, должны быть одинаковой длины. После вырезания билетов Алиса, а затем Боб попробуют пройти через турникет. Таким образом, Алиса сможет войти в метро всегда, а Боб сможет войти только если текст на его билете не совпадает с текстом на билете Алисы.</p>

<p>Так как дети маленькие, нужно помочь им определить, можно ли вырезать два различных билета одинаковой длины из полоски, чтобы попасть в метро, и, если это возможно, объяснить им, как это сделать.</p>

### 입력 

 <p>В первой строке задано одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq n \leq 10^6$</span></mjx-container>) --- количество букв, написанных на полоске.</p>

<p>Во второй строке содержится строка, состоящая из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строчных букв латинского алфавита --- текст на полоске.</p>

### 출력 

 <p>Если невозможно вырезать из полоски два различных слова одинаковой длины выведите <<<code>No</code>>> (без кавычек).</p>

<p>Иначе в первой строке выведите <<<code>Yes</code>>> (без кавычек), а во второй строке выведите три целых числа --- номер символа на полоске, с которого начнется билет Алисы, номер символа на полоске, с которого начнется билет Боба и длину билетов, которые вырежут дети. Каждый символ полоски должен попасть не более, чем в один билет, а также тексты на билетах должны быть различны. Символы на полоске нумеруются слева направо, <strong>начиная с 1</strong>.</p>

<p>Обратите внимание, что после вырезания билета из полоски, его нельзя переворачивать. Так, например, если вырезать билет <code>po</code> из полоски <code>rpo</code>, то получить билет <code>od</code>, перевернув билет <code>po</code> сверху вниз, не получится.</p>

