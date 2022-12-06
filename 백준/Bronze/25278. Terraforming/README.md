# [Bronze III] Terraforming - 25278 

[문제 링크](https://www.acmicpc.net/problem/25278) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Humanity's effort to turn Mars into a liveable planet is, in the words of World Government communicator Levi Uken (2315 A.D.), an "endeavour so great that it will take the united effort of mankind to accomplish."</p>

<p>At the beginning of the terraforming endeavour Mars has no oceans, no oxygen, and a mean temperature of $-30$ degrees Celsius.</p>

<p>Water</p>

<p>To enable a stable hydrological cycle, air moisture, weather patterns, and to moderate temperature swings, Mars needs $9$\% ocean coverage.</p>

<p>Temperature</p>

<p>At very low temperatures, oceans are actually glaciers for most of the year. Although the temperature on Mars in the $21$st century already reaches $20$ degree Celsius on 'hot’ summer days, its average is far below freezing. To enable liquid oceans, the temperature has to stay positive, at least at the equator, corresponding to a mean temperature of $+8$ degrees Celsius.</p>

<p>Oxygen</p>

<p>The most important parameter for terraforming is the oxygen level---without a breathable atmosphere, Mars is not liveable for humans. Earth’s oxygen content is $21\%$ of the atmosphere at sea level. However, already $14\%$ is perfectly livable for humans, such as Bolivian cities El Alto ($4150$ m) and La Paz ($3640$ m), each with nearly a million inhabitants in the $21$st century.</p>

### 입력 

 <p>On the first line, the number $n\in\{1,\ldots, 315\}$ of environmental changes on Mars. Each of the following $n$ lines consists of a parameter (oxygen, ocean, or temperature), followed by an integer.</p>

<p>The change for oxygen and oceans is in percentage points, the change for temperature is in degrees Celsius.</p>

### 출력 

 <p>If the environmental changes achieve at least $9$\% ocean coverage, at least $14\%$ oxygen, and at least $+8$ degrees celsius, output 'liveable'. Otherwise, output 'not liveable'.</p>

