# [Bronze I] Inverse Common Superstring - 21044 

[문제 링크](https://www.acmicpc.net/problem/21044) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

애드 혹(ad_hoc), 문자열(string)

### 문제 설명

<p>Given a set of string <em>S</em> = {<em>S</em><sub>1</sub>, <em>S</em><sub>2</sub>, ..., <em>S<sub>n</sub></em>}, a common superstring <em>R</em> of the set <em>S</em> is a string such that each string in <em>S</em> appears as a substring in <em>R</em>. For example, let <em>S</em> be {"abb", "baab", "bbc"}, then one possible common superstring <em>R</em> of <em>S</em> is "abbbaabbbc" which has the length of 10 characters. Notice that all strings <em>S</em> in appear as substring in <em>R</em>. To verify: "abb" appears in "[abb]baabbbc", "baab" appears in "abb[baab]bbc", and "bbc" appears in "abbbaab[bbc]". The string "abbbaabbbc" is also a common superstring of <em>S</em>; you can verify it by yourself.</p>

<p>Among all possible common superstrings, usually the shortest common superstring is more attractive. It has many real-world application such as sparse matrix compression, DNA sequencing, and many others. In the example above, the shortest common superstring will be "baabbc" with the length of 6 characters. To verify: "aab" appears in "b[aab]bc", "baab" in "[baab]bc", and "bbc" in "baa[bbc]".</p>

<p>Unfortunately, the problem of finding the shortest common superstring is known to be NP-hard, i.e. up to this moment, there is no known polynomial-time algorithm to solve the problem.</p>

<p>The inverse problem of finding the shortest common superstring will be: given a string <em>R</em>, find the set of string <em>S</em> such that <em>R</em> is the shortest common superstring of <em>S</em>. Of course this inverse problem is very easy and trivial! The set <em>S</em> can simply contains a single string which equals to <em>R</em> (notice that a string is also a substring to the string itself).</p>

<p>Now, you are going to solve a more challenging problem. Given a string <em>R</em>, find the lexicographically (alphabetically) smallest string which does NOT appear as a substring in <em>R</em>. To simplify the problem, a string is defined as a non-empty sequence of only lowercase alphabetical character (a-z). For example, let the string <em>R</em> be "icpc", then the lexicographically smallest string which does not appear as substring in <em>R</em> is "a".</p>

<p>String <em>S</em> = <em>S</em><sub>1</sub><em>S</em><sub>2</sub><em>S</em><sub>3</sub>... is lexicographically smaller than string <em>T</em> = <em>T</em><sub>1</sub><em>T</em><sub>2</sub><em>T</em><sub>3</sub>... if one of the following is true:</p>

<ul>
	<li>|<em>S</em>| < |<em>T</em>| and <em>S<sub>i</sub></em> = <em>T<sub>i</sub></em> for all 1 ≤ <em>i</em> ≤ |<em>S</em>|, or</li>
	<li>There exists an index <em>i</em> where <em>S<sub>i</sub></em> < <em>T<sub>i</sub></em> and <em>S<sub>j</sub></em> = <em>T<sub>j</sub></em> for all 1 ≤ <em>j</em> < <em>i</em>.</li>
</ul>

### 입력 

 <p>The first line contains a string which length between 1 and 1000, inclusive. The given string contains only lowercase alphabetical character (a-z).</p>

### 출력 

 <p>The output contains the smallest lexicographical string which is NOT a substring of the input string, in a line. The output string should contain only lowercase alphabetical character.</p>

