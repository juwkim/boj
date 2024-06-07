# [Silver III] Overflowing Bookshelf - 4621 

[문제 링크](https://www.acmicpc.net/problem/4621) 

### 성능 요약

메모리: 112004 KB, 시간: 140 ms

### 분류

자료 구조, 구현, 연결 리스트, 시뮬레이션

### 제출 일자

2024년 6월 7일 17:35:36

### 문제 설명

<p>Agnes C. Mulligan is a fanatical bibliophile – she is constantly buying new books, and trying to find space for those books. In particular, she has a shelf for her “to be read” books, where she puts her newest books. When she decides to read one of these books, she removes it from the shelf, making space for more books. Sometimes, however, she buys a new book and puts it on the shelf, but because of limited space, this pushes one or more books off the shelf at the other end. She always adds books on the left side of the shelf, making books fall off the right side. Of course, she can remove a book from any location on the shelf when she wants to read one. </p>

<p>Your task will be to write a simulator that will keep track of books added and removed from a shelf. At the end of the simulation, display the books remaining on the shelf, in order from left to right. Books in each simulation will be identified by a unique, positive integer, 0 < I ≤ 100. There are three types of events in the simulation:</p>

<ul>
	<li><code>Add</code>: A new book is pushed on the left end of the shelf, pushing other books to the right as needed. No book moves to the right unless it is pushed by an adjacent (touching) book on its left. Any book that is not entirely on the shelf falls off the right edge. No single book will ever be wider than the given shelf. No book that is currently on the shelf will be added again.</li>
	<li><code>Remove</code>: If the book is on the shelf, then the book is removed from the shelf, leaving a hole. If the book isn't on the shelf, the operation is ignored.</li>
	<li><code>End</code>: End the simulation for this case and print the contents of the shelf.</li>
</ul>

### 입력 

 <p>The input file will contain data for one or more simulations. The end of the input is signalled by a line containing -1. Each simulation will begin with the integer width of the shelf, s, 5 ≤ s ≤ 100, followed by a series of <code>add</code> and <code>remove</code> events. An <code>add</code> event is a single line beginning with an upper case 'A' followed by the book ID, followed by the integer width of the book, w, 0 < w ≤ s. A <code>remove</code> event is a single line beginning with an upper case 'R' followed by the the book ID. Finally, the <code>end</code> event is a line containing only a single upper case 'E'. Each number in an event is preceded by a single blank.</p>

### 출력 

 <p>For each simulation case, print a single line containing a label (as shown in the output sample), followed by the list of IDs of books remaining on the shelf, in order from left to right.</p>

