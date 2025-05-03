# [Silver I] Erratic Ants - 10484 

[문제 링크](https://www.acmicpc.net/problem/10484) 

### 성능 요약

메모리: 112308 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 4일 02:54:30

### 문제 설명

<p>The ants of a particular colony are in search of food. Unfortunately hidden dangers are all around the colony which makes foraging difficult. There are traps, obstacles, and predators lurking about. Fortunately, the colony has the perfect ant for the job. Max is neither a smart ant nor an efficient ant but he has got blind luck on his side. In all of his wanderings, he has always managed to stay on safe ground and he (eventually) always finds a source of food to report back to the colony.</p>

<p>The problem is that Max rarely takes anything resembling an optimal (shortest) route to find a food source. However, Max can reliably bring back the exact details of the (often winding and convoluted) path that he took to get to the food source. Your job is to help the colony by finding the optimal route located within Max’s convoluted directions to allow the colony to forage more efficiently.</p>

### 입력 

 <p>The first integer in the input, 1 ≤ n ≤ 100, denotes the number of paths to food that Max has reported back. This is followed by a blank line and then descriptions of each of the n paths. Each path description begins with an integer, s (0 ≤ s ≤ 60), which denotes the number of steps taken in the path. The next s lines contain directional steps expressed as upper-case characters N, E, S, and W corresponding to steps taken in the directions north, east, south, and west respectively. Each step moves Max one unit of distance. Max’s paths always start at the colony and end at a food source. Between each pair of path descriptions is a blank line.</p>

<p>When searching for an optimal path, the only directional steps that may be taken are ones that have previously been taken by Max, or the same steps in reverse.</p>

### 출력 

 <p>For each given path, give the number of steps found to be in an optimal (shortest) path.</p>

