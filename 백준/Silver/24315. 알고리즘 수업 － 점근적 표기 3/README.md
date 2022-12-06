# [Silver IV] 알고리즘 수업 - 점근적 표기 3 - 24315 

[문제 링크](https://www.acmicpc.net/problem/24315) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

수학(math)

### 문제 설명

<p>오늘도 서준이는 점근적 표기 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>알고리즘의 소요 시간을 나타내는 Θ-표기법(빅-쎄타)을 다음과 같이 정의한다.</p>

<p>Θ(<em>g</em>(<em>n</em>)) = {<em>f</em>(<em>n</em>) | 모든 <em>n</em> ≥ <em>n<sub>0</sub></em>에 대하여 <em>c<sub>1</sub></em> × <em>g</em>(<em>n</em>) ≤ <em>f</em>(<em>n</em>) ≤ <em>c<sub>2</sub></em> × <em>g</em>(<em>n</em>)인 양의 상수 <em>c<sub>1</sub></em>, <em>c<sub>2</sub></em>, <em>n<sub>0</sub></em>가 존재한다}</p>

<p>이 정의는 실제 Θ-표기법(<a href="https://en.wikipedia.org/wiki/Big_O_notation">https://en.wikipedia.org/wiki/Big_O_notation</a>)과 다를 수 있다.</p>

<p>함수 <em>f</em>(<em>n</em>) = <em>a<sub>1</sub>n </em>+ <em>a<sub>0</sub></em>, 양의 정수 <em>c<sub>1</sub></em>, <em>c<sub>2</sub></em>, <em>n<sub>0</sub></em>가 주어질 경우 Θ(<em>n</em>) 정의를 만족하는지 알아보자.</p>

### 입력 

 <p>첫째 줄에 함수 <em>f</em>(<em>n</em>)을 나타내는 정수 <em>a<sub>1</sub></em>, <em>a</em><sub><em>0</em></sub>가 주어진다. (0 ≤ |<em>a<sub>i</sub></em>| ≤ 100)</p>

<p>다음 줄에 양의 정수 <em>c<sub>1</sub>, c<sub>2</sub></em>가 주어진다. (1 ≤ <em>c<sub>1</sub></em> ≤ <em>c<sub>2</sub></em> ≤ 100)</p>

<p>다음 줄에 양의 정수 <em>n<sub>0</sub></em>가 주어진다. (1 ≤ <em>n<sub>0</sub></em> ≤ 100)</p>

### 출력 

 <p><em>f</em>(<em>n</em>), <em>c<sub>1</sub>, c<sub>2</sub></em>, <em>n<sub>0</sub></em>가 Θ(<em>n</em>) 정의를 만족하면 1, 아니면 0을 출력한다.</p>

