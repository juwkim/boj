# [Silver IV] S-Trees - 6341 

[문제 링크](https://www.acmicpc.net/problem/6341) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

이분 탐색, 구현, 시뮬레이션

### 제출 일자

2023년 12월 17일 02:00:48

### 문제 설명

<p>A Strange Tree (S-tree) over the variable set X<sub>n</sub> = {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>} is a binary tree representing a Boolean function f : {0, 1}<sup>n</sup> → {0, 1}. Each path of the S-tree begins at the root node and consists of n+1 nodes. Each of the S-tree's nodes has a depth, which is the amount of nodes between itself and the root (So the root has depth 0). The nodes with depth less than n are called non-terminal nodes. All non-terminal nodes have two children: the right child and the left child. Each non-terminal node is marked with some variable x, from the variable set X<sub>n</sub>. All non-terminal nodes with the same depth are marked with the same variable, and non-terminal nodes with different depth are marked with different variables. So, there is a unique variable x<sub>i1</sub> corresponding to the root, a unique variable x<sub>i2</sub> corresponding to the nodes with depth 1, and so on. The sequence of the variables  x<sub>i1</sub>, x<sub>i2</sub>, ..., x<sub>in</sub> is called the variable ordering. The nodes having depth n are called terminal nodes. They have no children and are marked with either 0 or 1. Note that the variable ordering and the distribution of 0's and 1's on terminal nodes are sufficient to completely describe an S-tree.</p>

<p>As stated earlier, each S-tree represents a Boolean function f. If you have an S-tree and values for the variables x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>, then it is quite simple to find out what  f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>) is: start with the root. Now repeat the following: if the node you are at is labelled with a variable x<sub>i</sub>, then depending on whether the value of the variable is 1 or 0, you go its right or left child, respectively. Once you reach a terminal node, its label gives the value of the function.</p>

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/stree.png" style="height:193px; width:514px"></p>

<p style="text-align:center">Figure 1: S-trees for the function  x<sub>1</sub> ∧ (x<sub>2</sub> ∨ x<sub>3</sub>)</p>

<p>On the picture, two S-trees representing the same Boolean function,  f(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>) = x<sub>1</sub> ∧ (x<sub>2</sub> ∨ x<sub>3</sub>), are shown. For the left tree, the variable ordering is x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, and for the right tree it is x<sub>3</sub>, x<sub>1</sub>, x<sub>2</sub>.</p>

<p>The values of the variables  x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>, are given as a Variable Values Assignment (VVA) </p>

<p style="text-align:center">(x<sub>1</sub> = b<sub>1</sub>, x<sub>2</sub> = b<sub>2</sub>, ..., x<sub>n</sub> = b<sub>n</sub>)</p>

<p>with  b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>n</sub> ∈ {0,1}. For instance, (x<sub>1</sub> = 1, x<sub>2</sub> = 1 x<sub>3</sub> = 0) would be a valid VVA for n = 3, resulting for the sample function above in the value  f(1, 1, 0) = 1 ∧ (1 ∨ 0) = 1. The corresponding paths are shown bold in the picture.</p>

<p>Your task is to write a program which takes an S-tree and some VVAs and computes  f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>) as described above.</p>

### 입력 

 <p>The input file contains the description of several S-trees with associated VVAs which you have to process. Each description begins with a line containing a single integer n,  1 ≤ n ≤ 7, the depth of the S-tree. This is followed by a line describing the variable ordering of the S-tree. The format of that line is x<sub>i1</sub> x<sub>i2</sub> ...x<sub>in</sub>. (There will be exactly n different space-separated strings). So, for n = 3 and the variable ordering x<sub>3</sub>, x<sub>1</sub>, x<sub>2</sub>, this line would look as follows:</p>

<p>x3 x1 x2</p>

<p>In the next line the distribution of 0's and 1's over the terminal nodes is given. There will be exactly 2n characters (each of which can be 0 or 1), followed by the new-line character. The characters are given in the order in which they appear in the S-tree, the first character corresponds to the leftmost terminal node of the S-tree, the last one to its rightmost terminal node.</p>

<p>The next line contains a single integer m, the number of VVAs, followed by m lines describing them. Each of the m lines contains exactly n characters (each of which can be 0 or 1), followed by a new-line character. Regardless of the variable ordering of the S-tree, the first character always describes the value of x<sub>1</sub>, the second character describes the value of x<sub>2</sub>, and so on. So, the line</p>

<p>110</p>

<p>corresponds to the VVA (x<sub>1</sub> = 1, x<sub>2</sub> = 1, x<sub>3</sub> = 0).</p>

<p>The input is terminated by a test case starting with n = 0. This test case should not be processed.</p>

### 출력 

 <p>For each S-tree, output the line "S-Tree #j:", where j is the number of the S-tree. Then print a line that contains the value of f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>) for each of the given m VVAs, where f is the function defined by the S-tree.</p>

<p>Output a blank line after each test case.</p>

