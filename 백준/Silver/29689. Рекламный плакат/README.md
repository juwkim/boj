# [Silver IV] Рекламный плакат - 29689 

[문제 링크](https://www.acmicpc.net/problem/29689) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 5월 15일 13:19:47

### 문제 설명

<p>Однажды в одном далеком-далеком городе БайтСити компания МакроХард решила разместить по всему городу свои рекламные плакаты. Для этих плакатов было заготовлено несколько рекламных лозунгов.</p>

<p>Каждый лозунг состоит из нескольких слов, порядок которых, разумеется, менять нельзя. Каждое следующее слово можно расположить на плакате или в новой строке горизонтально, или, начиная со следующей строки, вертикально по одной букве слова в одной строке. При этом нельзя два последовательных слова написать вертикально, так как в этом случае их нельзя будет различить.</p>

<p>Известно, что рекламный плакат можно сделать сколь угодно высоким, но, к сожалению, ширина плаката ограничена. Поэтому компания МакроХард хочет разместить лозунг на плакате таким образом, чтобы минимизировать максимальную ширину. Каждое слово печатается одним и тем же моноширинным шрифтом, потому достаточно минимизировать длину самого длинного слова, записанного горизонтально.</p>

<p>В данной задаче Вам дан один рекламный лозунг. Необходимо найти размещение, минимизирующее ширину плаката.</p>

### 입력 

 <p>В первой строке входного файла задано одно число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100$</span></mjx-container>) --- число слов в рекламном лозунге. В следующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строках записан сам лозунг --- по одному слову в строке.</p>

<p>Длина каждого слова не менее двух и не более 100 символов. Слова состоят только из строчных латинских букв.</p>

### 출력 

 <p>В выходной файл выведите единственное число --- минимальную ширину плаката.</p>

