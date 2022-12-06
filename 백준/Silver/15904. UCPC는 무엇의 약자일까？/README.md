# [Silver V] UCPC는 무엇의 약자일까? - 15904 

[문제 링크](https://www.acmicpc.net/problem/15904) 

### 성능 요약

메모리: 29200 KB, 시간: 88 ms

### 분류

그리디 알고리즘(greedy), 문자열(string)

### 문제 설명

<p>UCPC는 '전국 대학생 프로그래밍 대회 동아리 연합 여름 대회'의 줄임말로 알려져있다. 하지만 이 줄임말이 정확히 어떻게 구성되었는지는 아무도 모른다. UCPC 2018을 준비하던 ntopia는 여러 사람들에게 UCPC가 정확히 무엇의 줄임말인지 물어보았지만, 아무도 정확한 답을 제시해주지 못했다. ntopia가 들은 몇 가지 답을 아래에 적어보았다.</p>

<ul>
	<li>Union of Computer Programming Contest club contest</li>
	<li>Union of Computer Programming contest Club contest</li>
	<li>Union of Computer Programming contest club Contest</li>
	<li>Union of Collegiate Programming Contest club contest</li>
	<li>Union of Collegiate Programming contest Club contest</li>
	<li>Union of Collegiate Programming contest club Contest</li>
	<li>University Computer Programming Contest</li>
	<li>University Computer Programming Club contest</li>
	<li>University Computer Programming club Contest</li>
	<li>University Collegiate Programming Contest</li>
	<li>University CPC</li>
	<li>...</li>
</ul>

<p>ntopia는 이렇게 다양한 답을 듣고는 UCPC가 무엇의 약자인지는 아무도 모른다고 결론내렸다. 적당히 슥삭해서 UCPC를 남길 수 있으면 모두 UCPC의 약자인 것이다!</p>

<p>문자열이 주어지면 이 문자열을 적절히 축약해서 "UCPC"로 만들 수 있는지 확인하는 프로그램을 만들어보자.</p>

<p>축약이라는 것은 문자열에서 임의의 문자들을 제거하는 행동을 뜻한다. 예를 들면, "apple"에서 a와 e를 지워 "ppl"로 만들 수 있고, "University Computer Programming Contest"에서 공백과 소문자를 모두 지워 "UCPC"로 만들 수 있다.</p>

<p>문자열을 비교할 때는 대소문자를 구분해 정확히 비교한다. 예를 들어 "UCPC"와 "UCpC"는 다른 문자열이다. 따라서 "University Computer programming Contest"를 "UCPC"로 축약할 수 있는 방법은 없다.</p>

<p>그나저나 UCPC는 정말 무엇의 약자였을까? 정확히 아시는 분은 제보 부탁드립니다.</p>

### 입력 

 <p>첫 번째 줄에 알파벳 대소문자, 공백으로 구성된 문자열이 주어진다. 문자열의 길이는 최대 1,000자이다. 문자열의 맨 앞과 맨 끝에 공백이 있는 경우는 없고, 공백이 연속해서 2번 이상 주어지는 경우도 없다.</p>

### 출력 

 <p>첫 번째 줄에 입력으로 주어진 문자열을 적절히 축약해 "UCPC"로 만들 수 있으면 "<code>I love UCPC</code>"를 출력하고, 만들 수 없으면 "<code>I hate UCPC</code>"를 출력한다.</p>

