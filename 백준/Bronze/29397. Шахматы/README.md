# [Bronze I] Шахматы - 29397 

[문제 링크](https://www.acmicpc.net/problem/29397) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

애드 혹

### 제출 일자

2024년 4월 2일 10:37:54

### 문제 설명

<p>Вчера мудрая Сова в своем великолепном замке <<Каштаны>> нашла шахматы. Но выслушать и запомнить правила игры полностью смог только Кролик. В связи с этим, Сова решила упростить правила. В результате нововведений на доске остались только 2 фигуры, которые, для простоты запоминания, было решено назвать в честь жителей Волшебного Леса. Одна из фигур  --- это конечно же ужасный Слонопотам, в честь которого, кстати, назван обычный шахматный слон. А вторую фигуру единогласно было решено назвать в честь Тигры (кто же еще сможет схватить Ужо…пото… Слонопотама?). Тигра недоволен ходами существующих фигур и хочет ходить (а точнее прыгать), по-своему, ведь больше всего на свете Тигра любит прыгать, прыгать и прыгать. А точнее он хочет, чтобы его фигура могла прыгать либо на две клетки по вертикали или горизонтали, либо на одну клетку по диагонали. Также Сова решила, что будет справедливо, если фигура Слонопотама не будет ходить, поскольку настоящий Слонопотам обычно прячется в засаде и не двигается, чтобы его не заметили.</p>

<p>Помогите жителям Волшебного Леса понять, сумеет ли Тигра схватить, то есть попасть в одну клетку со Слонопотамом в ходе шахматной партии.</p>

### 입력 

 <p>Во входном файле содержатся координаты двух клеток, с местонахождением Тигры и Слонопотама, каждая в отдельной строке. Координаты клеток задаются в виде пары буквы (от <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container> до <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container>) и цифры (от <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> до <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container>) без пробелов.</p>

### 출력 

 <p>В выходной файл выведите <<YES>>, если фигура Тигры может схватить фигуру Слонопотама, и <<NO>> --- если не может.</p>

