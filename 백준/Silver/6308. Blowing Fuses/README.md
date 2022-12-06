# [Silver V] Blowing Fuses - 6308 

[문제 링크](https://www.acmicpc.net/problem/6308) 

### 성능 요약

메모리: 114328 KB, 시간: 132 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Maybe you are familiar with the following situation. You have plugged in a lot of electrical devices, such as toasters, refrigerators, microwave ovens, computers, stereos, etc, and have them all running. But at the moment when you turn on the TV, the fuse blows, since the power drawn from all the machines is greater than the capacity of the fuse. Of course this is a great safety feature, avoiding that houses burn down too often due to fires ignited by overheating wires. But it is also annoying to walk down to the basement (or some other inconvenient place) to replace to fuse or switch it back on.</p>

<p>What one would like to have is a program that checks before turning on an electrical device whether the combined power drawn by all running devices exceeds the fuses capacity (and it blows), or whether it is safe to turn it on.</p>

### 입력 

 <p>The input consists of several test cases. Each test case describes a set of electrical devices and gives a sequence of turn on/off operations for these devices.</p>

<p>The first line of each test case contains three integers n, m and c, where n is the number of devices (n , 20), m the number of operations performed on these devices and c is the capacity of the fuse (in Amperes). The following n lines contain one positive integer ci each, the consumption (in Amperes) of the i-th device.</p>

<p>This is followed by m lines also containing one integer each, between 1 and n inclusive. They describe a sequence of turn on/turn off operations performed on the devices. For every number, the state of that particular devices is toggled, i.e. if it is currently running, it is turned off, and if it is currently turned off, it will by switched on. At the beginning all devices are turned off.</p>

<p>The input will be terminated by a test case starting with n = m = c = 0. This test case should not be processed.</p>

### 출력 

 <p>For each test case, first output the number of the test case. Then output whether the fuse was blown during the operation sequence. The fuse will be blown if the sum of the power consumptions ci of turned on devices at some point exceeds the capacity of the fuse c.</p>

<p>If the fuse is not blown, output the maximal power consumption by turned on devices that occurred during the sequence.</p>

<p>Output a blank line after each test case.</p>

