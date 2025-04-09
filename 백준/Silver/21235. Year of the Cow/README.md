# [Silver I] Year of the Cow - 21235 

[문제 링크](https://www.acmicpc.net/problem/21235) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

그래프 이론, 그래프 탐색, 구현, 파싱, 문자열

### 제출 일자

2025년 4월 9일 13:23:18

### 문제 설명

<p>Farmer John's cows are excited to learn that Chinese New Year was recently celebrated, ushering in the year of the Ox, always a bovine favorite.</p>

<p>As we know, the zodiac animals for Chinese calendar years follow a 12-year cycle: Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig, Rat, and then Ox again.</p>

<p>Bessie the cow is proud to say she was born in a year of the Ox, many years ago. Her friend Elsie wants to know how many years apart from Bessie she was born, and hopes you can help her deduce this by looking at relationships between the birth years of several cows on the farm.</p>

### 입력 

 <p>The first line of input contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 100$</span></mjx-container>). Each of the next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines contains an 8-word phrase specifying the relationship between the birth years of two cows. It is of the form</p>

<p>"Mildred born in previous Dragon year from Bessie",</p>

<p>or</p>

<p>"Mildred born in next Dragon year from Bessie"</p>

<p>The last word is the name of a cow on the farm, which is either "Bessie" or a cow that has already been mentioned in a previous line of input.</p>

<p>The first word is the name of a cow on the farm who is not "Bessie" and who has not yet been mentioned in the input. All cow names have at most 10 characters that are in the range a..z or A..Z.</p>

<p>The 5th word is one of the 12 zodiac animals above.</p>

<p>The 4th word is either "previous" or "next". For example, if the phrase is "Mildred born in previous Dragon year from Bessie", then Mildred's year of birth was the Dragon year closest to and strictly before (not equal to) Bessie's birth year.</p>

### 출력 

 <p>Please output the number of years by which Bessie and Elsie's birth years differ. It is guaranteed that this number can be determined by the input given.</p>

