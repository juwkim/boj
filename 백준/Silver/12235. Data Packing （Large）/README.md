# [Silver IV] Data Packing (Large) - 12235 

[문제 링크](https://www.acmicpc.net/problem/12235) 

### 성능 요약

메모리: 116016 KB, 시간: 152 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 정렬(sorting)

### 문제 설명

<p>Adam, being a well-organized man, has always been keenly interested in organizing all his stuff. In particular, he fondly remembers the many hours of his youth that were spent moving files from his computer onto Compact Discs.</p>

<p>There were two very important rules involved in this procedure. First, in order to ensure that all discs could be labeled clearly, Adam would never place more than two files on the same disc. Second, he would never divide a single file over multiple discs. Happily, the discs he was using were always large enough to make this possible.</p>

<p>Thinking back, Adam is now wondering whether he arranged his files in the best way, or whether he ended up wasting some Compact Discs. He will provide you with the capacity of the discs he used (all his discs had the same capacity) as well as a list of the sizes of the files that he stored. Please help Adam out by determining the minimum number of discs needed to store all his files—following the two very important rules, of course.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with a line containing two integers: the number of files to be stored <strong>N</strong>, and the capacity of the discs to be used <strong>X</strong> (in MBs). The next line contains the <strong>N</strong> integers representing the sizes of the files <strong>S</strong><strong><sub>i</sub></strong> (in MBs), separated by single spaces.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>X</strong> ≤ 700.</li>
	<li>1 ≤ <strong>S</strong><strong><sub>i</sub></strong> ≤ X.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 10</span><sup style="line-height:1.6em">4</sup></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the minimum number of discs needed to store the given files.</p>

