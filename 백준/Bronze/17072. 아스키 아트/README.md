# [Bronze I] 아스키 아트 - 17072 

[문제 링크](https://www.acmicpc.net/problem/17072) 

### 성능 요약

메모리: 29200 KB, 시간: 268 ms

### 분류

구현(implementation)

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="height: 225px; width: 225px;"></p>

<p>위와 같이, 아스키 문자로 그린 그림을 ‘아스키 아트’ 라고 한다. 우리가 알고 있는 일반적인 그림 파일(.jpg, .png 등)들은 기본적으로 해상도에 맞게 픽셀 단위로 분할된 2차원 그리드에 대해 각 픽셀의 정보를 담는 방식으로 저장된다. 이 정보에는 여러 가지가 있으나, 그중 ‘R’, ‘G’, ‘B’ 값은 ‘Red’, ‘Green’, ‘Blue’의 3색이 각각 어느 정도 섞여 있는지를 나타내 주는 지표이며, 각 값은 0 이상 255 이하의 범위에 있는 정숫값을 가진다.</p>

<p>아스키 아트는 격자 그리드에서 픽셀 하나 단위로 문자를 할당하여 그림을 그리는 방식이기 때문에, 우리가 알고 있는 모든 그림 파일은 아스키 아트로 다시 그릴 수가 있다. 그러나 여러 색을 가질 수 있는 그림 파일에 비해, 아스키 아트는 색상을 조절할 수 없고, 각 픽셀 내부의 채도만 조정할 수 있다. 원본 이미지가 흑백 이미지였다면 제법 비슷하게 바꿀 수 있으나, 여러 색으로 이루어졌다면 원본 이미지의 느낌을 살리기 힘들 것이다.</p>

<p>하지만 이미지를 흑백 이미지로 바꾸는 필터를 통해 원본 이미지를 흑백 이미지로 바꾸고, 그 이후 아스키 아트로 변환할 수 있다면 퀄리티가 높아질 수 있다.<br>
아래는 이미지 하나가 아스키 아트로 변하는 예시를 보여준다.</p>

<p style="text-align: center;"><img alt="" src="">    <img alt="" src="">    <img alt="" src=""></p>

<p>어떤 그림 하나를 흑백 이미지로 바꾸기 위해 각 픽셀마다 R, G, B 3색이 어떤 비율로 혼합될지 결정하는 Intensity function을 사용한다. Intensity function은 0 이상 255 이하의 정수 R, G, B의 값을 받아 정수 하나를 리턴하는 함수로, 아래와 같이 정의한다.</p>

<p style="text-align: center;"><strong><em>$$ I(R,G,B)=2126R+7152G+ 722B $$</em></strong></p>

<p>위의 함수의 결과값은 0 이상 2,550,000 이하의 값을 가지게 되며, 값이 높을수록 흰색에 가깝고, 값이 낮을수록 검은색에 가까운 픽셀이 된다.<br>
아스키 아트는 intensity function에 따라 정수 하나로 변환된 각 픽셀을 아래의 기준에 맞추어 변환하면 완성된다.</p>

<table class="table table-bordered" style="width: 500px;">
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>Intensity</strong></td>
			<td style="text-align: center;"><strong>변환 문자</strong></td>
			<td style="text-align: center;"><strong>아스키 코드</strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">0 이상 ~ 510,000 미만</td>
			<td style="text-align: center;">#</td>
			<td style="text-align: center;">35</td>
		</tr>
		<tr>
			<td style="text-align: center;">510,000 이상 ~ 1,020,000 미만</td>
			<td style="text-align: center;">o (알파벳 소문자)</td>
			<td style="text-align: center;">111</td>
		</tr>
		<tr>
			<td style="text-align: center;">1,020,000 이상 ~ 1,530,000 미만</td>
			<td style="text-align: center;">+</td>
			<td style="text-align: center;">43</td>
		</tr>
		<tr>
			<td style="text-align: center;">1,530,000 이상 ~ 2,040,000 미만</td>
			<td style="text-align: center;">-</td>
			<td style="text-align: center;">45</td>
		</tr>
		<tr>
			<td style="text-align: center;">2,040,000 이상</td>
			<td style="text-align: center;">.</td>
			<td style="text-align: center;">46</td>
		</tr>
	</tbody>
</table>

<p>지금까지의 작업을 잘 따라왔다면, 훌륭한 ASCII Art Generator를 하나 만들 수 있을 것이다.</p>

<p>원본 이미지 하나의 해상도와 각 픽셀별 R,G,B 값이 주어지면, 이미지의 아스키 아트를 출력하는 프로그램을 작성해 보자.</p>

### 입력 

 <p>첫 줄에 그림의 세로의 길이 <em>N</em>과 가로의 길이 <em>M</em>이 주어진다. (1 ≤ <em>N</em>,<em> M</em> ≤ 400)</p>

<p>두번째 줄부터 <em>N</em>+1번째 줄까지 각 줄에 3<em>M</em>개의 정수가 주어진다.</p>

<p>이 중 <em>i</em>+1번째 줄의 3<em>j</em>-2, 3<em>j</em>-1, 3<em>j</em>번째 정수는 각각 <em>R(i,j), G(i,j), B(i,j)</em>를 뜻하며, 모든 값은 0 이상 255 이하이다.</p>

<p>이 때 <em>R(i,j)</em>는 <em>i</em>행 <em>j</em>열 픽셀의 <em>R</em>값, <em>G(i,j)</em>는 <em>i</em>행 <em>j</em>열 픽셀의 <em>G</em>값, <em>B(i,j)</em>는 <em>i</em>행 <em>j</em>열 픽셀의 <em>B</em>값을 의미한다</p>

### 출력 

 <p>N×M 격자 형태로, 입력된 그림을 아스키 아트로 변환하여 출력한다.</p>

<p>줄 끝에 필요 없는 공백을 출력하지 않도록 주의한다.</p>

