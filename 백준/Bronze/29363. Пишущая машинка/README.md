# [Bronze II] Пишущая машинка - 29363 

[문제 링크](https://www.acmicpc.net/problem/29363) 

### 성능 요약

메모리: 111420 KB, 시간: 164 ms

### 분류

그리디 알고리즘, 수학

### 제출 일자

2025년 3월 5일 12:09:02

### 문제 설명

<p>Некоторое время назад была изобретена пишущая машинка нового поколения. Всем хочется тратить на написание больших текстов как можно меньше времени. Именно это и послужило предпосылкой к созданию такой машинки. </p>

<p>К обычному для всех печатных машинок набору клавиш (символы и перевод каретки на новую строку), у этой машинки добавились две новых. Первая кнопка позволяет стереть последний напечатанный символ, если он находится в той же строке, что и каретка. Вторая кнопка позволяет за одно нажатие напечатать в текущей строке последнее слово из предыдущей строки. Однако, из-за экспериментальности данной модели печатной машинки, вторая кнопка работает только в том случае, если каретка стоит в начале новой строки, в которой еще не было напечатано ни одного символа, причем ее нажатие перемещает каретку в конец скопированного и вставленного в текущую строку слова.</p>

<p>У злодеев всегда лучшее оборудование, и это прекрасно известно Шерлоку Холмсу. В деле, которое он в данный момент расследует, появилась новая зацепка. Новый подозреваемый был задержан и допрошен. Чтобы составить общую картину, Холмс хочет выянить, этот ли человек написал шифровку, которая проходит уликой по делу, или это сделал кто-то другой. </p>

<p>Шифровка выглядит как набор из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> слов, каждое из которых находится в отдельной строке. За подозреваемым велась слежка, и было установлено, что напечатать эту шифровку он мог только в небольшой промежуток времени. У Шерлока возник вопрос, мог ли он за это время успеть напечатать весь текст шифровки.</p>

<p>Исследовав этот текст, Холмс выяснил, за какое наименьшее количество нажатий на кнопки пишущей машинки его можно было написать. Повторите его исследование. Считайте, что для каждой буквы на машинке есть соответствующая ей кнопка, также есть кнопки <em>перевод каретки на новую строку</em>, <em>стереть последний символ в текущей строке</em> и <em>скопировать последнее слово из предыдущей строки в текущую, если в текущей еще не было напечатано ни одного символа</em>.</p>

### 입력 

 <p>В первой строке дано число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество слов в шифровке. В следующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строках перечислены сами слова шифровки. Слова состоят из маленьких и больших латинских букв. Суммарная длина слов не превышает <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mrow data-mjx-texclass="ORD"><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle></mrow><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$200{\,}000$</span></mjx-container>, все слова непусты.</p>

### 출력 

 <p>Выведите единственное целое число --- наименьшее количество нажатий на кнопки пишущей машинки, за которое можно набрать этот текст.</p>

