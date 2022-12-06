# [Silver V] Sorting (Small) - 12280 

[문제 링크](https://www.acmicpc.net/problem/12280) 

### 성능 요약

메모리: 115416 KB, 시간: 124 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Alex and Bob are brothers and they both enjoy reading very much. They have widely different tastes on books so they keep their own books separately. However, their father thinks it is good to promote exchanges if they can put their books together. Thus he has bought an one-row bookshelf for them today and put all his sons' books on it in random order. He labeled each position of the bookshelf the owner of the corresponding book ('Alex' or 'Bob').</p>

<p>Unfortunately, Alex and Bob went outside and didn't know what their father did. When they were back, they came to realize the problem: they usually arranged their books in their own orders, but the books seem to be in a great mess on the bookshelf now. They have to sort them right now!!</p>

<p>Each book has its own <em>worth</em>, which is represented by an integer. Books with odd values of worth belong to Alex and the books with even values of worth belong to Bob. Alex has a habit of sorting his books from the left to the right in an increasing order of worths, while Bob prefers to sort his books from the left to the right in a decreasing order of worths.</p>

<p>At the same time, they do not want to change the positions of the labels, so that after they have finished sorting the books according their rules, each book's owner's name should match with the label in its position.</p>

<p>Here comes the problem. A sequence of <strong>N</strong> values <strong>s</strong><strong><sub>0</sub></strong>, <strong>s</strong><strong><sub>1</sub></strong>, ..., <strong>s</strong><strong><sub>N-1</sub></strong> is given, which indicates the worths of the books from the left to the right on the bookshelf currently. Please help the brothers to find out the sequence of worths after sorting such that it satisfies the above description.</p>

### 입력 

 <p>The first line of input contains a single integer <strong>T</strong>, the number of test cases. Each test case starts with a line containing an integer <strong>N</strong>, the number of books on the bookshelf. The next line contains <strong>N</strong> integers separated by spaces, representing <strong>s</strong><strong><sub>0</sub></strong>, <strong>s</strong><strong><sub>1</sub></strong>, ..., <strong>s</strong><strong><sub>N-1</sub></strong>, which are the worths of the books.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 30.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 100</span></li>
	<li>-100 ≤ <strong>s</strong><strong><sub>i</sub></strong> ≤ 100</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>X</strong>: ", followed by <strong>t</strong><strong><sub>0</sub></strong>, <strong>t</strong><strong><sub>1</sub></strong>, ..., <strong>t</strong><strong><sub>N-1</sub></strong> in order, and separated by spaces. <strong>X</strong> is the test case number (starting from 1) and <strong>t</strong><strong><sub>0</sub></strong>, <strong>t</strong><strong><sub>1</sub></strong>, ..., <strong>t</strong><strong><sub>N-1</sub></strong> forms the resulting sequence of worths of the books from the left to the right.</p>

