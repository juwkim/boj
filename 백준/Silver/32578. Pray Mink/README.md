# [Silver II] Pray Mink - 32578 

[문제 링크](https://www.acmicpc.net/problem/32578) 

### 성능 요약

메모리: 110828 KB, 시간: 124 ms

### 분류

백트래킹, 수학, 정수론, 소수 판정

### 제출 일자

2025년 3월 13일 18:06:02

### 문제 설명

<p>Aaron, the mink, has two loves: biscuits and prime numbers. Growing up on our farm, he developed a special fondness for both. In the kitchen, he has cookie cutters shaped like the digits <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> through <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container>. He fills them with dough, bakes the digits, and arranges them in a row on a tray to form a whole positive number.</p>

<p>Recently, Aaron managed to bake and arrange a prime number. After admiring it, he got hungry and ate one of the digit-biscuits. Without rearranging the remaining digits, he simply shifted them left or right to fill the gap. To his delight, the new number was still prime!</p>

<p>Now, Aaron is curious to see how many prime numbers he can find in a row through this process. Each time, he eats a digit, shifts the remaining ones, and checks if the new number is prime. If leading zeros appear after eating a digit, he happily eats those as well right away. However, if at any point the resulting number is not prime, the process ends immediately.</p>

<p>Today, Aaron baked a new set of digits and formed a new number, not necessarily prime. Aaron’s goal is to see the maximum number of prime numbers in a row, starting with the initial number and continuing for as long as possible.</p>

<p>Your task is to compute the maximum possible number of occurrences of prime numbers in this process.</p>

### 입력 

 <p>The input consists of a single line with integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ N ≤ 10^9$</span></mjx-container>), the number baked by Aaron.</p>

### 출력 

 <p>Output one integer specifying the maximum number of prime numbers that Aaron can see through his process.</p>

