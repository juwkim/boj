# [Silver III] Making the Grade - 6490 

[문제 링크](https://www.acmicpc.net/problem/6490) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 6월 21일 19:45:58

### 문제 설명

<p>Mr. Chips has a simple grading scheme that lends itself to automated computation.  You will write a program that will read in his students' grades, bonus points, and attendance record, compute the student's grades, and output the average grade point of the class.</p>

<p>Problem Statement: Mr. Chips grades as follows.  All tests are based on 100 points and all test grades are between 0 and 100 points. If he has given more than 2 tests then he will drop the lowest test grade for each student before computing student averages.  After computing student averages he computes the overall class average (mean) and standard deviation (sd). The cutoff points for grades are: an average >= one sd above the mean is an A, an average >= the mean but < one sd above the mean is a B, an average >= one sd below the mean but < the mean is a C, and an average < one sd below the mean is a D.  For every two bonus points accrued by a student Mr. Chips increases their computed average by 3 percentage points. Thus, if students have one bonus point, their averages are not bumped at all.  If they have 4 or 5 bonus points, their averages are bumped by 6 percentage points, and so on. Bumping of averages based on bonus points takes place after the grade cutoff points have been determined.  Finally, for every 4 absences, students lose one letter grade (from A to B, B to C, C to D, and D to F).  For example, if they have 9 absences they will lose two letter grades. Students cannot get a grade lower than F. If students have perfect attendance, they gain one letter grade; although they cannot get a grade higher than an A.  During his computations, Mr. Chips always rounds his results to the nearest tenth. In summary, Mr. Chips drops a student's lowest test grade if more than 2 tests have been administered, computes each student's average, computes the class mean and sd, adjusts the students' averages based on bonus points, determines the student's unadjusted grades, and then adjusts the grades based on attendance.</p>

<p>The average grade point of a class is determined by using 4 points for each A, 3 points for each B, 2 points for each C, 1 point for each D, and 0 points for each F.  The total points for the class are added together and divided by the number of students in the class (which is always at least 2).</p>

<p>The standard deviation sd of a list of numbers x<sub>1</sub>, ..., x<sub>n</sub> is:    [graphic deleted]</p>

<p>If the calculated standard deviation is less than 1 then Mr. Chips uses 1 in place of the standard deviation for grade calculation.</p>

<p>Suppose Mr. Chips has 5 students and has given 3 tests. The following table shows the grades, number of bonuses and days absent, plus the computed average (with lowest test dropped), the adjusted average (with bonus), the unadjusted grade and the adjusted grade (with attendance). The mean and sd used to determine letter grade cutoffs are 69.0 and 20.1. For example, for an unadjusted B, one's average must be greater than or equal to 69.0 and less than 89.1.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>T1</td>
			<td>T2</td>
			<td>T3</td>
			<td>Bns</td>
			<td>Abst</td>
			<td>Avg</td>
			<td>AdjAvg</td>
			<td>Grade</td>
			<td>AdjGrd</td>
		</tr>
		<tr>
			<td>100</td>
			<td>100</td>
			<td>80</td>
			<td>3</td>
			<td>2</td>
			<td>100.0</td>
			<td>103.0</td>
			<td>A</td>
			<td>A</td>
		</tr>
		<tr>
			<td>80</td>
			<td>80</td>
			<td>80</td>
			<td>0</td>
			<td>5</td>
			<td>80.0</td>
			<td>80.0</td>
			<td>B</td>
			<td>C</td>
		</tr>
		<tr>
			<td>60</td>
			<td>20</td>
			<td>70</td>
			<td>5</td>
			<td>3</td>
			<td>65.0</td>
			<td>71.0</td>
			<td>B</td>
			<td>B</td>
		</tr>
		<tr>
			<td>40</td>
			<td>40</td>
			<td>40</td>
			<td>5</td>
			<td>0</td>
			<td>40.0</td>
			<td>46.0</td>
			<td>D</td>
			<td>C</td>
		</tr>
		<tr>
			<td>100</td>
			<td>20</td>
			<td>20</td>
			<td>1</td>
			<td>9</td>
			<td>60.0</td>
			<td>60.0</td>
			<td>C</td>
			<td>F</td>
		</tr>
	</tbody>
</table>

<p>avg grd pnt is 2.2</p>

### 입력 

 <p>The first line contains an integer N between 1 and 10 describing how many of Mr. Chip's classes are represented in the input.  The first line for each class contains two integers S and T. S is the number of students in the class (1 < S < 31) and T is the number of tests the students took (1 < T < 11).  The next S lines will each represent one student in the class. A student line first lists each of their T test scores as integers between 0 and 100 inclusive, and then lists their bonus points and their number of absences.</p>

### 출력 

 <p>There should be N+2 lines of output.  The first line of output should read MAKING THE GRADE OUTPUT.   There will then be one line of output for each of Mr. Chip's classes showing that class's average grade point. The final line of output should read END OF OUTPUT.</p>

