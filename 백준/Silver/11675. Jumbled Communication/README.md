# [Silver V] Jumbled Communication - 11675 

[문제 링크](https://www.acmicpc.net/problem/11675) 

### 성능 요약

메모리: 115408 KB, 시간: 132 ms

### 분류

비트마스킹(bitmask), 브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Your best friend Adam has recently bought a Raspberry Pi and some equipment, including a wireless temperature sensor and a 433MHz receiver to receive the signals the sensors sends. Adam plans to use the Raspberry Pi as an in-door display for his weather sensor. As he is very good with electronics, he quickly managed to get the receiver to receive the signals of the sensor. However, when he looked at the bytes sent by the sensor he could not make heads or tails of them. After some hours looking through a lot of websites, he found a document explaining that his weather sensor scrambles the data it sends, to prevent it from being used together with products from other manufacturers.</p>

<p>Luckily, the document also describes how the sensor scrambles its communication. The document states that the sensor applies the expression <code>x ^ (x << 1)</code> to every byte sent. The <code>^</code> operator is bit-wise XOR<sup>1</sup>, e.g., <code>10110000 ^ 01100100 = 11010100</code>. The <code><<</code> operator is a (non-circular) left shift of a byte value<sup>2</sup>, e.g., <code>10111001 << 1 = 01110010</code>.</p>

<p>In order for Adam’s Raspberry Pi to correctly interpret the bytes sent by the weather sensor, the transmission needs to be unscrambled. However, Adam is not good at programming (actually he is a pretty bad programmer). So he asked you to help him and as a good friend, you are always happy to oblige. Can you help Adam by implementing the unscrambling algorithm?</p>

<p><sup>1</sup>In bit-wise XOR, the ith bit of the result is 1 if and only if exactly one of the two arguments has the ith bit set.</p>

<p><sup>2</sup>In <code>x << j</code>, the bits of x are moved j steps to the left. The j most significant bits of x are discarded, and j zeroes are added as the least significant bits of the result.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with an integer n (1 ≤ n ≤ 10<sup>5</sup>), the number of bytes in the message sent by the weather sensor;</li>
	<li>one line with n integers b<sub>1</sub>, . . . , b<sub>n</sub> (0 ≤ b<sub>i</sub> ≤ 255 for all i), the byte values of the message.</li>
</ul>

### 출력 

 <p>Output n byte values (in decimal encoding), the unscrambled message.</p>

