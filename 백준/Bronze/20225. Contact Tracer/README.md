# [Bronze I] Contact Tracer - 20225 

[문제 링크](https://www.acmicpc.net/problem/20225) 

### 성능 요약

메모리: 30840 KB, 시간: 384 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Novel virus infections are spreading. The virus is known to transmit on close contact with carriers, whether or not with any symptoms. Therefore, it is effective for epidemic prevention to identify and test those who had close contact with persons confirmed or were judged highly probable to be infected. To realize this, a system is desired that perpetually records all the close contact events by an application on mobile phones and, when infection is confirmed, identifies all persons with direct or indirect infection risks based on the record.</p>

<p>You were asked to develop such a system, and have already finished the mobile phone part. When the installed application detects a close contact event with another person carrying a phone with the same application installed, it sends IDs of both to the surveillance center.</p>

<p>Your next task is to develop a program that, when infection of a user is confirmed, identifies users with risks of direct or indirect transmission from the infected user.</p>

<p>When a user of the system is confirmed to be infected, those users who made close contacts with the infected user within a certain time period (period of communicability) are suspected of infection. If a suspected user had close contact with still another user after that possible infection event, that user also is suspected of infection. The suspects are propagated repetitively in this manner.</p>

<p>When a user is confirmed infected, the ID of the user and the list of all the close contact events of all users with all users happened after the time when the confirmed user possibly becomes a carrier are given. All the events in the given list should be assumed to be within the period of communicability of the confirmed user. The output should be the number of users to whom the virus was possibly transmitted directly or indirectly from the infected user.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<blockquote><i>m</i> <i>n</i> <i>p</i> <i>a</i><sub>1</sub> <i>b</i><sub>1</sub> … <i>a<sub>n</sub></i> <i>b<sub>n</sub></i></blockquote>

<p>Each of the datasets starts with a line containing three integers: <i>m</i> (1 ≤ <i>m</i> ≤ 100) is the number of users, <i>n</i> (0 ≤ <i>n</i> ≤ 1000) is the number of events in the list, and <i>p</i> (1 ≤ <i>p</i> ≤ <i>m</i>) is the ID of the user confirmed to be infected.</p>

<p>The following <i>n</i> lines contain the close contact events between users, one event per line, in time order. Each line indicates that the users whose IDs are <i>a<sub>i</sub></i> and <i>b<sub>i</sub></i> had close contact. Here, <i>a<sub>i</sub></i> and <i>b<sub>i</sub></i> satisfy 1 ≤ <i>a<sub>i</sub></i> ≤ <i>m,</i> 1 ≤ <i>b<sub>i</sub></i> ≤ <i>m,</i> and <i>a<sub>i</sub></i> ≠ <i>b<sub>i</sub></i>.</p>

<p>The end of the input is indicated by a line containing three zeros. The number of datasets does not exceed 50.</p>

### 출력 

 <p>For each dataset, output a single line containing the total number of users including the user confirmed to be infected and users to whom the virus was possibly transmitted directly or indirectly from the confirmed user.</p>

