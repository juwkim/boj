# [Bronze I] Ancient Cipher - 7386 

[문제 링크](https://www.acmicpc.net/problem/7386) 

### 성능 요약

메모리: 32548 KB, 시간: 104 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>Ancient Roman empire had a strong government system with various departments, including a secret service department. Important documents were sent between provinces and the capital in encrypted form to prevent eavesdropping. The most popular ciphers in those times were so called <em>substitution cipher</em> and <em>permutation cipher</em>.</p>

<p>Substitution cipher changes all occurrences of each letter to some other letter. Substitutes for all letters must be different. For some letters substitute letter may coincide with the original letter. For example, applying substitution cipher that changes all letters from '<code>A</code>' to '<code>Y</code>' to the next ones in the alphabet, and changes '<code>Z</code>' to '<code>A</code>', to the message "<code>VICTORIOUS</code>" one gets the message "<code>WJDUPSJPVT</code>". </p>

<p>Permutation cipher applies some permutation to the letters of the message. For example, applying the permutation $\langle 2, 1, 5, 4, 3, 7, 6, 10, 9, 8\rangle$ to the message "<code>VICTORIOUS</code>" one gets the message "<code>IVOTCIRSUO</code>".</p>

<p>It was quickly noticed that being applied separately, both substitution cipher and permutation cipher were rather weak. But when being combined, they were strong enough for those times. Thus, the most important messages were first encrypted using substitution cipher, and then the result was encrypted using permutation cipher. Encrypting the message "<code>VICTORIOUS</code>" with the combination of the ciphers described above one gets the message "<code>JWPUDJSTVP</code>".</p>

<p>Archeologists have recently found the message engraved on a stone plate. At the first glance it seemed completely meaningless, so it was suggested that the message was encrypted with some substitution and permutation ciphers. They have conjectured the possible text of the original message that was encrypted, and now they want to check their conjecture. They need a computer program to do it, so you have to write one.</p>

### 입력 

 <p>Input file contains two lines. The first line contains the message engraved on the plate. Before encrypting, all spaces and punctuation marks were removed, so the encrypted message contains only capital letters of the English alphabet. The second line contains the original message that is conjectured to be encrypted in the message on the first line. It also contains only capital letters of the English alphabet. </p>

<p>The lengths of both lines of the input file are equal and do not exceed~$100$.</p>

### 출력 

 <p>Output "<code>YES</code>" if the message on the first line of the input file could be the result of encrypting the message on the second line, or "<code>NO</code>" in the other case.</p>

