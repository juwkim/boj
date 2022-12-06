# [Bronze I] Ethel’s Encryption - 11288 

[문제 링크](https://www.acmicpc.net/problem/11288) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>Ethel suspected that the North Side Alliance (NSA) were spying on her communications with her sister Lucy. In order to thwart the NSA’s attempts, Ethel encrypted all of their communications using a Caesar cipher.</p>

<p>A Caesar cipher is an encryption method where each letter in the plaintext is shifted by an offset in order to produce the encrypted text. For example, given the offset value of 2, A becomes C, B becomes D, Y becomes A, and so on.</p>

<p>Your task is to decrypt Ethel’s encrypted messages given that the offset is calculated by a<sup>b</sup>.</p>

### 입력 

 <p>The first line contains three integers n, a, and b. n is the number of characters in the encrypted message, including spaces. The numbers a and b are used to calculate the offset a<sup>b</sup>, with 0 ≤ a ≤ 2<sup>31</sup> and 0 ≤ b ≤ 2<sup>16</sup>, however at least a or b will be greater than 0 in each input.</p>

<p>The second line contains n characters representing the encrypted message. It is guaranteed to only contain upper-case letters (A-Z) or spaces, and is immediately followed by a newline.</p>

### 출력 

 <p>The output should consist of a single line with the decrypted message in upper-case characters. Note that space are preserved between the encrypted and decrypted messages. This should immediately be followed by a newline.</p>

