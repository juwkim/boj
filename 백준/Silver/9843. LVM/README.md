# [Silver IV] LVM - 9843 

[문제 링크](https://www.acmicpc.net/problem/9843) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

자료 구조(data_structures), 구현(implementation), 스택(stack)

### 문제 설명

<p>You are designing a virtual machine for a new programming language called Lombok. The Lombok Virtual Machine (LVM) runs an assembler-like machine code. It operates on a stack and a single register.</p>

<p>In detail, the instructions work as follows:</p>

<p><code><strong>PUSH x</strong></code>: This instruction pushes a given integer onto the stack. If the stack for example looks like this</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8998a199-4068-4cf2-b1b1-71e51f3cc8ad/-/preview/" style="width: 116px; height: 110px;"></p>

<p>and the machine executes the instruction <code>PUSH -11</code>, the stack looks like this afterwards:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/113a77f3-e0ca-471e-ab13-f722ca5d34ff/-/preview/" style="width: 117px; height: 156px;"></p>

<p><strong><code>STORE</code></strong>: This instruction takes the topmost integer from the stack and stores it in the register. If the stack for example looks like this</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e07868c6-7f1e-4028-95fb-24b4985f4130/-/preview/" style="width: 116px; height: 156px;"></p>

<p>the register contains any integer, and the machine executes the instruction <code>STORE</code>, the stack looks like this afterwards:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/dc8f368b-a7f3-46ed-bde0-e7b81baecf5d/-/preview/" style="width: 117px; height: 108px;"></p>

<p>and the register contains the integer 3.</p>

<p><code><strong>LOAD</strong></code>: This instruction copies the content of the register and pushes it onto the stack. If the register for example contains the integer 6, the stack looks like this</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6fa0ed7a-d9ab-4fb8-9fa2-efe739277008/-/preview/" style="width: 115px; height: 106px;"></p>

<p>and the machine executes the instruction <code>LOAD</code>, the stack looks like this afterwards</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f7e945c9-eb9d-47c1-aea2-a2167e2ab1a7/-/preview/" style="width: 118px; height: 153px;"></p>

<p>and the register still contains the integer 6.</p>

<p><code><strong>PLUS</strong></code>: This instruction takes the two topmost integers from the stack, adds them, and pushes the resulting integer back onto the stack. If the stack for example looks like this</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/87b51a8b-93fb-47bf-9c3f-96c8fc74bf68/-/preview/" style="width: 114px; height: 152px;"></p>

<p>and the machine executes the instruction <code>PLUS</code>, the stack looks like this afterwards:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8528630e-5636-4f44-9f2b-e33dc762db89/-/preview/" style="width: 116px; height: 105px;"></p>

<p><code><strong>TIMES</strong></code>: This instruction takes the two topmost integers from the stack, multiplies them, and pushes the resulting integer back onto the stack. If the stack for example looks like this</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e97b531a-2911-4b33-abfe-17cc8c4810fc/-/preview/" style="width: 121px; height: 153px;"></p>

<p>and the machine executes the instruction <code>TIMES</code>, the stack looks like this afterwards:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/5095b3fb-b620-4c92-81bb-e3266b5f7eb0/-/preview/" style="width: 116px; height: 107px;"></p>

<p><code><strong>IFZERO n</strong></code>: This instruction removes the topmost integer from the stack, and checks if it is equal to 0. If that is the case, it jumps to the n<sup>th</sup> instruction (start counting at 0). If not, the machine continues as usual with the next instruction. See example below.</p>

<p><code><strong>DONE</strong></code>: Finally, the <code>DONE</code> instruction prints out the integer on top of the stack, and terminates the program regardless of the following instructions.</p>

<p>Computation starts with the first instruction. Initially, the stack is empty and the register contains the number 0.</p>

### 입력 

 <p>The first line of the input contains an integer n between 2 and 1000, indicating the number of instructions of the program. The following n lines contain the program instructions. Arguments are separated by a space character from the preceding instruction.</p>

### 출력 

 <p>The output consists of a single integer, which is the result of the first DONE instruction encountered during execution.</p>

