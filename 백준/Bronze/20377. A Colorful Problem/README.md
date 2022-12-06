# [Bronze I] A Colorful Problem - 20377 

[문제 링크](https://www.acmicpc.net/problem/20377) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>In computer graphics it is often necessary to map one discrete set of colors to a second, smaller discrete set of colors. The goal of this program is to perform just a mapping in RGB color space. The input to the program consists of a target set of 16 RGB color values, and a collection of RGB color values to be mapped to the "closest" color in the target set.</p>

<p>The input is a list of RGB color values, one color per line, with each color having a red, green, and blue component, in that order, specified as integers from 0 to 255 (0 indicates complete absence of that component, 255 indicates full intensity of that component). The first 16 colors form the target set of colors to which all the rest of the colors in the input should be mapped.</p>

<p>For a given color, the "closest" color in the target set is the color with the smallest euclidean distance from the original color. That is if $rgb$ is the color to be mapped, and $\{R_1G_1B_1, \dots, R_{16}G_{16}B_{16}\}$ is the set of target colors, the closest color is the one which minimizes the distance equation $d = \sqrt{(R_i - r)^2 + (G_i - g)^2 + (B_i - b)^2}$, where $i$ is an integer from 1 to 16.</p>

<p>The program should output one line for each color to be mapped to the target set. As illustrated in the sample out below, that line should contain the color to be mapped followed by the words "maps to", and then the color from the target set which the original color was mapped to. All colors should be specified as described above, in the order red, green, blue.</p>

### 입력 

 Empty

### 출력 

 Empty

