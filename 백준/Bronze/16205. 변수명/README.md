# [Bronze I] 변수명 - 16205 

[문제 링크](https://www.acmicpc.net/problem/16205) 

### 성능 요약

메모리: 32152 KB, 시간: 128 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>변수명을 정하는 표기법은 여러 가지가 있다.</p>

<ul>
	<li>카멜 표기법 (Camel Case): 각 단어의 첫 글자를 대문자로 적는다. 단, 가장 첫 글자는 소문자를 사용한다.
	<ul>
		<li>예시: <code>camelCase</code>, <code>variableN</code>, <code>thisIsCamelCase</code>, <code>howToSolveThisProblem</code></li>
	</ul>
	</li>
	<li>스네이크 표기법 (Snake Case): 소문자만 사용하고, 각 단어의 사이에 언더바(_)를 넣어서 적는다.
	<ul>
		<li>예시: <code>snake_case</code>, <code>variable_n</code>, <code>this_is_snake_case</code>, <code>how_to_solve_this_problem</code></li>
	</ul>
	</li>
	<li>파스칼 표기법 (Pascal Case): 카멜 표기법과 같지만, 가장 첫 글자도 대문자를 사용한다.
	<ul>
		<li>예시: <code>PascalCase</code>, <code>VariableN</code>, <code>ThisIsPascalCase</code>, <code>HowToSolveThisProblem</code></li>
	</ul>
	</li>
</ul>

<p>한 표기법을 사용한 변수명이 주어졌을 때, 이를 다른 표기법으로 변환하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 사용한 표기법의 번호와 변수명이 주어진다. 번호가 1인 경우는 카멜 표기법, 2인 경우는 스네이크 표기법, 3인 경우는 파스칼 표기법이다.</p>

<p>입력으로 주어지는 변수명의 길이는 100을 넘지 않는다.</p>

<p>카멜 표기법, 파스칼 표기법을 사용한 변수명은 알파벳 소문자와 대문자로만 이루어져 있고, 스네이크 표기법을 사용한 변수명은 알파벳 소문자와 언더바(_)로만 이루어져 있다. 또, 스네이크 표기법을 사용한 변수명의 첫 글자와 마지막 글자는 언더바가 아니고, 언더바가 연속해서 두 개 이상 사용하는 경우는 없다.</p>

### 출력 

 <p>첫째 줄에 카멜 표기법을 사용한 경우, 둘째 줄에 스네이크 표기법을 사용한 경우, 셋째 줄에 파스칼 표기법을 사용한 경우를 출력한다.</p>

