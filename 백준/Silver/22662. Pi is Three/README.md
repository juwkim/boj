# [Silver V] Pi is Three - 22662 

[문제 링크](https://www.acmicpc.net/problem/22662) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p><i>π</i> (spelled pi in English) is a mathematical constant representing the circumference of a circle whose di- ameter is one unit length. The name <i>π</i> is said to come from the first letter of the Greek words περιφέρεια (meaning periphery) and περίμετρος (perimeter).</p>

<p>Recently, the government of some country decided to allow use of 3, rather than 3.14, as the approximate value of π in school (although the decision was eventually withdrawn probably due to the blame of many people). This decision is very surprising, since this approximation is far less accurate than those obtained before the common era.</p>

<p>Ancient mathematicians tried to approximate the value of <i>π</i> without calculators. A typical method was to calculate the perimeter of inscribed and circumscribed regular polygons of the circle. For example, Archimedes (287–212 B.C.) proved that 223/71 < <i>π</i> < 22/7 using 96-sided polygons, where 223/71 and 22/7 were both accurate to two fractional digits (3.14). The resultant approximation would be more accurate as the number of vertices of the regular polygons increased.</p>

<p>As you see in the previous paragraph, <i>π</i> was approximated by fractions rather than decimal numbers in the older ages. In this problem, you are requested to represent <i>π</i> as a fraction with the smallest possible denominator such that the representing value is not different by more than the given allowed error. If more than one fraction meets this criterion, the fraction giving better approximation is preferred.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset has a real number <i>R</i> (0 < <i>R</i> ≤ 1) representing the allowed difference between the fraction and <i>π</i>. The value may have up to seven digits after the decimal point. The input is terminated by a line containing 0.0, which must not be processed.</p>

### 출력 

 <p>For each dataset, output the fraction which meets the criteria in a line. The numerator and denominator of the fraction should be separated by a slash as shown in the sample output, and those numbers must be integers.</p>

