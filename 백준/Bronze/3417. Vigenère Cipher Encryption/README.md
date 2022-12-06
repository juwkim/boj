# [Bronze II] Vigenère Cipher Encryption - 3417 

[문제 링크](https://www.acmicpc.net/problem/3417) 

### 성능 요약

메모리: 29652 KB, 시간: 1732 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>One of the oldest and most common encryption algorithms is Vigenère Cipher. It is quite an old thing — a similar encryption was first described in 1553 by Giovan Battista Bellaso and improved in 1586 by Blaise de Vigenère.</p>

<p>Vigenère encryption produces a single letter of ciphertext for each letter of plaintext, combining one plaintext letter with one single letter of a key on the corresponding position. If the key is shorter than the plaintext, it is simply repeated as needed, e.g. for a key of length 3 and plaintext of length 7, letters will be combined like this (K<sub>i</sub> is the key letter, P<sub>i</sub> is the plaintext letter, and C<sub>i</sub> is the resulting ciphertext letter).</p>

<pre> K<sub>1</sub> K<sub>2</sub> K<sub>3</sub> K<sub>1</sub> K<sub>2</sub> K<sub>3</sub> K<sub>1</sub>
 P<sub>1</sub> P<sub>2</sub> P<sub>3</sub> P<sub>4</sub> P<sub>5</sub> P<sub>6</sub> P<sub>7</sub>
----------------------
 C<sub>1</sub> C<sub>2</sub> C<sub>3</sub> C<sub>4</sub> C<sub>5</sub> C<sub>6</sub> C<sub>7</sub>
</pre>

<p>The letter of the key specifies how many positions should be the plaintext letter “shifted forward” in the alphabet. If a key letter is A, the correspoding plaintext letter will be shifted by one character, B means two positions, etc. The alphabet is considered circular, so if the last letter (Z) should be shifted, it becomes A again. Please note that A (key) combined with another A (plaintext) will result in B, which may be a little unusual for the common Vigenère cipher. The Vigenère square at the end of this problem statement gives an overview how letters of a plaintext get combined with letters of a key to produce the ciphertext.</p>

<p>Your task is to write a program that will encrypt messages using the Vigenère cipher with a given key.</p>

### 입력 

 <p>The input contains several instances. Each instance consists of two lines, the first line is the encryption key and the second line is the plaintext. Both key and plaintext consist of uppercase letters of the English alphabet {A,B,C,...,Z}. The length of the key will be between 1 and 1000, the length of the plaintext between 1 and 100 000, inclusive. </p>

<p>Input is terminated by a line containing one zero.</p>

### 출력 

 <p>For each input instance, output the ciphertext — the encrypted version of the message.</p>

