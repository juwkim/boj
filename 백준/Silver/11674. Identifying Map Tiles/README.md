# [Silver IV] Identifying Map Tiles - 11674 

[문제 링크](https://www.acmicpc.net/problem/11674) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Map websites such as Bing Maps and Google Maps often store their maps as many different image files, called tiles. The lowest zoom level (level 0) consists of a single tile with a low-detail image of the whole map, zoom level 1 consists of four tiles each containing a slightly more detailed version of a quarter of the map, and in general zoom level n contains 4 n different tiles that each contain a part of the map.</p>

<p>One way of identifying a tile is by means of a quadkey. A quadkey is a string of digits uniquely identifying a tile at a certain zoom level. The first digit specifies in which of the four quadrants of the whole map the tile lies: 0 for the top-left quadrant, 1 for the top-right quadrant, 2 for the bottom-left quadrant and 3 for the bottom-right quadrant. The subsequent digits specify in which sub quadrant of the current quadrant the tile is. The quadkeys for zoom levels 1 to 3 are shown in Figure I.1(a).</p>

<table class="table">
	<tbody>
		<tr>
			<td style="text-align: center;"><img alt="" src="" style="height:215px; width:368px"></td>
			<td style="text-align: center;"><img alt="" src="" style="height:209px; width:209px"></td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<td style="text-align: center;">(a) Quadkeys for zoom levels 1 to 3</td>
			<td style="text-align: center;">(b) Coordinates for zoom level 3</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center;">Figure I.1: Visualisation of the two representations. The images are taken from the MSDN.</td>
		</tr>
	</tfoot>
</table>

<p>Another way of identifying a tile is to give the zoom level and x and y coordinates, where (0, 0) is the left-top corner. The coordinates for the tiles of zoom level 3 are shown in Figure I.1(b). Given the quadkey of a tile, output the zoom level and x and y coordinates of that tile.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with a string s (1 ≤ length(s) ≤ 30), the quadkey of the map tile.</li>
</ul>

<p>The string s consists of only the digits ‘0’, ‘1’, ‘2’ and ‘3’.</p>

### 출력 

 <p>Output three integers, the zoom level and the x and y coordinates of the tile.</p>

