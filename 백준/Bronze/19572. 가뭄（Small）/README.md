# [Bronze II] 가뭄(Small) - 19572 

[문제 링크](https://www.acmicpc.net/problem/19572) 

### 성능 요약

메모리: 121220 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>가뭄에 찌든 신촌을 위해서 국렬이는 세 칸으로 구성되어 있는 신촌에 비를 내릴 것이다. 그러나 국렬이는 무능해서 각 칸마다 비를 내리지 못하고, 두 칸에 동일하게 비를 내리는 것만 할 수 있다.</p>

<p>1번째 칸, 2번째 칸에 동시에 뿌리는 비의 강수량을 <em>a</em> cm, 1번째 칸, 3번째 칸에 동시에 뿌리는 비의 강수량을 <em>b</em> cm, 2번째 칸, 3번째 칸에 동시에 뿌리는 비의 강수량을 <em>c</em> cm라고 하자. <em>a</em>, <em>b</em>, <em>c</em>는 모두 양의 실수여야 한다. 가뭄에 찌든 신촌이라도 비가 너무 많이 오면 상당히 곤란하고, 비가 너무 조금 와도 곤란하다. 그래서 각 칸에 해당하는 지역은 강수량이 정확히 <em>d<sub>i</sub></em> cm가 되어야 한다. 이때 정확한 <em>a</em>, <em>b</em>, <em>c</em>의 값을 구하여라.</p>

### 입력 

 <p>3개의 양의 정수가 입력으로 들어온다. 각각은 <em>d</em><sub>1</sub>, <em>d</em><sub>2</sub>, <em>d</em><sub>3</sub>을 의미한다. (1 ≤ <em>d</em><sub>1</sub>, <em>d</em><sub>2</sub>, <em>d</em><sub>3</sub> ≤ 10<sup>6</sup>)</p>

### 출력 

 <p>조건에 맞게 비를 내릴 수 없다면 <code><span style="background-color:#dddddd;">-1</span></code>을 출력한다.</p>

<p>조건에 맞게 비를 내릴 수 있다면 <code><span style="background-color:#dddddd;">1</span></code>을 출력하고, 다음 줄에 <i data-stringify-type="italic">a</i>, <i data-stringify-type="italic">b</i>, <i data-stringify-type="italic">c</i>를 소수 첫째 자리까지 반올림한 것을 공백으로 구분하여 출력한다.</p>

