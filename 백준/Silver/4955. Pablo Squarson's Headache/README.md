# [Silver V] Pablo Squarson's Headache - 4955 

[문제 링크](https://www.acmicpc.net/problem/4955) 

### 성능 요약

메모리: 115444 KB, 시간: 160 ms

### 분류

구현(implementation)

### 문제 설명

<p>Pablo Squarson is a well-known cubism artist. This year's theme for Pablo Squarson is "Squares". Today we are visiting his studio to see how his masterpieces are given birth.</p>

<p>At the center of his studio, there is a huuuuuge table and beside it are many, many squares of the same size. Pablo Squarson puts one of the squares on the table. Then he places some other squares on the table in sequence. It seems his methodical nature forces him to place each square side by side to the one that he already placed on, with machine-like precision.</p>

<p>Oh! The first piece of artwork is done. Pablo Squarson seems satisfied with it. Look at his happy face.</p>

<p>Oh, what's wrong with Pablo? He is tearing his hair! Oh, I see. He wants to find a box that fits the new piece of work but he has trouble figuring out its size. Let's help him!</p>

<p>Your mission is to write a program that takes instructions that record how Pablo made a piece of his artwork and computes its width and height. It is known that the size of each square is 1. You may assume that Pablo does not put a square on another.</p>

<p>I hear someone murmured "A smaller box will do". No, poor Pablo, shaking his head, is grumbling "My square style does not seem to be understood by illiterates".</p>

<p style="text-align: center;"><img alt="" src="" style="height:345px; width:652px"></p>

### 입력 

 <p>The input consists of a number of datasets. Each dataset represents the way Pablo made a piece of his artwork. The format of a dataset is as follows.</p>

<pre>N
n<sub>1</sub> d<sub>1</sub>
n<sub>2</sub> d<sub>2</sub>
...
n<sub>N-1</sub> dN-1</pre>

<p>The first line contains the number of squares (= N) used to make the piece of artwork. The number is a positive integer and is smaller than 200.</p>

<p>The remaining (N-1) lines in the dataset are square placement instructions. The line “ni di” indicates placement of the square numbered i (≤ N-1). The rules of numbering squares are as follows. The first square is numbered "zero". Subsequently placed squares are numbered 1, 2, ..., (N-1). Note that the input does not give any placement instruction to the first square, which is numbered zero.</p>

<p>A square placement instruction for the square numbered i, namely “ni di”, directs it to be placed next to the one that is numbered ni, towards the direction given by di, which denotes leftward (= 0), downward (= 1), rightward (= 2), and upward (= 3).</p>

<p>For example, pieces of artwork corresponding to the four datasets shown in Sample Input are depicted below. Squares are labeled by their numbers.</p>

<p style="text-align: center;"><img alt="" src="/upload/images2/A-2.png" style="height:301px; width:715px"></p>

<p>The end of the input is indicated by a line that contains a single zero.</p>

### 출력 

 <p>For each dataset, output a line that contains the width and the height of the piece of artwork as decimal numbers, separated by a space. Each line should not contain any other characters.</p>

