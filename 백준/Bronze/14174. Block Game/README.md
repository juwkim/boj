# [Bronze I] Block Game - 14174 

[문제 링크](https://www.acmicpc.net/problem/14174) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

문자열(string)

### 문제 설명

<p>Farmer John is trying to teach his cows to read by giving them a set of N spelling boards typically used with preschoolers (1≤N≤100). Each board has a word and an image on each side. For example, one side might have the word 'cat' along with a picture of a cat, and the other side might have the word 'dog' along with a picture of a dog. When the boards are lying on the ground, N words are therefore shown. By flipping over some of the boards, a different set of N words can be exposed.</p>

<p>To help the cows with their spelling, Farmer John wants to fashion a number of wooden blocks, each embossed with a single letter of the alphabet. He wants to make sufficiently many blocks of each letter so that no matter which set of N words is exposed on the upward-facing boards, the cows will be able to spell all of these words using the blocks. For example, if N=3 and the words 'box', 'cat', and 'car' were facing upward, the cows would need at least one 'b' block, one 'o' block, one 'x' block, two 'c' blocks, two 'a' blocks, one 't' block, and one 'r' block.</p>

<p>Please help the Farmer John determine the minimum number of blocks for each letter of the alphabet that he needs to provide, so that irrespective of which face of each board is showing, the cows can spell all N visible words.</p>

### 입력 

 <p>Line 1 contains the integer N.</p>

<p>The next N lines each contain 2 words separated by a space, giving the two words on opposite sides of a board. Each word is a string of at most 10 lowercase letters.</p>

### 출력 

 <p>Please output 26 lines. The first output line should contain a number specifying the number of copies of 'a' blocks needed. The next line should specify the number of 'b' blocks needed, and so on.</p>

