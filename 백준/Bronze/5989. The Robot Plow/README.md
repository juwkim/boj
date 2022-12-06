# [Bronze I] The Robot Plow - 5989 

[문제 링크](https://www.acmicpc.net/problem/5989) 

### 성능 요약

메모리: 28776 KB, 시간: 176 ms

### 분류

구현(implementation)

### 문제 설명

<p>Farmer John has purchased a new robotic plow in order to relieve him from the drudgery of plowing field after field after field. It achieves this goal but at a slight disadvantage: the robotic plow can only plow in a perfect rectangle with sides of integer length.</p>

<p>Because FJ's field has trees and other obstacles, FJ sets up the plow to plow many different rectangles, which might end up overlapping. He's curious as to just how many squares in his field are actually plowed after he programs the plow with various plow instructions, each of which describes a rectangle by giving its lower left and upper right x,y coordinates.</p>

<p>As usual, the field is partitioned into squares whose sides are parallel to the x and y axes. The field is X squares wide and Y squares high (1 <= X <= 240; 1 <= Y <= 240). Each of the I (1 <= I <= 200) plow instructions comprises four integers: Xll, Yll, Xur, and Yur (1 <= Xll <= Xur; Xll <= Xur <= X; 1 <= Yll <= Yur; Yll <= Yur <= Y) which are the lower left and upper right coordinates of the rectangle to be plowed. The plow will plow all the field's squares in the range (Xll..Xur, Yll..Yur) which might be one more row and column than would initially be assumed (depending on how you go about your assumptions, of course).</p>

<p>Consider a field that is 6 squares wide and 4 squares high. As FJ issues a pair of plowing instructions (shown), the field gets plowed as shown by '*' and '#' (normally plowed field all looks the same, but '#' shows which were most recently plowed):</p>

<pre>    ......             **....             #####.
    ......  (1,1)(2,4) **....  (1,3)(5,4) #####.
    ......             **....             **....
    ......             **....             **....</pre>

<p>A total of 14 squares are plowed.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: X, Y, and I</li>
	<li>Lines 2..I+1: Line i+1 contains plowing instruction i which is described by four integers: Xll, Yll, Xur, and Yur</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the total number of squares plowed</li>
</ul>

<p> </p>

