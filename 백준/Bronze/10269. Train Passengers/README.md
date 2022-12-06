# [Bronze I] Train Passengers - 10269 

[문제 링크](https://www.acmicpc.net/problem/10269) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>The Nordic Company of Passing Carriages is losing money at an alarming rate because most of their trains are empty. However, on some lines the passengers are complaining that they cannot fit in the cars and have to wait for the next train!</p>

<p>The authorities want to fix this situation. They asked their station masters to write down, for a given train, how many people left the train at their station, how many went in, and how many had to wait. Then they hired your company of highly paid consultants to assign properly sized trains to their routes.</p>

<p>You just received the measurements for a train, but before feeding them to your optimisation algorithm you remembered that they were collected on a snowy day, so any sensible station master would have preferred to stay inside their cabin and make up the numbers instead of going outside and counting.</p>

<p>Verify your hunch by checking whether the input is inconsistent, i.e., at every time the number of people in the train did not exceed the capacity nor was below 0 and no passenger waited in vain. The train should start and finish the journey empty, in particular passengers should not wait for the train at the last station.</p>

### 입력 

 <p>The first line contains two integers C and n (2 ≤ n ≤ 100), the total capacity and the number of stations the train stops in. The next n lines contain three integers each, the number of people that left the train, entered the train, and had to stay at a station. Lines are given in the same order as the train visits each station. All integers including C are between 0 and 10<sup>9</sup> inclusive.</p>

### 출력 

 <p>One line containing one word: possible if the measurements are consistent, impossible otherwise.</p>

