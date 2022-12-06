# [Gold I] 수열과 쿼리 37 - 18436 

[문제 링크](https://www.acmicpc.net/problem/18436) 

### 성능 요약

메모리: 128772 KB, 시간: 336 ms

### 분류

세그먼트 트리(segtree), 자료 구조(data_structures)

### 문제 설명

<p>길이가 N인 수열 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 있다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.</p>

<ul>
	<li><code>1 i x</code>: A<sub>i</sub>를 x로 바꾼다.</li>
	<li><code>2 l r</code>: l ≤ i ≤ r에 속하는 모든 A<sub>i</sub>중에서 짝수의 개수를 출력한다.</li>
	<li><code>3 l r</code>: l ≤ i ≤ r에 속하는 모든 A<sub>i</sub>중에서 홀수의 개수를 출력한다.</li>
</ul>

<p>수열의 인덱스는 1부터 시작한다.</p>

### 입력 

 <p>첫째 줄에 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.</p>

<p>둘째 줄에는 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)</p>

<p>셋째 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.</p>

<p>넷째 줄부터 M개의 줄에는 쿼리가 한 줄에 하나씩 주어진다. (1 ≤ i ≤ N, 1 ≤ l ≤ r ≤ N, 1 ≤ x ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>2, 3번 쿼리의 정답을 한 줄에 하나씩 출력한다.</p>

