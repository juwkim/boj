# [Silver V] Identify, Sort, Index, Solve - 26150 

[문제 링크](https://www.acmicpc.net/problem/26150) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>ISIS Puzzle은 "Identify, Sort, Index, Solve"의 절차로 푸는 퍼즐을 통칭한다.</p>

<p>퍼즐을 좋아하는 하이비는 HCPC에 아래와 같은 ISIS 퍼즐 문제를 내기로 했다.</p>

<ol>
	<li>$ N $개의 문자열 $ S_1, S_2, \ldots, S_N $이 주어진다.</li>
	<li>Identify: 각 문자열과 대응되는 문제의 제목을 알아낸 뒤, 그 문제의 번호 $ I_i $와 난이도 $ D_i $를 알아낸다.</li>
	<li>Sort: 문제들을 번호 $ I_i $의 오름차순으로 정렬한다.</li>
	<li>Index: 각 문제 이름 $ S_i $에서 $ D_i $번째의 글자를 추출한다. <strong>이때 추출된 글자가 소문자라면 대문자로 변환한다.</strong></li>
	<li>Solve: Index 단계에서 추출한 글자들을 Sort 단계에서 정렬한 순서대로 나열한다.</li>
</ol>

<p>하지만 Identify는 구현이 어려울 것이라고 생각해, Identify까지 완료된 자료를 주기로 했다.</p>

<p>Identify가 완료된 자료가 주어질 때, Sort, Index, Solve까지 완료한 뒤 나오는 문자열을 출력해보자.</p>

### 입력 

 <p>첫째 줄에는 자료의 수 $ N $이 주어진다. $( 1 \le N \le 100 )$</p>

<p>둘째 줄부터 $ N $개의 줄에 걸쳐서 문제 제목 $ S_i $, 번호 $ I_i $, 난이도 $ D_i $가 주어진다. $( 1 \le |S_i| \le 100; $ $ 1 \le I_i \le 100\,000; $ $ 1 \le D_i \le |S_i| )$</p>

<p>$ S_i $는 알파벳 대소문자와 숫자로만 이루어져 있다.</p>

<p>두 문제가 동일한 번호를 가지고 있는 경우는 없다.</p>

### 출력 

 <p>Solve 단계까지 완료한 뒤 나오는 문자열을 출력한다.</p>

