# [Bronze III] Superlatives - 6162 

[문제 링크](https://www.acmicpc.net/problem/6162) 

### 성능 요약

메모리: 30888 KB, 시간: 72 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Typically, droughts are classified into “abnormally dry”, “moderate drought”, “severe drought”, “extreme drought”, and “exceptional drought”. The current drought is so “exceptional” in most of California that there have been discussions of adding one or more steps to the scale. But really, that will only delay the problem. Any system of discrete labels is not completely scalable. As computer scientists, you know that the answer is to build a naming system that allows you to just add more and more syllables. So how about “mega drought”, “mega mega drought”, “mega mega mega drought”, and so on? You can extend it arbitrarily. Here, you’ll write a program that finds the right number of “mega” to add.</p>

<p>You will be given two numbers: the amount of rain that was expected, and the amount of rain that actually occurred. If the former is less than the latter, we have no drought. If the expected rain is more than the actual rain, but not by a factor of more than 5, we just have a “drought”. If the expected rain is more by a factor of strictly more than 5, but not by a factor of more than 25, we have a “mega drought”. If it is more by a factor of strictly more than 25, but not by a factor more than 125, we have a “mega mega drought”. And so on — for each factor of 5, you add another “mega”.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>Each data set has two integer numbers 0 ≤ E, A ≤ 1, 000, 000, with A > 0, the expected and actual amount of rain.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then output a string describing the type of drought that is going on (“no drought”, “drought”, “mega drought”, “mega mega drought”, etc.).</p>

<p>Each data set should be followed by a blank line.</p>

