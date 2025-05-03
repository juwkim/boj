# [Silver I] Zipline - 17597 

[문제 링크](https://www.acmicpc.net/problem/17597) 

### 성능 요약

메모리: 110716 KB, 시간: 112 ms

### 분류

기하학, 수학, 피타고라스 정리, 삼분 탐색

### 제출 일자

2025년 5월 3일 19:15:44

### 문제 설명

<p>A zipline is a very fun and fast method of travel. It uses a very strong steel cable, connected to two poles. A rider (which could be a person or some cargo) attaches to a pulley which travels on the cable. Starting from a high point on the cable, gravity pulls the rider along the cable.</p>

<p>Your friend has started a company which designs and installs ziplines, both for fun and for utility. However, there’s one key problem: determining how long the cable should be between the two connection points. The cable must be long enough to reach between the two poles, but short enough that the rider is guaranteed to stay a safe distance above the ground. Help your friend determine these bounds on the length.</p>

<p>The cable connects to two vertical poles that are <em>w</em> meters apart, at heights <em>g</em> and <em>h</em> meters, respectively. You may assume that the cable is inelastic and has negligible weight compared to the rider, so that there is no sag or slack in the cable. That is, at all times the cable forms two straight line segments connecting the rider to the two poles, with the sum of the segments lengths equal to the total length of the cable. The lowest part of the rider hangs <em>r</em> meters below the cable; therefore the cable must stay at least <em>r</em> meters above the ground at all times during the ride. The ground is flat between the two poles. Please refer to the diagram in Figure M.1 for more information.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/feb834cc-1d79-4865-acab-b906a8b54d8d/-/preview/" style="width: 512px; height: 192px;"></p>

<p style="text-align: center;">Figure M.1: A zipline, annotated with the four variables used to describe it.</p>

### 입력 

 <p>The input starts with a line containing an integer <em>n</em>, where 1 ≤ <em>n</em> ≤ 1 000. The next <em>n</em> lines each describe a zipline configuration with four integers: <em>w</em>, <em>g</em>, <em>h</em>, and <em>r</em>. These correspond to the variables described above. The limits on their values are: 1 ≤ <em>w</em>, <em>g</em>, <em>h</em> ≤ 1 000 000, and 1 ≤ <em>r</em> ≤ min(<em>g</em>, <em>h</em>).</p>

### 출력 

 <p>For each zipline, print a line of output with two lengths (in meters): the minimum and maximum length the cable can be while obeying the above constraints. Both lengths should have an absolute error of at most 10<sup>−6</sup>.</p>

