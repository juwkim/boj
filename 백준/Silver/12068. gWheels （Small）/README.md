# [Silver IV] gWheels (Small) - 12068 

[문제 링크](https://www.acmicpc.net/problem/12068) 

### 성능 요약

메모리: 110544 KB, 시간: 340 ms

### 분류

브루트포스 알고리즘, 수학, 정수론

### 제출 일자

2023년 12월 23일 08:09:34

### 문제 설명

<p>A typical mountain bike has two groups of gears: one group connected to the pedals, and one group connected to the rear tire. A gear group consists of many gears, which usually have different numbers of teeth. A chain connects one of the gears in the pedal gear group to one of the gears in the tire gear group, and this determines the ratio between the cyclist's pedaling speed and the tire speed. For example, if the chain connects a gear with 5 teeth on the pedals to a gear with 10 teeth on the tires, the ratio will be 1/2, since the cyclist needs to make the pedal gear rotate twice to make the tire rotate once. The cyclist can change the chain to connect any one gear from the pedal group to any one gear from the tire group.</p>

<p>You have just bought a special new mountain bike with <em>three</em> groups of gears: one connected to the pedals, one connected to the tire, and one extra group in between. This mountain bike has two chains; the first chain must always connect one gear from the pedal gear group to one gear on the extra gear group, and the second chain must always connect one gear from the extra gear group to one gear on the tire gear group. Moreover, the two chains cannot both use the same gear from the extra gear group.</p>

<p>Given the numbers of teeth on the available gears on the pedals, extra, and tire groups, is it possible to make the ratio (between pedaling speed and tire speed) be exactly <strong>P/Q</strong>? For a given set of gears, you may need to answer multiple such questions.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each begins with one line with 3 integers <strong>N<sub>p</sub></strong>, <strong>N<sub>e</sub></strong>, and <strong>N<sub>t</sub></strong>, representing the numbers of gears on the pedals, extra, and tire groups. Then, three more lines follow. These contain <strong>N<sub>p</sub></strong>, <strong>N<sub>e</sub></strong>, and <strong>N<sub>t</sub></strong> integers, respectively, representing the numbers of teeth on the different gears on the pedals, extra, and tire gear groups, respectively. (It is guaranteed that the numbers of teeth on the gears within a group are all distinct.) The next line after that consists of one integer, <strong>M</strong>, the number of questions. Finally, there are <strong>M</strong> lines, each with 2 integers, <strong>P</strong> and <strong>Q</strong>, representing the target ratio. (It is not guaranteed that this ratio is a reduced fraction.)</p>

### 출력 

 <p>For each test case, first output one line containing "Case #x:", where x is the test case number (starting from 1). Then output one line for each question within the test case, in the order that the questions were presented: <code>Yes</code> if it's possible to make the ratio <strong>P/Q</strong>, and <code>No</code> if it's impossible.</p>

