# [Bronze I] Cardinal Adjacencies - 21309 

[문제 링크](https://www.acmicpc.net/problem/21309) 

### 성능 요약

메모리: 37812 KB, 시간: 1288 ms

### 분류

구현(implementation)

### 문제 설명

<p>In landscape ecology, one is interested in the <em>connectedness</em> of regions, particularly near shorelines. A fine grid is overlaid on a map or aerial photo and grid squares with land are marked:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 220px; height: 218px;"></p>

<p>Land squares which share an <strong>edge</strong> are <em>cardinal</em> (North, East, South and West) <em>adjacent</em> (blue lines in the image) and land squares which share an <strong>edge</strong> <em>or</em> a <strong>vertex</strong> (red <em>and</em> blue lines in the image) are <em>intercardinal adjacent</em>. Write a program which takes as input a marked grid and outputs the total <em>cardinal adjacencies</em> in the grid and the total number of <em>intercardinal</em> adjacencies in the grid.</p>

### 입력 

 <p>The input consists of multiple lines. The first line of input contains two space separated decimal integers <em><strong>nrows</strong></em> and <em><strong>ncolumns</strong></em>, (0 < <em><strong>nrows</strong></em>, <em><strong>ncolumns</strong></em> ≤ 1000). This line is followed by <em><strong>nrows</strong></em> additional lines of input each of which contains <em><strong>mcolumns</strong></em> space separated values of 0 or 1. 1 indicates land.</p>

### 출력 

 <p>There is one line of output containing two space separated decimal integers: the number of <em>cardinal adjacencies</em> followed by the number of <em>intercardinal adjacencies</em>.</p>

