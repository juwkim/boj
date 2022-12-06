# [Bronze II] Library Codes - 7599 

[문제 링크](https://www.acmicpc.net/problem/7599) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>A local library is redoing its book labels with the Dewey Decimal classification. Where possible, labels are printed horizontally, but if they are too wide, they are printed vertically. A fixed pitch font is used, so all characters are the same width. To make the labels readable, a 1mm gap must be left before and after the number.</p>

<p>Given the width of a book in mm, the width of a character of the font and the text of the label, it is easy to decide if the label could be displayed horizontally or if it would have to be displayed vertically. </p>

### 입력 

 <p>Input consists of data about a number of libraries. The final line contains # 0 (separated by a space) – this line should not be processed.</p>

<p>For a library, the first line of input will be the name of the library (up to 20 letters only, no spaces), followed by a single positive integer, f, which is the width in mm of a single character in the font used by the library. 1 < f < 8. The next line contains a single integer, c, the number of books to be processed. There then follows c lines, each containing data about 1 book. Each line contains a positive integer, w, the width of the book in mm (5 <= w <=50), and the text to be displayed on the label. The text will contain between 3 and 6 characters. </p>

### 출력 

 <p>Output for each library begins with the name of the library on a single line, followed by 1 line for every book listed in the input. Each book will begin with "Book n", where n is the number of the book in the library's list, the first book being 1, followed with either the word horizontal, or the word vertical according to how the book is to be displayed. </p>

