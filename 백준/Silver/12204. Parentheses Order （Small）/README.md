# [Silver IV] Parentheses Order (Small) - 12204 

[문제 링크](https://www.acmicpc.net/problem/12204) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

Empty

### 문제 설명

<p>An <b>n</b> parentheses sequence consists of <b>n</b> <code>(</code>s and <b>n</b> <code>)</code>s.</p>

<p>A valid parentheses sequence is defined as the following:</p>

<p><i>You can find a way to repeat erasing adjacent pair of parentheses <code>()</code> until it becomes empty.</i></p>

<p>For example, <code>(())</code> is a valid parentheses, you can erase the pair on the 2nd and 3rd position and it becomes <code>()</code> then you can make it empty. <code>)()(</code> is not a valid parentheses, after you erase the pair on the 2nd and 3rd position, it becomes <code>)(</code> and you cannot erase any more.</p>

<p>Now, we have all valid <b>n</b> parentheses sequences. Find the <b>k</b>-th smallest sequence in lexicographical order.</p>

<p>For example, here are all valid 3 parentheses sequences in lexicographical order:</p>

<pre>((()))
(()())
(())()
()(())
()()()
</pre>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each line represents a test case consisting of 2 integers, <strong>n</strong> and <strong>k</strong>.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the <strong>k</strong>-th smallest parentheses sequence in all valid <strong>n</strong> parentheses sequences. Output "Doesn't Exist!" when there are less than <strong>k</strong> different <strong>n</strong> parentheses sequences.</p>

