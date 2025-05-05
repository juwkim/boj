# [Silver I] Zadanie próbne - 8870 

[문제 링크](https://www.acmicpc.net/problem/8870) 

### 성능 요약

메모리: 109412 KB, 시간: 92 ms

### 분류

런타임 전의 전처리

### 제출 일자

2025년 5월 6일 02:05:42

### 문제 설명

<pre>int ret = 0;
for(int s = 1; s<=n; s++) {
  for(int k = s; k<=n; k++) {
    for(int i = k; i<=n; i++) {
      ret = (ret+s*k/i)%2010;
    }
  }
}</pre>

### 입력 

 <p>W pierwszej i jedynej linii wejścia znajduje się wartość zmiennej <strong>n</strong> (1<=<strong>n</strong><=2010).</p>

### 출력 

 <p>Twój program powinien wypisać pojedyncza liczbę - wartość zmiennej ret po wykonaniu pętli.</p>

