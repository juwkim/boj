# [Bronze II] Ultimate Binary Watch - 24578 

[문제 링크](https://www.acmicpc.net/problem/24578) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

비트마스킹(bitmask), 구현(implementation)

### 문제 설명

<p><img alt="" src="" style="width: 209px; height: 165px; float: right;">The Ultimate Binary Watch is a maker project that uses small LEDs to display time on a watch face. The display uses four columns of four LEDs each, with each column representing one digit of the current time in hours and minutes. Time is displayed in 24-hour format, with the 1st (left-most) column displaying the tens position for hours, the 2nd column displaying the ones position for hours, the 3rd column displaying the tens position for minutes, and the last (right-most) column displaying the ones position for minutes. The bottom LED of each column shows the lowest-order bit of its represented digit, with the bit positions increasing moving up the column. For example, the time 1615 would be displayed as shown in the figure.</p>

<p>Write a program that will take a 24-hour time and print the corresponding watch face.</p>

### 입력 

 <p>The input has a single line with 4 digits describing a valid 24-hour time between 0000 and 2359.</p>

### 출력 

 <p>Output four lines with a representation of the watch face displaying the given time. The tens of hours shall be in the 1st column, the single hours in the 3rd, the tens of minutes in the 7th, and the single minutes in the 9th. Use asterisks to represent bits that are set and periods to represent bits that are clear. Columns not used are to be filled with spaces. No extra whitespace are to appear at the beginning or end of any output line.</p>

