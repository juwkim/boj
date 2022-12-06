# [Bronze I] What is the air speed velocity... - 9159 

[문제 링크](https://www.acmicpc.net/problem/9159) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>...of a fully laden swallow? This fearful question was posed to the intrepid band of Grail searchers. Their response of “African or European?” was partly correct. The air speed would most definitely depend on the sub-species of swallow. King Arthur, fearing more intense questioning in this vein, ordered his royal mathematicians to determine the air speed of a fully laden swallow – both African and European.</p>

<p>The mathematicians called upon the royal birders to capture a number of swallows of both types, lade them fully, and then release them from point A and time their arrival at point B. Since they didn’t want to confuse their figures, the European and African swallows were each started from a different location, so that each group flew a different distance, but all swallows in the same group flew the same distance. They then asked the royal map-makers to determine the distance (measured in furlongs) between the two starting points and the finish point. Using 10 swallows of each type, the royal mathematicians would then compute the average air speed for each group.</p>

<p>However, the royal mathematicians were somewhat lazy. After gathering all the data, they decided it was MUCH too hard to do all those nasty calculations by hand. So, they quickly constructed a time machine and have come into the future to enlist your help: they need you to write a program to do the calculations, which they will then take back into the past with them. Thus the searchers of the Grail will be saved from certain doom, (should this dastardly question be posed again), and you will go down in history as a hero. (Well, maybe not history, since they are from the past, so maybe you’ll go down in futurory?)</p>

<p>There’s one tricky bit (you knew it was coming): the royal mathematicians cannot agree on exactly how the average should be calculated. Some believe that, for each group, one should add up all of the times and then divide the total distance covered by all the swallows of that type by the total time (this is method 1). Others are of the opinion that the average speed is determined by computing the speed for each swallow, summing those values and then dividing that total by the total number of swallows (this is method 2). Your program should compute the average both ways, to avoid a nasty falling out among the royal mathematicians.</p>

<p>The input provided by the royal mathematicians is somewhat disorganized – the two breeds’ times have been intermixed and they weren’t too careful about capitalization. But each entry is on a separate line and marked with an ‘A’ or ‘a’ or ‘E’ or ‘e’ to aid in identification. Each line begins with this single letter, followed by a single space. The final datum on the line is the elapsed time the swallow flew, expressed in hours. Since the time-keeping of the era wasn’t very accurate, this value is simply a real number (> 0) with a single level of precision, such as 1.5 (one and a half hours), or 0.4 (four-tenths of an hour).</p>

### 입력 

 <p>The very first line of the input file will consist of 2 integers, both greater than 0, separated by a single space. The first integer is the distance the African swallows flew and the second integer is the distance the European swallows flew. Next come the times for the swallows (20 lines total: 10 for African, 10 for European – NOT in this order). Thus the input file has a total of 21 lines.</p>

<p> </p>

### 출력 

 <p>The format for the output should be grouped by methods, with Method 1 being displayed first. Each method will produce 3 lines of output:</p>

<ul>
	<li>Line 1: the name of the method (capitalized, with a digit identifying it), e.g. “Method 1” (the quotes are not part of your output.)</li>
	<li>Line 2: the speed of a fully-laden African swallow (expressed in furlongs per hour), e.g. “African: 3.00 furlongs per hour” (the quotes are not part of your output.)</li>
	<li>Line 3: the speed of a fully-laden European swallow (expressed in furlongs per hour) e.g. “European: 3.00 furlongs per hour” (the quotes are not part of your output.)</li>
</ul>

<p>The format for the data for each method is as follows:</p>

<ul>
	<li>The full name of the breed of swallow (capitalized), beginning with African</li>
	<li>A colon</li>
	<li>A single space</li>
	<li>The speed (to two digits of accuracy, with leading 0 for values < 1.0)</li>
	<li>A single space</li>
	<li>The phrase “furlongs per hour” (the quotes are not part of the output).</li>
</ul>

<p>See the Sample output section below for any clarifications you require.</p>

