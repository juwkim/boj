# [Bronze II] Civil Engineering - 5187 

[문제 링크](https://www.acmicpc.net/problem/5187) 

### 성능 요약

메모리: 30840 KB, 시간: 112 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Civil Engineering is concerned with how to build things so that they don’t collapse (whereas architects care more about how things look). Such “things” would include buildings in an earthquake-prone area like LA, or dams in a hurricane-prone area like Louisiana. Here, we will look at a simple problem related to building construction. Suppose that you want to put a building on top of an area, but have a limit on the total weight of your building. Evaluating whether a proposed construction exceeds that weight can be quite a chore. So we are asking you to write a program to take care of that chore for civil engineers.</p>

<p>The input will describe a collection of oblongs (i.e., rectangular 3-dimensional blocks) which are supposed to be assembled to give the building. Each oblong comes with information about its dimensions (height, width, depth), as well as the the material it is made from. In addition, you have, for each material, the density (weight per volume). You are supposed to find out the total weight of all oblongs.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of a data set contains two numbers m, n between 1 and 10000. m is the number of materials in your database, and n is the number of oblongs in the building.</p>

<p>This is followed by m lines, each giving the density of one material (this is a non-negative integer number), in grams per cubic centimeter.</p>

<p>Next are n lines, each with four numbers h, w, d,i, where h, w, d are the height, width, and depth of the oblong (in centimeters), and i is the index of the material. h, w, d will be non-negative integers, and i an integer between 1 and m.</p>

<p>We will guarantee that for all inputs, the total weight will not exceed the maximum number you can store in a 32-bit integer.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the total weight of the oblongs in grams.</p>

