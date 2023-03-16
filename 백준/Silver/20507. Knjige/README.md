# [Silver IV] Knjige - 20507 

[문제 링크](https://www.acmicpc.net/problem/20507) 

### 성능 요약

메모리: 116272 KB, 시간: 152 ms

### 분류

구성적

### 문제 설명

<p>Tin is a very special boy. He doesn’t like a lot of things, for example he doesn’t like Barcelona, getting defeated in video games or any sort of mess...</p>

<p>Today he is visiting his friend Ante to once and for all decide who is the best FIFA player. The moment he entered Ante’s apartment, he was greeted with an unpleasant surprise. Ante has two shelves on his wall side by side. The left one contains n books about the numerous accomplishments of Barcelona <strong>stacked on top of each other</strong>, and the right one is empty.</p>

<p>He didn’t mind so much that Ante was reading, in his opinion, trashy books, but what bothered him much more was that the books were a total mess, that is, they weren’t sorted from thinnest to thickest. As Ante is a good friend, he immediately hurried to rearrange the books to Tin’s liking. In one move he can:</p>

<ul>
	<li><strong>take a book from the top</strong> of some shelf in his left or right hand, if he is not holding some other book in that hand; or</li>
	<li><strong>put the book</strong> he is holding in some hand <strong>on top</strong> of some shelf.</li>
</ul>

<p>Ante’s strong suit is football, not rearranging books, so he asks you to find some sequence of moves, that he will then perform, so that in the end all books will be on the <strong>left shelf</strong> and sorted <strong>from thinnest to thickest</strong>, in the order <strong>from top to bottom</strong>.</p>

### 입력 

 <p>The first line contains an integer n (1 ≤ n ≤ 100), the number of books on the left shelf.</p>

<p>The second line contains n integers d<sub>i</sub> (1 ≤ d<sub>i</sub> ≤ 1000) that represent the thicknesses of the books, from top to bottom.</p>

### 출력 

 <p>In the first line output an integer k (0 ≤ k ≤ 100 000), the number of moves in your solution.</p>

<p>In the following k lines output the moves in the form INSTRUCTION HAND SHELF, where:</p>

<ul>
	<li><code>INSTRUCTION</code> is the word <code>UZMI</code> (Croatian for take) if Ante should take a book from some shelf, or the word <code>STAVI</code> (Croatian for put) if he should put a book on some shelf</li>
	<li><code>HAND</code> is the letter <code>L</code> if Ante should use his left hand, or the letter <code>D</code> (Croatian word for right is desno) if he should use his right hand</li>
	<li><code>SHELF</code> is the letter <code>L</code> if this move acts on the left shelf, or the letter <code>D</code> if it acts on the right shelf.</li>
</ul>

<p>Your solution does <strong>not</strong> have to be of minimum possible length, but the number of moves must not exceed 100 000. It can be proven that for the given constraints a solution always exists.</p>

