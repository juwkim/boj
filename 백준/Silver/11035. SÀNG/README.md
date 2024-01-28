# [Silver III] SÀNG - 11035 

[문제 링크](https://www.acmicpc.net/problem/11035) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2024년 1월 28일 23:42:45

### 문제 설명

<p>Sàng của Eratosthenes là thuật toán nổi tiếng để tìm tất cả các số nguyên tố nhỏ hơn N. Thuật toán như sau: </p>

<ol>
	<li>Ghi ra tất cả các số nguyên giữa 2 và N. </li>
	<li>Tìm số nhỏ nhất chưa bị gạch và gọi nó là P (P là số nguyên tố). </li>
	<li>Gạch bỏ P và tất cả các bội số của nó mà chưa bị gạch. </li>
	<li>Nếu còn số chưa bị gạch bỏ, chuyển sang bước 2. </li>
</ol>

<p>Viết một chương trình, cho N và K, tìm số nguyên thứ K bị gạch.</p>

### 입력 

 <p>Gồm nhiều bộ test, mỗi bộ test nằm trên một dòng gồm các số nguyên N và K (2 ≤ K < N ≤ 1000). </p>

### 출력 

 <p>Với mỗi test, in ra trên một dòng số thứ K bị gạch bỏ.</p>

