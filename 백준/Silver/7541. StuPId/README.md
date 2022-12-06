# [Silver V] StuPId - 7541 

[문제 링크](https://www.acmicpc.net/problem/7541) 

### 성능 요약

메모리: 120616 KB, 시간: 292 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>At DUT, the Dreamland University of Technology, all students have personal id, numbers with six or seven digits. But they’re not just any numbers. Only those that have a checksum with a zero as last digit can be valid ids.</p>

<p>Here’s how to compute the checksum of an id number. Multiply the digits from back to front (!) with repeating factors 9, 3, 7. Then simply add the products. Example:</p>

<pre>id number :  1  3  9  0  2  7  2
factors   :  9  7  3  9  7  3  9
products  :  9 21 27  0 14 21 18</pre>

<p>Here the checksum is 9+21+27+0+14+21+18 = 110. The last digit is zero, so the id is valid. Sometimes students have very bad handwriting and the teaching assistents have a hard time identifying the id’s. You’re asked to help in special cases, where exactly one digit is unreadable. In that case, the missing digit can be computed (there’s always exactly one correct digit, thanks to 9, 3 and 7 being relatively prime to 10). Note that the students always begin concentrated and thus the first digit will always be readable (and not zero).</p>

### 입력 

 <p>The first line contains the number of scenarios. Each scenario is a single line that contains an id number with one digit replaced by a question mark and with six or seven digits length.</p>

### 출력 

 <p>The output for every scenario begins with a line containing “Scenario #i:”, where i is the number of the scenario starting at 1. Then print a single line containing the correct id number. Terminate the output for the scenario with a blank line.</p>

