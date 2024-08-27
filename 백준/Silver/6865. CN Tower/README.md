# [Silver III] CN Tower - 6865 

[문제 링크](https://www.acmicpc.net/problem/6865) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2024년 8월 28일 08:25:56

### 문제 설명

<p>Christy C. Coder is traveling to Waterloo for a programming competition. On the way, she stops in Toronto to do some sightseeing. The unfortunate thing about traveling is that everyone back home expects her to bring back pictures of everything. Christy hates taking pictures: it makes her look like such a tourist! Fortunately, Christy has a plan to make her picture-taking quite painless.</p>

<p>At 553m tall, CN Tower is the world's tallest free-standing building. 351m up the tower is the "360" rotating restaurant, which rotates a full 360 degrees every 72 minutes. From there, Christy can see the whole city, and take close-up pictures of all the landmarks using her fancy new 100x optical zoom camera. Since the restaurant it self rotates, she only needs to stand in one place to take pictures in all directions.</p>

<p>The waiters insist that she order something or leave, and Christy is not interested in any of the items on the menu. Therefore, she must act quickly before she gets kicked out. Given the locations of the landmarks of which Christy wants to take a picture, your task is to determine the minimum amount of time that she must spend in the restaurant in order for it to rotate enough to bring all the landmarks in view. Assume that Christy always points her camera exactly perpendicular to the window to minimize distortion due to the glass. Note that multiple landmarks may occupy the same (angular) position, and these landmarks would only require one photograph to capture them.</p>

<p>Since the restaurant staff only realize she is a tourist once she starts taking pictures, we begin measuring the time required once she takes her first picture. Therefore, Christy can move to any position in the restaurant without hassle from the restaurant staff and begin taking pictures from there.</p>

### 입력 

 <p>The first line of input consists of an integer n (2 ≤ n ≤ 1000), the number of landmarks Christy wants to photograph. Each of the following n lines specify a landmark. Each landmark specification consists of the landmark name (a string of uppercase and lowercase letters of length at most 40 characters), a space, and the compass angle d, in degrees, to the landmark from the CN Tower (0 = north, 90 = east, 180 = south, 270 = west). Note that d is a real number which satisfies 0 ≤ d < 360, with d specified to the hundredth of a degree (i.e., at most two decimal places).</p>

### 출력 

 <p>A single integer, the minimum number of seconds that Christy must remain in the restaurant. If the time is not an integer number of seconds, round it up to the nearest second (i.e., take the ceiling of the number).</p>

