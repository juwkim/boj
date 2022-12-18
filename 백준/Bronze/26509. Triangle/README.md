# [Bronze III] Triangle - 26509 

[문제 링크](https://www.acmicpc.net/problem/26509) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

기하학(geometry), 수학(math), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Determine if it is possible to produce two triangles of given side lengths, by cutting some rectangle with a single line segment, and freely rotating and flipping the resulting pieces.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 114px; height: 108px;"></p>

<p>Hint: The Pythagorean Theorem states that for any right triangle a<sup>2</sup>+b<sup>2</sup>=c<sup>2</sup>, where c is the length of the hypotenuse and a and b are the lengths of the remaining sides.</p>

### 입력 

 <p>The first line of input contains a positive integer n, indicating the number of problem sets. Each problem set consists of two lines. The first line contains three space-separated positive integers, indicating the desired side lengths of the first triangle. Similarly, the second line contains three space-separated positive integers, denoting the desired side lengths of the second triangle. It is not guaranteed that the side lengths produce valid right triangle. All side lengths are less than or equal to 100.</p>

### 출력 

 <p>For each problem set print, on a single line, whether there exists a rectangle which could have been cut to form triangles of the given side lengths. If such a rectangle exists, print YES. Otherwise, print NO.</p>

