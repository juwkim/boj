# [Silver III] Binary tree - 13237 

[문제 링크](https://www.acmicpc.net/problem/13237) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 트리

### 제출 일자

2024년 1월 28일 07:45:55

### 문제 설명

<p>A binary tree is a mathematical structure made of nodes where each node can have up to two children nodes. One child node will be called left child and the other right child. ch If node B is a child node of A, then we say that A is the parent node of B. In a binary tree, there is only one node that has no parent and we call this node the root of the tree. We call the height of a node  N to the distance in nodes between the node N and the root node. The root node’s height is 0.</p>

<p>In this problem, you’ll have to compute the heights of every node of the tree. Each node will be identified by an integer from 1 to the number of nodes n.</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/13237/1.png" style="float:right; height:169px; width:250px">Check the following tree:</p>

<p>The root of the tree is 1. The left child of 1 is 2, the right child of 1 is 3.</p>

<p>The nodes 4, 5, 6 and 7 do not have any child.</p>

<p>The heights of the nodes are:</p>

<ul>
	<li>Node 1: 0</li>
	<li>Nodes 2 and 3: 1</li>
	<li>Nodes 4, 5, 6 and 7: 2</li>
</ul>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/13237/2.png" style="float:right; height:250px; width:228px">The following tree is a bit different:</p>

<p>Node 1 is still the root and has 2 and 3 as left and right children but 3 only have right child. On the contrary, node 4 only has left child (5).</p>

<p>The heights:</p>

<ul>
	<li>Node 1: 0</li>
	<li>Nodes 2 and 3: 1</li>
	<li>Node 4: 2</li>
	<li>Node 5: 3</li>
</ul>

### 입력 

 <p>The first line of the input will contain the number of nodes n. (1 ≤ n ≤ 20)</p>

<p>The following n lines will contain one integer each representing the parent of a node. That is, the second line of the input will contain the parent of node 1, the third line the parent of node 2, etc.</p>

<p>The root node will be identified by -1. Remember that node 1 won’t always be the root node.</p>

### 출력 

 <p>Print n lines. The first line should be the height of node 1, the second should be the height of node 2, and so on.</p>

