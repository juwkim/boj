# [Silver IV] 예쁜 숫자 - 3152 

[문제 링크](https://www.acmicpc.net/problem/3152) 

### 성능 요약

메모리: 113760 KB, 시간: 132 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>p는 2보다 큰 정수이다. 다음과 같은 규칙으로 무한 이진 트리의 각 노드에 정수인 숫자가 매겨진다.</p>

<ul>
	<li>루트 노드에는 1을 매긴다.</li>
	<li>노드에 x가 매겨져 있다면 해당 노드의 왼쪽 자식 노드에는 p * x, 오른쪽 자식 노드에는 p * x + 1이 매겨진다.</li>
</ul>

<p>예를 들어 p = 3 일때 트리의 시작 부분은 다음과 같을 것이다.</p>

<p style="text-align:center"><img src="" style="height:305px; width:587px"></p>

<p>어떤 숫자는 무한 이진 트리 내의 서로 다른 두 노드에 매겨진 두 숫자의 합으로 표현 할 수 있는 방법이 한 가지면 "예쁜 숫자"로 분류된다. 주어진 p로 만든 무한 이진 트리 내에서  n<sub>1</sub>, n<sub>2</sub>, n<sub>3</sub>, n<sub>4</sub>가 "예쁜"지 출력하는 프로그램을 작성하라.</p>

### 입력 

 <p>한 줄에 정수 p, n<sub>1</sub>, n<sub>2</sub>, n<sub>3</sub>, n<sub>4</sub>가 차례로 주어진다. (2 < p < 50, 0 < n<sub>1</sub> < 10<sup>18</sup>, 0 < n<sub>2</sub> < 10<sup>18</sup>, 0 < n<sub>3</sub> < 10<sup>18</sup>, 0 < n<sub>4</sub> < 10<sup>18</sup>)</p>

### 출력 

 <p>한 줄에 차례로 n<sub>1</sub>, n<sub>2</sub>, n<sub>3</sub>, n<sub>4</sub>가 예쁘면 1을, 아니면 0을 출력한다.</p>

