# [Bronze I] Cow Tipping - 14457 

[문제 링크](https://www.acmicpc.net/problem/14457) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation)

### 문제 설명

<p>Farmer John occasionally has trouble with bored teenagers who visit his farm at night and tip over his cows. One morning, he wakes up to find it has happened again -- his N<sup>2</sup> cows began the night grazing in a perfect N×N square grid arrangement (1 ≤ N ≤ 10), but he finds that some of them are now tipped over.</p>

<p>Fortunately, Farmer John has used parts from his tractor and forklift to build a glorious machine, the Cow-Untipperator 3000, that can flip over large groups of cows all at once, helping him put all his cows back on their feet as quickly as possible. He can apply the machine to any "upper-left rectangle" in his grid of cows -- a rectangular sub-grid that contains the upper-left cow. When he does so, the machine flips over every cow in this rectangle, placing tipped cows back on their feet, but unfortunately also tipping over cows that were already on their feet! In other words, the machine "toggles" the state of each cow in the rectangle.</p>

<p>Farmer John figures that by applying his machine sufficiently many times to the appropriate collection of rectangles, he can eventually restore all the cows to their rightful, un-tipped states. Please help him determine the minimum number of applications of his machine needed to do this.</p>

<p>Note that applying the machine to the same rectangle twice would be pointless, since this would have no net impact on the cows in the rectangle. Therefore, you should only consider applying the machine to each upper-left rectangle possibly only once.</p>

### 입력 

 <p>The first line of the input is the integer N.</p>

<p>Each of the N subsequent lines contains a string of N characters, each either 0 (representing an up-tipped cow) or 1 (representing a tipped cow).</p>

### 출력 

 <p>Please output the minimum number of times Farmer John needs to apply the Cow-Untipperator 3000 to restore all his cows to their feet.</p>

