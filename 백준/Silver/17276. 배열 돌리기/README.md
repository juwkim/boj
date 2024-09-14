# [Silver II] 배열 돌리기 - 17276 

[문제 링크](https://www.acmicpc.net/problem/17276) 

### 성능 요약

메모리: 124948 KB, 시간: 352 ms

### 분류

구현

### 제출 일자

2024년 9월 14일 20:40:28

### 문제 설명

<p>크기가 n x n인 2차원 정수 배열 X가 있다. (n은 홀수)</p>

<p>X를 45° 의 배수만큼 시계방향 혹은 반시계방향으로 돌리려고 한다. X를 시계 방향으로 45° 돌리면 아래와 같은 연산이 동시에 X에 적용되어야 한다:</p>

<ul>
	<li>X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.</li>
	<li>X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. </li>
	<li>X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.</li>
	<li>X의 가운데 행을 X의 주 대각선으로 옮긴다.</li>
	<li>위 네 가지 경우 모두 원소의 기존 순서는 유지 되어야 한다.</li>
	<li>X의 다른 원소의 위치는 변하지 않는다.</li>
</ul>

<p>반시계 방향으로 45° 돌리는 경우도 위와 비슷하게 정의된다.</p>

<p>예를 들어, 아래 그림 중앙에 5x5 배열 X가 있고, 이 배열을 시계방향 혹은 반시계방향으로 45° 돌렸을 때의 결과가 우측 그리고 좌측에 있다. 굵은 원소는 주 대각선 / 중간 열 / 부 대각선 / 중간 행에 위치한 원소이다.</p>

<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 33%; text-align: center;">
			<table class="table table-bordered" style="width: 100%;">
				<tbody>
					<tr>
						<td style="width: 20%;"><strong>3</strong></td>
						<td style="width: 20%;">2</td>
						<td style="width: 20%;"><strong>5</strong></td>
						<td style="width: 20%;">4</td>
						<td style="width: 20%;"><strong>15</strong></td>
					</tr>
					<tr>
						<td style="width: 20%;">6</td>
						<td style="width: 20%;"><strong>8</strong></td>
						<td style="width: 20%;"><strong>9</strong></td>
						<td style="width: 20%;"><strong>14</strong></td>
						<td style="width: 20%;">10</td>
					</tr>
					<tr>
						<td style="width: 20%;"><strong>1</strong></td>
						<td style="width: 20%;"><strong>7</strong></td>
						<td style="width: 20%;"><strong>13</strong></td>
						<td style="width: 20%;"><strong>19</strong></td>
						<td style="width: 20%;"><strong>25</strong></td>
					</tr>
					<tr>
						<td style="width: 20%;">16</td>
						<td style="width: 20%;"><strong>12</strong></td>
						<td style="width: 20%;"><strong>17</strong></td>
						<td style="width: 20%;"><strong>18</strong></td>
						<td style="width: 20%;">20</td>
					</tr>
					<tr>
						<td style="width: 20%;"><strong>11</strong></td>
						<td style="width: 20%;">22</td>
						<td style="width: 20%;"><strong>21</strong></td>
						<td style="width: 20%;">24</td>
						<td style="width: 20%;"><strong>23</strong></td>
					</tr>
				</tbody>
			</table>
			</td>
			<td style="width: 34%; text-align: center;">
			<table class="table table-bordered" style="width: 100%;">
				<tbody>
					<tr>
						<td style="width: 20%;"><strong>1</strong></td>
						<td style="width: 20%;">2</td>
						<td style="width: 20%;"><strong>3</strong></td>
						<td style="width: 20%;">4</td>
						<td style="width: 20%;"><strong>5</strong></td>
					</tr>
					<tr>
						<td style="width: 20%;">6</td>
						<td style="width: 20%;"><strong>7</strong></td>
						<td style="width: 20%;"><strong>8</strong></td>
						<td style="width: 20%;"><strong>9</strong></td>
						<td style="width: 20%;">10</td>
					</tr>
					<tr>
						<td style="width: 20%;"><strong>11</strong></td>
						<td style="width: 20%;"><strong>12</strong></td>
						<td style="width: 20%;"><strong>13</strong></td>
						<td style="width: 20%;"><strong>14</strong></td>
						<td style="width: 20%;"><strong>15</strong></td>
					</tr>
					<tr>
						<td style="width: 20%;">16</td>
						<td style="width: 20%;"><strong>17</strong></td>
						<td style="width: 20%;"><strong>18</strong></td>
						<td style="width: 20%;"><strong>19</strong></td>
						<td style="width: 20%;">20</td>
					</tr>
					<tr>
						<td style="width: 20%;"><strong>21</strong></td>
						<td style="width: 20%;">22</td>
						<td style="width: 20%;"><strong>23</strong></td>
						<td style="width: 20%;">24</td>
						<td style="width: 20%;"><strong>25</strong></td>
					</tr>
				</tbody>
			</table>
			</td>
			<td style="width: 33%; text-align: center;">
			<table class="table table-bordered" style="width: 100%;">
				<tbody>
					<tr>
						<td style="width: 20%;"><strong>11</strong></td>
						<td style="width: 20%;">2</td>
						<td style="width: 20%;"><strong>1</strong></td>
						<td style="width: 20%;">4</td>
						<td style="width: 20%;"><strong>3</strong></td>
					</tr>
					<tr>
						<td style="width: 20%;">6</td>
						<td style="width: 20%;"><strong>12</strong></td>
						<td style="width: 20%;"><strong>7</strong></td>
						<td style="width: 20%;"><strong>8</strong></td>
						<td style="width: 20%;">10</td>
					</tr>
					<tr>
						<td style="width: 20%;"><strong>21</strong></td>
						<td style="width: 20%;"><strong>17</strong></td>
						<td style="width: 20%;"><strong>13</strong></td>
						<td style="width: 20%;"><strong>9</strong></td>
						<td style="width: 20%;"><strong>5</strong></td>
					</tr>
					<tr>
						<td style="width: 20%;">16</td>
						<td style="width: 20%;"><strong>18</strong></td>
						<td style="width: 20%;"><strong>19</strong></td>
						<td style="width: 20%;"><strong>14</strong></td>
						<td style="width: 20%;">20</td>
					</tr>
					<tr>
						<td style="width: 20%;"><strong>23</strong></td>
						<td style="width: 20%;">22</td>
						<td style="width: 20%;"><strong>25</strong></td>
						<td style="width: 20%;">24</td>
						<td style="width: 20%;"><strong>15</strong></td>
					</tr>
				</tbody>
			</table>
			</td>
		</tr>
		<tr>
			<td style="width: 33%; text-align: center;">X를 반시계 방향으로 45° 회전한 경우</td>
			<td style="width: 34%; text-align: center;">배열 X (5x5)</td>
			<td style="width: 33%; text-align: center;">X를 시계 방향으로 45° 회전한 경우</td>
		</tr>
	</tbody>
</table>

<p>입력으로 2차원 배열 X와 어느 방향으로 몇 도 회전할지 입력 받아, 그 결과를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 줄에 테스트 케이스의 수 T가 주어진다 (1 ≤ T ≤ 10).</p>

<p>각 테스트 케이스에 대해: 첫 줄에 배열의 크기를 나타내는 n (1 ≤ n < 500, n은 홀수) 그리고 각도 d가 주어진다. d는 0 ≤ |d| ≤ 360 을 만족하며 |d| 는 45의 배수이다. d가 양수이면 시계방향으로 d° 돌려야 하고, 음수이면 반시계방향으로 |d|° 돌려야 한다. 다음 n줄에 걸쳐 각 줄에 n개의 정수가 공백으로 구분되어 주어진다 (X의 원소들을 나타낸다). 각 값은 1 이상 1,000,000 이하의 정수이다.</p>

### 출력 

 <p>각 테스트 케이스에 대해 회전 연산을 마친 후 배열의 상태를 출력한다. n줄에 걸쳐 각 줄에 n개의 정수를 공백으로 구분하여 출력한다. </p>

