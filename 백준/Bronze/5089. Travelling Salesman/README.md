# [Bronze I] Travelling Salesman - 5089 

[문제 링크](https://www.acmicpc.net/problem/5089) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Bob Smith has to tour New Zealand visiting his company's customers. His database churns out a list of the towns where each customer lives, but it has not been well programmed so may display a given town more than once. Your job is to help Bob by removing the duplicates and telling him how many towns he actually has to visit.</p>

### 입력 

 <p>Input consists of a number of lists, each representing a week of visits. The first line of each week is a single integer, N (1 < N <= 100), which is the number of towns in the list. Input is terminated by N = 0 – this week should not be processed.</p>

<p>Each week contains a list of N towns, each on a line by itself. The name of a town may contain more than one word. The first letter of each word in a town's name begins with an upper case letter; all other letters are lower case. A town's name will contain no more than 20 characters.</p>

### 출력 

 <p>Output consists of a single line for each week. It contains the word Week, followed by a space, followed by the week number, the first week being 1, followed by a space, followed by the actual number of towns to be visited, duplicates having been removed.</p>

