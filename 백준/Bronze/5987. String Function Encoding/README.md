# [Bronze I] String Function Encoding - 5987 

[문제 링크](https://www.acmicpc.net/problem/5987) 

### 성능 요약

메모리: 29020 KB, 시간: 80 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Bessie discovered a new function that the entire herd can apply to its character strings.</p>

<p>Given both a number N (1 <= N <= 15) and a string S, with length strictly greater than N, define f(N, S) as a new string composed of the concatenation of the substring from character N (zero based -- first character is number 0) through the end of S and the string S itself.</p>

<p>For example, with N = 2, and S = "COW", f(N, S) = "W" + "COW" = "WCOW". Also, f(3, "USACO") = "CO" + "USACO" = "COUSACO".</p>

<p>Bessie is enthralled with this function and wants to iterate it several times. For example, if she iterates the function once for "COW" and N = 2, she will get "WCOW". If she applies the function with N = 2 again to that string, she will get "OWWCOW", and if she applies it one more time with N = 2, she will get "WCOWOWWCOW".</p>

<p>Help Bessie encode a total of Z (1 <= Z <= 100) strings, str_1, str_2, and so on.  Each str_i has length in the range 2..100 and contains only upper case letters. Each string is presented with its own N_i (0 <= N_i < length(str_i), and iteration count C_i (1 <= C_i <= 12).</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: Z</li>
	<li>Lines 2..Z+1: Line i+1 contains two space-separated integers, a space, and string to be encoded: N_i, C_i, and str_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..Q: Line j contains the iterated, encoded version of str_j</li>
</ul>

<p> </p>

