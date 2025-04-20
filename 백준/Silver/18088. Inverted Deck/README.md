# [Silver I] Inverted Deck - 18088 

[문제 링크](https://www.acmicpc.net/problem/18088) 

### 성능 요약

메모리: 275780 KB, 시간: 372 ms

### 분류

해 구성하기, 구현, 정렬

### 제출 일자

2025년 4월 20일 19:09:06

### 문제 설명

<p>As a huge fan of the popular collectible card game Numinous Wilds: the Elven Reign Chronicles (NWERC), you have a large collection of cards which you carefully organise by their rarity. One day you notice that someone has touched your collection, and that some of the cards are now out of order. The most natural suspect, of course, is your little brother Billy, who was absolutely 100% forbidden from playing with your cards. After a few minutes of interrogation Billy confesses that he indeed took a few consecutive cards from the middle of the stack, but he swears that he put them back in exactly the same order as they were. You suspect that Billy, being so young, may have simply mistakenly reversed the order of the cards that he took. Now you want to check your theory and decide if you can find the batch of cards that Billy took to play with.</p>

<p>Is it possible to restore the order of the cards into non-decreasing order of their rarity by reversing just one contiguous batch of cards?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line containing an integer n (1 ≤ n ≤ 10<sup>6</sup>), the number of cards in your collection.</li>
	<li>One line containing n integers v<sub>1</sub>, . . . , v<sub>n</sub> (1 ≤ v<sub>i</sub> ≤ 10<sup>9</sup> for all i), the current order of the cards’ rarity values.</li>
</ul>

### 출력 

 <p>If the cards can be sorted by reversing exactly one contiguous subsequence of the list, then output the 1-based start and end indices of such a subsequence. Otherwise, output “impossible”. If there are multiple valid solutions you may output any one of them.</p>

