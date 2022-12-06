# [Bronze II] Ragged Right - 10501 

[문제 링크](https://www.acmicpc.net/problem/10501) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>Word wrapping is the task of deciding how to break a paragraph of text into lines. For aesthetic reasons, we’d like all the lines except the last one to be about the same length. For example, we would say the text on the left looks less ragged than the text on the right:</p>

<pre>This is a                         This
paragraph                         is a paragraph
of text.                          of text.</pre>

<p>Your job is to compute a raggedness value for an arbitrary paragraph of text. We’ll measure raggedness in a way similar to the TEX typesetting system. Let n be the length, measured in characters, of the longest line of the paragraph. If some other line contains only m characters, then we’ll charge a penalty score of (n − m)<sup>2</sup> for that line. The raggedness will be the sum of the penalty scores for every line except the last one.</p>

### 입력 

 <p>Input consists of a single paragraph of text containing at most 100 lines. Each line of the paragraph contains a sequence of between 1 and 80 characters (letters, punctuation characters, decimal digits and spaces). No line starts or ends with spaces. The paragraph ends at end of file.</p>

### 출력 

 <p>Print out a single integer, the raggedness score for paragraph.</p>

