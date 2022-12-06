# [Silver V] 알고리즘 수업 - 선택 알고리즘 2 - 24399 

[문제 링크](https://www.acmicpc.net/problem/24399) 

### 성능 요약

메모리: 250552 KB, 시간: 364 ms

### 분류

구현(implementation)

### 문제 설명

<p>오늘도 서준이는 선택 알고리즘 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><i>N</i>개의 서로 다른 양의 정수가 규칙 없이 저장된 배열 A가 있다. 평균 선형 시간 선택 알고리즘으로 배열 A에서 <i>Q </i>번째 작은 원소를 찾는 경우 배열 A의 원소가 <em>K </em>번 교환된 직후의 배열 A를 출력해보자.</p>

<p>크기가 <em>N</em>인 배열에 대한 평균 선형 시간 선택 알고리즘 의사 코드는 다음과 같다.</p>

<pre>select(A[], p, r, q) { # A[p..r]에서 q번째 작은 원소를 찾는다.
    if (p = r) then return A[p];
    t <- partition(A, p, r);  # 분할
    k <- t - p + 1;           # 기준원소가 전체에서 k번째 작은 원소임
    if (q < k) then return select(A, p, t - 1, q);  # 왼쪽 그룹으로 범위를 좁힘
    else if (q = k) then return A[t];               # 기준원소가 찾는 원소임
    else return select(A, t + 1, r, q - k);         # 오른쪽 그룹으로 범위를 좁힘
}

partition(A[], p, r) {
    x <- A[r];    # 기준원소
    i <- p - 1;   # i는 x보다 작거나 같은 원소들의 끝 지점
    for j <- p to r - 1  # j는 아직 정해지지 않은 원소들의 시작 지점
        if (A[j] ≤ x) then A[++i] <-> A[j]; # i값 증가 후 A[i] <-> A[j] 교환
    if (i + 1 ≠ r) then A[i + 1] <-> A[r];  # i + 1과 r이 서로 다르면 A[i + 1]과 A[r]을 교환
    return i + 1;
}</pre>

### 입력 

 <p>첫째 줄에 배열 A의 크기 <em>N</em>(5 ≤ <em>N</em> ≤ 10,000), 찾을 원소 정보 <em>Q</em>(1 ≤ <em>Q</em> ≤ <em>N</em>), 교환 횟수 <em>K</em>(1 ≤ <em>K</em> ≤ 10<sup>8</sup>)가 주어진다.</p>

<p>다음 줄에 서로 다른 배열 A의 원소 <em>A<sub>1</sub></em>, <em>A<sub>2</sub></em>, ..., <em>A<sub>N</sub></em>이 주어진다. (1 ≤ <em>A<sub>i</sub></em> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>배열 A에 <em>K </em>번 교환이 발생한 직후의 배열 A를 한 줄에 출력한다. 교환 횟수가 <em>K </em>보다 작으면 -1을 출력한다.</p>

