# [Bronze II] Draw - 26554 

[문제 링크](https://www.acmicpc.net/problem/26554) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

구현

### 제출 일자

2024년 9월 30일 03:06:52

### 문제 설명

<p>You’re bored during class one day. Instead of drawing shapes all over your paper, you decide to write a program that will do it for you! Write a program that, when given the type of shape and the dimensions, will draw the specified shape. The program will also be able to either leave the shape empty or fill it in. The shape names and examples are shown below.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>rectangle</td>
			<td>
			<pre>##
##</pre>
			</td>
			<td>
			<pre>###
# #
###</pre>
			</td>
			<td>
			<pre>###
###
###</pre>
			</td>
		</tr>
		<tr>
			<td>left triangle</td>
			<td>
			<pre>#
##
###</pre>
			</td>
			<td>
			<pre>#
##
# #
####</pre>
			</td>
			<td>
			<pre>#
##
###
####</pre>
			</td>
		</tr>
		<tr>
			<td>right triangle</td>
			<td>
			<pre>  #
 ##
###</pre>
			</td>
			<td>
			<pre>   #
  ##
 # #
####</pre>
			</td>
			<td>
			<pre>   #
  ##
 ###
####</pre>
			</td>
		</tr>
		<tr>
			<td>diamond</td>
			<td>
			<pre> #
# #
 #</pre>
			</td>
			<td>
			<pre>  # 
 # #
#   #
 # #
  #</pre>
			</td>
			<td>
			<pre>  #
 ###
#####
 ###
  #</pre>
			</td>
		</tr>
	</tbody>
</table>

<p>The rectangle can be any number of rows and columns. The left triangle, the right triangle, and the diamond will always have the same number of rows and columns. For the diamond, the number of rows and columns will always be odd.</p>

### 입력 

 <p>The first line will contain a single integer n that indicates the number of data sets that follow. Each data set will be one line that starts with the shape name. If the shape is a rectangle, the name will be followed by two integers, r and c, representing the number of rows and columns respectively. If not, then the shape name will be followed by one integer, denoting the number of both rows and columns. The line will end with either y or n, y meaning that the shape is filled in and n meaning that the shape is empty.</p>

### 출력 

 <p>You will print the specified shape of the specified size, either filled or empty as denoted by the letter at the end of the line. There are examples of the shapes in the table above. There are no lines of whitespace between data sets.</p>

