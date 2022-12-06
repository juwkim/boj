# [Silver V] Monkey Business - 22733 

[문제 링크](https://www.acmicpc.net/problem/22733) 

### 성능 요약

메모리: 115136 KB, 시간: 140 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>A technician has been training the monkeys used in the laboratory where she works to open and close doors. Next to the laboratory, there is a long hallway that contains a number of offices which initially have closed doors. The offices in the hallway are numbered starting at 1 and ending at N, where N is the number of offices in the hallway. Interestingly the number of monkeys in the laboratory is exactly equal to the number of doors in the hallway.</p>

<p>At night the technician lets the monkeys out of their cages one at a time for exercise. The first monkey that is let out of the cage runs down the hallway and opens every door (i.e., 1, 2, 3, 4, . . .). The second monkey runs down the hallway and closes all of the even numbered doors (i.e., 2, 4, 6, 8, . . .). The third monkey runs down the hallway and examines every third door (i.e., 3, 6, 9, 12, . . .). The monkey will open any closed door that it examines, and close any open door that it examines. The fourth monkey examines every fourth door, and so forth. This process continues until all of the monkeys have been let out of their cages and allowed to run down the hallway. The last monkey will only examine the last door.</p>

<p>It would be nice to know which doors are left open at the end of the night. For example, given a hallway that contains five doors (and five monkeys), doors 1 and 4 will be open after all the monkeys have been let out of their cages. The technician has decided to write a grant to fund this work and has asked you for help. She requires you to write a program that, given as input the number of doors in a hallway, shows the open doors after all of the monkeys have been let out of cages. As said above, there are as many monkeys as there are doors, and all of the doors are initially closed.</p>

### 입력 

 <p>The input consists from a series of test cases. Each test case consists of a single positive integer which specifies the number of doors in the hallway. The input is terminated by a single zero. This is not part of the input.</p>

### 출력 

 <p>For each test case, you should output a list of numbers that identify the doors that are open after all monkeys have been let out of their cages. The numbers in the list should be output one per line in increasing order.</p>

<p>You should output a blank line between two test cases.</p>

