# [Silver I] 여섯 방정식 - 9765 

[문제 링크](https://www.acmicpc.net/problem/9765) 

### 성능 요약

메모리: 108384 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘, 유클리드 호제법, 수학, 정수론

### 제출 일자

2025년 4월 11일 00:59:37

### 문제 설명

<p>여섯 개의 간단한 방정식이 주어진다. 이때, x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>5</sub>, x<sub>6</sub>, x<sub>7</sub>를 찾는 프로그램을 작성하시오. x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>5</sub>, x<sub>6</sub>, x<sub>7</sub>은 2보다 크거나 같고, 20,000,000보다 작거나 같은 소수이다. 여섯 방정식은 아래와 같다.</p>

<ul>
	<li>c<sub>1</sub> = x<sub>1</sub>x<sub>2</sub></li>
	<li>x<sub>4</sub> = c<sub>4</sub>x<sub>1</sub></li>
	<li>c<sub>3</sub> = x<sub>6</sub>x<sub>7</sub></li>
	<li>x<sub>8</sub> = x<sub>7</sub>c<sub>2</sub></li>
	<li>c<sub>5</sub> = x<sub>2</sub>x<sub>3</sub></li>
	<li>c<sub>6</sub> = x<sub>6</sub>x<sub>5</sub></li>
</ul>

<p>c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub>, c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub>은 양의 정수로 (20,000,000)<sup>2</sup>을 넘지 않는다. c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub>, c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub>이 주어졌을 때, x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>5</sub>, x<sub>6</sub>, x<sub>7</sub>을 푸는 프로그램을 작성하시오. 항상 풀 수 있는 방정식만 입력으로 주어진다. </p>

### 입력 

 <p>첫째 줄에 c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub>, c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub>이 주어진다. (c<sub>1</sub> ≠ c<sub>5</sub>, c<sub>3</sub> ≠ c6)</p>

### 출력 

 <p>x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>5</sub>, x<sub>6</sub>, x<sub>7</sub> 를 공백으로 구분해 출력한다. 가능한 답이 여러 가지인 경우, 아무거나 출력한다.</p>

