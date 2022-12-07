# [Silver IV] Bucket Brigade - 17198 

[문제 링크](https://www.acmicpc.net/problem/17198) 

### 성능 요약

메모리: 114276 KB, 시간: 140 ms

### 분류

너비 우선 탐색(bfs), 많은 조건 분기(case_work), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>A fire has broken out on the farm, and the cows are rushing to try and put it out!</p>

<p>The farm is described by a <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>×</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10 \times 10$</span></mjx-container> grid of characters like this:</p>

<pre>..........
..........
..........
..B.......
..........
.....R....
..........
..........
.....L....
..........
</pre>

<p>The character 'B' represents the barn, which has just caught on fire. The 'L' character represents a lake, and 'R' represents the location of a large rock.</p>

<p>The cows want to form a "bucket brigade" by placing themselves along a path between the lake and the barn so that they can pass buckets of water along the path to help extinguish the fire. A bucket can move between cows if they are immediately adjacent in the north, south, east, or west directions. The same is true for a cow next to the lake --- the cow can only extract a bucket of water from the lake if she is immediately adjacent to the lake. Similarly, a cow can only throw a bucket of water on the barn if she is immediately adjacent to the barn.</p>

<p>Please help determine the minimum number of '.' squares that should be occupied by cows to form a successful bucket brigade.</p>

<p>A cow cannot be placed on the square containing the large rock, and the barn and lake are guaranteed not to be immediately adjacent to each-other.</p>

### 입력 

 <p>The input file contains 10 rows each with 10 characters, describing the layout of the farm. There are exactly one barn, one lake, and one rock.</p>

### 출력 

 <p>Output a single integer giving the minimum number of cows needed to form a viable bucket brigade.</p>

