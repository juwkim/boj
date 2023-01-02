# [Silver IV] Dreary Design (Small) - 12175 

[문제 링크](https://www.acmicpc.net/problem/12175) 

### 성능 요약

메모리: 115416 KB, 시간: 172 ms

### 분류

브루트포스 알고리즘(bruteforcing), 조합론(combinatorics), 수학(math)

### 문제 설명

<p>One way to represent a color is as a triple of component values (each of which can range from 0 to <strong>K</strong>, inclusive) representing levels of red, green, and blue. For example, in the color system where <strong>K</strong> = 3, (0, 2, 3) and (0, 3, 2) would be two of the possible distinct colors.<br>
<br>
We will consider a color to be <em>bland</em> if and only if all pairs of its component values differ by no more than <strong>V</strong>. For example, in a system with <strong>K</strong> = 2 and <strong>V</strong> = 1, the color (2, 1, 1) is bland, because its red and green components differ by 1, its red and blue components differ by 1, and its green and blue components differ by 0, and none of these differences exceeds 1. But (2, 1, 0) is not bland, because the red and blue components differ by more than 1.<br>
<br>
Mr. Turner loves to create gloomy landscape images and wants to design a color system in which there are many bland colors available. Given values for <strong>K</strong> and <strong>V</strong>, can you tell him how many distinct bland colors are there?</p>

<h3>Solving this problem</h3>

<p>Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each contains two space-separated integers <strong>K</strong> and <strong>V</strong>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><strong>V</strong> ≤ <strong>K</strong>.</li>
	<li>0 ≤ <strong>K</strong> ≤ 255.</li>
	<li>0 ≤ <strong>V</strong> ≤ 100.</li>
	<li>All answers are guaranteed to fit in a 32-bit signed integer.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of distinct bland colors.</p>

