# [Bronze V] Intercepting Information - 26209 

[문제 링크](https://www.acmicpc.net/problem/26209) 

### 성능 요약

메모리: 113248 KB, 시간: 152 ms

### 분류

구현(implementation)

### 문제 설명

<p>Spies Breaching Computers (SBC) is a private digital spy agency that is developing a new device for intercepting information using electromagnetic waves, which allows spying even without physical contact with the target.</p>

<p>The device tries to collect information one byte at a time, this is, a sequence of $8$ bits where each of them, naturally, can have a value of $0$ or $1$. In certain situations, due to interference from other devices, the reading cannot be done successfully. In this case, the device returns the value $9$ for the corresponding bit, informing that the reading could not be performed.</p>

<p>In order to automate the recognition of the information the device reads, a request was made for a program that, based on the information read by the device, informs whether all bits were read successfully or not. Your task is to write this program.</p>

### 입력 

 <p>The input consists of a single line, containing $8$ integers $N_1$, $N_2$, $N_3$, $N_4$, $N_5$, $N_6$, $N_7$ and $N_8$, indicating the values read by the device ($N_i$ is <code>0</code>, <code>1</code> or <code>9</code> for $1 ≤ i ≤ 8$).</p>

### 출력 

 <p>Print a single line containing the capital letter “<code>S</code>” if all bits are read successfully; otherwise print a single line containing the capital letter “<code>F</code>”, corresponding to a failure.</p>

