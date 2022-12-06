# [Bronze II] Fall 2006: 100 Years of Engineering - 11018 

[문제 링크](https://www.acmicpc.net/problem/11018) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

물리학(physics)

### 문제 설명

<p>In Fall of 2006, we were celebrating 100 years of engineering at USC. To join in the fun, the contest was titled “100 Years of Engineering”, and had a problem for most of our engineering departments. Here, you get to learn about Aerospace and Mechanical Engineering. Aerospace engineers like building airplanes, rockets, and other stuff that flies. Not all of it is rocket science, though. Some questions are well within the grasp of programming contestants. For instance, once you have built a rocket to launch, you want to know how high it can fly before it lands.</p>

<p>Here is our model: the rocket consists of n stages, which are essentially fuel tanks. A stage lasts for a certain amount of time, and after it is empty, it is discarded. After the last fuel tank is discarded, the rocket cannot accelerate any more. As the rocket sheds its stages, it becomes lighter and lighter. We assume that the rocket itself weights M > 0 kilograms (kg), i.e., after shedding all its stages, the leftover weight is M.</p>

<p>In addition to M, you will be given, for each of the rocket’s stages i, its weight m<sub>i</sub> ≥ 0, the duration for which it lasts t<sub>i</sub> ≥ 0 (in seconds s), and the amount of thrust (force) it produces during that time F<sub>i</sub> ≥ 0 (in kg·m/s<sup>2</sup> ), where m stands for meters. We will pretend that the rocket fuel itself does not weigh anything. We assume that the rocket is shot straight up, and ignore all effects of wind, friction, leaving the Earth’s gravity field, etc. We also assume that the initial speed of the rocket is 0 m/s, until the first stage starts burning.</p>

<p>The important physical formulas you will need are: (1) a = F/m, i.e., the acceleration of an object of mass m under force F is a = F/m. (2) In the Earth’s gravity field, any object accelerates toward the Earth at a constant acceleration of g = 9.81 m/s<sup>2</sup> . (3) If an object starts out with velocity v, and accelerates at acceleration a, then in t seconds, it travels distance vt + (1/2)at<sup>2</sup>, and its new speed after those t seconds is v + at.</p>

<p>Assume that fuel tanks are used (and discarded) in the order 1, 2, . . . , n. You are to compute the height at which the rocket was right when the last stage fell off. Our inputs will always be such that the rocket will lift off, and not crash into the Earth before the last stage is discarded.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains the number of stages n (between 1 and 30), and the weight M of the rocket itself. 0.01 ≤ M ≤ 1,000,000 is a floating point number.</p>

<p>This is followed by n lines, each consisting of three non-negative floating point numbers 0.01 ≤ m<sub>i</sub>, t<sub>i</sub>, F<sub>i</sub> ≤ 1,000,000, describing a stage. So the initial weight of the rocket is M + Σ<sub>i</sub>m<sub>i</sub>.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the height at which the rocket was when the last stage fell off, rounded to two decimals.</p>

<p>Each data set should be followed by a blank line.</p>

