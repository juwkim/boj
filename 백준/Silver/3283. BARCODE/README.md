# [Silver II] BARCODE - 3283 

[문제 링크](https://www.acmicpc.net/problem/3283) 

### 성능 요약

메모리: 109412 KB, 시간: 84 ms

### 분류

애드 혹, 다이나믹 프로그래밍, 구현, 문자열

### 제출 일자

2025년 1월 9일 05:52:38

### 문제 설명

<p>To speed a work of cashiers, each product is marked with a series of black and white vertical bars called bar code. It can be transformed to a sequence of zeroes and ones with an optical reader. That sequence represents a code of a product.</p>

<p>Bar code consists of black and white vertical bars, which can be thin or thick. White and black bars alternate, i.e. no two adjacent bars are of the same color. Thin bar represent 0 and thick bar represent 1, regardless of its color. Thus a bar code represents a sequence of binary digits.</p>

<p>Each bar in a bar code on a product appears as five ‘squares’ high column (see the picture below). Width of a thin bar is one and of a thick bar are two ‘squares’. For example, bar code depicted below represents the sequence 010001.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/88bc75cd-216d-464e-a483-bf6ebb0125d2/-/preview/" style="width: 129px; height: 84px;"></p>

<p>Bar code reader used in this problem fell on a floor and since then was unable to properly recognize a color of some ‘squares’ of a bar code.</p>

<p>Write a program that will from a given scanning of a bar code with our faulty reader determine which sequence of binary digits it represents if it is possible.</p>

### 입력 

 <p>The first line of input file contains an integer N, 1 ≤ N ≤ 100, representing total width of scanned bar code.</p>

<p>Each of next five lines contains N characters, each of which can be ‘X’, ‘.’ (dot) or ‘?’ (question mark), where X represents successfully recognized black ‘square’, a dot represents successfully recognized white ‘square’ and question mark means that our reader didn’t determine the colour of the ‘square’.</p>

### 출력 

 <p>The first and only line of output file should contain a sequence of binary digits represented with bar code given in input file if it can be determined. If a sequence cannot be determined, word ‘UNDETERMINABLE’ should be written to the first line instead.</p>

