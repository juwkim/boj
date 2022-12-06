# [Silver V] Get Many Persimmon Trees - 22811 

[문제 링크](https://www.acmicpc.net/problem/22811) 

### 성능 요약

메모리: 116912 KB, 시간: 408 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Seiji Hayashi had been a professor of the Nisshinkan Samurai School in the domain of Aizu for a long time in the 18th century. In order to reward him for his meritorious career in education, Katanobu Matsudaira, the lord of the domain of Aizu, had decided to grant him a rectangular estate within a large field in the Aizu Basin. Although the size (width and height) of the estate was strictly specified by the lord, he was allowed to choose any location for the estate in the field. Inside the field which had also a rectangular shape, many Japanese persimmon trees, whose fruit was one of the famous products of the Aizu region known as 'Mishirazu Persimmon', were planted. Since persimmon was Hayashi's favorite fruit, he wanted to have as many persimmon trees as possible in the estate given by the lord.</p>

<p>For example, in Figure 1, the entire field is a rectangular grid whose width and height are 10 and 8 respectively. Each asterisk (*) represents a place of a persimmon tree. If the specified width and height of the estate are 4 and 3 respectively, the area surrounded by the solid line contains the most persimmon trees. Similarly, if the estate's width is 6 and its height is 4, the area surrounded by the dashed line has the most, and if the estate's width and height are 3 and 4 respectively, the area surrounded by the dotted line contains the most persimmon trees. Note that the width and height cannot be swapped; the sizes 4 by 3 and 3 by 4 are different, as shown in Figure 1.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">Figure 1: Examples of Rectangular Estates</p>

<p>Your task is to find the estate of a given size (width and height) that contains the largest number of persimmon trees.</p>

### 입력 

 <p>The input consists of multiple data sets. Each data set is given in the following format.</p>

<pre><i>N</i>
<i>W</i><code> </code><i>H</i>
<i>x</i><sub>1</sub><code> </code><i>y</i><sub>1</sub>
<i>x</i><sub>2</sub><code> </code><i>y</i><sub>2</sub>
...
<i>x</i><sub><i>N</i></sub><code> </code><i>y</i><sub><i>N</i></sub>
<i>S</i><code> </code><i>T</i>
</pre>

<p><i>N</i> is the number of persimmon trees, which is a positive integer less than 500. <i>W</i> and <i>H</i> are the width and the height of the entire field respectively. You can assume that both <i>W</i> and <i>H</i> are positive integers whose values are less than 100. For each <i>i</i> (1 <= <i>i</i> <= <i>N</i>), <i>x</i><sub><i>i</i></sub> and <i>y</i><sub><i>i</i></sub> are coordinates of the <i>i</i>-th persimmon tree in the grid. Note that the origin of each coordinate is 1. You can assume that 1 <= <i>x</i><sub><i>i</i></sub> <= <i>W</i> and 1 <= <i>y</i><sub><i>i</i></sub> <= <i>H</i>, and no two trees have the same positions. But you should not assume that the persimmon trees are sorted in some order according to their positions. Lastly, <i>S</i> and <i>T</i> are positive integers of the width and height respectively of the estate given by the lord. You can also assume that 1 <= <i>S</i> <= <i>W</i> and 1 <= <i>T</i> <= <i>H</i>.</p>

<p>The end of the input is indicated by a line that solely contains a zero.</p>

### 출력 

 <p>For each data set, you are requested to print one line containing the maximum possible number of persimmon trees that can be included in an estate of the given size.</p>

