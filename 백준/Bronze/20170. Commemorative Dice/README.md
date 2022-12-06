# [Bronze I] Commemorative Dice - 20170 

[문제 링크](https://www.acmicpc.net/problem/20170) 

### 성능 요약

메모리: 30888 KB, 시간: 76 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 확률론(probability)

### 문제 설명

<p>Since the year 2000, an ICPC regional contest has been held every year in Korea. To commemorate the 21st regional contest this year, it is decided to make a dice. The commemorative dice is a regular cube with a positive number written on each of its sides like an ordinary dice; however, the six numbers are not necessarily to be 1, 2, 3, 4, 5, 6 but just their sum is 21.</p>

<p>The dice can be used in various ways. For example, two people can play a game as follows: Each of the two picks one out of the many dice and then rolls the dice. The winner is the one who tosses a bigger number. It is important which dice to choose in this game because once the dice are set, the probability of one winning against the other is determined. Suppose that KyungYong chooses the dice shown in the figure below left and TaeCheon chooses the dice shown in the figure below right. Then, KyungYong wins when and only when TaeCheon tosses number 1, so the probability that KyungYong wins is 2/3.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 351px; height: 131px;"></p>

<p>Given the dice of the first and second players, write a program to calculate the probability of the first player winning.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of two lines. The first line contains six positive integers that are written on the sides of the dice of the first player. Also, the second line contains six positive integers that are written on the sides of the dice of the second player. The six integers given in a line add up to 21 and are separated by a single space.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line that contains an irreducible fraction representing the probability of the first player winning. A fraction should consist of a numerator displayed before a slash and a non-zero denominator displayed after the slash. There are no spaces either before or after the slash. Note that an irreducible fraction refers to a fraction in which the numerator and denominator are integers that have no other common divisors than 1.</p>

