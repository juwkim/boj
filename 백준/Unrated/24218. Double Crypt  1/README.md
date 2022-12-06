# [Unrated] Double Crypt  1 - 24218 

[문제 링크](https://www.acmicpc.net/problem/24218) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

구현(implementation)

### 문제 설명

<p>The Advanced Encryption Standard (AES) involves a new strong encryption algorithm. It works with three <em>blocks</em> of $128$ bits. Given a message block $p$ (plaintext) and a key block $k$, the AES encryption function $E$ returns an encrypted block $c$ (ciphertext):</p>

<p>$c = E(p, k)$.</p>

<p>The inverse of the AES encryption function $E$ is the decryption function $D$ such that</p>

<p>$D ( E(p, k), k ) = p$, $E ( D(c, k), k ) = c$.</p>

<p>In <em>Double AES</em>, two independent key blocks $k_1$ and $k_2$ are used in succession, first $k_1$, then $k_2$:</p>

<p>$c_2 = E ( E(p, k_1), k_2 )$.</p>

<p>In this task, an integer $s$ is also given. Only the leftmost $4 \times s$ bits of all keys are relevant, while the other bits (the rightmost $128$ minus $4 \times s$ bits) are all zero.</p>

<p>You are to recover the encryption key pairs for some messages encrypted by Double AES. You are given both the plaintext $p$ and the corresponding double-encrypted ciphertext $c_2$, and the structure of the encryption keys as expressed by the integer $s$.</p>

<p>You must submit the recovered keys, and not a recovery program.</p>

### 입력 

 <p>You are given ten problem instances in the text files named <code>double1.in</code> to <code>double10.in</code>. Each input file consists of three lines. The first line contains the integer $s$, the second line the plaintext block $p$, and the third line the ciphertext block $c_2$ obtained from $p$ by Double AES encryption. Both blocks are written as strings of 32 hexadecimal digits ('<code>0</code>'..'<code>9</code>', '<code>A</code>'..'<code>F</code>'). The library provides a routine to convert strings to blocks. All input files are solvable.</p>

### 출력 

 <p>The first line contains the key block $k_1$, and the second line the key block $k_2$, such that </p>

<p>$c_2 = E ( E(p, k_1), k_2 )$.</p>

<p>Both blocks must be written as strings of 32 hexadecimal digits ('<code>0</code>'..'<code>9</code>', '<code>A</code>'..'<code>F</code>'). If there are multiple solutions, you need submit only one of them.</p>

