# [Bronze I] Take Your Vitamins - 4749 

[문제 링크](https://www.acmicpc.net/problem/4749) 

### 성능 요약

메모리: 30840 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Manufacturers of food products are required to place nutrition information labels on their packages. A major part of this information is a listing of important vitamins and minerals, listing both the amount of the chemical present in one serving and the percentage of an adult’s minimum daily requirement for that chemical.</p>

<p>Write a program to help prepare these nutritional labels by computing that percentage from the information on the amount present in one serving and the amount constituting the minimum daily requirement.</p>

### 입력 

 <p>Input consists of one or more lines, each of the form:</p>

<p>A U R V</p>

<p>where A is the amount of a vitamin/mineral present in one serving of the food product, U is the units in which A is measured, R is the minimum daily requirement for that vitamin/mineral, measured in the same units as A, and V is the name of that vitamin/mineral.</p>

<p>A and R will be floating point numbers. U will be a string of alphabetic characters with no embedded spaces. V will be a string of characters, possibly including spaces. A, U, R, and V will be separated from one another by exactly one space, and V is terminated by the end of the input line.</p>

<p>End of the input is signaled by a line in which A is negative.</p>

### 출력 

 <p>For each line of input data, your program should determine the percentage of the recommended daily requirement being provided for that vitamin/mineral. If it is at least 1%, your program should print a line of the form</p>

<p>V A U P%</p>

<p>where V, A, and U are the quantities from the input, and P is the percentage of the minimum daily requirement represented by the amount A.</p>

<p>V should be printed left-justified on the line. A should be printed with 1 digit precision, and P with zero digits precision. V, A, U, and P should be separated by one space each.</p>

<p>After the last such line, your program should print a line stating</p>

<p>Provides no significant amount of:</p>

<p>followed by a list of the names of all vitamins/minerals which are provided as less than 1% of the minimum daily requirement. These should be printed one name per line, in the order they occurred within the input.</p>

