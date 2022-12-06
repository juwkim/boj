# [Silver V] Booklet Printing - 4670 

[문제 링크](https://www.acmicpc.net/problem/4670) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>When printing out a document, normally the first page is printed first, then the second, then the third, and so on until the end. However, when creating a fold-over booklet, the order of printing must be altered. A fold-over booklet has four pages per sheet, with two on the front and two on the back. When you stack all the sheets in order, then fold the booklet in half, the pages appear in the correct order as in a regular book. For example, a 4-page booklet would print on 1 sheet of paper: the front will contain page 4 then page 1, and the back will contain page 2 then page 3.</p>

<pre>Front              Back
-------------      -------------
|     |     |      |     |     |
|  4  |  1  |      |  2  |  3  |
|     |     |      |     |     |
-------------      -------------
</pre>

<p>Your task is to write a program that takes as input the number of pages to be printed, then generates the printing order.</p>

### 입력 

 <p>The input file contains one or more test cases, followed by a line containing the number 0 that indicates the end of the file. Each test case consists of a positive integer n on a line by itself, where n is the number of pages to be printed; n will not exceed 100.</p>

### 출력 

 <p>For each test case, output a report indicating which pages should be printed on each sheet, exactly as shown in the example. If the desired number of pages does not completely fill up a sheet, then print the word Blank in place of a number. If the front or back of a sheet is entirely blank, do not generate output for that side of the sheet. Output must be in ascending order by sheet, front first, then back.</p>

