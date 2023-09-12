# [Bronze III] XOR 1 - 5497 

[문제 링크](https://www.acmicpc.net/problem/5497) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

해 구성하기

### 문제 설명

<p>You are implementing an application for a mobile phone, which has a black-and-white screen. The x-coordinates of the screen start from the left and the y-coordinates from the top, as shown in the figures. For the application, you need various images, which are not all of the same size. Instead of storing the images, you want to create the images using the phone’s graphics library. You may assume that at the start of drawing an image, all pixels of the screen are white. The only graphics operation in the phone’s library is <code>XOR(L,R,T,B)</code>, which will reverse the pixel values in the rectangle with top left coordinate (<code>L</code>,<code>T</code>) and bottom right coordinate (<code>R</code>,<code>B</code>), where <code>L</code> stands for the left, <code>T</code> for the top, <code>R</code> for the right and <code>B</code> for the bottom coordinate. Note that in some other graphics libraries the order of the arguments is different.</p>

<p>As an example, consider the image in Figure-3. Applying <code>XOR(2,4,2,6)</code> to an all white image gives the image in Figure-1. Applying <code>XOR(3,6,4,7)</code> to the image of Figure-1 gives the image in Figure-2, and applying <code>XOR(1,3,3,5)</code> to the image in Figure-2 finally gives the image in Figure-3</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/64a2724d-4502-42c9-a046-cdcfb2bc9ea2/-/crop/309x314/0,0/-/preview/" style="width: 154px; height: 156px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/64a2724d-4502-42c9-a046-cdcfb2bc9ea2/-/crop/315x314/343,0/-/preview/" style="width: 158px; height: 157px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/64a2724d-4502-42c9-a046-cdcfb2bc9ea2/-/crop/311x314/691,0/-/preview/" style="width: 156px; height: 157px;"></td>
		</tr>
		<tr>
			<td>Figure-1</td>
			<td>Figure-2</td>
			<td>Figure-3</td>
		</tr>
	</tbody>
</table>

<p>Given a set of black-and-white pictures, your task is to generate each picture from an initially white screen using as few <code>XOR</code> calls as you can. You are given the input files describing the images, and you are to submit files including the required <code>XOR</code> call parameters, not a program to create these files.</p>

### 입력 

 <p>You are given 10 problem instances in the text files named xor1.in to xor10.in. Each input file is organized as follows. The first line of an input file contains one integer N, 5 ≤ N ≤ 2000, meaning that there are N rows and N columns in the image. The remaining lines represent the rows of the image from top to bottom. Each line contains N integers: the pixel values in the row from left to right. Each of these integers is either a 0 or a 1, where 0 represents a white pixel and 1 represents a black pixel.</p>

### 출력 

 <p>The first line contains an integer K: the number of <code>XOR</code> calls specified in the file. The following K lines represent these calls from the first call to the last call to be executed. Each of these K lines contains four integers: the <code>XOR</code> call parameters <code>L</code>, <code>R</code>, <code>T</code>, <code>B</code> in that order.</p>

