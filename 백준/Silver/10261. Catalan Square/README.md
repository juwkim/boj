# [Silver IV] Catalan Square - 10261 

[문제 링크](https://www.acmicpc.net/problem/10261) 

### 성능 요약

메모리: 114328 KB, 시간: 136 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 조합론(combinatorics), 수학(math)

### 문제 설명

<p><img alt="" src="" style="float:right; height:222px; width:252px">Last weekend you and your friends went to visit the local farmer’s market at the town square. As you were standing around in a circle talking, you couldn’t help overhearing two of your friends musing over what sounded like an interesting problem: They were considering the number of ways in which you could all shake hands, such that everyone in the circle simultaneously shaked hands with one other person, but where no arms crossed each other.</p>

<p>After a few seconds’ thought you decided to join your two friends, to share (with them) the solution to their problem. “If we are \(2n\) persons”, you said, “pick any particular person, and let that person shake hands with somebody. That person will have to leave an even number of people on each side of the person with whom he/she shakes hands. Of the remaining \(n-1\) pairs of people, he/she can leave zero on the right and \(n-1\) pairs on the left, \(1\) on the right and \(n−2\) pairs on the left, and so on. The pairs remaining on the right and left can independently choose any of the possible non-crossing handshake patterns, so the count \(C_n\) for \(n\) pairs of people is given by:</p>

<p>\[C_n = C_{n−1}C_0 + C_{n−2}C_1 + \dots + C_1C_{n−2} + C_0C_{n−1}\]</p>

<p>which, together with the fact that \(C_0 = C_1 = 1\), is just the definition of the Catalan numbers.” By consulting your handy combinatorics book, you find out that there is a much more efficient formula for calculating \(C_n\), namely:</p>

<p>\[C_n = \frac{\begin{pmatrix} 2n \\ n \end{pmatrix}}{n+1}\]</p>

<p>After a collective groan from the group, your particularly cheeky friend Val called out “Well, since we are at the town square, why don’t you try to square your Catalan numbers!”. This was met with much rejoicing, while you started to think about how to square the Catalan sequence...</p>

<p>Let \(C_n\) be the \(n\)th Catalan number as defined above. By regarding the sequence \((C_n)_{n \ge 0}\) of Catalan numbers, we can define a sequence (Sn)n≥0, corresponding to “squaring the Catalan sequence”, by considering the Cauchy product, or discrete convolution, of \((C_n)_{n \ge 0}\) with itself, i.e.,</p>

<p>\[S_n = \sum_{k=0}^{n}{C_kC_{n-k}}\]</p>

<p>Your task is to write a program for calculating the number \(S_n\).<sup>1</sup></p>

<p><sup>1</sup>To see why \((S_n)_{n \ge 0}\) could be said to correspond to the square of the Catalan sequence we could look at Cauchy products of power series. Suppose that \(p(x) = \sum_{n=0}^{\infty } {a_nx^n}\) and \(q(x) = \sum_{n=0}^{\infty }{b_nx^n}\), then \(p(x) \cdot q(x) = \sum_{n=0}^{\infty }{c_nx^n}\) where \(c_n = \sum_{k=0}^{n}{a_kb_{n-k}}\).</p>

### 입력 

 <p>The input contains one line containing one non-negative integer: \(n\), with 0 ≤ \(n\) ≤ 5 000.</p>

### 출력 

 <p>Output a line containing \(S_n\).</p>

