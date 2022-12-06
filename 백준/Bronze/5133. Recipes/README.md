# [Bronze I] Recipes - 5133 

[문제 링크](https://www.acmicpc.net/problem/5133) 

### 성능 요약

메모리: 32952 KB, 시간: 76 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>A little-known fact about Richard Stallman is that he not only loves to share his source code, but also his recipes. Due to this sharing process, he often needs to adjust a recipe to feed extra programmers. To accommodate, he multiplies the amount of each ingredient in the recipe by some constant factor. Of late, Stallman has gotten tired of carrying out this computation by hand, and has made a few mistakes as there are fractions involved. Hungry programmers get upset when his food is bad, and Stallman gets upset when his programming friends don’t like his food, not to mention when they start losing focus and breaking the build due to their hunger pangs. Your task is to prevent this by writing a program to automate the recipe conversion process.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each one a recipe of the following form:</p>

<p>The first line contains two integers I and C, the number of ingredients in the recipe and the constant which Stallman would like to multiply by, respectively. This is followed by I lines, one for each ingredient, where each line contains three integers w, n, and d, describing the amount of the ingredient in the original recipe. The first number, w, is the number of whole units of the ingredient. For example, if we’re talking about flour, w = 2 indicates that 2 cups are needed. The next two numbers, n and d, represent the fractional portion of the ingredient. Again in the case of flour, n = 1 and d = 4 indicates we need 1/4 cup. Note that while w and n are separated by white space, n and d are separated by a single slash. In Stallman’s recipes, the possible values of d are limited to 1, 2, 3, 4, and 8.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next I lines, output the new amount of each ingredient. If there is no fractional portion, the new amount is a single integer. If there is a fractional portion, it should be in reduced form and separated from the whole units by a single space. Each data set should be followed by a blank line.</p>

