# [Bronze I] Gleaming the Cubes - 20386 

[문제 링크](https://www.acmicpc.net/problem/20386) 

### 성능 요약

메모리: 30840 KB, 시간: 108 ms

### 분류

기하학(geometry), 3차원 기하학(geometry_3d), 구현(implementation)

### 문제 설명

<p>As chief engineer of the Starship Interprize, the task of repairing the hyperstellar, cubic, transwarped-out software has fallen on your shoulders. Simply put, you must compute the volume of the intersection of anywhere from 2 to 1000 cubes.</p>

### 입력 

 <p>The input consists of several sets of cubes for which the volume of their intersections must be computed. The first line of the data contains a number (from 2 to 1000) which indicates the number of cubes which follow, one cube per line. Each line which describes a cube contains four integers. The first three integers are the x, y, and z coordinates of the corner of a cube, and the fourth integer is the positive distance which the cube extends in each of the three directions (parallel to the x, y, and z axes) from that corner.</p>

<p>Following the data for the first set of cubes will be a number which indicates how many cubes are in a second set, followed by the cube descriptions for the second set, again one per line. Following this will be a third set, and so on.</p>

<p>Note that the data will always contain at least one set of cubes, and every set will contain at least 2 and at most 1000 cubes. For any given set of cubes, the volume of their intersections will not exceed 1,000,000 units.</p>

### 출력 

 <p>Your program should continue to process sets of cubes, outputting the volume of their intersections to the output, one set per line, until a zero is read for the number of cubes.</p>

