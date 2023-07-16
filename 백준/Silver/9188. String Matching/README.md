# [Silver V] String Matching - 9188 

[문제 링크](https://www.acmicpc.net/problem/9188) 

### 성능 요약

메모리: 129980 KB, 시간: 304 ms

### 분류

브루트포스 알고리즘, 문자열

### 문제 설명

<p>It's easy to tell if two words are identical - just check the letters. But how do you tell if two words are almost identical?  And how close is "almost"?</p>

<p>There are lots of techniques for approximate word matching.  One is to determine the best substring match, which is the number of common letters when the words are compared letter-by-letter.  The key to this approach is that the words can overlap in any way.  For example, consider the words CAPILLARY and MARSUPIAL.  One way to compare them is to overlay them:</p>

<pre>CAPILLARY
MARSUPIAL</pre>

<p>There is only one common letter (A).  Better is the following overlay:</p>

<pre>CAPILLARY
     MARSUPIAL</pre>

<p>with two common letters (A and R), but the best is:</p>

<pre>   CAPILLARY
MARSUPIAL</pre>

<p>Which has three common letters (P, I and L).</p>

<p>The approximation measure appx(word1, word2) for two words is given by:</p>

<pre>     common letters * 2
-----------------------------
length(word1) + length(word2)
</pre>

<p>Thus, for this example, appx(CAPILLARY, MARSUPIAL) = 6 / (9 + 9) = 1/3.  Obviously, for any word W appx(W, W) = 1, which is a nice property, while words with no common letters have an appx value of 0.</p>

### 입력 

 <p>The input for your program will be a series of words, two per line, until the end-of-file flag of -1.  Using the above technique, you are to calculate appx() for the pair of words on the line and print the result. The words will all be uppercase.</p>

### 출력 

 <p>Print the value for appx() for each pair as a reduced fraction. Fractions reducing to zero or one should have no denominator.</p>

