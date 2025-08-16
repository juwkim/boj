# [Silver I] Kicksort - 24006 

[문제 링크](https://www.acmicpc.net/problem/24006) 

### 성능 요약

메모리: 794604 KB, 시간: 4216 ms

### 분류

구현, 애드 혹, 시뮬레이션

### 제출 일자

2025년 8월 16일 18:37:17

### 문제 설명

<p>Here at Kickstart, we are fans of the well-known <a href="https://en.wikipedia.org/wiki/Quicksort" target="_blank">Quicksort</a> algorithm, which chooses a <i>pivot</i> value from a list, moves each other value into one of two new lists depending on how it compares with the pivot value, and then recursively sorts each of those new lists. However, the algorithm might choose a pivot that causes all of the other values to end up in only one of the two new lists, which defeats the purpose of the divide-and-conquer strategy. We call such a pivot a <i>worst-case pivot</i>.</p>

<p>To try to avoid this problem, we have created our own variant, Kicksort. Someone told us that it is good to use a value in the middle as a pivot, so our algorithm works as follows:</p>

<pre>  Kicksort(A): // A is a 0-indexed list with E elements
    If E ≤ 1, return A.
    Otherwise:
      Create empty new lists B and C.
      Choose A[floor((E-1)/2)] as the pivot P.
      For i = 0 to E-1, except for i = floor((E-1)/2):
        If A[i] ≤ P, append it to B.
        Otherwise, append it to C.
    Return the list Kicksort(B) + [P] + Kicksort(C).
    // [P] is a new list with just P; + means concatenate
</pre>

<p>For practice, we are trying Kicksort out on lists that are permutations of the numbers 1 through <b>N</b>. Unfortunately, it looks like Kicksort still has the same problem as Quicksort: it is possible for every pivot to be a worst-case pivot!</p>

<p>For example, consider the list <code>1 4 3 2</code>. Kicksort will choose <code>4</code> as a pivot, and all of the other values <code>1 3 2</code> will end up in one of the two new lists. Then, when Kicksort is called on that list <code>1 3 2</code>, it will choose <code>3</code>, and once again, all of the other values will end up in one of the two new lists. Finally, it will choose <code>1</code> from the list <code>1 2</code>, and the other value <code>2</code> will of course end up in only one of the two new lists. In every case, the algorithm will choose a worst-case pivot. (Notice that when Kicksort is called on a list with 0 or 1 elements, it does not choose a pivot at all.)</p>

<p>Please help us investigate this further! Given a permutation of the numbers 1 through <b>N</b>, determine whether Kicksort will choose only worst-case pivots.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow; each consists of two lines. The first line has one integer <b>N</b>: the number of elements in the permutation. The second line contains <b>N</b> integers <b>A<sub>i</sub></b>, which are a permutation of the values from 1 through <b>N</b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is <code>YES</code> if Kicksort will choose only worst-case pivots when sorting this list, or <code>NO</code> otherwise.</p>

