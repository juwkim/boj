# [Bronze II] Aerospace & Mechanical Engineering - 5190 

[문제 링크](https://www.acmicpc.net/problem/5190) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 수학(math), 물리학(physics)

### 문제 설명

<p>Aerospace Engineers and Mechanical Engineers like to build machines that do something exciting in the physical world. Aerospace engineers like building airplanes, rockets, and other stuff that flies. Not all of it is rocket science, though. Some questions are well within the grasp of programming contestants. For instance, once you have built a rocket launch it, you want to know how high it can fly before it lands.</p>

<p>Here is our model: the rocket consists of n stages, which are essentially fuel tanks. A stage lasts for a certain amount of time, and after it is empty, it is discarded. After the last fuel tank is discarded, the rocket cannot accelerate any more. As the rocket sheds its stages, it becomes lighter and lighter. We assume that the rocket itself weights M > 0 kilograms (kg), i.e., after shedding all its stages, the leftover weight is M.</p>

<p>In addition to M, you will be given, for each of the rocket’s stages i, its weight mi ≥ 0, the duration for which it lasts ti ≥ 0 (in seconds s), and the amount of thrust (force) it produces during that time Fi ≥ 0 (in kg m/s<sup>2</sup> ), where m stands for meters. We will pretend that the rocket fuel itself does not weigh anything. We assume that the rocket is shot straight up, and ignore all effects of wind, friction, leaving the Earth’s gravity field, etc. We also assume that the initial speed of the rocket is 0 m/s, until the first stage starts burning. </p>

<p>The important physical formulas you will need are: (1) a = F/m, i.e., the acceleration of an object of mass m under force F is a = F/m. (2) In the Earth’s gravity field, any object accelerates toward the Earth at a constant acceleration of g = 9.81 m/s<sup>2</sup> . (3) If an object starts out with velocity v, and accelerates at acceleration a, then in t seconds, it travels distance vt + 1/2at<sup>2</sup>, and its new speed after those t seconds is v + at. </p>

<p>Assume that fuel tanks are used (and discarded) in the order 1, 2, . . . , n. You are to compute the height at which the rocket was right when the last stage fell off. Our inputs will always be such that the rocket will lift off, and not crash into the Earth before the last stage is discarded.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains the number of stages n (between 1 and 30), and the weight M of the rocket itself. M is a floating point number strictly greater than 0.</p>

<p>This is followed by n lines, each consisting of three non-negative floating point numbers mi,ti, Fi, describing a stage. So the initial weight of the rocket is M + Σ<sub>i</sub>mi.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the height at which the rocket was when the last stage fell off, rounded to two decimals.</p>

