# [Silver V] Ballot evaluation - 6495 

[문제 링크](https://www.acmicpc.net/problem/6495) 

### 성능 요약

메모리: 121024 KB, 시간: 648 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 많은 조건 분기(case_work), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Before the 2009 elections at the European Parliament, Bill and Ted have asked their friends to make guesses about the outcome of the ballot. Now, the results have been published, so Bill and Ted want to check who was right. But checking the results of their many friends would take a very long time, and they need the evaluation to be done by a computer. Since they are not so good at programming, they ask you for help.</p>

### 입력 

 <p>The data provided by Bill and Ted has the following format: The first line consists of the number <em>p</em> of parties followed by the number <em>g</em> of guesses (with <em>1 ≤ p ≤ 50</em> and <em>1 ≤ g ≤ 10000</em>). Then follow <em>p</em> lines, each line consisting of a unique party name of length ≤ 20 (only containing letters a-z, A-Z and digits 0-9) and the achieved vote percentage of this party with one digit after the decimal point. After the parties follow <em>g</em> lines, each consisting of a guess. A guess has the form <em>P<sub>1</sub> + P<sub>2</sub> + ... + P<sub>k</sub> COMP n</em>, where <em>P<sub>1</sub></em> to <em>P<sub>k</sub></em> are party names, <em>COMP</em> is one of the comparison operators <, >, <=, >= or = and <em>n</em> is an integer between 0 and 100, inclusively. Each party name occurs at most once in each guess.</p>

### 출력 

 <p>For each guess, sum up the vote percentages of the parties and compare them with the specified integer <em>n</em>. Then, print a line stating whether the guess was correct. See the sample output for details.</p>

