# [Bronze II] Ресторан - 23738 

[문제 링크](https://www.acmicpc.net/problem/23738) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="width: 630px; max-width: 100%;"></p>

<p style="text-align: center;">그림 A.1: Ресторан «Матрешка»</p>

<p>팀 레드시프트를 따라 모스크바 여행에 간 한별이는 거리에 늘어선 ‘<span style="color:#3498db;">Ресторан</span>’가 적힌 간판들을 보고 어떤 가게일까 고민하기 시작했다.</p>

<p>러시아어 알파벳에는 영어 알파벳과 비슷하게 생긴 글자들이 있는데, <span style="color:#3498db;">А</span>, <span style="color:#3498db;">В</span>, <span style="color:#3498db;">Е</span>, <span style="color:#3498db;">К</span>, <span style="color:#3498db;">М</span>, <span style="color:#3498db;">Н</span>, <span style="color:#3498db;">О</span>, <span style="color:#3498db;">Р</span>, <span style="color:#3498db;">С</span>, <span style="color:#3498db;">Т</span>, <span style="color:#3498db;">У</span>, <span style="color:#3498db;">Х</span>의 $12$가지가 있다. <span style="color:#3498db;">А</span>, <span style="color:#3498db;">К</span>, <span style="color:#3498db;">М</span>, <span style="color:#3498db;">О</span>, <span style="color:#3498db;">Т</span>의 다섯 글자는 보이는 대로 읽으면 되지만, 나머지 $7$가지 글자는 영어 알파벳의 발음과 다르게 읽어야 한다!</p>

<ul>
	<li>‘<span style="color:#3498db;">В</span>’는 ‘B’처럼 보이지만 ‘v’로 읽는다.</li>
	<li>‘<span style="color:#3498db;">Е</span>’는 ‘E’처럼 보이지만 ‘ye’로 읽는다.</li>
	<li>‘<span style="color:#3498db;">Н</span>’은 ‘H’처럼 보이지만 ‘n’으로 읽는다.</li>
	<li>‘<span style="color:#3498db;">Р</span>’은 ‘P’처럼 보이지만 ‘r’으로 읽는다.</li>
	<li>‘<span style="color:#3498db;">С</span>’는 ‘C’처럼 보이지만 ‘s’로 읽는다.</li>
	<li>‘<span style="color:#3498db;">У</span>’는 ‘Y’처럼 보이지만 ‘u’로 읽는다.</li>
	<li>‘<span style="color:#3498db;">Х</span>’는 ‘X’처럼 보이지만 ‘h’로 읽는다.</li>
</ul>

<p>고민에 빠진 한별이를 위해 <span style="color:#3498db;">Ресторан</span>가 무슨 가게인지 알려 주자.</p>

### 입력 

 <p>최대 $100$글자의 단어가 주어진다. 모든 글자는 <strong>영어</strong> 대문자 A, B, E, K, M, H, O, P, C, T, Y, X 중 하나로 이루어져 있다. 입력이 러시아어 대문자로 주어지지 않음에 주의하자.</p>

### 출력 

 <p>입력으로 주어진 단어를 비슷한 러시아어 알파벳으로 읽었을 때, 어떤 발음이 되는지 영어 소문자로 나타내 출력한다.</p>

