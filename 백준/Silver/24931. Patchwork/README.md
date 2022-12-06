# [Silver V] Patchwork - 24931 

[문제 링크](https://www.acmicpc.net/problem/24931) 

### 성능 요약

메모리: 118076 KB, 시간: 184 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Adam’s grandmother has a birthday coming up and he wants to make her a beautiful patchwork quilt as a present. He has created a collection of patch designs that he will sew onto the quilt. However, he is having trouble deciding exactly where to place his patches. His current procedure is to sew on all patches in a given configuration, determine if he likes the way it looks, and cut them all off if he doesn’t. This is highly inefficient and Adam is running out of time.</p>

<p>Adam starts with a rectangular white cloth to be used as the base for his quilt and has a collection of possible patch types. Each patch type is a rectangular piece of cloth with a specified design. Fortunately, Adam has come prepared and he has an unlimited quantity of every patch type. Adam has asked you to write a program to determine what the cloth will look like after sewing the patches on in a specific order and in specific locations. Note that Adam cuts off excess fabric that hangs off the edge of the quilt’s base so your program should do the same.</p>

<p>Help Adam by writing a program to output the completed quilt.</p>

### 입력 

 <p>The first line of input consists of two integers $R,C$ ($1≤R,C≤100$) giving the dimensions of the quilt. Initially, this quilt is white and is represented by a grid with $R$ rows and $C$ columns where each entry is the character ‘<code>.</code>’ (a period) representing white.</p>

<p>The second line contains a single integer $N$ ($1≤N≤100$), which is the number of different patch types. The following describes the patches:</p>

<ul>
	<li>The first line in the description of the $i$th patch type consists of two integers $r_i,c_i$ ($1≤r_i,c_i≤100$) giving the number of rows $r_i$ and columns $c_i$ in this patch.</li>
	<li>Then $r_i$ lines follow, each containing $c_i$ non-whitespace ASCII characters which describes the $i$th patch type.</li>
</ul>

<p>The next line contains a single integer $M$ ($1≤M≤100$), which is the number of patches that Adam wishes to sew onto the quilt.</p>

<p>The next $M$ lines of input describe the placement and types of these patches. The $j$th such line contains three integers $q_j$ ($1≤q_j≤R$), $t_j$ ($1≤t_j≤C$), and $p_j$ ($1≤p_j≤N$). This means that the $p_j$th patch is sewn onto the quilt with its top-left corner on the $q_j,t_j$ row/column position of the quilt. This list is given in the order that they are sewn onto the quilt.</p>

### 출력 

 <p>Display the completed quilt. That is, display $R$ rows and $C$ columns of ASCII characters where each position is the pattern of the quilt after sewing on the given patches whilst removing excess fabric.</p>

