# [Silver IV] Non-decreasing subsegment - 13243 

[문제 링크](https://www.acmicpc.net/problem/13243) 

### 성능 요약

메모리: 114488 KB, 시간: 116 ms

### 분류

구현(implementation)

### 문제 설명

<p>A subsegment is a continuous piece of the list. For example: In the list [1, 2, 3, 4, 5], we have subsegments such as [1, 2, 3, 4], [2, 3] or [3, 4]. [1, 3, 4, 5] is not a subsegment because 1 and 3 are not continuous in the original list.</p>

<p>Given the list [3, 1, 2, 4, 2, 2, 3, 6] the non-decreasing subsegments are:</p>

<ul>
	<li>[3], [1], [2], [4], [2], [2], [3], [6] (each element is a subsegment by itself)</li>
	<li>[1, 2, 4]</li>
	<li>[2, 2, 3, 6] (notice the sequence never decreases)</li>
</ul>

<p>Hence the longest subsegment is [2, 2, 3, 6] and has a size of 4 elements.</p>

<p>You’ll need to compute the length of the longest subsegment and the sum of these elements. In a case of more than one non-decreasing subsegment with the maximum length, return the length and the sum of the one who appears first in the input.</p>

### 입력 

 <p>The first line will contain an integer n (1 ≤ n ≤ 10<sup>5</sup>), the size of the list. The next line will contain n integers, the elements of the list, separated by spaces (the values will be between 1 and 10<sup>9</sup>).</p>

### 출력 

 <p>Two integers separated by a single space: the first one representing the size of the longest non-decreasing subsegment of the list and the second it’s sum. In the case of equally longest non-decreasing subsegment, output the length and the sum of the subsegment that appears first.</p>

