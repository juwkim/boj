# [Silver V] Harp Tuning - 24570 

[문제 링크](https://www.acmicpc.net/problem/24570) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p><img alt="" src="" style="width: 204px; height: 295px; float: right;">The CCC harp is a stringed instrument with strings labelled A, B, . . . , T. Like other instruments, it can be out of tune.</p>

<p>A musically inclined computer science student has written a clever computer program to help tune the harp. The program analyzes the sounds produced by the harp and provides instructions to fix each string that is out of tune. Each instruction includes a group of strings, whether they should be tightened or loosened, and by how many turns.</p>

<p>Unfortunately, the output of the program is not very user friendly. It outputs all the tuning instructions on a single line. For example, the single line <code>AFB+8HC-4</code> actually contains two tuning instructions: <code>AFB+8</code> and <code>HC-4</code>. The first instruction indicates that harp strings A, F, and B should be tightened 8 turns, and the second instruction indicates that harp strings H and C should be loosened 4 turns.</p>

<p>Your job is to take a single line of tuning instructions and make them easier to read.</p>

### 입력 

 <p>There will be one line of input which is a sequence of tuning instructions. Each tuning instruction will be a sequence of uppercase letters, followed by a plus sign (+) or minus sign (-), followed by a positive integer. There will be at least one instruction and at least one letter per instruction. Also, each uppercase letter will appear at most once.</p>

### 출력 

 <p>There will be one line of output for each tuning instruction. Each line of output will consist of three parts, each separated by a single space: the uppercase letters referring to the strings, <code>tighten</code> if the instruction contained a plus sign or <code>loosen</code> if the instruction contained a minus sign, and the number of turns.</p>

