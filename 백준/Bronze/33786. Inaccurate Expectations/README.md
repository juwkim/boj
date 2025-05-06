# [Bronze I] Inaccurate Expectations - 33786 

[문제 링크](https://www.acmicpc.net/problem/33786) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

임의 정밀도 / 큰 수 연산, 수학, 재귀

### 제출 일자

2025년 5월 6일 16:02:04

### 문제 설명

<p>Jake is doing a lot of programming. Recently Jake has been working on an archiving tool, because organizing isn't one of his strengths. Jake learned that testing is an important part of programming. He needs to make some file generating tool, to make sure his archiving tool is not messing up. Jake has already created a simple generator to generate some folders and files, ready to use his archiving tool on. However the generator seems to take a very long time to finish, if it finishes at all.</p>

<p>It seems Jake has some inaccurate expectations of the effect of his generator. Can you help Jake figure out how many files his generating tool is actually creating, for the given input?</p>

<p>The generator $g(root, n)$ works as follows: in the root folder, $n$ files and $n$ folders are created. In each of those folders, $g(folder, n - 1)$ is used to generate the contents of that folder. Calling $g(folder, 0)$ does nothing, of course.</p>

### 입력 

 <p>A single integer n, $0 \leq n \leq 1000$</p>

### 출력 

 <p>A single integer, the number of files (not the folders) created by $g(root, n)$.</p>

