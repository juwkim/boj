# [Silver I] Compression - 31899 

[문제 링크](https://www.acmicpc.net/problem/31899) 

### 성능 요약

메모리: 121616 KB, 시간: 104 ms

### 분류

애드 혹

### 제출 일자

2025년 5월 11일 03:07:14

### 문제 설명

<p>Infinite Compression Plan Consortium (ICPC) has developed a new, great data compression strategy, called “Don’t Repeat Yourself” (DRY). DRY works on a string of characters, and if the string contains two consecutive instances of the same substring, it simply removes one of them. For example, in the string “<code>alfalfa seeds</code>”, it could remove one of the two “<code>e</code>” substrings in “<code>seeds</code>”, and one of the two “<code>lfa</code>” substrings in “<code>alfalfa</code>”, resulting in “<code>alfa seds</code>”. DRY can also take advantage of previous removals — for instance, in the string “<code>seventeenth baggage</code>”, it will first remove the duplicate “<code>e</code>” in “<code>seventeenth</code>” and the duplicate “<code>g</code>” in “<code>baggage</code>”, resulting in “<code>sevententh bagage</code>”, and then remove the duplicate “<code>ent</code>” in “<code>sevententh</code>” and “<code>ag</code>” in “<code>bagage</code>”, resulting in “<code>seventh bage</code>”.</p>

<p>If there are multiple choices of repeating consecutive substrings to remove, DRY should choose in a way that results in the shortest possible final string. For example, in the string “<code>ABBCDCABCDCD</code>”, DRY has two choices — either removing the repeated “<code>B</code>” near the beginning, or the repeated “<code>CD</code>” at the end. If the “<code>B</code>” is removed, then DRY will be able to remove the repeated “<code>ABCDC</code>”, resulting in “<code>ABCDCD</code>”, from which the “<code>CD</code>” at the end will finally be removed, resulting in “<code>ABCD</code>”. However, if DRY removed the “<code>CD</code>” at the end first, it would be left with “<code>ABBCDCABCD</code>”, from which only the repeated “<code>B</code>” can be removed to obtain “<code>ABCDCABCD</code>” — and from that string nothing more can be removed. So, the correct choice for DRY is to begin by compressing the double “<code>B</code>”, and to finally end up with “<code>ABCD</code>”.</p>

<p>ICPC observed that DRY obtains the best results on binary strings — that is, strings composed only of zeroes and ones. So, it has tasked you with implementing the best possible DRY algorithm working on binary strings. For any binary string, you should output a shortest string that can be obtained by repeatedly applying DRY to it.</p>

### 입력 

 <p>The input consists of a single line containing a nonempty string of length less than or equal to <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^5$</span></mjx-container>, consisting only of zeroes and ones.</p>

### 출력 

 <p>Output one line, containing a shortest possible result of running DRY on the input string. If there is more than one possible shortest result, any one will be accepted.</p>

