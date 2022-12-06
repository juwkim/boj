# [Silver V] Zigzag - 15779 

[문제 링크](https://www.acmicpc.net/problem/15779) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>어떤 수열에서, 연속된 3개의 수를 보았을 때, 그 수가 단조증가 수열이거나, 단조감소 수열인 경우가 없으면 이 수열을 "<strong>지그재그 수열</strong>" 이라고 말한다.</p>

<p>좀 더 정확하게는, 길이 <em>N</em>의 수열 <em>A</em>가 모든 1 이상 <em>N</em>-2 이하의 자연수 <em>i</em>에 대해서, <em>A<sub>i</sub></em> ≤ <em>A</em><sub><em>i</em>+1</sub> ≤ <em>A</em><sub><em>i</em>+2</sub>도 만족하지 않고, <em>A<sub>i</sub></em> ≥ <em>A</em><sub><em>i</em>+1</sub> ≥ <em>A</em><sub><em>i</em>+2</sub>도 만족하지 않으면, <em>A</em>는 지그재그 수열이다.</p>

<p>길이 <em>N</em>의 수열 <em>A</em>가 주어졌을 때, <em>A</em>의 연속된 부분 수열 중 지그재그 수열의 최대 길이를 구하여라.</p>

<p>길이 <em>M</em>의 <em>B</em>가 길이 <em>N</em>인 <em>A</em>의 연속된 부분 수열이라는 것은, 어떤 <em>i</em>가 존재 해서, <em>B</em><sub>1</sub> = <em>A<sub>i</sub></em>, <em>B</em><sub>2</sub> = <em>A</em><sub><em>i</em>+1</sub>, ..., <em>B<sub>M</sub></em> = <em>A</em><sub><em>i</em>+<em>M</em>-1</sub> 인 것을 말한다.</p>

### 입력 

 <p>입력은 두 줄로 이루어져 있다. 첫째 줄에는 수열의 길이 <em>N</em>이 주어진다.</p>

<p>둘째 줄에는 공백으로 구분된 <em>N</em>개의 정수가 주어진다. <em>i</em>번째 수는 <em>A<sub>i</sub></em>를 의미한다.</p>

### 출력 

 <p><em>A</em>의 연속된 부분 수열 중 지그재그 수열의 최대 길이를 구하여라. </p>

