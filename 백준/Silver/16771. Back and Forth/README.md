# [Silver I] Back and Forth - 16771 

[문제 링크](https://www.acmicpc.net/problem/16771) 

### 성능 요약

메모리: 110900 KB, 시간: 108 ms

### 분류

백트래킹, 브루트포스 알고리즘, 구현, 시뮬레이션

### 제출 일자

2025년 4월 7일 08:34:34

### 문제 설명

<p>Farmer John has two milking barns, each of which has a large milk tank as well as a storage closet containing <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container> buckets of various sizes. He likes to carry milk back and forth between the two barns as a means of exercise.</p>

<p>On Monday, Farmer John measures exactly <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1000$</span></mjx-container> gallons of milk in the tank of the first barn, and exactly <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1000$</span></mjx-container> gallons of milk in the tank of the second barn.</p>

<p>On Tuesday, he takes a bucket from the first barn, fills it, and carries the milk to the second barn, where he pours it into the storage tank. He leaves the bucket at the second barn.</p>

<p>On Wednesday, he takes a bucket from the second barn (possibly the one he left on Tuesday), fills it, and carries the milk to the first barn, where he pours it into the storage tank. He leaves the bucket at the first barn.</p>

<p>On Thursday, he takes a bucket from the first barn (possibly the one he left on Wednesday), fills it, and carries the milk to the second barn, where he pours it into the tank. He leaves the bucket at the second barn.</p>

<p>On Friday, he takes a bucket from the second barn (possibly the one he left on Tuesday or Thursday), fills it, and carries the milk to the first barn, where he pours it into the tank. He leaves the bucket at the first barn.</p>

<p>Farmer John then measures the milk in the tank of the first barn. How many possible different readings could he see?</p>

### 입력 

 <p>The first line of input contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container> integers, giving the sizes of the buckets initially at the first barn. The second line of input contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container> more integers, giving the sizes of the buckets initially at the second barn. All bucket sizes are in the range <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>…</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \dots 100$</span></mjx-container>.</p>

### 출력 

 <p>Please print the number of possible readings Farmer John could get from measuring the milk in the tank of the first barn after Friday.</p>

