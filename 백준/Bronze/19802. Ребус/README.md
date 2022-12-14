# [Bronze I] Ребус - 19802 

[문제 링크](https://www.acmicpc.net/problem/19802) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

파싱(parsing), 문자열(string)

### 문제 설명

<p>На прошлом уроке английского Пете задали домашнее задание. Оно заключалось в разгадывании ребусов. Каждый ребус --- это последовательность картинок. С двух сторон от каждой картинки могут располагаться апострофы. Каждая картинка обозначает некоторое слово. Предположим, что перед некоторой картинкой нарисовано $i$ апострофов, а после нее $j$ апострофов. Это значит, что у слова, которое сопоставляется картинке, необходимо убрать $i$ букв с начала и $j$ с конца, а оставшуюся его часть записать вместо картинки и апострофов. Так необходимо сделать с каждой картинкой и окружающими ее апострофами. После этого нужно <<склеить>> получившиеся кусочки в одно слово. Оно и будет разгадкой ребуса.</p>

<p>У Пети нет проблем с тем, чтобы сопоставить каждой картинке слово. Но ему очень лень заниматься отбрасыванием лишних букв и склеиванием слов. Поэтому он попросил вас помочь ему. Дана строка, которая состоит из маленьких латинских букв, апострофов (символов с кодом 39), а также пробелов, которые разделяют слова. Апостроф относиться к некоторому слову, если между ними нет пробела. Если апостроф стоит слева от слова, то у него необходимо убрать одну букву с начала, если справа --- с конца. Потом необходимо склеить все слова в одно.</p>

<p>Например, пусть дана строчка <<team ''''school ''olympiad'''>>. В первом слове ничего изменять не надо, так как к нему не относится ни один апостроф. Во втором необходимо убрать первые четыре буквы и получить <<ol>>, из третьего слова получится <<ymp>>. После скеливания трех кусочков получим строку <<teamolymp>>.</p>

### 입력 

 <p>В первой строке входного файла дан ребус, длиной не более $100$ символов, который необходимо решить. Гарантируется, что в строчке присутствуют только апострофы (код символа --- 39), пробелы и маленькие латинские буквы, а также, что ребус корректен --- нет слова, у которого нобходимо удалить букв больше, чем его длина.</p>

### 출력 

 <p>Выведите одно слово --- ответ на ребус.</p>

