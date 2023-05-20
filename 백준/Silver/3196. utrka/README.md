# [Silver IV] utrka - 3196 

[문제 링크](https://www.acmicpc.net/problem/3196) 

### 성능 요약

메모리: 115096 KB, 시간: 168 ms

### 분류

구현, 정렬

### 문제 설명

<p>We have to write a computer program to rank the drivers during a car race. </p>

<p>Along the closed racetrack there are K checkpoints (designated with numbers from 1 to K) with judges at the each checkpoint. When some driver passes through the checkpoint, judge sends a message to the computer system with the number of the checkpoint and the number of the driver (drivers are designated with numbers from 1 to N). </p>

<p>Race starts just before the first checkpoint i.e. drivers pass through that checkpoint immediately after the start. </p>

<p>Write a program that will calculate the current ranking of the drivers, given all of the messages sent by the judges. </p>

<p>If two drivers have regularly passed the same number of checkpoints, the driver who passed the last point earlier is ranked higher. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4a53e988-3d85-41e0-b91f-696b27ec2861/-/preview/" style="width: 329px; height: 329px;"></p>

<p>The figure above depicts a racetrack with five checkpoints. Drivers must pass the points in the right order. If a driver passes other points between two consecutive checkpoints, we ignore those extra passes. </p>

### 입력 

 <p>First line of input contains three integers K, N and M, 1 ≤ K ≤ 100, 1 ≤ N ≤ 100, 1 ≤ M ≤ 10000. </p>

<p>Each of the following M lines contains two integers X and Y. They represent a message from a judge saying that the driver with number X passed by the checkpoint Y. Events in the input are given in chronological order. </p>

<p>Note: there will always be a solution for the given test data. </p>

### 출력 

 <p>First and only line of output should contain the final ranking of drivers in the race, after all M messages from the judges have been processed. </p>

