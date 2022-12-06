# [Silver V] Does This Make Me Look Fat? - 9979 

[문제 링크](https://www.acmicpc.net/problem/9979) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 파싱(parsing), 정렬(sorting), 문자열(string)

### 문제 설명

<p>As the host of a popular daytime television talk show, you are working through the details of an upcoming episode on dieting. Your guest is the controversial Dr. Kevorkian, who has recently invented his own weight-loss plan, "Do You Want To Diet?" that guarantees to reduce your body weight by 1 pound every day.</p>

<p>You have a number of dieters scheduled to be on the show who have all been using Dr. Kevorkians new plan. You want to make the episode more dramatic by introducing your guests in decreasing order of their weights on the day of the show. The problem is that the forms you had them fill out only requested the following information: Name, Days on the diet, Weight at start of diet. Hopefully you can dredge up those long-forgotten math skills before the filming time tonight!</p>

### 입력 

 <p>Input to this problem will consist of a (non-empty) series of up to 100 data sets. Each data set will be formatted according to the following description, and there will be no blank lines separating data sets.</p>

<p>A single data set has 3 components:</p>

<ol>
	<li>Start line - A single line, "START"</li>
	<li>Dieter list - A series of 1 to 10 (inclusive) single lines consisting of three fields, with each field separated from the others by a single space:
	<ul>
		<li>Name - The dieters first name. This will be a text string containing 1 to 20 (inclusive) alphanumeric characters (no spaces).</li>
		<li>Days On Diet - The number of days the dieter has been on the "Do You Want To Diet" as of the day of the talk show. This will be a non-zero positive integer strictly less than 1000.</li>
		<li>Starting Weight - The weight, in pounds, of the dieter just before starting the diet. This will be a non-zero positive integer strictly less than 10,000.</li>
	</ul>
	</li>
	<li>End line - A single line, "END"</li>
</ol>

<p>Here are some facts that may be useful:</p>

<ul>
	<li>All dieters lost exactly 1 pound every day they were on the diet, as advertised.</li>
	<li>Nobody stayed on the diet long enough to weigh less than 1 pound at the time of the show.</li>
	<li>All dieters in a given input set will have different weights on the day of the show.</li>
	<li>All dieters in a given input set will have different names.</li>
</ul>

### 출력 

 <p>For each input data set, there will be exactly one output set, and there will be exactly one blank line separating output sets.</p>

<p>A single output set consists of a series of lines, each containing the Name of one of the dieters from the Dieter list. The list will be sorted in descending order according to weight at the time of the TV show. All dieters must be listed.</p>

