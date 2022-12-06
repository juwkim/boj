# [Bronze II] “Bubble Gum, Bubble Gum, in the dish, how many pieces do you wish?” - 4500 

[문제 링크](https://www.acmicpc.net/problem/4500) 

### 성능 요약

메모리: 28776 KB, 시간: 220 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Alex and Karyn were at it again. The elementary school sisters were playing their favorite game to decide who gets to play on the computer next.</p>

<p>The rules of the game are quite simple. Given p people (p > 0), one of the p people is chosen to pick a number n (n > p) representing the number of pieces of bubble gum desired. Once this<br>
value is chosen, the people are iterated through, one at a time, starting at 1, from “left” to “right”, starting with the person who chose the number. Iterating is done in a circular fashion, meaning that once the person on the far right is reached, the next person in the iteration will be the person on the far left. Upon reaching n, the person at that location is the winner.</p>

<p>Given a list of names, followed by the name of the person choosing the number of pieces of bubble gum, followed by the number that person chose, determine who wins the game.</p>

### 입력 

 <p>The first value in the input file will be an integer t (0 < t < 1000) representing the number of test cases in the input file. Following this, on a case by case basis, will be a list of the names of the people (p), on a single line. Names will be no larger than 20 characters in length and all names are unique. There will be no more than 20 names. Each name is followed by a space, save for the last name, which is followed by a newline. On the next line is the name of the person choosing the number of pieces of bubble gum, followed by a newline. The test case is concluded with the number of pieces of gum n (p < n < 1000), which is also followed by a newline.</p>

<p> </p>

### 출력 

 <p>For each test case, report the name of the person that won the game, followed by a newline.</p>

<p> </p>

