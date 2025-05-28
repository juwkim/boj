# [Silver I] Biomedical Engineering - 5188 

[문제 링크](https://www.acmicpc.net/problem/5188) 

### 성능 요약

메모리: 109544 KB, 시간: 120 ms

### 분류

다이나믹 프로그래밍, 문자열

### 제출 일자

2025년 5월 28일 15:48:37

### 문제 설명

<p>Biomedical Engineering tries to use biological phenomena to engineer drugs or other substances at a very small scale. It is a very promising technology. In designing new drugs, an important aspect is to design them such that they will be able to attach to the right receptor cells in the body, where they cause or inhibit certain reactions. While the underlying biology can be very complex, we can look at the following very simplified view.</p>

<p>The docking site can be described as a string z with n letters, describing the chemical properties at the n consecutive locations. We want to assemble a matching string from given primitive components, so that it will attach at the site. In our simplified view, we have m strings yi, where yi consists of ni letters. The goal is to select a sequence of these strings yi such that their concatenation is exactly equal to z. We assume that we have an unlimited supply of the biological substances described by the yi, so we can use arbitrarily many copies of the same yi in our assembly.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of a data set contains the number m of strings available for assembly, between 1 and 100. The second line is the string z, which will be between 1 and 1000 characters long, consisting only of uppercase and lowercase letters.</p>

<p>This is followed by m lines, each giving one string yi. Each string yi will be between 1 and 1000 characters long, consisting only of uppercase and lowercase letters.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the minimum number of segments which can be used to assemble z. If the assembly is impossible, then output “Impossible” instead.</p>

