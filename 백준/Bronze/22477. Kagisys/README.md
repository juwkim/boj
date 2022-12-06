# [Bronze I] Kagisys - 22477 

[문제 링크](https://www.acmicpc.net/problem/22477) 

### 성능 요약

메모리: 30840 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 문자열(string)

### 문제 설명

<p>ある部屋ではICカードを用いて鍵を開け閉めする電子錠システムを用いている。 このシステムは以下のように動作する。</p>

<p>各ユーザーが持つICカードを扉にかざすと、そのICカードのIDがシステムに渡される。 システムはIDが登録されている時、施錠されているなら開錠し、そうでないのなら施錠し、それぞれメッセージが出力される。 IDが登録されていない場合は、登録されていないというメッセージを出力し、開錠及び施錠はおこなわれない。</p>

<p>さて、現在システムにはN個のID(U<sub>1</sub>, U<sub>2</sub>, ……, U<sub>N</sub>)が登録されており、施錠されている。 M回ICカードが扉にかざされ、そのIDはそれぞれ順番にT<sub>1</sub>, T<sub>2</sub>, ……, T<sub>M</sub>であるとする。 この時のシステムがどのようなメッセージを出力するか求めよ。</p>

### 입력 

 <p>入力は以下の形式で与えられる。</p>

<pre>N
U<sub>1</sub>
U<sub>2</sub>
……
U<sub>N</sub>
M
T<sub>1</sub>
T<sub>2</sub>
……
T<sub>M</sub>
</pre>

### 출력 

 <p>各T<sub>1</sub>, T<sub>2</sub>, ……, T<sub>M</sub>について、</p>

<ul>
	<li>
	<p>開錠された時は、"Opened by "の後に続けてIDを、</p>
	</li>
	<li>
	<p>施錠された時は、"Closed by "の後に続けてIDを、</p>
	</li>
	<li>
	<p>IDが登録されていないものだった場合は"Unknown "の後に続けてIDを それぞれ1行に出力せよ。</p>
	</li>
</ul>

<p>初期状態では施錠された状態である。</p>

