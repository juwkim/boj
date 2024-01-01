# [Silver II] 222-풀링 - 17829 

[문제 링크](https://www.acmicpc.net/problem/17829) 

### 성능 요약

메모리: 123132 KB, 시간: 324 ms

### 분류

분할 정복, 구현, 재귀

### 제출 일자

2024년 1월 2일 07:23:36

### 문제 설명

<p>조기 졸업을 꿈꾸는 종욱이는 요즘 핫한 딥러닝을 공부하던 중, 이미지 처리에 흔히 쓰이는 합성곱 신경망(Convolutional Neural Network, CNN)의 풀링 연산에 영감을 받아 자신만의 풀링을 만들고 이를 222-풀링이라 부르기로 했다.</p>

<p>다음은 8×8 행렬이 주어졌다고 가정했을 때 222-풀링을 1회 적용하는 과정을 설명한 것이다</p>

<ol>
	<li>
	<p>행렬을 2×2 정사각형으로 나눈다.</p>

	<p><img alt="" src="https://upload.acmicpc.net/61c48878-d2bb-4680-a7d3-8f9922f3c30f/-/preview/" style="width: 350px; height: 350px;"></p>
	</li>
	<li>
	<p>각 정사각형에서 2번째로 큰 수만 남긴다. 여기서 2번째로 큰 수란, 정사각형의 네 원소를 크기순으로 a<sub>4 </sub>≤<sub> </sub>a<sub>3 </sub>≤ a<sub>2 </sub>≤<sub> </sub>a<sub>1</sub> 라 했을 때, 원소 a<sub>2</sub>를 뜻한다.</p>

	<p><img alt="" src="https://upload.acmicpc.net/c2d98fd8-f0dd-4ab4-8fe7-f360e74fa86e/-/preview/" style="height: 350px; width: 676px;"></p>
	</li>
	<li>
	<p>2번 과정에 의해 행렬의 크기가 줄어들게 된다.</p>
	</li>
</ol>

<p>종욱이는 <em>N</em>×<em>N</em> 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.</p>

<p>랩실 활동에 치여 삶이 사라진 종욱이를 애도하며 종욱이의 궁금증을 대신 해결해주자.</p>

### 입력 

 <p>첫째 줄에 <em>N</em>(2 ≤ <em>N</em> ≤ 1024)이 주어진다. <em>N</em>은 항상 2의 거듭제곱 꼴이다. (<em>N</em>=2<em><sup>K</sup></em>, 1 ≤ <em>K</em> ≤ 10)</p>

<p>다음 <em>N</em>개의 줄마다 각 행의 원소 <em>N</em>개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다. </p>

### 출력 

 <p>마지막에 남은 수를 출력한다.</p>

