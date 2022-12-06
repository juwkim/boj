# [Bronze II] Fermat's Last Theorem - 22825 

[문제 링크](https://www.acmicpc.net/problem/22825) 

### 성능 요약

메모리: 30840 KB, 시간: 148 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>In the 17th century, Fermat wrote that he proved for any integer <em>n</em> ≥ 3, there exist no positive integers <i>x</i>, <i>y</i>, <i>z</i> such that <em>x<sup>n</sup></em> + <em>y<sup>n</sup></em> = <em>z<sup>n</sup></em>. However he never disclosed the proof. Later, this claim was named Fermat's Last Theorem or Fermat's Conjecture.</p>

<p>If Fermat's Last Theorem holds in case of <i>n</i>, then it also holds in case of any multiple of <i>n</i>. Thus it suffices to prove cases where <i>n</i> is a prime number and the special case <i>n</i> = 4.</p>

<p>A proof for the case <i>n</i> = 4 was found in Fermat's own memorandum. The case <i>n</i> = 3 was proved by Euler in the 18th century. After that, many mathematicians attacked Fermat's Last Theorem. Some of them proved some part of the theorem, which was a partial success. Many others obtained nothing. It was a long history. Finally, Wiles proved Fermat's Last Theorem in 1994.</p>

<p>Fermat's Last Theorem implies that for any integers <em>n</em> ≥ 3 and <i>z</i> > 1, it always holds that</p>

<p style="text-align: center;"><em>z<sup>n</sup></em> > max{<em>x<sup>n</sup></em> + <em>y<sup>n</sup></em> | <em>x</em> > 0, <em>y</em> > 0, <em>x<sup>n</sup></em> + <em>y<sup>n</sup></em> ≤ <em>z<sup>n</sup></em>}.</p>

<p>Your mission is to write a program that verifies this in the case <i>n</i> = 3 for a given <i>z</i>. Your program should read in integer numbers greater than 1, and, corresponding to each input <i>z</i>, it should output the following:</p>

<p style="text-align: center;"><em>z</em><sup>3</sup> - max{<em>x</em><sup>3</sup> + <em>y</em><sup>3</sup> | <em>x</em> > 0, <em>y</em> > 0, <em>x</em><sup>3</sup> + <em>y</em><sup>3</sup> ≤ <em>z</em><sup>3</sup>}.</p>

### 입력 

 <p>The input is a sequence of lines each containing one positive integer number followed by a line containing a zero. You may assume that all of the input integers are greater than 1 and less than 1111.</p>

### 출력 

 <p>The output should consist of lines each containing a single integer number. Each output integer should be</p>

<p style="text-align: center;"><em>z</em><sup>3</sup> - max{<em>x</em><sup>3</sup> + <em>y</em><sup>3</sup> | <em>x</em> > 0, <em>y</em> > 0, <em>x</em><sup>3</sup> + <em>y</em><sup>3</sup> ≤ <em>z</em><sup>3</sup>}</p>

<p>for the corresponding input integer <i>z</i>. No other characters should appear in any output line.</p>

