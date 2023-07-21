# [Bronze III] Eszett - 28373 

[문제 링크](https://www.acmicpc.net/problem/28373) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현, 문자열

### 문제 설명

<p>For those trying to learn German, the letter 'ß', called <em>Eszett</em> or <em>sharp S</em>, is usually a source of great confusion. This letter is unique to the German language and it looks similar to a 'b' but is pronounced like an 's'.</p>

<p>Adding to the confusion is the fact that, until a few years ago, only a lowercase version of 'ß' existed in standard German orthography. Wherever an uppercase 'ß' was needed, for example in legal documents and shop signs, it was (and usually still is) replaced by capital double letters 'SS'. In 2017, the capital 'ẞ' was officially introduced into the German language and may now be used in those scenarios, instead.</p>

<p>Other than being confusing for foreigners, the practice of replacing 'ß' with 'SS' also introduces some ambiguity because a given uppercase word featuring one or more occurrences of 'SS' may correspond to multiple different lowercase words, depending on whether each 'SS' is a capitalized 'ß' or 'ss'.</p>

<p>Given one uppercase word, find all the lowercase words that it could be derived from. As the letter 'ß' is not part of the ASCII range, please write an uppercase 'B', instead.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with a string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>s</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le |s| \le 20$</span></mjx-container>) consisting of uppercase letters.</li>
</ul>

<p>It is guaranteed that the letter <code>S</code> occurs at most three times in <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>. Note that <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> need not be an actual German word.</p>

### 출력 

 <p>Output all the possible lowercase strings corresponding to <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>. Any order will be accepted, but each string must occur exactly once.</p>

