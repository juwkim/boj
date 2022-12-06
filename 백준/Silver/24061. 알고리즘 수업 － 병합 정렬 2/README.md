# [Silver IV] 알고리즘 수업 - 병합 정렬 2 - 24061 

[문제 링크](https://www.acmicpc.net/problem/24061) 

### 성능 요약

메모리: 228016 KB, 시간: 852 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A의 원소가 <em>K </em>번 변경된 직후의 배열 A를 출력해 보자.</p>

<p>크기가 <em>N</em>인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.</p>

<pre>merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
}</pre>

### 입력 

 <p>첫째 줄에 배열 A의 크기 <em>N</em>(5 ≤ <em>N</em> ≤ 500,000), 변경 횟수 <em>K</em>(1 ≤ <em>K</em> ≤ 10<sup>8</sup>)가 주어진다.</p>

<p>다음 줄에 서로 다른 배열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>배열 A에 <em>K </em>번 변경이 발생한 직후의 배열 A를 한 줄에 출력한다. 변경 횟수가 <em>K </em>보다 작으면 -1을 출력한다.</p>

