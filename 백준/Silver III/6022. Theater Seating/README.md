# [Silver III] Theater Seating - 6022 

[문제 링크](https://www.acmicpc.net/problem/6022) 

### 성능 요약

메모리: 110752 KB, 시간: 132 ms

### 분류

기하학, 구현, 피타고라스 정리, 정렬

### 제출 일자

2024년 2월 15일 05:16:09

### 문제 설명

<p>The cows have built an amphitheater with seats in the form of a rectangle with *odd* width W (11 <= W <= 101) and with R rows (4 <= R <= 50) of seats. The distance between two adjacent seats on the same row is the same as the distance between a pair of seats that are in front of/behind each other on adjacent rows.</p>

<p>The cows wish to sell tickets over the internet and have automatic seating assignment for each ticket they sell.</p>

<p>Ticket purchasers always want the best seat, so every seat has a unique 'priority' associated with it (even if some seats might appear to the layman to have the same priority). The middle seat of the first row (which is closest to the stage) is located at 1,(W+1)/2 and has the very best priority. The closest seats (euclidean distance!) to it have the next set of best values. The next closest seats have slightly worse values, and so on.</p>

<p>All seats of equal distance on the first row are better than all seats of that same distance on the second row (and so on).</p>

<p>Since some seats are equidistant from the best seat, those on the same row that are closest to seat number 1 (the left-most seat when the seats are viewed from the stage) are given better priority (see the diagram below).</p>

<p>Here's a diagram of a small (11 x 5) theater where the seat's 'priority' is shown with #1 being the best:</p>

<pre>                      Seat Number
            1  2  3  4  5  6  7  8  9 10 11
         +----------------------------------
   Row 5 | 54 50 44 38 32 29 33 39 45 51 55
   Row 4 | 52 42 34 25 21 18 22 26 35 43 53
   Row 3 | 48 36 23 14 12  9 13 15 24 37 49
   Row 2 | 46 30 19 10  5  4  6 11 20 31 47
   Row 1 | 40 27 16  7  2  1  3  8 17 28 41</pre>

<p>Write a program that prints the seating priority chart for a supplied width and row count.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: W and R</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..R: Line i contains W space-separated integers that are the seating priorities for row R-i+1</li>
</ul>

<p> </p>

