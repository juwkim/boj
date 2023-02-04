# [Silver IV] Organ-free Man - 23785 

[문제 링크](https://www.acmicpc.net/problem/23785) 

### 성능 요약

메모리: 114488 KB, 시간: 124 ms

### 분류

그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>Every so often, a shipment of universal robots comes from Earth to Mars in order to help you with routine colonization tasks. The robots are called Organ-free Men (precisely OFMv5001.41.912) and each one of them is identified by a unique serial number, which is a positive integer.</p>

<p>To prevent space theft, OFMs are transported from Earth to Mars in a locked state and have to be first unlocked by a special password. The password to unlock an OFM is based on its serial number and a function f(x). The function f(x) is defined as follows:</p>

<p>If 0 ≤ x ≤ 9, then f(x) = x!, and if x > 9, then f(x) = (x mod 10)! + f(⌊x/10⌋). The brackets ⌊⌋ denote the floor value of a number (e.g. ⌊2.43⌋ = 2). Exclamation mark denotes the factorial, i.e., x! = 1 × 2 × · · · × x for x > 0 and 0! = 1.</p>

<p>To unlock an OFM with a serial number y, you need to input smallest such non-negative integer x, so that f(x) = y holds.</p>

<p>Will you manage to unlock all robots that were shipped to you?</p>

### 입력 

 <p>The input consists of one integer y (1 ≤ y ≤ 10<sup>9</sup>), the serial number of a particular OFM.</p>

### 출력 

 <p>Output a single non-negative integer x, the password to unlock the particular OFM.</p>

