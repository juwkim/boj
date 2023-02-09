# [Bronze II] Finalists - 26310 

[문제 링크](https://www.acmicpc.net/problem/26310) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 정렬(sorting)

### 문제 설명

<p>Frank is trying his best to win a slot in Asia Pacific to the World Finals. But he could not find the selection rules to estimate his chance. Last night, Frank’s coach found the following document.</p>

<pre>=====================================================================
World Finals team selection rules from Asia Pacific (2022 cycle)

Due to COVID-19 outbreak, this year's Asia Pacific rules will
again be quite different from those of usual years. The plan
for having an Asia Pacific semi-final contest (play-off contest)
has been cancelled and postponed to the next year.

Only the following six regionals will be held this year.

Ho Chi Minh, Vietnam
Jakarta, Indonesia
Manila, Philippines
Seoul, Korea
Taoyuan, Taiwan
Yokohama, Japan

We have set a team participation rule. This rule is a special one
for this year (2022 cycle) only.

Teams from a hosting country (Indonesia, Japan, Korea, Philippines,
Taiwan and Vietnam) can only join the regional held in their own
country. Universities from non-hosting countries should choose a
regional. Note that all teams from a single university have to join
the same regional.

World Finals team selection rules are as follows.

Apply Steps A1 through A4 below in this order.

A1. Define the site score of a regional as follows.
0.56 * number of universities in regional
+ 0.24 * number of teams in regional
+ 0.14 * number of universities in preliminary contests
+ 0.06 * number of teams in preliminary contests
+ 0.3 * number of foreign teams

Only teams or universities solving at least one problem are counted.

A2. Sort our six regionals according to their site scores.

A3. Let N be the number of World Finals slots given from the ICPC
Headquarters. Until the sum of the number of allocated slots
reaches N, allocate slots to regionals, one by one, in the
descending order of their site scores. When all six regionals
are allocated one slot each, continue from the regional with the
highest site score in the round robin fashion.

A4. For each regional, let M be the number of slots allocated to the
regional through the step A3. Select the M highest ranked
universities. The team with the highest rank in the university
is automatically selected.
=====================================================================
</pre>

<p>Assume that the document is the final selection rules for teams from Asia Pacific. Given N and the necessary numbers to calculate the site scores, please write a program to compute the number of slots allocated to Taiwan.</p>

### 입력 

 <p>There are seven lines in the inputs. The first line contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, the number of World Finals slots given from the ICPC Headquarters. Each of the following six lines consists of one string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> and five non-negative integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D462 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D462 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D453 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mi>t</mi></msub><mo>,</mo><msub><mi>p</mi><mi>u</mi></msub><mo>,</mo><msub><mi>r</mi><mi>t</mi></msub><mo>,</mo><msub><mi>r</mi><mi>u</mi></msub><mo>,</mo><mi>f</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p_t , p_u, r_t , r_u, f$</span></mjx-container>. The string and the numbers are separated by spaces. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> is a country hosting a regional contest. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mi>t</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p_t$</span></mjx-container> is the number of teams solving at least one problem in the preliminary contests hosted by the country <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D462 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mi>u</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p_u$</span></mjx-container> is the number of universities solving at least one problem in the preliminary contests hosted by the country <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mi>t</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$r_t$</span></mjx-container> is the number of teams solving at least one problem in the regional contest hosted by the country <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D462 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mi>u</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$r_u$</span></mjx-container> is the number of universities solving at least one problem in the regional contest hosted by the country <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D453 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$f$</span></mjx-container> is the number of foreign teams solving at least one problem in the regional hosted by the country <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>.</p>

### 출력 

 <p>Output the number of slots allocated to Taiwan.</p>

