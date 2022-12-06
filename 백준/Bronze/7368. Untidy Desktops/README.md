# [Bronze I] Untidy Desktops - 7368 

[문제 링크](https://www.acmicpc.net/problem/7368) 

### 성능 요약

메모리: 116544 KB, 시간: 276 ms

### 분류

기하학(geometry), 구현(implementation), 수학(math)

### 문제 설명

<p>Many companies are moving towards "paperless offices" in an attempt to increase productivity. Unfortunately, people who are unorganized with papers are unorganized without papers too! Instead of having piles of paper scattered all over a desk, people have windows overlapping and covering one another. For these people, finding the right window on the computer screen is just as hard as finding the right piece of paper on the desk.</p>

<p>For this problem, you will be given the locations and sizes of n windows on a computer desktop (1 ≤ n ≤ 50). You have been asked to evaluate how untidy the computer desktop is by counting the number of windows that overlap with at least one other window. Two windows overlap if at least one pixel is in both windows (including the boundary of the windows).</p>

### 입력 

 <p>The input will consist of multiple cases. Each case will start with a line containing a single integer n. This will be followed by n lines of the form</p>

<p>r c w h</p>

<p>where r, c are the row and column coordinates of the upper left corner of the window, and w, h are the width and height of the window. You may assume that the upper left corner of the computer desktop has coordinates (0, 0), the screen has 1024 rows and 1280 columns, and all windows are completely within the boundary of the screen. A value of n = 0 will terminate the input.</p>

### 출력 

 <p>For each test case, print on a single line the number of windows that overlap with at least one other window.</p>

<p> </p>

