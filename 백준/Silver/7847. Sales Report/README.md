# [Silver IV] Sales Report - 7847 

[문제 링크](https://www.acmicpc.net/problem/7847) 

### 성능 요약

메모리: 148888 KB, 시간: 780 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 트리를 사용한 집합과 맵

### 문제 설명

<p>The Unknown Trading Company have installed a new inventory-tracking system, which stores a complete database of goods and trading points worldwide. Each salespoint and each item was assigned an integer unique identifier (id). For every sale, the system logs id of the item, number of items sold, and id of the salespoint.</p>

<p>Your task is to output a summary report, tabulating total sales by items and salespoints. The report must be a two-dimensional table, with the first row containing item ids in increasing order, first column containing salespoint ids in increasing order, and values inside the table representing total sales of corresponding item from the corresponding salespoint. The value in first column of the first row must be &minus;1. The values in cells without corresponding sales must be 0.</p>

### 입력 

 <p>Input contains number of records <i>N</i>, followed by <i>N</i> triplets of integers <i>q<sub>i</sub></i> <i>s<sub>i</sub></i> <i>v<sub>i</sub></i>, where <i>q<sub>i</sub></i> -- item id, <i>s<sub>i</sub></i> -- salespoint id, <i>v<sub>i</sub></i> -- number of items sold.</p>

### 출력 

 <p>Output file must a table as described above, row-by-row.</p>

