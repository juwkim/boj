# [Silver II] Rummy Score - 26345 

[문제 링크](https://www.acmicpc.net/problem/26345) 

### 성능 요약

메모리: 111408 KB, 시간: 148 ms

### 분류

백트래킹

### 제출 일자

2025년 3월 30일 12:32:10

### 문제 설명

<p>Mack and Zack (Dr. Orooji’s twins) play Rummy with a modified deck of playing cards. The card values are 1 through 13 (1 does not serve the dual purpose of 1 and 14; it is only 1) and there are no suits. Also, a deck may contain any number of each card value (unlike a standard deck of cards which has exactly four of each).</p>

<p>Given the seven cards in a Rummy hand (held by Mack or Zack), you are to determine the points lost by the hand. In Rummy, you group three (or more) cards together if they have the same value or they have consecutive values. Examples of a group include {4, 4, 4}, {6, 6, 6, 6, 6}, {9, 10, 11}, and {1, 2, 3, 4}. The “points lost by a hand” is the sum of values for cards that are not in a group.</p>

<p>When computing the points lost by a hand, you group the cards to minimize the loss, i.e., you want the smallest total sum of values for the ungrouped cards. Note that a given card could possibly belong to more than one group; you need to pick the group that minimizes the total points lost. For example, given the seven cards {2, 2, 2, 3, 4, 8, 10}, the grouping {2, 3, 4} is better than the grouping {2, 2, 2}. Note also that a card can be used in only one group, e.g., from the Rummy hand {2, 2, 2, 3, 4, 8, 10}, we can not create the two groups {2, 2, 2} and {2, 3, 4} since there are not a total of four cards with a value of 2 in the hand.</p>

### 입력 

 <p>The first input line contains only a positive integer, n, indicating the number of Rummy hands. The hands are on the following n input lines, one set per line. Each set contains seven integers, each integer between 1 and 13, inclusive (the values are separated by a single space).</p>

### 출력 

 <p>At the beginning of each test case, output “Rummy Hand: v” where v is the input values. Then, on the next output line, print the points lost by the hand. Leave a blank line after the output for each test case. Follow the format illustrated in Sample Output.</p>

