# [Bronze III] Statistics - 20674 

[문제 링크](https://www.acmicpc.net/problem/20674) 

### 성능 요약

메모리: 124332 KB, 시간: 148 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Coronavirus cases are now rising very fast in Neverland. The rise is mainly caused by a new variant of the virus which is spreading more rapidly than the original version. People are frustrated by seeing another pick in the statistics, while at the same time, there is no clear estimate on when vaccination will be available in the country.</p>

<p>Although the new variant of coronavirus is not believed to be more deadly, the rise in the new case statistics has made people panicked and afraid. Therefore, the government of Neverland has decided to manipulate the new case statistics slightly to reduce people’s anxiety. The goal of the manipulation is to show that the new cases are not rising in the coming few days. More precisely, the number of new cases announced in each of the coming days must be equal or lower than the number announced in its preceding day. Due to investigations, the only way to change the statistics is to throw away some test results. Therefore, the announced numbers must be always less than or equal to the real numbers.</p>

<p>As the manipulation is not free, the government is going to hire a computer scientist to calculate the minimum total amount by which the real numbers must be changed in order to achieve the above goal. Due to your experience in the ICPC programming contests, the government has selected you for this critical mission.</p>

### 입력 

 <p>The first line of the input consists of n (1 ⩽ n ⩽ 10 000), the number of the coming days. Each of the next n lines contains an integer p<sub>i</sub> (0 ⩽ p<sub>i</sub> ⩽ 1000), indicating the real number of new cases at the i-th day.</p>

### 출력 

 <p>In the output, print the minimum total amount by which the real numbers must be changed in order to have new cases not to be rising in the coming days.</p>

