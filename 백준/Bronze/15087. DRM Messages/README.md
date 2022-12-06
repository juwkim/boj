# [Bronze I] DRM Messages - 15087 

[문제 링크](https://www.acmicpc.net/problem/15087) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>DRM Encryption is a new kind of encryption. Given an encrypted string (which we’ll call a DRM message), the decryption process involves three steps: Divide, Rotate and Merge. This process is described in the following example with the DRM message “EWPGAJRB”:</p>

<ul>
	<li><strong>Divide</strong> – First, divide the message in half to “EWPG” and “AJRB”.</li>
	<li><strong>Rotate</strong> – For each half, calculate its rotation value by summing up the values of each character (A = 0, B = 1, . . . Z = 25). The rotation value of “EWPG” is 4 + 22 + 15 + 6 = 47. Rotate each character in “EWPG” 47 positions forward (wrapping from Z to A when necessary) to obtain the new string “ZRKB”. Following the same process on “AJRB” results in “BKSC”.</li>
	<li><strong>Merge</strong> – The last step is to combine these new strings (“ZRKB” and “BKSC”) by rotating each character in the first string by the value of the corresponding character in the second string. For the first position, rotating ‘Z’ by ‘B’ means moving it forward 1 character, which wraps it around to ‘A’. Continuing this process for every character results in the final decrypted message, “ABCD”.</li>
</ul>

### 입력 

 <p>The input contains a single DRM message to be decrypted. All characters in the string are uppercase letters and the string’s length is even and ≤ 15 000.</p>

### 출력 

 <p>Display the decrypted DRM message.</p>

