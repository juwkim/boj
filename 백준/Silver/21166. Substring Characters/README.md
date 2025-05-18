# [Silver I] Substring Characters - 21166 

[문제 링크](https://www.acmicpc.net/problem/21166) 

### 성능 요약

메모리: 111328 KB, 시간: 176 ms

### 분류

브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵, 문자열, 두 포인터, 집합과 맵

### 제출 일자

2025년 5월 18일 16:04:14

### 문제 설명

<p>The set of distinct characters in a string is referred to as the generalized period of the string.  As an example, the generalized period of the string "<code>aabbabb</code>" is {'<code>a</code>','<code>b</code>'}</p>

<p>A proper substring is a contiguous substring that is contained in a string and is not the string itself. So "<code>aabbabb</code>" is not a proper substring of the above example.</p>

<p>A minimal proper substring is one that can have no character removed from either end and still have the same generalized period. "<code>aabb</code>" is a proper substring of the example, but it is not minimal. "<code>ab</code>" is minimal.</p>

<p>Unique means that multiple occurrences of the same minimal proper substring in a string are only to be counted once. In the example, "<code>ab</code>" appears twice, but is counted once---hence the number of proper minimal unique substrings with the same generalized period of the entire string is two: "<code>ab</code>" and "<code>ba</code>".</p>

<p>Your team is to write a program to count the number of proper minimal unique substrings of a given string that have the same generalized period as the string itself. </p>

### 입력 

 <p>Input to your program is a series of lines terminated by end-of-file. Each line is a test case consisting of alphanumeric characters (a--z, A--Z, 0--9).  Upper-case and lower-case letters are distinct.  The new line character is not part of the test case string.  No test case string will exceed <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$80$</span></mjx-container> characters. There will be at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> test strings in input.</p>

### 출력 

 <p>For each input line print a line containing the number of proper minimal unique substrings of the input string with no leading or trailing whitespace and no extra leading signs or zeros.</p>

