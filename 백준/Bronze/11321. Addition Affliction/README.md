# [Bronze I] Addition Affliction - 11321 

[문제 링크](https://www.acmicpc.net/problem/11321) 

### 성능 요약

메모리: 30840 KB, 시간: 164 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Albert is a Computer Science student that loves math! Unfortunately, despite his love for math, he does not have a very good handle on the basics! He especially has difficulties with addition, an affliction that has plagued him since his youngest days.</p>

<p>Unfortunately for Albert, addition is a common part of life. He would like to finally master the mysterious magic of addition. Albert has noticed that numbers which add to a multiple of 10 are the easiest.</p>

<p>Albert would like you to help him achieve his addition aspirations; he doesn’t want you to do all of his work for him (that wouldn’t help!), but if you could rearrange some of his practice expressions into something a little easier, he would be very grateful!</p>

### 입력 

 <p>Each line of input will be a summation of nonnegative integers in the form</p>

<p>x<sub>1</sub> + x<sub>2</sub> + · · · + x<sub>N</sub></p>

<p>for some N(2 ≤ N < 1000), where 0 ≤ x<sub>i</sub> ≤ 100000 for each x<sub>i</sub>.</p>

<p>Lines will not contain any whitespace, only digits and the plus symbols.</p>

<p>The input will be terminated by a line containing only 0.</p>

### 출력 

 <p>For each line, print the same expression but with the numbers in an easier order: put pairs of numbers that add to a multiple of 10 at the front. That is, if there is a number x<sub>i</sub> in the sequence for which x<sub>i</sub> + x<sub>j</sub> is a multiple of 10 for some other number x<sub>j</sub> in the sequence, and x<sub>j</sub> is not already paired with another number, then x<sub>i</sub>, x<sub>j</sub> should appear adjacent to each other before any unpaired numbers.</p>

<p>Note that there may be several correct answers for a given line, e.g. "1+2+4+6" could be rearranged as "4+6+1+2" or "6+4+2+1".</p>

