# [Silver V] 알고리즘 수업 - 퀵 정렬 2 - 24091 

[문제 링크](https://www.acmicpc.net/problem/24091) 

### 성능 요약

메모리: 249968 KB, 시간: 584 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>오늘도 서준이는 퀵 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 퀵 정렬로 배열 A를 오름차순 정렬할 경우 배열 A의 원소가 <em>K </em>번 교환된 직후의 배열 A를 출력해 보자.</p>

<p>크기가 <em>N</em>인 배열에 대한 퀵 정렬 의사 코드는 다음과 같다.</p>

<pre>quick_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- partition(A, p, r);  # 분할
        quick_sort(A, p, q - 1);  # 왼쪽 부분 배열 정렬
        quick_sort(A, q + 1, r);  # 오른쪽 부분 배열 정렬
    }
}

partition(A[], p, r) {
    x <- A[r];    # 기준원소
    i <- p - 1;   # i는 x보다 작거나 작은 원소들의 끝지점
    for j <- p to r - 1  # j는 아직 정해지지 않은 원소들의 시작 지점
        if (A[j] ≤ x) then A[++i] <-> A[j]; # i값 증가 후 A[i] <-> A[j] 교환
    if (i + 1 != r) then A[i + 1] <-> A[r]; # i + 1과 r이 서로 다르면 A[i + 1]과 A[r]을 교환
    return i + 1;
}</pre>

### 입력 

 <p>첫째 줄에 배열 A의 크기 <em>N</em>(5 ≤ <em>N</em> ≤ 10,000), 교환 횟수 <em>K</em>(1 ≤ <em>K</em> ≤ 10<sup>8</sup>)가 주어진다.</p>

<p>다음 줄에 서로 다른 배열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>배열 A에 <em>K </em>번 교환이 발생한 직후의 배열 A를 한 줄에 출력한다. 교환 횟수가 <em>K </em>보다 작으면 -1을 출력한다.</p>

