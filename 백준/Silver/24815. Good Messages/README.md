# [Silver III] Good Messages - 24815 

[문제 링크](https://www.acmicpc.net/problem/24815) 

### 성능 요약

메모리: 112004 KB, 시간: 132 ms

### 분류

구현, 시뮬레이션, 문자열

### 제출 일자

2024년 4월 15일 23:19:24

### 문제 설명

<p>Boris works at a secret communication station for the government training new employees on how to encode messages. Messages at this station are encoded with a rotation ("Caesar") cipher that replaces each letter with one at a set offset in the alphabet, e.g., for offset <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container> an '<code>a</code>' is replaced by a '<code>c</code>' and '<code>y</code>' is replaced by '<code>a</code>'. In order to encode a message, this cipher may be applied more than once. Each such application counts as a step in the encoding process. Boris teaches the new employees to encode messages by demonstrating each step of the encoding individually. However, Boris does not does not like seeing messages that contain at least half as many vowels as consonants after applying an encoding step. (Boris considers '<code>a</code>', '<code>e</code>', '<code>i</code>', '<code>o</code>', '<code>u</code>', and '<code>y</code>' as vowels). He grows annoyed and more and more unhappy with each step where this situation occurs.</p>

<p>Your job is to encode a given message and determine whether Boris will see fewer steps that annoy him than ones that don't.  Since Boris wants to be happy in his job he will give a message that annoys him too much to a colleague.</p>

### 입력 

 <p>The input consists of a single test case. The first line of the input contains a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$O$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>O</mi><mo>≤</mo><mn>25</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le O \le 25$</span></mjx-container>) that represent the offset used for the rotation cipher. The second line contains the message to encode, which consists entirely of lowercase English characters. The length of the message is between <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$80$</span></mjx-container> characters. The third line will contain an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>26</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 26$</span></mjx-container>), the number of times the cipher must be applied.</p>

### 출력 

 <p>Output '<code>Boris</code>' if strictly more steps sound good than bad, and '<code>Colleague</code>' otherwise.</p>

