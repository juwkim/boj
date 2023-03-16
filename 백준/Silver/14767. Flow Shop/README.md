# [Silver IV] Flow Shop - 14767 

[문제 링크](https://www.acmicpc.net/problem/14767) 

### 성능 요약

메모리: 125164 KB, 시간: 352 ms

### 분류

구현, 다이나믹 프로그래밍

### 문제 설명

<p>Sean’s Swathers makes custom swathers (equipment used to harvest grain). All swathers go through the same basic stages in their construction: for example they all need to have a cutting bar, a grain belt, and a reel fitted. However, these components can be customized based on the buyer’s needs, so these various stages may take different amounts of time between different swathers.</p>

<p>N swathers have been ordered and there are M stages in the manufacturing process. The swathers will each go through the same sequence of stages.</p>

<p>In particular, the processing occurs as follows: For each swather i and each stage j, it takes Pi,j units of time to complete stage j for swather i. The workers at each stage may only work on one swather at a time. At the start of the day all swather orders are ready to be processed by the first stage. At any point in the process, if the workers at stage j are idle and there are swathers waiting to be processed at this stage then the workers will pick the swather that has the lowest label (they are labelled from 1 to N). Note that the work on a stage j can only be started after the work on the stage j − 1 is completed.</p>

<p>Determine the time each swather is completed.</p>

### 입력 

 <p>There is only one test case in each file. It begins with a single line containing N and M (1 ≤ N, M ≤ 1000), the number of swathers and stages (respectively). Following this are N lines, each with M integers. The j’th integer of the i’th line is P<sub>i,j</sub> , giving the amount of time it will take for the workers at stage j to complete swather i (1 ≤ P<sub>i,j</sub> ≤ 10<sup>6</sup>).</p>

### 출력 

 <p>Output a single line containing N integers T<sub>1</sub> T<sub>2</sub> . . . T<sub>n</sub> with a single space between consecutive integers. These should be such that stage M for swather i is completed at time T<sub>i</sub>.</p>

