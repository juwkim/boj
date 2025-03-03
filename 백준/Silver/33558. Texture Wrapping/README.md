# [Silver III] Texture Wrapping - 33558 

[문제 링크](https://www.acmicpc.net/problem/33558) 

### 성능 요약

메모리: 110736 KB, 시간: 104 ms

### 분류

구현

### 제출 일자

2025년 3월 3일 17:51:16

### 문제 설명

<p>세로 길이가 $N$, 가로 길이가 $M$인 평면에 세로 길이가 $U$, 가로 길이가 $V$인 텍스처를 씌우려고 한다. 평면의 제일 왼쪽 위 칸에 텍스처의 왼쪽 위 칸이 만나게 해서 씌우려고 한다. 하지만 평면의 가로 또는 세로의 길이가 텍스처의 가로 또는 세로의 길이보다 길 수 있어 세 가지 방법 중 하나를 사용해서 평면을 다 씌울 수 있도록 하려고 한다.</p>

<p>세 가지의 방법은 다음과 같다.</p>

<p>1. clamp-to-edge</p>

<p>텍스처의 모서리를 늘려 빈 공간을 채우는 방식이다. 평면의 어떤 칸의 행 좌표가 텍스처의 세로 길이 이상이면 텍스처의 맨 아래 행에서 평면 칸과 동일한 열 좌표에 있는 칸을 해당 평면 칸에 씌운다. 열 좌표가 텍스처의 가로 길이 이상이면 텍스처의 맨 오른쪽 열에서 평면 칸과 동일한 행 좌표에 있는 칸을 해당 평면 칸에 씌운다. 행 좌표와 열 좌표가 각각 텍스처의 세로 길이, 가로 길이 이상이면 텍스처의 맨 아래 오른쪽 칸을 해당 평면 칸에 씌운다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/390492b8-cc68-44d3-a361-78a92a02bc39/-/preview/" style="height: 70%; width: 70%; margin-left: 0px; margin-right: 0px;"></p>

<p>2. repeat</p>

<p>텍스처를 반복적으로 붙이면서 씌우는 방식이다. 평면을 아래 그림과 같이 세로 길이가 $U$, 가로 길이가 $V$인 조각으로 쪼갠 후 각 조각의 맨 왼쪽 위 칸이 텍스처의 맨 왼쪽 위 칸이 오도록 텍스처를 씌운다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8c02835b-e6ce-4afb-9460-ad81e5f3a2ac/-/preview/" style="height: 70%; width: 70%; margin-left: 0px; margin-right: 0px;"></p>

<p>3. mirrored-repeat</p>

<p>텍스처를 텍스처 경계면에 대해 거울 반전 시키면서 붙여나가며 씌우는 방식이다. 평면을 아래 그림과 같이 세로 길이가 $U$, 가로 길이가 $V$인 조각으로 쪼갠 후 각 조각에서 왼쪽 조각을 씌울 때의 텍스처를 좌우반전, 아래쪽 조각을 씌울 때의 텍스처를 상하반전해서 해당 조각의 칸들을 씌운다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/32dc77ad-4c3c-432d-aeb1-029768b4f372/-/preview/" style="height: 70%; width: 70%; margin-left: 0px; margin-right: 0px;"></p>

<p>평면의 크기와 텍스처, 그리고 사용할 방법이 주어질 때 평면의 최종 모습을 출력하자.</p>

### 입력 

 <p>첫 번째 줄에 평면의 크기 $N$과 $M$이 공백으로 구분되어 주어진다. $(1 \leq N \leq 200; 1 \leq M \leq 200)$</p>

<p>두 번째 줄에 텍스처의 크기 $U$와 $V$가 공백으로 구분되어 주어진다. $(1 \leq U \leq 200; 1 \leq V \leq 200)$</p>

<p>세 번째 줄부터 $U$개의 줄에 걸쳐 텍스처의 정보가 주어진다. 텍스쳐의 각 줄은 알파벳 대소문자 또는 숫자로 구성된 길이가 $V$인 문자열이다</p>

<p>$U+3$번째 줄에 텍스처를 씌울 방법이 주어진다. <code>clamp-to-edge</code>, <code>repeat</code>, <code>mirrored-repeat</code> 중 하나로 주어진다.</p>

### 출력 

 <p>텍스처를 씌운 평면의 최종 모습을 출력한다.</p>

