# [Silver IV] Ants - 18295 

[문제 링크](https://www.acmicpc.net/problem/18295) 

### 성능 요약

메모리: 199156 KB, 시간: 848 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 문자열(string)

### 문제 설명

<p>Charles is fascinated by ants. In order to observe a colony of ants over a long period, Charles managed to build a program that uniquely identifies each ant, using image recognition. (Yes, every ant is unique.) Inside the program, each ant is tagged with a unique nonnegative integer. Whenever there is a birth in the colony, the new ant is given a new tag, different from all tags already assigned. Whenever some ant disappears, its tag falls back into the pool of available tags.</p>

<p>Charles’s program works as follows. It first scans the whole colony, building the list of tags of the ants that are recognized. Then it assigns fresh tags to the new ants. To do so, the program simply picks the first natural number (i.e., nonnegative integer) that is not currently assigned to any ant, and so on.</p>

<p>Due to some glitches in the image recognition device and in the program, there are sometimes negative or very large numbers that appear in the input list. These are simply ignored by Charles’s program.</p>

<p>Your job is to reimplement the part of Charles’s program that finds a fresh tag to assign to a new ant.</p>

### 입력 

 <p>The input consists of the following lines:</p>

<ul>
	<li>on the first line: an integer N;</li>
	<li>on the next N lines: some integers X<sub>1</sub>, . . . , X<sub>N</sub>, one per line.</li>
</ul>

### 출력 

 <p>The smallest natural number that does not belong to the set {X<sub>1</sub>, . . . , X<sub>N</sub>}.</p>

