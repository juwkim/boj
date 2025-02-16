# [Silver II] Internet Service Providers - 3753 

[문제 링크](https://www.acmicpc.net/problem/3753) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

미적분학, 수학, 삼분 탐색

### 제출 일자

2025년 2월 16일 09:47:49

### 문제 설명

<p>A group of N Internet Service Provider companies (ISPs) use a private communication channel that has a maximum capacity of C traffic units per second. Each company transfers T traffic units per second through the channel and gets a profit that is directly proportional to the factor T(C - T N). The problem is to compute T_optim, the smallest value of T that maximizes the total profit the N ISPs can get from using the channel. Notice that N, C, T, and T_optim are integer numbers.</p>

<p>Write a program that reads sets of data from an input text file. </p>

### 입력 

 <p>Each data set corresponds to an instance of the problem above and contains two integral numbers – N and C – with values in the range from 0 to 10<sup>9</sup>. The input data are separated by white spaces, are correct, and terminate with an end of file. </p>

### 출력 

 <p>For each data set the program computes the value of T_optim according to the problem instance that corresponds to the data set. The result is printed on the standard output from the beginning of a line. There must be no empty lines on the output. An example of input/output is shown below.</p>

