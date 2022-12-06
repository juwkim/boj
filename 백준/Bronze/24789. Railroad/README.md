# [Bronze I] Railroad - 24789 

[문제 링크](https://www.acmicpc.net/problem/24789) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

애드 혹(ad_hoc), 그래프 이론(graphs), 구현(implementation)

### 문제 설명

<p>Theta likes to play with her DUPLO railway set. The railway set she has consists of pieces of straight tracks, curved tracks, Y-shaped switches, and X-shaped level junctions, as well as bridges that allow one track to cross over another.  There are also straight tracks that are railroad crossings to allow car traffic to cross.</p>

<p>Close-ups of some of the pieces are shown below:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 200px; height: 150px;"> <img alt="" src="" style="width: 200px; height: 150px;"> <img alt="" src="" style="width: 200px; height: 150px;"></p>

<p>To play, she picks a number of X-shaped level junctions and a number of Y-shaped switches and connects them with straight and curved pieces, using bridges as necessary.</p>

<p>Because the set doesn't include any bumpers, she wants to build a closed track, like all the examples shown in the manual that came with the set:</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">Figure 1: Various track layouts possible with the DUPLO railway system. Curved pieces are shown in green, straights in red, switches in orange, level junctions in yellow, bridges in blue, and crossings in black. DUPLO is a trademark of the LEGO Group.</p>

<p>Unfortunately, sometimes, this doesn't seem to work with the number of X-shaped level junctions and Y-shaped switches she starts out with.</p>

<p>She quickly figures out exactly when it is possible to build a closed track - can you figure it out, too?</p>

<p>Write a program that outputs if it is possible to build a railroad that does not require any bumpers (i.e., which does not have any dead-end tracks).</p>

### 입력 

 <p>The input consists of a single test case with two integer numbers $X$ ($0 \le X \le 1000$) and $Y$ ($0 \le Y \le 1000$) denoting the number of level junctions and switches, respectively. You may assume that Theta has sufficiently many straight and curved pieces as well as bridges.</p>

### 출력 

 <p>Output <code>possible</code> if she can build a closed track using all level junctions and all switches without any dead ends, or <code>impossible</code> otherwise.</p>

