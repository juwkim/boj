# [Silver II] Calender Colors - 22504 

[문제 링크](https://www.acmicpc.net/problem/22504) 

### 성능 요약

메모리: 115240 KB, 시간: 304 ms

### 분류

브루트포스 알고리즘, 백트래킹

### 제출 일자

2025년 6월 15일 02:42:14

### 문제 설명

<p>Taro is a member of a programming contest circle. In this circle, the members manage their schedules in the system called <i>Great Web Calender</i>.</p>

<p>Taro has just added some of his friends to his calendar so that he can browse their schedule on his calendar. Then he noticed that the system currently displays all the schedules in only one color, mixing the schedules for all his friends. This is difficult to manage because it's hard to tell whose schedule each entry is.</p>

<p>But actually this calender system has the feature to change the color of schedule entries, based on the person who has the entries. So Taro wants to use that feature to distinguish their plans by color.</p>

<p>Given the colors Taro can use and the number of members, your task is to calculate the subset of colors to color all schedule entries. The colors are given by "Lab color space".</p>

<p>In Lab color space, the distance between two colors is defined by the square sum of the difference of each element. Taro has to pick up the subset of colors that maximizes the sum of distances of all color pairs in the set.</p>

### 입력 

 <p>The input is like the following style.</p>

<pre><var><i>N</i></var> <var><i>M</i></var>
<var><i>L</i><sub>0</sub></var> <var><i>a</i><sub>0</sub></var> <var><i>b</i><sub>0</sub></var>
<var><i>L</i><sub>1</sub></var> <var><i>a</i><sub>1</sub></var> <var><i>b</i><sub>1</sub></var>
<var>…</var>
<var><i>L</i><sub><i>N</i>−1</sub></var> <var><i>a</i><sub><i>N</i>−1</sub></var> <var><i>b</i><sub><i>N</i>−1</sub></var></pre>

<p>The first line contains two integers <var><i>N</i></var> and <var><i>M</i></var> (<var>0≤<i>M</i>≤<i>N</i>≤20</var>), where <var><i>N</i></var> is the number of colors in the input, and <var><i>M</i></var> is the number of friends Taro wants to select the colors for. Each of the following <var><i>N</i></var> lines contains three decimal integers <var><i>L</i></var>(<var>0.0≤<i>L</i>≤100.0</var>), <var><i>a</i></var>(<var>−134.0≤<i>a</i>≤220.0</var>) and <var><i>b</i></var>(<var>−140.0≤<i>b</i>≤122.0</var>) which represents a single color in Lab color space.</p>

### 출력 

 <p>Output the maximal of the total distance. The output should not contain an error greater than <var>10<sup>−5</sup></var>.</p>

