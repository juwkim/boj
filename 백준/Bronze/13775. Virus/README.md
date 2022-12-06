# [Bronze II] Virus - 13775 

[문제 링크](https://www.acmicpc.net/problem/13775) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

문자열(string)

### 문제 설명

<p>Shroeder and Patsy heard from a friend whose computer had been attacked by a ransom virus. A nasty message appeared telling their friend that all his files had been encrypted and that it would cost him to have them restored.</p>

<p>Being keen programmers, Shroeder and Patsy, just for fun you understand, wondered how that worked. They tried a simple encryption which would depend of a key which was a single number.</p>

<p>They thought they could use a sort of Caesar cipher (where letters are shifted a number of places through the alphabet which is considered circular so A follows Z). They would start with a shift somewhere between 1 and 25 (the key), then increase it by one each letter. It would cycle round so after 25 would become 1 again.</p>

<p>To decipher, if you know the key it is quite easy, as long as you remember to shift in the opposite direction!</p>

### 입력 

 <p>Input consists of a single integer, K, the key, followed by a line of encrypted text. The text will be no more than 250 characters long, and will consist of lower case letters, spaces, digits and punctuation marks only. Only letters are to by encrypted.</p>

### 출력 

 <p>Output the line of text correctly decrypted.</p>

