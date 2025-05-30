# [Silver I] СТЕПЕН - 31275 

[문제 링크](https://www.acmicpc.net/problem/31275) 

### 성능 요약

메모리: 234684 KB, 시간: 660 ms

### 분류

분할 정복을 이용한 거듭제곱, 수학

### 제출 일자

2025년 5월 4일 02:03:21

### 문제 설명

<p>Дадена е таблица, съставена от n + 1 реда и n стълба. В първия ред на таблицата са записани цели положителни числа, а на следващите n реда са пресметнати и записани съответно вторите, третите и т. н. степени на числата от първия ред.</p>

<p>Например, в следващата таблица n = 4 и тя съдържа степените на числата 3, 5, 2 и 1 до петата им степен:</p>

<table class="table table-bordered table-center-30 td-center">
	<tbody>
		<tr>
			<td>3</td>
			<td>5</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td><strong>9</strong></td>
			<td>25</td>
			<td>4</td>
			<td>1</td>
		</tr>
		<tr>
			<td>27</td>
			<td><strong>125</strong></td>
			<td>8</td>
			<td>1</td>
		</tr>
		<tr>
			<td>81</td>
			<td>625</td>
			<td><strong>16</strong></td>
			<td>1</td>
		</tr>
		<tr>
			<td>243</td>
			<td>3125</td>
			<td>32</td>
			<td><strong>1</strong></td>
		</tr>
	</tbody>
</table>

<p>Напишете програма power, която събира числата от диагонала на таблицата (както е показан на фигурата с получерен шрифт) и извежда резултата по модул, който е зададен като цяло положително число m.</p>

<p>За примера, ако m = 3, тогава резултатът ще бъде 1, защото остатъкът при делене с 3 на сумата 9+125+16+1 е равен на 1.</p>

### 입력 

 <p>От първия ред на стандартния вход програмата въвежда целите положителни числа n и m. На втория ред във входа са записани (разделени с интервали) числата от първия ред на таблицата.</p>

### 출력 

 <p>Програмата трябва да изведе на стандартния изход пресметнатата сума като едно цяло число.</p>

