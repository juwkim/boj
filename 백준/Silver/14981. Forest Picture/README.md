# [Silver II] Forest Picture - 14981 

[문제 링크](https://www.acmicpc.net/problem/14981) 

### 성능 요약

메모리: 119696 KB, 시간: 184 ms

### 분류

구현

### 제출 일자

2025년 3월 12일 05:14:18

### 문제 설명

<p>The game “Draw a forest picture” is quite popular among younger visitors of the amusement park. The number of players in the game is virtually unlimited and nearly everybody becomes a winner. The game is simple. At the beginning, a leader of the game describes briefly a picture of a forest which he or she had seen recently. Then the players are given some paper and crayons and they have to reproduce the image as best as they can. Everybody who hands in at least partial image of virtually any piece of any forest anywhere on Earth depicted in any style wins a small reward in the form of a chocolate or a fruit.</p>

<p>In this problem, you have to implement an imitation of the game. As you are much more experienced than the younger players, your drawing has to meet the specifications exactly. The image you have to reproduce depicts a glade — an open area within a woodland which is somewhat less populated by the trees than the surrounding thick forest. The image has to be printed in the “ascii-art” style.</p>

<p>An M × M image is represented by a canvas consisting of M rows, each row containing M characters. Each pixel in the image is represented by some printable ASCII character on the canvas. The coordinates of the pixels in the image correspond to the coordinates of the characters on the canvas. The coordinates of the pixels in the bottom left corner and in the top right corner of the image are (0, 0) and (M − 1, M − 1), respectively. The x-coordinate of the pixel in the bottom right corner of the image is M − 1.</p>

<p>Each pixel in the image depicts either grass or a part of a standing tree or a tree stump. A pixel depicting grass is represented by a single dot character (“.”, ASCII code 46) on the canvas. Standing trees and tree stumps are depicted by more pixels, their representation on the canvas follows.</p>

<p>A standing tree has a positive height S and it consists of four parts: The roots, the tree trunk, the branches, and the treetop. The roots are represented by three horizontally adjacent characters: underscore, vertical bar, underscore (“_|_”, ASCII codes 95, 124, 95). The tree trunk is represented by S vertically adjacent vertical bars (“|”, ASCII code 124) located immediately above the center of the tree roots. The branches consist of S left branches located immediately to the left of the tree trunk, and S right branches located immediately to the right of the tree trunk. Each branch is adjacent to the tree trunk. A left branch is represented by a single forward slash character (“/”, ASCII code 47), a right branch is represented by a single backslash character (“\”, ASCII code 92). A treetop is represented by a single caret character (“^”, ASCII code 94) located immediately above the topmost character of the tree trunk.</p>

<p>A tree stump consists of three horizontally adjacent pixels represented by characters underscore, lowercase letter “o”, underscore (“_o_”, ASCII codes 95, 111, 95).</p>

<p>Note that a standing tree or a tree stump may appear in the image only partially or may not appear in the image at all, depending on its coordinates. See the sample data below for additional illustration of this fact.</p>

### 입력 

 <p>There are more test cases. Each case starts with a line containing two integers M, N separated by space (1 ≤ M ≤ 100, 1 ≤ N ≤ 10<sup>5</sup>). Next, there are N lines, each line contains a triple of integers S, X, Y , separated by spaces, which describe one standing tree or one tree stump. The values of X and Y represent the coordinates of the center of either tree roots or a tree stump. In case of S = 0 the triple describes a stump. In case of S > 0 the triple describes a standing tree with height S. It holds 0 ≤ S ≤ 9, −10<sup>9</sup> ≤ X, Y ≤ 10<sup>9</sup>.</p>

<p>It is guaranteed that no parts of two different standing trees and/or tree stumps should be depicted by the same pixel.</p>

### 출력 

 <p>For each test case, print the canvas with the image of the glade. The top row of the canvas should be the first printed row of the image. The bottom row of the canvas should be the last printed row of the image. The printout should be decorated by a square border made of asterisk characters (“*”, ASCII code 42), the thickness of the border should be one pixel. The border should frame the canvas tightly, that is, there should be no spaces between the border and canvas neither horizontally nor vertically. Print one empty line after each case.</p>

