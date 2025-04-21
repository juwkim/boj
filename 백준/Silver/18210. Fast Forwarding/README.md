# [Silver I] Fast Forwarding - 18210 

[문제 링크](https://www.acmicpc.net/problem/18210) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

그리디 알고리즘, 수학

### 제출 일자

2025년 4월 21일 13:53:15

### 문제 설명

<p>Mr. Anderson frequently rents video tapes of his favorite classic films. Watching the films so many times, he has learned the precise start times of his favorite scenes in all such films. He now wants to find how to wind the tape to watch his favorite scene as quickly as possible on his video player.</p>

<p>When the <strong>[play]</strong> button is pressed, the film starts at the normal playback speed. The video player has two buttons to control the playback speed: The <strong>[3x]</strong> button triples the speed, while the <strong>[1/3x]</strong> button reduces the speed to one third. These speed control buttons, however, do not take effect on the instance they are pressed. Exactly one second after playback starts and every second thereafter, the states of these speed control buttons are checked. If the <strong>[3x]</strong> button is pressed on the timing of the check, the playback speed becomes three times the current speed. If the <strong>[1/3x]</strong> button is pressed, the playback speed becomes one third of the current speed, unless it is already the normal speed.</p>

<p>For instance, assume that his favorite scene starts at 19 seconds from the start of the film. When the <strong>[3x]</strong> button is on at one second and at two seconds after the playback starts, and the <strong>[1/3x]</strong> button is on at three seconds and at five seconds after the start, the desired scene can be watched in the normal speed five seconds after starting the playback, as depicted in the following chart.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0beb6b46-3158-4622-8590-6248c98d4e85/-/preview/" style="width: 562px; height: 130px;"></p>

<p>Your task is to compute the shortest possible time period after the playback starts until the desired scene starts. The playback of the scene, of course, should be in the normal speed.</p>

### 입력 

 <p>The input consists of a single test case of the following format.</p>

<pre>t</pre>

<p>The given single integer t (0 ≤ t < 2<sup>50</sup>) is the start time of the target scene.</p>

### 출력 

 <p>Print an integer that is the minimum possible time in seconds before he can start watching the target scene in the normal speed.</p>

