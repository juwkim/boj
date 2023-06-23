# [Bronze I] Boxes - 6846 

[문제 링크](https://www.acmicpc.net/problem/6846) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘

### 문제 설명

<p>Nowadays, almost any item can be bought and sold on the internet. The problem is shipping. Before an item can be sent, it must be carefully packaged in a cardboard box to protect it.</p>

<p>While items come in many shapes and sizes, finding a box just the right size can be a problem. If the box is too small, the item will not fit. If the box is unnecessarily big, shipping cost will be higher, and the item is more likely to move around inside the box, and it may break.</p>

<p>Cardboard box manufacturers offer a fixed set of standard box sizes. Your task is to find the standard box size with the smallest volume into which an item will fit.</p>

<p>Each box is a rectangular prism with a given length, width, and height. Each item is also a rectangular prism with a given length, width, and height. An item may be rotated by multiples of 90 degrees in any direction before being packed into a box, but when it is packed, its faces must be parallel to the faces of the box. An item will fit into a box as long as its dimensions are equal to or less than the dimensions of the box.</p>

### 입력 

 <p>The first line of input will contain a single integer n, 0 < n < 1000, the number of different sizes of boxes available. The next n lines will contain three integers each, giving the length, width, and height of a box. The following line will contain a single integer m, 0 < m < 1000, the number of items to be packaged. The next m lines will contain three integers each, giving the length, width, and height of an item. All dimensions will be in millimetres and in the range from 1 mm to 2000 mm.</p>

### 출력 

 <p>Output is to consist of m lines, one for each item in the input. For each item, output a line containing a single integer, the volume (in mm<sup>3</sup>) of the smallest box into which the item will fit. The same size of box may be reused for any number of items. If an item does not fit in any box, print the line: <code>Item does not fit.</code></p>

