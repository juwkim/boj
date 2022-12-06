# [Silver V] Numbers On a Tree - 11203 

[문제 링크](https://www.acmicpc.net/problem/11203) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

수학(math), 트리(trees)

### 문제 설명

<p>Lovisa is at KTH listening to Stefan Nilsson lecturing about perfect binary trees. “A perfect binary tree has a distinguished node called the root which is usually drawn at the top. Each node has two children except the nodes in the lowest layer, which we call leaves.” Lovisa knows all this already, so she is a bit bored. Noticing this, Stefan comes up with a new challenge for Lovisa.</p>

<p>First, we label the nodes of a perfect binary tree with numbers as follows. We start at the bottom right leaf which gets number 1 and then label nodes on the same level in increasing order from right to left. After finishing a level, we move to the rightmost node in the level above and label all the nodes on that level from right to left. We proceed in this fashion until we reach the root.</p>

<p>When we want to describe a node in the tree, we can do it by describing a path starting at the root and going down toward the leaves. At each non-leaf node we can either go left (‘<code>L</code>’) or right (‘<code>R</code>’).</p>

<p style="text-align: center;"><img alt="" src="" style="height:215px; width:398px"></p>

<p style="text-align: center;">Figure A.1: Labeled binary tree of height 3 with two marked paths from the root. Path <code>LR</code> leads to label 11 while path RRL leads to 2. The root has number 15.</p>

<p>Lovisa’s task is to calculate the label of a node, given the height of the tree H and the description of the path from the root.</p>

### 입력 

 <p>The only line of input contains the height of the tree H, 1 ≤ H ≤ 30 and a string consisting of the letters ‘<code>L</code>’ and ‘<code>R</code>’, denoting a path in the tree starting in the root. The letter ‘<code>L</code>’ denotes choosing the left child, and the letter ‘<code>R</code>’ choosing the right child. The description of the path may be empty and is at most H letters.</p>

### 출력 

 <p>Output one line containing the label of the node given by the path.</p>

