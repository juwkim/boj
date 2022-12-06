# [Silver II] Great Pow! - 10895 

[문제 링크](https://www.acmicpc.net/problem/10895) 

### 성능 요약

메모리: 113248 KB, 시간: 116 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>\(a\)의 거듭제곱 \(a^{b}\)를 편하게 \(pow_{a}(b)\)라고 나타내어 보자.</p>

<p>그리고 \(pow_{a}^{0}(a) = a, pow_{a}^{k+1}(a) = pow_{a} (pow_{a}^{k}(a)) (k \ge 0)\)라고 하자.</p>

<p>우리의 일은 \(a\)와 \(k\)가 주어질 때 \(pow_{a}^{k}(a)\)를 계산하는 것이다. 즉</p>

<p style="text-align:center"><span style="font-size:18px">\(a^{a^{a^{a^{a^{...^{{...}^{{a}^{a}}}}}}}}\)</span> (\(a\)가 \(k+1\)개)</p>

<p>을 계산하는 것이다. 주의해야 할 점은 만약 \(k = 2\)이라고 할 때</p>

<p style="text-align:center">\((a^{a})^{a} \neq a^{(a^{a})}\)</p>

<p>라는 것이다. 우리가 구하는 것은 후자이다.</p>

### 입력 

 <p>첫 번째 줄에 \(a\)와 \(k\) (1 ≤ \(a\) ≤ 10<sup>9</sup>, 0 ≤ \(k\) ≤ 10<sup>9</sup>)가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>\(pow_{a}^{k}(a)\)의 값을 출력한다. 답이 매우 커질 수 있으므로 답을 \(a+1\)로 나눈 나머지를 출력한다.</p>

