# [Silver IV] Brain fold (Easy) - 27640 

[문제 링크](https://www.acmicpc.net/problem/27640) 

### 성능 요약

메모리: 112408 KB, 시간: 268 ms

### 분류

사칙연산, 수학

### 제출 일자

2023년 12월 24일 03:55:15

### 문제 설명

<p>Shandyna loves nerd sniping. (<a href="https://xkcd.com/356/">Relevant xkcd.</a> Don’t worry, she only does it in safe enviroments.)</p>

<p>Last time she got five of them at once. When I saw them, they were still sitting around, trying to imagine a folded sheet of paper.</p>

<p>You have a rectangular piece of paper. You fold it in half several times. For each fold, you pick up one side and place it over the opposite side. There are four sides to pick, so there are four ways to perform each fold. (Two of the folds are horizontal and two are vertical.)</p>

<p>Once you finish the last fold, you pick a straight line and cut along it, through all layers of the folded paper. How many pieces of paper will you have at the end?</p>

### 입력 

 <p>The first line of the input file contains an integer <em>t</em> = 100 specifying the number of test cases. Each test case is preceded by a blank line.</p>

<p>Each test case consists of three lines.</p>

<p>The first line contains a number <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>5</sup>) denoting the number of folds.</p>

<p>The second line consists of <em>n</em> characters specifying the folds in the order they are applied: <code>T</code>, <code>B</code>, <code>L</code> and <code>R</code> represent folds for which you pick up the top, bottom, left, and right side, respectively. (Hence, <code>T</code> represents the fold that places the top side over the bottom side.)</p>

<p>The last line describes the cut. To make your life easier, the cut will never pass through a corner of the square. As it can be shown that the number of pieces does not depend on the exact points where the cut intersects the sides of the square, we can specify the cut simply by giving the labels of the two sides it intersects. For example, <code>TR</code> is a cut that intersects the top and the right side of the folded paper.</p>

<p>Each cut can be made horizontally or vertically. That is, the two letters that describe each cut are either <code>T</code>+<code>B</code> or <code>L</code>+<code>R</code>.</p>

### 출력 

 <p>For each test case, output a single line containing <em>x</em> modulo 10<sup>9</sup> + 7, where <em>x</em> is the number of paper pieces we’re left with after cutting the paper.</p>

