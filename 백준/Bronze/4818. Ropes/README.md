# [Bronze I] Ropes - 4818 

[문제 링크](https://www.acmicpc.net/problem/4818) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>When climbing a section or “pitch”, the lead climber ascends first, taking a rope with them that they anchor to the rock for protection to ascend. Once at the top of a pitch, the lead climber has the second climber attach to the rope, so they can ascend with the safety of the rope. Once the second climber reaches the top of the pitch, the third attaches, and so on until all the climbers have ascended.</p>

<p>For example, for a 10 meter pitch and 50 meter rope, at most 6 climbers could ascend, with the last climber attaching to the end of the rope. To ascend safely, there must be at least 2 climbers and the rope must be at least as long as the pitch.</p>

<p>This process is repeated on each pitch of the climb, until the top is reached. Then to descend, the climbing rope is hung at its midpoint from an anchor (each half must reach the ground). The climbers then each rappel from this rope. The rope is retrieved from the anchor by pulling one side of the rope, slipping it though the anchor and allowing it to fall to the ground.</p>

<p>To descend safely, the rope must be at least twice as long as the sum of the lengths of the pitches.</p>

<p>For example, a 60 meter rope is required to rappel from a 30 meter climb, no matter how many climbers are involved.</p>

<p>Climbing ropes come in 50, 60 and 70 meter lengths. It is best to take the shortest rope needed for a given climb because this saves weight. You are to determine the maximum number of climbers that can use each type of rope on a given climb.</p>

### 입력 

 <p>The input consists of a number of cases. Each case specifies a climb on a line, as a sequence of pitch lengths as in:</p>

<pre>N P<sub>1</sub> P<sub>2</sub> ... P<sub>N</sub></pre>

<p>Here N is the positive number of pitches, with 1 ≤ N ≤ 100, and Pk is the positive integer length (in meters) of each pitch, with 1 ≤ P<sub>k</sub> ≤ 100. The last line (indicating the end of input) is a single 0.</p>

### 출력 

 <p>Three numbers for each climb separated by a space, indicating the maximum number of climbers that could use the 50, 60, or 70 meter rope lengths, respectively. State 0 if the given rope length is not suitable for that climb.</p>

