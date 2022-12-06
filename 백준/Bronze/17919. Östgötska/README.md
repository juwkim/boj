# [Bronze II] Östgötska - 17919 

[문제 링크](https://www.acmicpc.net/problem/17919) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Anders talks in the Swedish dialect of <em>östgötska</em>. Unfortunately, this makes it somewhat hard to get a programming job in the Swedish capital of Stockholm. The trendy Stockholm hipsters only accept applicants speaking the standard Swedish dialect, <em>rikssvenska</em>.</p>

<p>To increase his chances of passing interviews, he wishes to practice talking rikssvenska. To help him with this, he wants you to write a program that can determine whenever he accidentally reverts to speaking östgötska.</p>

<p>A simple way of determining if a sentence is written in östgötska is if at least $40\%$ of the words in the sentence contains the letter <code>ä</code>. For simplicity, this is encoded as the letter combination <code>ae</code> (meaning any appearance of the substring \texttt{ae} is to be regarded as an occurrence of the letter <code>ä</code>).</p>

### 입력 

 <p>The first and only line of input contains a sequence of space-separated words. Each word consists only of letters <code>a-z</code>. There are at most $100$ words, and each word contains at most $15$ letters <code>a-z</code> (meaning that the <code>ae</code> combination counts as two letters for this limit).</p>

### 출력 

 <p>Output "<code>dae ae ju traeligt va"</code> if the input sentence is in östgötska, otherwise output "<code>haer talar vi rikssvenska</code>".</p>

