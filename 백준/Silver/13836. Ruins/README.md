# [Silver V] Ruins - 13836 

[문제 링크](https://www.acmicpc.net/problem/13836) 

### 성능 요약

메모리: 115904 KB, 시간: 264 ms

### 분류

수학

### 문제 설명

<p>In 1936, a dictator Hiedler who aimed at world domination had a deep obsession with the Lost Ark. A person with this ark would gain mystic power according to legend. To break the ambition of the dictator, ACM (the Alliance of Crusaders against Mazis) entrusted a secret task to an archeologist Indiana Johns. Indiana stepped into a vast and harsh desert to find the ark.</p>

<p>Indiana finally found an underground treasure house at a ruin in the desert. The treasure house seems storing the ark. However, the door to the treasure house has a special lock, and it is not easy to open the door.</p>

<p>To open the door, he should solve a problem raised by two positive integers a and b inscribed on the door. The problem requires him to find the minimum sum of squares of differences for all pairs of two integers adjacent in a sorted sequence that contains four positive integers a<sub>1</sub>, a<sub>2</sub>, b<sub>1</sub> and b<sub>2</sub> such that a = a<sub>1</sub>a<sub>2</sub> and b = b<sub>1</sub>b<sub>2</sub>. Note that these four integers does not need to be different. For instance, suppose 33 and 40 are inscribed on the door, he would have a sequence <3, 5, 8, 11> as 33 and 40 can be decomposed into 3 × 11 and 5 × 8 respectively. This sequence gives the sum (5 − 3)<sup>2</sup> + (8 − 5)<sup>2</sup> + (11 − 8)<sup>2</sup> = 22, which is the smallest sum among all possible sorted sequences. This example is included as the first data set in the sample input.</p>

<p>Once Indiana fails to give the correct solution, he will suffer a calamity by a curse. On the other hand, he needs to solve the problem as soon as possible, since many pawns under Hiedler are also searching for the ark, and they might find the same treasure house. He will be immediately killed if this situation happens. So he decided to solve the problem by your computer program. Your task is to write a program to solve the problem presented above.</p>

### 입력 

 <p>The input consists of a series of data sets. Each data set is given by a line that contains two positive integers not greater than 10,000.</p>

<p>The end of the input is represented by a pair of zeros, which should not be processed.</p>

### 출력 

 <p>For each data set, print a single integer that represents the minimum square sum in a line. No extra space or text should appear.</p>

