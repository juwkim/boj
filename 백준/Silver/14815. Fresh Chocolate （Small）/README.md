# [Silver V] Fresh Chocolate (Small) - 14815 

[문제 링크](https://www.acmicpc.net/problem/14815) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

많은 조건 분기(case_work), 그리디 알고리즘(greedy), 수학(math), 정수론(number_theory)

### 문제 설명

<p>You are the public relations manager for a chocolate manufacturer. Unfortunately, the company's image has suffered because customers think the owner is cheap and miserly. You hope to undo that impression by offering a free factory tour and chocolate tasting.</p>

<p>Soon after starting the new project, you realized that the company owner's reputation is well-deserved: he only agreed to give away free chocolate if you would minimize the cost. The chocolate to be given away comes in packs of <strong>P</strong> pieces. You would like to open new packs for each tour group, but the owner insists that if there are leftover pieces from one group, they must be used with the next tour group before opening up any new packs.</p>

<p>For instance, suppose that each pack contains <strong>P</strong>=3 pieces, and that a tour group with 5 people comes. You will open two packs to give one piece to each person, and you will have one piece left over. Suppose that after that, another tour group with 6 people comes. They will receive the leftover piece, and then you will open two more packs to finish giving them their samples, and so you will have one piece left over again. If two groups with 4 people each come right after, the first of those will get the leftover piece plus a full pack, and the last 4 person group will get their pieces from two newly opened packs. Notice that you cannot open new packs until all leftovers have been used up, even if you plan on using all of the newly opened pack immediately.</p>

<p>In the example above, 2 out of the 4 groups (the first and last groups) got all of their chocolate from freshly opened packs. The other 2 groups got some fresh chocolate and some leftovers. You know that giving out leftovers is not the best way to undo the owner's miserly image, but you had to accept this system in order to get your cheap boss to agree to the project. Despite the unfavorable context, you are committed to doing a good job.</p>

<p>You have requests from <strong>N</strong> groups, and each group has specified the number of people that will come into the factory. Groups will come in one at a time. You want to bring them in in an order that maximizes the number of groups that get only fresh chocolate and no leftovers. You cannot reject groups, nor have a group get chocolate more than once, and you need to give exactly one piece to each person in each group.</p>

<p>In the example above, if instead of 5, 6, 4, 4, the order were 4, 5, 6, 4, a total of 3 groups (all but the 5 person group) would get only fresh chocolate. For that set of groups, it is not possible to do better, as no arrangement would cause all groups to get only fresh chocolate.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of two lines. The first line contains two integers <strong>N</strong>, the number of groups coming for a tour, and <strong>P</strong>, the number of pieces of chocolate per pack. The second line contains <strong>N</strong> integers <strong>G<sub>1</sub></strong>, <strong>G<sub>2</sub></strong>, ..., <strong>G<sub>N</sub></strong>, the number of people in each of the groups.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>N</strong> ≤ 100.</li>
	<li>1 ≤ <strong>G<sub>i</sub></strong> ≤ 100, for all i.</li>
	<li>2 ≤ <strong>P</strong> ≤ 3.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of groups that will receive only fresh chocolate if you bring them in in an order that maximizes that number.</p>

