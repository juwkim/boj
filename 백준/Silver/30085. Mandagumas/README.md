# [Silver II] Mandagumas - 30085 

[문제 링크](https://www.acmicpc.net/problem/30085) 

### 성능 요약

메모리: 116928 KB, 시간: 144 ms

### 분류

자료 구조, 덱, 구현

### 제출 일자

2025년 3월 18일 21:59:30

### 문제 설명

<p>Ilgu koridoriumi eina <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> labai mandagių žmonių. Koridoriuje yra įrengtos dviejų tipų durys:</p>

<ol>
	<li>„A“ tipo durys: atidaromos traukiant. Priėjus tokias duris, pirmasis žmogus mandagiai praleidžia visus kitus iš eilės, ir tampa paskutinis. Visų kitų žmonių tvarka eilėje tarpusavyje nepasikeičia.</li>
	<li>„B“ tipo durys: atidaromos stumiant. Priėjus tokias duris, pirmasis žmogus mandagiai praleidžia antrąjį, antrasis – trečiąjį ir taip toliau. Taigi perėjus „B“ tipo duris, visa eilė „apsivečia“: paskutinis ėjęs dabar tampa pirmasis, o pirmas – paskutinis.</li>
</ol>

<p>Mandagieji žmonės iš pradžių yra sunumeruoti nuo <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> iki <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>. Jums duota seka durų, kurias jie turi praeiti. Raskite, kokia tvarka bus išsidėstę žmonės perėję pro visas duris.</p>

### 입력 

 <p>Pirmojoje eilutėje įrašytas mandagių žmonių skaičius <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>. Antrojoje eilutėje įrašytas durų skaičius koridoriuje <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>. Kitose <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> eilučių įrašyta po vieną simbolį, <code>A</code> arba <code>B</code>, kurie žymi durų tipus koridoriuje, ta tvarka, kuria juos praeis žmonės.</p>

### 출력 

 <p>Jūs turite išvesti <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> skaičių po vieną eilutėje – mandagių žmonių numerius, ta tvarka, kuria jie bus išsidėstę perėje pro visas duris.</p>

