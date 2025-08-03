# [Silver I] Building for UN - 3583 

[문제 링크](https://www.acmicpc.net/problem/3583) 

### 성능 요약

메모리: 108384 KB, 시간: 100 ms

### 분류

해 구성하기

### 제출 일자

2025년 8월 3일 22:37:06

### 문제 설명

<p>The United Nations has decided to build a new headquarters in Saint Petersburg, Russia. It will have a form of a rectangular parallelepiped and will consist of several rectangular floors, one on top of another. Each floor is a rectangular grid of the same dimensions, each cell of this grid is an office.</p>

<p>Two offices are considered adjacent if they are located on the same floor and share a common wall, or if one’s floor is the other’s ceiling.</p>

<p>The St. Petersburg building will host n national missions. Each country gets several offices that form a connected set.</p>

<p>Moreover, modern political situation shows that countries might want to form secret coalitions. For that to be possible, each pair of countries must have at least one pair of adjacent offices, so that they can raise the wall or the ceiling they share to perform secret pair-wise negotiations just in case they need to.</p>

<p>You are hired to design an appropriate building for the UN.</p>

### 입력 

 <p>The input file consists of a single integer number n (1 ≤ n ≤ 50) — the number of countries that are hosted in the building.</p>

### 출력 

 <p>On the first line of the output file write three integer numbers h, w, and l — height, width and length of the building respectively.</p>

<p>h descriptions of floors should follow. Each floor description consists of l lines with w characters on each line. Separate descriptions of adjacent floors with an empty line.</p>

<p>Use capital and small Latin letters to denote offices of different countries. There should be at most 1 000 000 offices in the building. Each office should be occupied by a country. There should be exactly n different countries in the building. In this problem the required building design always exists.</p>

