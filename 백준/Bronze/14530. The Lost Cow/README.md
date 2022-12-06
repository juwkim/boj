# [Bronze II] The Lost Cow - 14530 

[문제 링크](https://www.acmicpc.net/problem/14530) 

### 성능 요약

메모리: 30888 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>Farmer John has lost his prize cow Bessie, and he needs to find her!</p>

<p>Fortunately, there is only one long path running across the farm, and Farmer John knows that Bessie has to be at some location on this path. If we think of the path as a number line, then Farmer John is currently at position \(x\) and Bessie is currently at position \(y\) (unknown to Farmer John). If Farmer John only knew where Bessie was located, he could walk directly to her, traveling a distance of \(|x - y|\). Unfortunately, it is dark outside and Farmer John can't see anything. The only way he can find Bessie is to walk back and forth until he eventually reaches her position.</p>

<p>Trying to figure out the best strategy for walking back and forth in his search, Farmer John consults the computer science research literature and is somewhat amused to find that this exact problem has not only been studied by computer scientists in the past, but that it is actually called the "Lost Cow Problem" (this is actually true!).</p>

<p>The recommended solution for Farmer John to find Bessie is to move to position \(x+1\), then reverse direction and move to position \(x-2\), then to position \(x+4\), and so on, in a "zig zag" pattern, each step moving twice as far from his initial starting position as before. As he has read during his study of algorithms for solving the lost cow problem, this approach guarantees that he will at worst travel 9 times the direct distance \(|x-y|\) between himself and Bessie before he finds her (this is also true, and the factor of 9 is actually the smallest such worst case guarantee any strategy can achieve).</p>

<p>Farmer John is curious to verify this result. Given \(x\) and \(y\), please compute the total distance he will travel according to the zig-zag search strategy above until he finds Bessie.</p>

### 입력 

 <p>The single line of input contains two distinct space-separated integers \(x\) and \(y\). Both are in the range \(0 \ldots 1,000\).</p>

### 출력 

 <p>Print one line of output, containing the distance Farmer John will travel to reach Bessie.</p>

