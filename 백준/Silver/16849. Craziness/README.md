# [Silver I] Craziness - 16849 

[문제 링크](https://www.acmicpc.net/problem/16849) 

### 성능 요약

메모리: 112016 KB, 시간: 4312 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 6월 19일 04:32:09

### 문제 설명

<p>When you ask anyone about their family after a major gathering (e.g., for any kind of holidays), they will typically tell you how crazy their family is.<sup>1</sup> Somehow, years of knowing each other — and probably genetic similarity — mean that family members know exactly how to egg each other on or exasperate each other. Somehow, when put in the same room, a group of normal quiet people suddenly become insanely wild. Here, you will calculate which family members to invite to maximize the total craziness.</p>

<p>For each pair of family members i, j, you will be given a (positive or negative) number c<sub>i,j</sub>, which is how much craziness this pair will contribute if both are invited; negative numbers mean that this pair will actually calm things down. The goal is to find the non-empty (i.e., at least one person must be invited) subset to invite to achieve maximum total craziness, which is the sum of crazinesses over all pairs of invited family members, plus the individual crazinesses of all guests.</p>

<p><sup>1</sup>If you asked salmon why they swim up rivers for weeks, they’d probably tell you: “I can’t miss that party — my salmon family is crazy, man!!!”</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of a data set contains the number 2 ≤ n ≤ 20 of relatives to choose from. This is followed by n lines, each with n doubles −1000.0 ≤ c<sub>i,j</sub> ≤ 1000.0. c<sub>i,j</sub> is the craziness added when you invite both i and j. We promise you that c<sub>i,j</sub> = c<sub>j,i</sub> for all i and j. c<sub>i,i</sub> is the craziness that person i himself/herself contributes.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the maximum total craziness you can get by inviting a non-empty subset of these relatives, rounded to two decimals.</p>

