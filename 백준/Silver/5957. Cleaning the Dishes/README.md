# [Silver V] Cleaning the Dishes - 5957 

[문제 링크](https://www.acmicpc.net/problem/5957) 

### 성능 요약

메모리: 30840 KB, 시간: 112 ms

### 분류

자료 구조(data_structures), 구현(implementation), 시뮬레이션(simulation), 스택(stack)

### 문제 설명

<p>Bessie and Canmuu are teaming up to wash the massive pile of N (1 <= N <= 10,000) dirty dishes left over after the CowMoose Festival. Bessie is washing the dishes; Canmuu will dry them.</p>

<p>Each dish has a unique serial number in the range 1..N. At the beginning, the dishes are stacked in order with #1 on the top and #N on the bottom.</p>

<p>Bessie first washes some number of dishes D_i by taking one from the top of the incoming pile, washing it, and then stacking it on the other side of the sink (this reverses the order of those dishes).</p>

<p>Once she has finished washing those dishes, either she washes another set of dishes or Canmuu comes back to dry D_i dishes while Bessie goes off to eat her well-earned snack. He takes those dishes, one by one, off the stack that Bessie left him, dries the dish, and stacks it (again in reverse order) in the 'cleaned' stack.</p>

<p>Canmuu then either takes another set of dishes to dry or goes off to get a snack while Bessie comes back to wash. They repeat these operations until all of the dishes are washed and dried.</p>

<p>What is the final order (top to bottom) in which the clean, dry dishes are stacked?</p>

<p>To illustrate, suppose that Bessie has a stack of 5 dishes to wash:</p>

<pre>1 <-- top
2
3
4
5 <-- bottom</pre>

<p>D_1 is 3, so Bessie takes three dishes from the top of the stack, one by one, washes them, and stacks on the other side of the sink for Canmuu to dry:</p>

<pre>       Unwashed
       | Washed but not dried
       | | Washed & Dried
       | | |
TOP    1             
       2          2   
       3      ->  3      ->  3      ->    3   
       4          4          4 2        4 2 
BOTTOM 5 - -      5 1 -      5 1 -      5 1 -
    Initial      Dish 1     Dish 2     Dish 3</pre>

<p>Canmuu dries two of these, one by one, and places them onto the clean stack:</p>

<pre>TOP         3                   
          4 2    ->  4 2   ->  4   2
BOTTOM    5 1 -      5 1 3     5 1 3</pre>

<p>Bessie washes the final two dishes:</p>

<pre>TOP                              5
          4   2  ->    4 2 ->    4 2
BOTTOM    5 1 3      5 1 3     - 1 3</pre>

<p>Finally, Canmuu dries the last three dishes, stacking them in the resulting order below:</p>

<pre>TOP                                          1
                                  4          4
          5    ->      5  ->      5  ->      5
          4 2        4 2          2          2
BOTTOM  - 1 3      - 1 3      - 1 3      - - 3</pre>

<p>So the final order is: 1, 4, 5, 2, 3.</p>

<p>Each of the main input lines contains both a command, C_i (1 <= C_i <= 2) where 1 indicates Bessie washing while 2 indicates Canmuu drying, and the number of dishes D_i (1 <= D_i <= N) to be washed or dried.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer indicating the number of dishes to wash and dry: N</li>
	<li>Lines 2..??: Each line contains a command and a count of dishes to process: C_i and D_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..N: Line i contains the i-th cleaned dish, starting from the top</li>
</ul>

<p> </p>

