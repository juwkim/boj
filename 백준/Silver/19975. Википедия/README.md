# [Silver III] Википедия - 19975 

[문제 링크](https://www.acmicpc.net/problem/19975) 

### 성능 요약

메모리: 113340 KB, 시간: 288 ms

### 분류

문자열

### 제출 일자

2024년 2월 5일 08:24:36

### 문제 설명

<p>Воодушевленный успехом <<Википедии>>, Петя решил создать аналогичную энциклопедию на своей домашней странице. Поскольку Петя изучает английский язык, он решил сделать английскую версию энциклопедии.</p>

<p>Для начала он взял несколько текстов из <<Encyclopedia Britannica>> и набрал их. Теперь он хочет расставить внутри статей ссылки на другие статьи. Однако статей очень много, поэтому он решил автоматизировать процесс.</p>

<p>Ссылка на статью на вики-странице устроена следующим образом: </p>

<p style="text-align: center;"><<<code>[[Название статьи|текст ссылки]]</code>>>.</p>

<p>Например, во фразе <<<code>In the wild cats are often enemies of [[Dog|dogs]].</code>>> слово <<dogs>> будет ссылкой на статью <<Dog>>. Если название статьи совпадает с текстом ссылки, можно ссылку можно оформить просто как</p>

<p style="text-align: center;"><<<code>[[Название статьи]]</code>>>.</p>

<p>Например, во фразе <<<code>Growing together a [[dog]] and a cat can often be friends.</code>>> слово <<dog>> будет ссылкой на статью <<dog>>. При этом в названиях статей регистр первой буквы игнорируется, а регистр остальных букв важен. Например, слово <<dog>> может быть ссылкой на статью <<Dog>>, а слово <<DOG>> --- нет.</p>

<p>Помогите Пете расставить ссылки на его сайте. Сайт представляет собой множество статей. Каждая статья имеет название --- одно слово, и текст. Для слова названия известны все его словоформы и синонимы.</p>

<p>Будем называть словом в тексте последовательность букв английского алфавита, ограниченную с обеих сторон символами, не являющимися буквами, либо началом или концом строки. В тексте статьи требуется найти все слова, которые являются словоформами или синонимами названий других статей и превратить их в вики-ссылки.</p>

### 입력 

 <p>Первая строка входного файла содержит число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество статей в Петиной википедии (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le n \le 50$</span></mjx-container>). Далее следуют описания статей.</p>

<p>Описание каждой статьи начинается со строки, которая содержит название этой статьи. Далее следует строка, содержащая одно число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> --- количество словоформ и синонимов к названию статьи, это число не превышает 10. Следующие <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> строк содержат по одному слову на строке --- словоформы и синонимы к названию текущей статьи. Далее следует строка, содержащая число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D459 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$l$</span></mjx-container> --- количество строк в тексте статьи, это число не превышает 10. Затем следует текст статьи --- <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D459 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$l$</span></mjx-container> строк, каждая из которых имеет длину не более 80 символов.</p>

<p>Все названия статей различны. Все словоформы и синонимы всех названий различны и отличаются от названий статей.</p>

<p>Все слова состоят из букв латинского алфавита, длина каждого слова во входном файле не превышает 20, во входном файле встречаются только пробелы, переводы строк и символы с ASCII кодами от 32 до 126.</p>

### 출력 

 <p>Выведите в выходной файл версии статей с расставленными ссылками. Выводите статьи следующим образом. Сначала выведите название статьи. Затем выведите текст статьи, разбитый на строки также как и во входном файле. Все слова в тексте, которые совпадают с названием статьи, или со словоформой или синонимом названия статьи, отличной от той, в которой они встречаются, следует превратить в ссылки. При сравнении слов следует игнорировать регистр первой буквы, но соблюдать регистр остальных. Слова, совпадающие с названием, следует превратить в краткую версию ссылки, а не совпадающие --- в полную.</p>

