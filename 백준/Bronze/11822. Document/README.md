# [Bronze I] Document - 11822 

[문제 링크](https://www.acmicpc.net/problem/11822) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>It is necessary to produce legislative framework document, just to be able to organize an important event. To be entered into force, this document must be signed by N officials, and the order in which officials sign the document is ﬁxed. We assume that officials are numbered in the order of signing, starting from the official number 1, and ending with official number N. </p>

<p>It is known that every official accept documents only at ﬁxed set of days of weeks (visiting days). Also, despite the week has seven days, officials accept documents only on the working days (Monday to Friday). Every official has at least one visiting day within week. </p>

<p>One official needs exactly one day to sign the document, i.e. if an official reviews the document at some day, other officials can not review this document that day. </p>

<p>Some Monday morning you get a document to be signed (let us count this day as the ﬁrst day). Write a program which will calculate the minimum number of days required to get all signs for this document in the speciﬁed order. If the document can not be completed within one week, you can continue to sign it next week, and so on. </p>

<p>It is guaranteed that the document is very well prepared and any official will sign it at the ﬁrst submit within one day, without any claims. </p>

### 입력 

 <p>First line of input ﬁle contains N — the number of officials (1 ≤ N ≤ 50). The following N lines contain ﬁve space-separated integers each, corresponding to the days of week from Monday to Friday, inclusive. The number in i-th row, corresponding to j-th day of week, is equal to 0, if i-th official doesn’t accept documents at j-th day of week, otherwise it equals 1. </p>

<p> </p>

### 출력 

 <p>Output ﬁle contains one integer — the minimal number of days required to sign the document. </p>

<p> </p>

