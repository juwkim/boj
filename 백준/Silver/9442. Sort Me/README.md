# [Silver IV] Sort Me - 9442 

[문제 링크](https://www.acmicpc.net/problem/9442) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

정렬(sorting), 문자열(string)

### 문제 설명

<p>We know the normal alphabetical order of the English alphabet, and we can then sort words or other letter sequences.  For instance these words are sorted:</p>

<div style="margin-left: 40px;">ANTLER<br>
ANY<br>
COW<br>
HILL<br>
HOW<br>
HOWEVER<br>
WHATEVER<br>
ZONE</div>

<p>The standard rules for sorting letter sequences are used:</p>

<ol>
	<li>The first letters are in alphabetical  order.</li>
	<li>Among strings with the same prefix, like the prefix AN in ANTLER and ANY, they are ordered by the first character that is different, T or Y here. </li>
	<li>One whole string may be a prefix of another string, like HOW and HOWEVER.  In this case the longer sequence comes after the shorter one.</li>
</ol>

<p>The Gorellians, at the far end of our galaxy, have discovered various samples of English text from our electronic transmissions, but they did not find the order of our alphabet.  Being a very organized and orderly species, they want to have a way of ordering words, even in the strange symbols of English.  Hence they must determine their own order.  Unfortunately they cannot agree, and every Gorellian year, they argue and settle on a new order.</p>

<p>For instance, if they agree on the alphabetical order</p>

<div style="margin-left: 40px;">UVWXYZNOPQRSTHIJKLMABCDEFG</div>

<p>then the words above would be sorted as</p>

<div style="margin-left: 40px;">WHATEVER<br>
ZONE<br>
HOW<br>
HOWEVER<br>
HILL<br>
ANY<br>
ANTLER<br>
COW</div>

<p>The first letters of the words are in <em>their</em> alphabetical order.  Where words have the same prefix, the first differing letter determines the order, so the order goes ANY,  then ANTLER, since Y is before T in <em>their</em> choice of alphabet.  Still HOWEVER comes after HOW, since HOW is a prefix of HOWEVER.</p>

<p>Dealing with the different alphabetical orders each year by hand (or tentacle) is tedious.  Your job is to implement sorting with the English letters in a specified sequence.</p>

### 입력 

 <p>The input will contain one or more datasets.  Each dataset will start with a line containing an integer <em>n</em> and a string <em>s</em>, where s is a permutation of the English uppercase alphabet, used as the Gorellians' alphabet in the coming year.  The next <em>n</em> lines (1 ≤ <em>n</em> ≤ 20) will each contain one non-empty string of letters.  The length of each string will be no more than 30.  Following the last dataset is a line containing only 0.</p>

### 출력 

 <p>The first line of output of each dataset will contain "year " followed by the number of the dataset, starting from 1.   The remaining n lines are the <em>n</em> input strings sorted assuming the alphabet has the order in <em>s</em>.</p>

