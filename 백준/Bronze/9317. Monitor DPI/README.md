# [Bronze III] Monitor DPI - 9317 

[문제 링크](https://www.acmicpc.net/problem/9317) 

### 성능 요약

메모리: 126160 KB, 시간: 352 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Monitor resolution is increasing fairly quickly and as a responsible consumer you want to be able to compare the Dots Per Inch (DPI) of the screens you are considering purchasing. Unfortunately for you the manufacturers don’t specify the DPI, they only specify the diagonal size in inches and the resolution in width by height. You may assume the width to height ratio is 16:9 for all screens.</p>

<p>Let:</p>

<p>\[W = \text{ the width of the screen in inches} \\ H = \text{ the height of the screen in inches} \\ D = \text{ Diagonal size of screen in inches}\]</p>

<p>Since:</p>

<p>\[D = \sqrt{W^2+H^2}\]</p>

<p>And:</p>

<p>\[H = \frac{9}{16}W\]</p>

<p>Thus</p>

<p>\[D = \sqrt{W^2 + \left(\frac{9}{16}W\right)^2} = \sqrt{\left(1+\frac{9^2}{16^2}\right)W^2} = \sqrt{1+\frac{9^2}{16^2}}W \]\[ W = \frac{16 \times D}{\sqrt{337}}  \]\[ \text{DPI}_{\text{Horizontal}} = \frac{\text{Resolution}_{\text{Horizontal}}}{W} \]\[ \text{DPI}_{\text{Vertical}} = \frac{\text{Resolution}_{\text{Vertical}}}{H} \]</p>

### 입력 

 <p>Each input line will have 3 numbers, the decimal value D, the integer value \(\text{Resolution}_{\text{Horizontal}}\), and the integer value \(\text{Resolution}_{\text{Vertical}}\). An input line of three zeroes will signify end of input</p>

### 출력 

 <p>For each test case (line of input) you should calculate the horizontal and vertical DPI and output it rounded to 2 decimal places as follows:</p>

<pre>Horizontal DPI: XXX.XX
Vertical DPI: XXX.XX</pre>

