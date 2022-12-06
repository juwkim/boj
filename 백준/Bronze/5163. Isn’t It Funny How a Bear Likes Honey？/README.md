# [Bronze III] Isn’t It Funny How a Bear Likes Honey? - 5163 

[문제 링크](https://www.acmicpc.net/problem/5163) 

### 성능 요약

메모리: 30840 KB, 시간: 144 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>One of the famous stories in A. A. Milne’s “The Tales of Winnie-the-Pooh” revolves around Pooh’s intent to steal some honey from a beehive high up in a tree. After failed attempts at climbing the tree, he decides to float up to the beehive with a balloon. Never mind the fact that the story involves a balloon inflated with regular air, we are going to calculate here whether a collection of helium-filled balloons is going to be enough to lift up Pooh.</p>

<p>In order to calculate that, we will give you Pooh’s weight as well as the radius of the balloons. We assume the balloons are perfectly circular. We will ignore the weight of the balloons themselves and strings. Here is what you need to know about flotation: each liter of helium (1000cm<sup>3</sup>) is enough to lift one gram of weight. As a courtesy reminder, the volume of a sphere of radius r is 4/3πr<sup>3</sup>.<sup>1</sup> (We will make sure that in the inputs, there will be no case where the buoyancy exactly compensates for the weight, i.e., no “ties”. To avoid rounding problems, we will guarantee that either the buoyancy will fall short of the required one by at least 0.001, or will exceed the required one by at least 0.001.)</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line contains an integer b and a floating point number w. b ≥ 0 is the number of balloons Pooh is using, and w is Pooh’s weight (in grams).</p>

<p>This is followed by b lines, each containing one floating point number r<sub>i</sub> ≥ 0. This is the radius of the ith balloon (in cm).</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output “Yes” or “No”, depending on whether the balloons together will be able to lift Pooh. Each data set should be followed by a blank line.</p>

