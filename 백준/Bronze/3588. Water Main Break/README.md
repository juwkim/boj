# [Bronze I] Water Main Break - 3588 

[문제 링크](https://www.acmicpc.net/problem/3588) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>A few weeks ago, in fact, right after restrictions on water usage by individuals had been announced, a water main broke right on the campus of our friends in Westwood. You may recall the images of a completely flooded campus, with entire garages underwater and students kayaking around. It took LADWP half an eternity to fix, and by the time they had fixed it, 20 million gallons of water<sup>1</sup> had been wasted. Given the aging infrastructure we have (many water pipes in the US are 100 years old), we should expect this to be quite regular. And in fact, water main breaks do happen on a regular basis.</p>

<p>In this problem, you will be given information on a number of water main breaks: when they started, when they ended, and at what rate the water flowed out. You will also be given a time interval, and are to compute how much water in total was wasted during that interval.</p>

<p><sup>1</sup>That corresponds to the combined daily water usage of about 130,000 LA residents.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of a data set contains three integers a single integer 0 ≤ n ≤ 30: the total number of water main breaks. The next line contains two integers 0 ≤ s ≤ f ≤ 1000. [s, f] is the interval (in seconds) during which you are to compute the water wasted; s is the start time, and f is the finish time. This is followed by n lines, each describing a water main break. Each line i contains three integers s<sub>i</sub>, f<sub>i</sub>, r<sub>i</sub>. 0 ≤ s<sub>i</sub> ≤ f<sub>i</sub> ≤ 1000 are the start and finish time of the water main break, in seconds. 0 ≤ r<sub>i</sub> ≤ 1000 is the rate at which water flows out of the pipe, given in gallons per second.</p>

<p>Notice that the water main break is fixed at time fi+1, so that ri gallons of water leave at times s<sub>i</sub>, s<sub>i+1</sub>, s<sub>i+2</sub>, . . . , f<sub>i−1</sub>, f<sub>i</sub></p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then, on a line by itself, print the total number of gallons of water that have been wasted during the interval [s, f]. Notice that we thus count water that is leaking at times s, s + 1, . . . , f − 1, f.</p>

<p>Each data set should be followed by a blank line.</p>

