# [Silver V] Олимпийские игры - 29645 

[문제 링크](https://www.acmicpc.net/problem/29645) 

### 성능 요약

메모리: 112004 KB, 시간: 132 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 정렬

### 제출 일자

2023년 12월 6일 11:05:20

### 문제 설명

<p>Работать постоянным комментатором на Олимпийских играх --- дело крайне сложное. Чтобы это понять, достаточно представить себе, сколько соревнований необходимо комментировать. Так как не все соревнования проходят динамично, комментатору часто предоставляется много свободного времени в эфире, которое требуется заполнить различными рассказами.</p>

<p>Известный комментатор Дима однажды из достоверных источников узнал, что перед проведением первых Олимпийских игр была проведена их генеральная репетиция с целью выявления недостатков организации. Также Диме удалось выяснить для каждого из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> разыгранных на репетиции комплектов медалей названия стран, представители которых получили золотую, серебряную и бронзовую медали.</p>

<p>Своим слушателям Дима хочет зачитать в эфире результаты неофициального командного зачета репетиции олимпиады, однако не может их подсчитать. Поэтому он просит Вас написать программу, которая поможет ему правильно определить хотя бы страну-победителя зачета.</p>

<p>Напомним, что первым критерием при подсчете результатов является число золотых медалей, завоеванных представителями страны, вторым --- серебряных, третьим --- бронзовых. Наконец, если у двух стран количества золотых, серебряных и бронзовых медалей совпадают, то выше ставится страна, название которой лексикографически меньше. Например, если в соревнованиях принимали участие три страны: <<RUSSIA>> (4 золотые, 6 серебряных, 5 бронзовых медалей), <<ALBANIA>> (4, 0, 2) и <<RUSIA>> (4, 6, 5), то первое место займет <<RUSIA>>, второе --- <<RUSSIA>>, третье --- <<ALBANIA>>.</p>

### 입력 

 <p>В первой строке входного файла содержится число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество разыгранных на репетиции олимпиады комплектов медалей (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100$</span></mjx-container>). В каждой из следующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк содержатся три отделенные друг от друга пробелами слова, состоящие из заглавных латинских букв, --- названия стран, представители которых получили золотую, серебряную и бронзовую медали соответственно. Длина каждой строки входного файла не превышает 200 символов.</p>

### 출력 

 <p>В выходной файл выведите название страны-победителя неофициального командного зачета.</p>

