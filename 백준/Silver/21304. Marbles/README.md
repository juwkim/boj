# [Silver I] Marbles - 21304 

[문제 링크](https://www.acmicpc.net/problem/21304) 

### 성능 요약

메모리: 109544 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘, 수학, 확률론

### 제출 일자

2025년 5월 6일 02:28:49

### 문제 설명

<p>For a booth at the campus spring carnival, Toni wants to have players draw two marbles from a bowl of red and green marbles. Players go on to the next level of the game if one marble is red and one is green.</p>

<p>Toni wants to be able to choose the exact probability of drawing one red and one green marble. She wants enough marbles in the bowl to make it hard to guess the probability, but she needs to be able to limit the maximum number of marbles since her bowl is only so big.</p>

<p>Write a program to find out how many red and how many green marbles to put in the bowl.</p>

### 입력 

 <p>Input consists of a single line containing four space separated decimal integers: <strong><em>p</em></strong>, <strong><em>q</em></strong>, <strong><em>N</em></strong> and <strong><em>M</em></strong>. You are to find the number of red marbles (<strong><em>r</em></strong>) and green (<strong><em>g</em></strong>) marbles so that <strong><em>r</em></strong> ≤ <strong><em>g</em></strong>, <strong><em>N</em></strong> ≤ (<strong><em>r</em></strong>+<strong><em>g</em></strong>) ≤ <strong><em>M</em></strong> ≤ 1000, 2 ≤ <strong><em>N</em></strong> ≤ 1000 and (<strong><em>r</em></strong>+<strong><em>g</em></strong>) is the smallest sum ≥ <strong><em>N</em></strong>. In addition, the probability of drawing one red marble and one green marble (not necessarily in that order) when drawing exactly two marbles at random from the bowl is <em>exactly</em> <strong><em>p</em></strong>/<strong><em>q</em></strong>. <strong><em>q</em></strong> > 0, GCD(<strong><em>p</em></strong>, <strong><em>q</em></strong>) will always be <strong>1</strong>. If no solution exists that meet Toni’s requirements, then print out <code>NO SOLUTION</code>.</p>

### 출력 

 <p>The single output line consists of two space separated decimal integers <strong><em>r</em></strong> followed by <strong><em>g</em></strong> or the words <code>NO SOLUTION</code> if no solution exists for the supplied input.</p>

