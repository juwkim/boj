# [Bronze I] Date bugs - 6335 

[문제 링크](https://www.acmicpc.net/problem/6335) 

### 성능 요약

메모리: 30840 KB, 시간: 144 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>There are rumors that there are a lot of computers having a problem with the year 2000. As they use only two digits to represent the year, the date will suddenly turn from 1999 to 1900. In fact, there are also many other, similar problems. On some systems, a 32-bit integer is used to store the number of seconds that have elapsed since a certain fixed date. In this way, when 2<sup>32</sup> seconds (about 136 Years) have elapsed, the date will jump back to whatever the fixed date is. </p>

<p>Now, what can you do about all that mess? Imagine you have two computers C<sub>1</sub> and C<sub>2</sub> with two different bugs: One with the ordinary Y2K-Bug (i. e. switching to a<sub>1</sub> := 1900 instead of b<sub>1</sub> := 2000) and one switching to a<sub>2</sub> := 1904 instead of b<sub>2</sub> := 2040. Imagine that the C<sub>1</sub> displays the year y<sub>1</sub> := 1941 and C<sub>2</sub> the year y<sub>2</sub> := 2005. Then you know the following (assuming that there are no other bugs): the real year can't be 1941, since, then, both computers would show the (same) right date. If the year would be 2005, y<sub>1</sub> would be 1905, so this is impossible, too. Looking only at C<sub>1</sub> , we know that the real year is one of the following: 1941, 2041, 2141, etc. We now can calculate what C<sub>2</sub> would display in these years: 1941, 1905, 2005, etc. So in fact, it is possible that the actual year is 2141. </p>

<p>To calculate all this manually is a lot of work. (And you don't really want to do it each time you forgot the actual year.) So, your task is to write a program which does the calculation for you: find the first possible real year, knowing what some other computers say (y<sub>i</sub>) and knowing their bugs (switching to a<sub>i</sub> instead of b<sub>i</sub> ). Note that the year a<sub>i</sub> is definitely not after the year the computer was built. Since the actual year can't be before the year the computers were built, the year your program is looking for can't be before any a<sub>i</sub> .</p>

### 입력 

 <p>The input file contains several test cases, in which the actual year has to be calculated. The description of each case starts with a line containing an integer n (1 ≤ n ≤ 20), the number of computers. Then, there is one line containing three integers y<sub>i</sub>,a<sub>i</sub>,b<sub>i</sub> for each computer (0 ≤ a<sub>i</sub> ≤ y<sub>i</sub> < b<sub>i</sub> < 10000). y<sub>i</sub> is the year the computer displays, b<sub>i</sub> is the year in which the bug happens (i. e. the first year which can't be displayed by this computer) and a<sub>i</sub> is the year that the computer displays instead of b<sub>i</sub>. </p>

<p>The input is terminated by a test case with n = 0. It should not be processed.</p>

### 출력 

 <p>For each test case, output output the line "Case #k:", where k is the number of the situation. Then, output the line "The actual year is z.", where z is the smallest possible year (satisfying all computers and being greater or equal to u). If there is no such year less than 10000, output "Unkown bugs detected.".</p>

<p>Output a blank line after each case.</p>

