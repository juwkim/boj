# [Bronze I] Runway Planning - 10286 

[문제 링크](https://www.acmicpc.net/problem/10286) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Most airports have multiple runways. To identify runways, they are given a number indicating the direction of the runway. Such a runway number is obtained by dividing the heading of the runway in degrees by ten, rounding the result, and optionally prefixing it with a ‘0’ if the result has only a single digit. For example, a runway with a heading of 82<sup>◦</sup>is indicated by the number 08.</p>

<p>If you are paying attention, you might think “a runway can be used in both directions, and therefore has two headings, but it is only assigned one runway number.” You are correct: normally a runway is identified by two numbers, based on the direction in which the runway is used. To simplify matters, we only concern ourselves with the smallest of these two numbers, except if it is zero; we then use 18 instead. The runway numbers thus range from 01 to 18.</p>

<p>Now, you might think, “what if two runways have the same heading?” In that case, the characters ‘L’ and ‘R’ are appended to the number of the left and right runway, respectively. But what if three runways have the same heading? Then, the character ‘C’ is appended to the center runway. “But”, I can hear you ask, “what if four runways have the same heading?” If you really want to know, look up how Dallas/Fort Worth International Airport solved this problem after the contest. At any rate, we do not concern ourselves with multiple runways having the same heading in this problem, so you can forget all you read in this paragraph.</p>

<p>The runway in use is mostly determined by the current direction of the wind. It is preferred to take off and land with headwind. If it is not possible to have the wind coming from straight ahead, its direction should be as close to that as possible. For example, if an airport has the runways 05 and 15, and the wind has a heading of 70<sup>◦</sup>, taking off and landing using runway 05 is preferred, since the heading of that runway is closest to the heading of the wind.</p>

<p>Now, consider an airport already having one or more runways, and planning the construction of a new runway. Obviously, this runway should have a unique runway number: not only would we otherwise have a problem outside the boundaries of our restricted runway numbering outlined above, but, most importantly, this increases the probability of being able to take off or land with headwind.</p>

<p>The engineers at the airport under consideration have already determined the heading of the new runway, but still need you to determine the runway number. Note that the engineers are not very considerate with their input to your problem. They give you one heading of the runway, but it can be either the lowest or the highest heading of the runway. Be sure to give the lowest of the two runway numbers, as discussed in the second paragraph of this problem statement, even if you are given the highest of the two headings from the engineers.</p>

### 입력 

 <p>On the first line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with a single integer h (1 ≤ h ≤ 360): the heading of the new runway in degrees.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with the runway number of the newly constructed runway.</li>
</ul>

