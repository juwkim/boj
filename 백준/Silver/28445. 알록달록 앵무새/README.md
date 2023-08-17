# [Silver V] 알록달록 앵무새 - 28445 

[문제 링크](https://www.acmicpc.net/problem/28445) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

자료 구조, 구현, 정렬, 문자열, 트리를 사용한 집합과 맵

### 문제 설명

<p>재현이가 키우는 앵무새 포포와 레몬이는 그동안 새끼들을 참 많이도 낳았다. 그렇게 태어난 앵무새들을 관찰하며 재현이는 앵무새들의 색에 간단한 규칙이 있다는 것을 발견했다. 그것은 바로 자식 앵무새의 몸통 색은 아빠 새의 몸통 색과 꼬리 색, 엄마 새의 몸통 색과 꼬리 색 중 하나이며 꼬리 색도 마찬가지로 이 넷 중 하나의 색으로 정해진다는 것이다.</p>

<p>아빠 새의 몸통 색과 꼬리 색, 엄마 새의 몸통 색과 꼬리 색이 주어질 때 가능한 자식 앵무새의 몸통 색과 꼬리색의 모든 쌍을 사전 순으로 출력하라. (단, 중복되는 몸통 색, 꼬리 색의 쌍은 출력하지 않는다.)</p>

### 입력 

 <p>첫 번째 줄에 아빠 새의 몸통 색과 꼬리 색이 주어진다.</p>

<p>두 번째 줄에 엄마 새의 몸통 색과 꼬리 색이 주어진다.</p>

<p>각각의 색은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>자 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>자 이내의 알파벳 소문자로 이루어진 문자열로 주어지며, 같은 색이 중복되어 나타날 수 있다.</p>

### 출력 

 <p>자식 새의 몸통 색과 꼬리 색의 쌍을 한 줄에 하나씩 사전 순으로 출력한다. 사전 순으로 출력하라는 말은 몸통 색이 다르다면 몸통 색의 사전 순으로, 몸통 색이 같다면 꼬리 색의 사전 순으로 출력하라는 것을 의미한다.</p>

