# [Silver II] The Leisurely Stroll - 5992 

[문제 링크](https://www.acmicpc.net/problem/5992) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 트리

### 제출 일자

2024년 12월 17일 12:14:43

### 문제 설명

<p>Bessie looks out the barn door at the beautiful spring day and thinks to herself, "I'd really like to enjoy my walk out to the pastures for the tender spring grass." She knows that once she leaves the barn, she will traverse a path for a while, take one of two choices that lead to other paths, follow one of them, take one of two other choices, and continue on until the path leads to a verdant pasture.</p>

<p>She decides to make the set of path choices that enables her to walk over the greatest number of cow paths on her way to breakfast. Given the description of these paths, determine how many cow paths she traverses, presuming that she commences choosing various paths as soon as she leaves the barn.</p>

<p>The farm has P (1 <= P <= 1,000) pastures that are lead to by P-1 choice-nodes (range 1..P-1) connected by paths. From the barn (which is node 1), only one set of path traversals exists to reach any choice-node or pasture.</p>

<p>Consider this set of paths (lines), pastures ('%'), and the highlighted ('#') route to a pasture on the right:</p>

<pre>                 %                             %
                /                             /
      2----%   7----8----%          2----%   7####8----%
     / \      /      \             # #      #      #
    1   5----6        9----%      1   5####6        9----%
     \   \    \        \           \   \    \        #
      \   %    %        %           \   %    %        %
       \                             \
        3-----%                       3-----%
         \                             \
          4----%                        4----%
           \                             \
            %                             %</pre>

<p>The pasture reached from choice-node 9 is one of two that enable Bessie to traverse seven different cowpaths on the way to breakfast. These are the 'furthest' pastures from node 1, the barn.</p>

<p>Three integers describe each node: Cn, D1, and D2. Cn is the nodenumber (1 <= Cn <= P-1); D1 and D2 are the destinations from that node (0 <= D1 <= P-1; 0 <= D2 <= P-1). If D1 is 0, the node leads to a pasture in that direction; D2 has the same property.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: P</li>
	<li>Lines 2..P: Line i+1 contains three space-separated integeres that describe a choice-node: Cn, D1, and D2</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the largest number of paths Bessie can traverse on the way to the furthest pasture.</li>
</ul>

<p> </p>

