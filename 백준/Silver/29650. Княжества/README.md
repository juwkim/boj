# [Silver V] Княжества - 29650 

[문제 링크](https://www.acmicpc.net/problem/29650) 

### 성능 요약

메모리: 115140 KB, 시간: 244 ms

### 분류

구현

### 제출 일자

2024년 5월 19일 22:20:30

### 문제 설명

<blockquote>
<p>Лествичное право (от старо-славянского <<лествица>> - лестница) - обычай великокняжеского наследования в Киевской Руси.</p>
</blockquote>

<p>В великом государстве Эн правил мудрый правитель Эм. У мудрого правителя Эм было несколько сыновей. И чтобы каждый из сыновей вырос хорошим правителем, решил Эм каждому выделить по княжеству великому в управление. Но не все княжества равны между собой были, ибо часть была в плодородных землях черноземных, часть в лесах темных, часть в степях диких, да и по размеру княжества были различны. Задумался мудрый Эм, и порешил занумеровать все княжества в порядке главенства -- самое главное княжество нарек он Первым, следующее -- Вторым, и так далее. И княжеств в Энском государстве было бесчисленное множество, и каждое свой номер имело. Старшему наследнику отдал Эм Первое княжество. И Второму своему сыну отдал он Второе княжество, и так далее.</p>

<p>Но тут родилися у Эм внуки, и снова задумался мудрый правитель. Ибо внукам надлежало тоже быть хорошими правителями, а значит и им надобно было выделить княжества. И порешил Эм, что выделит он всем внукам по княжеству, но не в порядке старшинства, а иначе --  сперва лучшие княжества среди сыновей в порядке старшинства распределяются, затем следующие княжества сыновьям старшего брата в правление отдаются, также по старшинству распределенные, потом второго брата сыновьям, по старшинству, и так далее. И обрадовался Эм, ибо система такая позволяла и правнукам, и всем прочим потомкам мужеского пола выделять княжества в правление, и по главенству княжества верно распределены были. И когда родился у Эм еще один сын, то все внуки его и правнуки, и остальные потомки мужеского пола править стали княжеством с на единицу большим номером, а сын новорожденный стал править княжеством с номером на единицу большим чем у второго по младшинству сына, ибо никакой внук не правил княжеством более главным, чем каждый из сыновей, а среди сыновей порядок главенства старшинством задается.</p>

<p>Но тут печаль у Эм приключилась. Умер сын его, и великое княжество без правителя осталось. И призадумался Эм, и решил, что если погиб потомок, то княжество, без правителя оставшееся, правитель следующего княжества княжить будет. Так, все следующие потомки мужекого пола станут княжить земли с на единицу меньшим номером, и все княжества верно по главенству распределены будут.</p>

<p>Получилось так, что в великом государстве в каждый момент времени есть порядок на князях, задаваемый следующим образом: сначала правитель Эм, потом его сыновья в порядке старшинства, потом сыновья старшего сына также в порядке старшинства, потом аналогично сыновья второго по старшинству сына Эма и так далее вплоть до самого младшего.</p>

<p>Таким образом, любой князь из более позднего поколения идет после любого князя из более младшего (даже, если первый старше). Например, любой правнук идет после любого внука.</p>

<p>Летописец государства Эн прилежно вел запись всех событий государства, всех смертей и рождений, в хронологическом порядке. В ваши руки попала эта бесценная летопись. Требуется написать программу для обработки этой летописи, которая будет способна определять, кто правит в <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>-ом княжестве в определенные моменты времени?</p>

### 입력 

 <p>В первой строчке содержится единственное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество событий и запросов в государстве великом (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>2000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 2000$</span></mjx-container>). Следующие строки содержат описания событий в государстве великом и запросов о том, кто в каком княжестве княжит по одному событию или запросу в строчке и в порядке происшествия данных событий в следующем формате:</p>

<ul>
	<li>строка вида <<+ Father Son>> сообщает о великом событии, что у князя с именем <<Father>> родился сын, которого он нарек <<Son>>;</li>
	<li>строка вида <<- Name>> сообщает о великом горе, что умер князь, нареченный <<Name>>;</li>
	<li>строка вида <<? k>> есть суть вопрос --- кто в данный момент княжит в <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>-ом по главенству княжестве (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>k</mi><mo>≤</mo><mn>2500</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le k \le 2500$</span></mjx-container>).</li>
</ul>

<p>Никакие два князя за все время существования государства не имели одинаковых имен и все имена князей в летописи данной записаны только строчными и заглавными латинскими буквами и имеют длину не более 20 символов.</p>

<p>Летопись началась вестись в тот момент, когда в государстве жил один единственный мудрый правитель, именовали которого <<M>>, то есть просто Эм, и правил он в Первом княжестве.</p>

### 출력 

 <p>На каждый запрос вида <<? k>> в выходной файл выведите по одной строке, содержащей имя князя, правившего на момент запроса в <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>-ом по главенству княжестве, или единственный символ <<->>, если на момент запроса в <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>-ом княжестве нет правителя, ибо нет такого количества живых князей. </p>

<p>Все ответы выводите на запросы в том порядке, в котором они задаются во входном файле.</p>

