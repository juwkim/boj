# [Silver II] Autobus - 32970 

[문제 링크](https://www.acmicpc.net/problem/32970) 

### 성능 요약

메모리: 110760 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘, 파싱, 문자열

### 제출 일자

2025년 3월 23일 22:39:06

### 문제 설명

<p>Mr. Malnar decided to visit one of the few cities he has not yet visited, Wroclaw (Pol. <em>Wrocław</em>), located in the southwest of Poland. Since he hadn’t traveled by bus for a long time, he missed the experience; however, he was disappointed to learn that there is no direct bus line between Zagreb and Wroclaw.</p>

<p>The best alternative is transferring in the Austrian city of Graz. Mr. Malnar found a timetable, i.e., a list of bus lines operating on the routes <em>Zagreb-Graz</em> and <em>Graz-Wroclaw</em>. A bus on a specific route runs daily, departing exactly at the start of the departure time minute and arriving precisely at the end of the last minute of the arrival time. The time required for transferring is negligible, i.e., it is possible to board a bus if you arrive at the destination before the bus you wish to transfer to departs (the arrival time of the first bus must be strictly less than the departure time of the second bus).</p>

<p>Determine the shortest time required to travel from Zagreb to Wroclaw.</p>

### 입력 

 <p>The first line contains a positive integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>200</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ n ≤ 200$</span></mjx-container>), the number of bus lines.</p>

<p>In the next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines, the names of two cities connected by the symbol "<code>-</code>" are given in order, the first representing the departure city and the second the destination city, followed by the departure time and arrival time in the format <code>h:mm--h:mm</code>, where <code>h</code> represents the hours, and <code>mm</code> represents the minutes of that time. Note that <strong>two</strong> digits for minutes will always be shown. If the number of minutes is a single digit, a leading zero will be included. It is guaranteed that each trip (without transfers) will last at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$24$</span></mjx-container> hours.</p>

### 출력 

 <p>If it is possible to travel from Zagreb to Wroclaw, print the travel time in the first line in the format <code>h:mm</code> (described above).</p>

