# [Silver IV] Coded Communication - 5115 

[문제 링크](https://www.acmicpc.net/problem/5115) 

### 성능 요약

메모리: 116348 KB, 시간: 208 ms

### 분류

Empty

### 문제 설명

<p>When you communicate over long distances — well, really, short distances, too — the bits that you transmit sometimes get accidentally flipped. This could be a serious problem, for instance, if scientists misunderstood the Martians’ ransom demands. To deal with this kind of problem, most long-range or wireless communication uses error-correcting codes. The simplest example to understand the concept is as follows: if you want to just send one bit ‘0’ or ‘1’, you could replace it by “000” and “111”, respectively. Now, if at most one bit gets flipped in your message, the receiver can still figure out whether your bit was ‘0’ or ‘1’. This kind of code based on duplication is not particularly efficient, and one of the very active areas of research at USC and throughout the world is to design codes that use as few extra bits as possible while allowing as many bit flips as possible.</p>

<p>Here, you will solve a much easier problem. Given a code that someone else has already designed, and a received codeword, you are to figure out how many bits have to have been flipped during transmission. More specifically, you will be given a list of 1 ≤ n ≤ 1000 candidate strings mi of zeros and ones that would be correct messages, each exactly b bits long (1 ≤ b ≤ 100). You will also be given the received message r, another bit string of b bits. You are to figure out the minimum number f of bits of r you’d need to flip to get any string m<sub>i</sub>.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of each data set contains the two numbers n and b. This is followed by n lines, each describing one valid codeword as a string of b zeros and ones. After these n lines, there is one more line, containing the string r, again a string of b zeros and ones.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output the minimum distance f of the received code from any valid codeword.</p>

<p>Each data set should be followed by an empty line.</p>

