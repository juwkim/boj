# [Silver IV] Buy One Get One Free - 6230 

[문제 링크](https://www.acmicpc.net/problem/6230) 

### 성능 요약

메모리: 116756 KB, 시간: 180 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting), 두 포인터(two_pointer)

### 문제 설명

<p>Farmer John has discovered the Internet is buying bales of hay online when he notices a special deal. For every bale of hay of size A (1 <= A <= 1,000,000) he buys, he can get a bale of hay of size B (1 <= B < A) for free!</p>

<p>The deal, however, is restricted: the larger bale must be high quality hay and the smaller one must be low quality hay. FJ, being a frugal and thrifty fellow, does not care: any quality of hay will do as long as he saves some money.</p>

<p>Given a list of the sizes of N (1 <= N <= 10,000) bales of high quality hay and M (1 <= M <= 10,000) bales of low quality hay, find the maximum number of bales of hay Farmer John can purchase.  He can buy bales of high quality hay without getting the free bale of low quality hay, but he cannot buy bales of low quality hay (i.e., he must get them for free in the deal).</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M.</li>
	<li>Lines 2..N+1: Line i+1 contains a single integer which is the size of the ith bale of high quality hay.</li>
	<li>Lines N+2..N+M+1: Line i+N+1 contains a single integer which is the size of the ith bale of low quality hay.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The maximum total number of bales of hay Farmer John can obtain.</li>
</ul>

