# [Bronze II] 회문 - 14561 

[문제 링크](https://www.acmicpc.net/problem/14561) 

### 성능 요약

메모리: 28776 KB, 시간: 156 ms

### 분류

수학(math)

### 문제 설명

<p>n진수는 base가 n인 수를 말한다. 예를 들어 십진수는 base가 10인 수이다. n진수의 수 A<sub>m</sub>A<sub>m-1</sub>A<sub>m-2</sub>…A<sub>1</sub>A<sub>0</sub>를 n진수로 표현해보면 A<sub>m</sub>A<sub>m-1</sub>A<sub>m-2</sub>…A<sub>1</sub>A<sub>0</sub> = A<sub>m </sub>× n<sup>m </sup>+ A<sub>m-1</sub> × n<sup>m–1</sup> + A<sub>m-2</sub> × n<sup>m–2</sup> + … + A<sub>1</sub> × n<sup>1</sup> + A<sub>0</sub> × n<sup>0</sup>이다. 예를 들면, 12468은 12468 = 1 × 10<sup>4</sup> + 2 × 10<sup>3</sup> + 4 × 10<sup>2</sup> + 6 × 10<sup>1</sup> + 8 × 10<sup>0</sup>로 표현할 수 있다.</p>

<p>회문(Palindrome)이란 앞으로 읽으나 뒤로 읽으나 같은 글을 말한다. 예를 들면, madam, level, 12321은 회문이다. 반면에, Chung-ang이나 university, 54899는 회문이 아니다.</p>

<p>어떤 십진수의 수 A가 주어졌을 때, 이를 n진수로 표현하면 회문인지 아닌지 판별하는 프로그램을 만드시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 수 T(1 ≤ T ≤ 1000)이 주어진다.</p>

<p>둘째 줄부터 T줄에 걸쳐 테스트 케이스별로 어떤 십진수의 수 A(1 ≤ A ≤ 100,000,000,000)와 n(2 ≤ n ≤ 16)이 공백을 두고 주어진다.</p>

### 출력 

 <p>각 줄마다 테스트 케이스가 회문일 경우 1, 아닐 경우에는 0을 출력한다.</p>

