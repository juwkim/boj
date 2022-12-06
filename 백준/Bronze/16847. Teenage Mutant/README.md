# [Bronze II] Teenage Mutant - 16847 

[문제 링크](https://www.acmicpc.net/problem/16847) 

### 성능 요약

메모리: 30840 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 문자열(string)

### 문제 설명

<p>In common parlance, a “mutant” is an individual with a very unusual deformity, or — for some superheros — power. To biologists, it simply describes an accidental change in genetic information from a parent to a child. Telling mutation from inheritance is complicated a bit by the fact that some genetic traits are recessive, and may not be expressed for a generation, but then be visible later. Thus, to see whether a trait is really a mutation, you might have to go some generations back.</p>

<p>That’s what you’ll do here. You will get expressed traits for yourself and a number of your ancestors, described as strings of length n. A trait is a “mutant trait” if your value in that position is different from that of all your ancestors. You are to compute what fraction of your traits are mutant traits, i.e., how much of a mutant you are.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains two integers n, k, with 1 ≤ n ≤ 100, 1 ≤ k ≤ 100. This is followed by n + 1 lines of exactly k uppercase letters each. The first of those n + 1 lines is a description of your traits, and the remaining n lines each give you the string for one of your ancestors.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then, output the fraction of traits in which you are a mutant. Do not reduce the fraction; for example, if you are a mutant in two out of ten traits, write “2/10”, not “1/5” or “0.2”.</p>

<p>Each data set should be followed by a blank line.</p>

