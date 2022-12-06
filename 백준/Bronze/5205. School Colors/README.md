# [Bronze I] School Colors - 5205 

[문제 링크](https://www.acmicpc.net/problem/5205) 

### 성능 요약

메모리: 28776 KB, 시간: 208 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>You all know what our school colors are, right?<sup>1</sup> They may not be quite the prettiest combination, but at least you can read one written on top of the other quite well. Much better than, say, Cardinal and Red, or Green and Turquoise. One would imagine that universities do make some effort to select contrasting colors. But did they get the most contrasting ones?</p>

<p>Here, we’re going to write a program to find the most contrasting pair of colors among a given list. Each color is specified by a triple (\(R\), \(G\), \(B\)), denoting the red, green, and blue values. Each of these values will be an integer between 0 and 255. The triple (0, 0, 0) is the color Black, and (255, 255, 255) is White. When we want to know the contrast between two colors, for our purposes here, we just treat it as the Euclidean distance between the corresponding triples, i.e., for triples (\(R\), \(G\), \(B\)) and (\(R'\), \(G'\), \(B'\)), the contrast is \(\sqrt{(R - R')^2 + (G - G')^2 + (B - B')^2}\).</p>

<p><sup>1</sup>Hint: Cardinal and Gold</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of a data set contains a number n with 2 ≤ n ≤ 200, the number of colors in the data set. This is followed by n lines, each containing three numbers \(R_i\), \(G_i\), \(B_i\). These are the Red, Green, and Blue values of the ith color in the list.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the pair of colors having largest possible contrast. If there are multiple pairs achieving largest contrast, output all of them, sorted by increasing first index, breaking ties by increasing second index.</p>

