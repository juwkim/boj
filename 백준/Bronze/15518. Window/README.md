# [Bronze I] Window - 15518 

[문제 링크](https://www.acmicpc.net/problem/15518) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>In the building of Jewelry Art Gallery (JAG), there is a long corridor in the east-west direction. There is a window on the north side of the corridor, and <em>N</em> windowpanes are attached to this window. The width of each windowpane is <em>W</em>, and the height is <em>H</em>. The <em>i</em>-th windowpane from the west covers the horizontal range between <em>W</em> × (<em>i</em> - 1) and <em>W</em> × <em>i</em> from the west edge of the window.</p>

<p style="text-align:center"><img alt="" src="" style="height:148px; width:463px"></p>

<p style="text-align:center">Figure A1. Illustration of the window</p>

<p>You received instructions from the manager of JAG about how to slide the windowpanes. These instructions consist of <em>N</em> integers <em>x<sub>1</sub></em>, <em>x<sub>2</sub></em>, ..., <em>x<sub>N</sub></em>, and <em>x<sub>i</sub></em> ≤ <em>W</em> is satisfied for all <em>i</em>. For the <em>i</em>-th windowpane, if <em>i</em> is odd, you have to slide <em>i</em>-th windowpane to the east by <em>x<sub>i</sub></em>, otherwise, you have to slide <em>i</em>-th windowpane to the west by <em>x<sub>i</sub></em>.</p>

<p>You can assume that the windowpanes will not collide each other even if you slide windowpanes according to the instructions. In more detail, <em>N</em> windowpanes are alternately mounted on two rails. That is, the <em>i</em>-th windowpane is attached to the inner rail of the building if <em>i</em> is odd, otherwise, it is attached to the outer rail of the building.</p>

<p>Before you execute the instructions, you decide to obtain the area where the window is open after the instructions.</p>

### 입력 

 <p>The input consists of a single test case in the format below.</p>

<pre>N H W
x<sub>1</sub> ... x<sub>N</sub></pre>

<p>The first line consists of three integers <em>N</em>, <em>H</em>, and <em>W</em> (1 ≤ <em>N</em> ≤ 100, 1 ≤ <em>H</em>, <em>W</em> ≤ 100). It is guaranteed that <em>N</em> is even. The following line consists of <em>N</em> integers <em>x<sub>1</sub></em>, ..., <em>x<sub>N</sub></em> while represent the instructions from the manager of JAG. <em>x<sub>i</sub></em> represents the distance to slide the <em>i</em>-th windowpane (0 ≤ <em>x<sub>i</sub></em> ≤ <em>W</em>).</p>

### 출력 

 <p>Print the area where the window is open after the instructions in one line.</p>

