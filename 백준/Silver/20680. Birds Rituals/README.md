# [Silver V] Birds Rituals - 20680 

[문제 링크](https://www.acmicpc.net/problem/20680) 

### 성능 요약

메모리: 115280 KB, 시간: 152 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Birds are stupendous animals. Many species of them perform different rituals throughout their life; from courtship dances of peacocks to moonwalking of red-capped manakins. Among all, we are studying the <em>permutation dance</em> in this problem. This ritual is performed by a group of birds sitting in a row on a wire or tree branch, as shown in the figure.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 318px; height: 174px;"></p>

<p>The ritual can be simplified to a performance based on a sequence of actions of these types:</p>

<ul>
	<li>insertion: A new bird joins the group and inserts herself somewhere in the row of the birds.</li>
	<li>departure: A bird in the row leaves the group for rest of the ritual and flies away.</li>
	<li>relocation: A bird in the row flies from her position and sits (inserts herself) somewhere else in the row.</li>
</ul>

<p>Given the initial position of the birds in the row and the sequence of actions, your task is to compute the final position of the birds in the ritual.</p>

### 입력 

 <p>The input starts with a line containing two space-separated integers n (1 ⩽ n ⩽ 1000) and s (1 ⩽ s ⩽ 5000). The second line contains n space-separated bird names, as the initial configuration of the ritual (positioning of the birds in the row, from left to right). Each bird name is a non-empty string of at most 10 (lowercase) alphanumeric characters (<code>a</code> to <code>z</code>, and <code>0</code> to <code>9</code>).</p>

<p>The sequence of actions is provided in the next s lines, one action per line. Each line is in one of the following formats based on the action type. The <code>bird-name</code> parameter in the actions has the similar format as the second line of the input.</p>

<ul>
	<li>insertion: <code>insert bird-name position</code></li>
</ul>

<p>The <code>position</code> parameter is an integer showing the number of birds to the left of the insertion position. This parameter is in the range [0, M] where M is the total number of birds in the row before the insertion. Position 0 puts the bird in the beginning (leftmost position) of the row, and position M puts the bird in the end (rightmost position).</p>

<ul>
	<li>departure: <code>depart bird-name</code></li>
	<li>relocation: <code>relocate bird-name displacement</code></li>
</ul>

<p>The <code>displacement</code> parameter is an integer that can be positive, negative, or zero. The bird flies to her own position if the displacement is 0. Otherwise, the bird flies over k birds on his right (left) if displacement is positive (negative), where k is the absolute value of displacement. This parameter is in the range [−L, +R] where L and R are respectively the numbers of birds to the left and to the right of the moving bird in the row before the relocation. Displacement −L puts the bird in the beginning (leftmost position) of the row, and displacement+R puts the bird in the end (rightmost position).</p>

<p>No two participating birds share the same name. Moreover, it is guaranteed that all the actions are meaningful at the moment of execution and there is always at least one bird on the branch throughout the ritual.</p>

### 출력 

 <p>Print a single line in the output containing the final configuration of the ritual. The line should contain the space-separated list of the bird names in the row (from left to the right).</p>

