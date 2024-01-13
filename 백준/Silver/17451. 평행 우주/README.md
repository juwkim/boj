# [Silver III] 평행 우주 - 17451 

[문제 링크](https://www.acmicpc.net/problem/17451) 

### 성능 요약

메모리: 159324 KB, 시간: 208 ms

### 분류

그리디 알고리즘, 수학

### 제출 일자

2024년 1월 13일 19:24:51

### 문제 설명

<p>서기 2XXX년, 지구가 소행성과 충돌할 위기에 처했다! 똑똑한 과학자 키파는 평행 우주를 누비며 지구를 대신할 행성을 찾는 막중한 임무를 맡게 되었다.</p>

<p>우리는 현재 지구(=행성 0)에 있다. 여러 요인을 고려한 결과, 행성 1, 행성 2, …, 행성 (<span style="font-style: italic;">n</span>-1)을 <strong>순서대로</strong> 확인하고 지구(=행성 <span style="font-style: italic;">n</span>)에 돌아오는 것이 비용상 최적임을 알아냈다. 모든 정수 1 ≤ <span style="font-style: italic;">i</span> < <span style="font-style: italic;">n</span>에 대해, 행성 <span style="font-style: italic;">i</span>은 지구가 아니다.</p>

<p>지구에는 "초고속 걷기 기계"라는, 속도를 원하는 만큼 올릴 수 있는 특수한 장치가 있다. 지구를 벗어나면 속도를 떨어뜨릴 수 있을 뿐 높일 수는 없다.</p>

<p>다음 지역에 가기 위해서는 원칙적으로는 필요한 속도를 정확히 맞춰야 하지만, 다행히도 평행 우주는 일정한 간격을 두고 있기 때문에 필요한 속도의 양의 정수 배로도 다음 지역으로 이동할 수 있다. 또한, 충분히 빠른 속도로 이동 중이며, 지구의 대체 행성으로 적합한지 아닌지는 도착한 뒤 바로 알 수 있기 때문에 어떤 행성에서는 도달한 뒤 속도를 유지한 채 다음 행성으로 이동할 수도 있다.</p>

<p>모든 1 ≤ <span style="font-style: italic;">i</span> ≤ <span style="font-style: italic;">n</span>에 대해, 행성 (<span style="font-style: italic;">i</span>-1)에서 행성 <span style="font-style: italic;">i</span>로 이동하는 데 필요한 (최소) 속도 <span style="font-style: italic;">v</span><sub><span style="font-style: italic;">i</span></sub>가 주어진다. 지구에서 올려야 하는 속도를 최소화하시오.</p>

### 입력 

 <p>첫째 줄에 <span style="font-style: italic;">n</span>(1 ≤ <span style="font-style: italic;">n</span> ≤ 3·10<sup>5</sup>)이 주어진다.</p>

<p>둘째 줄에 <span style="font-style: italic;">n</span>개의 정수 <span style="font-style: italic;">v</span><sub>1</sub>, <span style="font-style: italic;">v</span><sub>2</sub>, …, <span style="font-style: italic;">v</span><sub><span style="font-style: italic;">n</span></sub>이 공백을 사이에 두고 주어진다. 모든 정수 1 ≤ <span style="font-style: italic;">i</span> ≤ <span style="font-style: italic;">n</span>에 대해 1 ≤ <span style="font-style: italic;">v</span><sub><span style="font-style: italic;">i</span></sub> ≤ 10<sup>9</sup>을 만족한다.</p>

### 출력 

 <p>수 하나를 출력한다. 이 수는 지구에서 올려야 하는 속도의 최솟값이다.</p>

