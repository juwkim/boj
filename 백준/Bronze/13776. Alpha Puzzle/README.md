# [Bronze I] Alpha Puzzle - 13776 

[문제 링크](https://www.acmicpc.net/problem/13776) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>An alpha puzzle is a type of crossword puzzle where each letter square (ie one that is not black) contains a number to represent a letter. Throughout the puzzle, a particular letter is always represented by the same number. All letters of the alphabet are used, so numbers range from 1 to 26.</p>

<p>In this problem you will be given a solution to an alpha puzzle and have to assign numbers to the letters. Some alpha puzzles assign numbers to letters randomly, but the one that appears in the New Zealand Herald every day uses a non-random method which you have to implement.</p>

<p>The answer grid is read left to right, top to bottom; spaces (which represent black squares) are ignored. The first letter encountered is assigned the number 1, the next number 2 and so on. Only the first occurrence of a letter is processed, so only 26 numbers are allocated.</p>

### 입력 

 <p>You will be presented with a single puzzle solution which starts with a single integer, S, on a line by itself (10 <= S <=20). S is the size of the puzzle – the number of rows and columns of squares that it contains.</p>

<p>There will then follow S lines, each containing S characters, all upper case letters or spaces. Every letter of the alphabet will appear at least once. </p>

### 출력 

 <p>Follow the rules for letter allocation described above then output the 26 letters of the alphabet in their assigned numerical order so that, for example, the first letter is the one to which the number 1 is assigned, the last the one to which 26 was assigned. </p>

