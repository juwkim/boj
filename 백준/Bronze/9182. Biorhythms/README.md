# [Bronze II] Biorhythms - 9182 

[문제 링크](https://www.acmicpc.net/problem/9182) 

### 성능 요약

메모리: 121220 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Some people believe that there are three cycles in a person's life that start the day he or she is born. These three cycles are the physical, emotional, and intellectual cycles, and they have periods of lengths 23, 28, and 33 days, respectively. There is one peak in each period of a cycle. At the peak of a cycle, a person performs at his or her best in the corresponding field (physical, emotional or mental). For example, if it is the mental curve, thought processes will be sharper and concentration will be easier. </p>

<p>Since the three cycles have different periods, the peaks of the three cycles generally occur at different times. We would like to determine when a triple peak occurs (the peaks of all three cycles occur in the same day) for any person. For each cycle, you will be given the number of days from the beginning of the current year at which one of its peaks (not necessarily the first) occurs. You will also be given a date expressed as the number of days from the beginning of the current year. You task is to determine the number of days from the given date to the next triple peak. The given date is not counted. For example, if the given date is 10 and the next triple peak occurs on day 12, the answer is 2, not 3. If a triple peak occurs on the given date, you should give the number of days to the next occurrence of a triple peak. </p>

### 입력 

 <p>You will be given a number of cases. The input for each case consists of one line of four integers (p, e, i, and d) separated by spaces. The values p, e, and i are the number of days from the beginning of the current year at which the physical, emotional, and intellectual cycle peaks, respectively. The value d is the given date and may be smaller than any of p, e, or i. All values are non-negative and at most 365, and you are guaranteed that a triple peak will occur within 21252 days of the given date. A line in which all four values are -1 indicates the end of input. </p>

### 출력 

 <p>For each test case, print the case number followed by a message indicating the number of days to the next triple peak, in the form: </p>

<pre>Case x: the next triple peak occurs in y days.</pre>

<p>where x and y are replaced by the appropriate values. </p>

