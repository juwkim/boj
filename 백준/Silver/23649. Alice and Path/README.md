# [Silver II] Alice and Path - 23649 

[문제 링크](https://www.acmicpc.net/problem/23649) 

### 성능 요약

메모리: 111444 KB, 시간: 100 ms

### 분류

애드 혹, 해 구성하기, 기하학, 문자열

### 제출 일자

2025년 2월 7일 20:19:03

### 문제 설명

<p>Consider an infinite planar board consisting of equal equilateral triangles. Alice was standing in such a triangle, facing one of its vertices. After that, she made a sequence of steps. There are three kinds of steps. Step "<code>l</code>" is to turn left and move to the neighboring triangle. Step "<code>r</code>" is to turn right and move to the neighboring triangle. Step "<code>b</code>" is to turn around and move to the neighboring triangle. Note that, after every possible step, Alice again faces one of the vertices of her new triangle: the girl looks at the vertex opposite to the side she just stepped over.</p>

<p>So, Alice went along some path consisting of steps "<code>l</code>", "<code>r</code>", and "<code>b</code>". Help her return to the triangle where she started! Compose a sequence of steps which will bring her there. The direction in which Alice will look after completing the steps is irrelevant: the important thing is to finish at the initial triangle.</p>

### 입력 

 <p>The input consists of a single line denoting the sequence of steps: it can contain the letters "<code>l</code>", "<code>r</code>", and "<code>b</code>", and has length from <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> to <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10\,000$</span></mjx-container> letters. It is guaranteed that completing this sequence of steps brings Alice to a triangle different from the initial one.</p>

### 출력 

 <p>Print a line containing a sequence of steps. It must have length from <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> to <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100\,000$</span></mjx-container> letters and consist of the letters "<code>l</code>", "<code>r</code>", and "<code>b</code>". After completing the input sequence of steps, and then the output sequence, Alice must finish at the initial triangle. If there are several possible answers, print any one of them. Note that the length of the output sequence need not be the minimum possible.</p>

