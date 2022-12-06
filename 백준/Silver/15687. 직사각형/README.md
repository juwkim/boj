# [Silver V] 직사각형 - 15687 

[문제 링크](https://www.acmicpc.net/problem/15687) 

### 성능 요약

메모리: 4452 KB, 시간: 8 ms

### 분류

기하학(geometry), 구현(implementation)

### 문제 설명

<p>직사각형의 정보를 저장할 클래스 Rectangle을 구현하시오.</p>

<ul>
	<li>C++14, C++17
	<ul>
		<li>클래스 이름: <code>Rectangle</code></li>
		<li><code>생성자</code>
		<ul>
			<li><code>Rectangle(width, height)</code>: 직사각형의 가로 길이를 <code>width</code>, 세로 길이를 <code>height</code> 설정한다. <code>width</code>는 1,000보다 작거나 같은 자연수, <code>height</code>는 2,000보다 작거나 같은 자연수이다.</li>
		</ul>
		</li>
		<li>멤버 변수
		<ul>
			<li><code>int width</code>: 직사각형의 가로 길이</li>
			<li><code>int height</code>: 직사각형의 세로 길이</li>
		</ul>
		</li>
		<li>멤버 함수
		<ul>
			<li><code>int get_width() const</code>: 직사각형의 가로 길이를 리턴한다.</li>
			<li><code>int get_height() const</code>: 직사각형의 세로 길이를 리턴한다.</li>
			<li><code>void set_width(int width)</code>: 직사각형의 가로 길이를 <code>width</code>로 변경한다. 만약, <code>width</code>가 0보다 작거나 같거나, 1,000보다 크면 변경하지 않는다.</li>
			<li><code>void set_height(int height)</code>: 직사각형의 세로 길이를 <code>height</code>로 변경한다. 만약, <code>height</code>가 0보다 작거나 같거나, 2,000보다 크면 변경하지 않는다.</li>
			<li><code>int area() const</code>: 직사각형의 넓이를 리턴한다.</li>
			<li><code>int perimeter() const</code>: 직사각형의 둘레 길이를 리턴한다.</li>
			<li><code>bool is_square() const</code>: 정사각형이면 <code>true</code>, 아니면 <code>false</code>를 리턴한다.</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

### 입력 

 Empty

### 출력 

 Empty

