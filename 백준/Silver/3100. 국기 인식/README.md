# [Silver IV] 국기 인식 - 3100 

[문제 링크](https://www.acmicpc.net/problem/3100) 

### 성능 요약

메모리: 117280 KB, 시간: 188 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>희원이는 국기 인식 시스템을 만들었다. 이 알고리즘은 국기를 6*9크기의 행렬로 필터링 시킨 뒤, 인식한다. 행렬에는 색을 나타내는 알파벳 대문자가 있다.</p>

<p>이 시스템은 아직 개발 초기 단계이기 때문에, 아래와 같이 간단한 형태만 인식할 수 있다.</p>

<pre>CCCCCCCCC     CCCCCCCCC     ZZZBBBCCC     ZZZAAAZZZ
CCCCCCCCC     CCCCCCCCC     ZZZBBBCCC     ZZZAAAZZZ
BBBBBBBBB     BBBBBBBBB     ZZZBBBCCC     ZZZAAAZZZ
BBBBBBBBB     BBBBBBBBB     ZZZBBBCCC     ZZZAAAZZZ
PPPPPPPPP     CCCCCCCCC     ZZZBBBCCC     ZZZAAAZZZ
PPPPPPPPP     CCCCCCCCC     ZZZBBBCCC     ZZZAAAZZZ</pre>

<p>즉, 위와 같이 삼등분 된 국기만 인식할 수 있다. 가운데 줄의 색상은 다른 두 줄과는 달라야 한다.</p>

<p>인식한 국기가 주어졌을 때, 간단한 형태가 되기 위해 바꿔야 하는 문자의 최소 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>총 6개줄에 걸쳐 9개 알파벳 대문자가 주어진다.</p>

### 출력 

 <p>첫째 줄에 간단한 형태가 되기 위해 바꿔야 하는 문자의 최소 개수를 출력한다.</p>

