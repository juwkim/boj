# [Silver V] The Perfect Cow - 6108 

[문제 링크](https://www.acmicpc.net/problem/6108) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>For the 39th year in a row, Farmer John was named "Dairy Farmer of the Year". The Dairy Association wants him to exhibit his most perfect cow at the upcoming Cow Convention in Herbster, Wisconsin on the frigid shores of Lake Superior.</p>

<p>FJ keeps up with scientific literature and knows that beauty is actually a trend toward the average rather than the existence of some superior trait. Thus, he wants to find his most average cow and share her beauty with the other Dairy Farmers during the weekend of revelry and partying at the convention.</p>

<p>Happily, each of the N*N cows (2 <= N <= 99; N odd) has her beauty rating (1 <= R_ij <= 1,000) inscribed on a tag in her ear, just like in this picture.</p>

<p>Cows aren't so good at math, so FJ lines them up into an N x N square. He asks them to find the median cow in each row (the median cow is the one whose  beauty number is bigger than or equal to half the cows in her group and also smaller than or equal to half the cows in her group -- the middle number of the group). From those N medians, FJ then finds the median of those numbers and brings that cow to the convention.</p>

<p>Given a set of N x N cows, find the beauty index of the most perfect (average) cow.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains N space-separated integers that are the N beauty indices for row i of the cow square</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the index of the most perfect cow as described in the task.</li>
</ul>

<p> </p>

