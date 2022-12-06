# [Silver V] Laser Turret Maintenance - 4476 

[문제 링크](https://www.acmicpc.net/problem/4476) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>As the Chief Weapons Officer of an Imperial Star Destroyer, one of your duties is the routine maintenance of laser turret panels. Each panel is a square composed of n × n turret sockets, n of which house a turret. To avoid asymmetric wear and tear on the panel circuits, turrets should be regularly moved between sockets. Turrets are capable of rotating in-place in 45° increments, but may not fire in between such rotations. All turrets are aligned with the panel grid upon insertion.</p>

<p>The most important constraint on turret placement is that turrets should not "conflict", meaning they should not be able to shoot each other. Thus, they must be positioned such that no two turrets on the same panel share the same grid horizontal, vertical, or diagonal line. To streamline the process of turret maintenance and reduce placement errors, the Empire has mandated that all turret socket exchanges be performed as rotations or reflections of existing configurations, as conflict prevention is invariant under such transformations.</p>

<p>Given a valid (non-conflicting) n × n panel configuration, there are three clockwise rotations: 90°, 180°, and 270°. In addition there are four mirror planes: vertical, horizontal, diagonal (across the cells where row = col), and anti-diagonal (across the cells where row + col = n–1). Thus there are eight Empire-approved configurations (some of which may be identical for configurations that are symmetric under rotation by 90° and/or 180°). Figure 1 shows eight approved configurations for n=5, while Figure 2 shows an example from n=6 of a configuration with an 180° symmetry and an example from n=4 of a configuration with a 90° symmetry.</p>

<p>While the panel is a two-dimensional matrix, the nature of a valid configuration (that there is only one turret in each row) allows it to be represented by a one-dimensional vector, giving the column positions for the turret in each row. The top row of the panel has index zero, similar to the numbering of screen coordinates.</p>

<p>Write a method that receives one valid panel configuration and computes, in the same one-dimensional form, the other seven configurations that are approved by the Empire under the rotations and reflections listed above. Specifically, your program is to write back the configuration received, followed by the configurations obtained by the 90°, 180°, and 270° rotations in that order followed by the reflections in the order vertical mirror, antidiagonal mirror, horizontal mirror, and diagonal mirror.</p>

### 입력 

 <p>Input consists of an indeterminate number of lines consisting of integers separated by white space. The first integer on the line gives the size of the problem (n); zero indicates the end of processing, otherwise 4 ≤ n ≤ 20. Following that n will be n integers giving the column positions.</p>

<p> </p>

### 출력 

 <p>For each problem, print eight lines giving the approved configurations in the order specified above, in which on each line the numbers are right justified in fields of three characters. These eight lines are followed by a blank line, which is shown in Sample Output as ‘(blank line)’.</p>

