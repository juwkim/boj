# [Silver IV] Birds on a Wire - 11187 

[문제 링크](https://www.acmicpc.net/problem/11187) 

### 성능 요약

메모리: 115684 KB, 시간: 144 ms

### 분류

많은 조건 분기(case_work), 그리디 알고리즘(greedy), 수학(math), 정렬(sorting)

### 문제 설명

<p>There is a long electrical wire of length ℓ centimetres between two poles where birds like to sit. After a long day at work you like to watch the birds on the wire from your balcony. Some time ago you noticed that they don’t like to sit closer than d centimetres from each other. In addition, they cannot sit closer than 6 centimetres to any of the poles, since there are spikes attached to the pole to keep it clean from faeces that would otherwise damage and weaken it. You start wondering how many more birds can possibly sit on the wire.</p>

<p>Given numbers ℓ and d, how many additional birds can sit on the wire given the positions of the birds already on the wire? For the purposes of this problem we assume that the birds have zero width.</p>

### 입력 

 <p>The first line contains three space separated integers: the length of the wire ℓ, distance d and number of birds n already sitting on the wire. The next n lines contain the positions of the birds in any order. All number are integers, 1 ≤ ℓ, d ≤ 1 000 000 000 and 0 ≤ n ≤ 20 000. (If you have objections to the physical plausibility of fitting that many birds on a line hanging between two poles, you may either imagine that the height of the line is 0 cm above ground level, or that the birds are ants instead.) You can assume that the birds already sitting on the wire are at least 6 cm from the poles and at least d centimetres apart from each other.</p>

### 출력 

 <p>Output one line with one integer – the maximal number of additional birds that can possibly sit on the wire.</p>

