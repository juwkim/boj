# [Silver I] 아주 서바이벌 - 23293 

[문제 링크](https://www.acmicpc.net/problem/23293) 

### 성능 요약

메모리: 143032 KB, 시간: 332 ms

### 분류

자료 구조, 구현, 시뮬레이션

### 제출 일자

2025년 4월 9일 10:00:48

### 문제 설명

<p>때는 2021년, 대한민국에는 '아주 서바이벌'이라는 온라인 게임이 대 유행 중이다. 이 게임은 바다 한가운데의 섬, 아주 아일랜드에서 벌어지는 배틀로얄 게임으로 플레이어들은 아주 아일랜드의 여러 지역을 돌아다니며 아이템을 획득하고, 조합해 다른 플레이어와 싸우게 된다.</p>

<p>상민이는 아주 서바이벌의 서버 개발자다. 이 게임이 흥행하면서 부정행위를 저지르는 플레이어가 늘어나자, 보다 못한 상민이는 게임의 로그를 분석해 부정행위를 전부 찾아내기로 했다.</p>

<p style="text-align: center;"><img alt="아주 서바이벌 지도" src="https://upload.acmicpc.net/d6c3457b-1d95-4a74-8fdf-5c7835af954a/-/preview/" style="width: 600px; height: 600px;"></p>

<p style="text-align: center;"><그림 1> 아주 서바이벌의 지도</p>

<p>아주 서바이벌에는 1번부터 53번 지역까지 총 <strong>53개</strong>의 지역이 존재하며, 모든 플레이어가 <strong>1번 지역</strong>(정문)에 모인 채로 게임이 시작된다.</p>

<p>플레이어들은 이동, 획득, 조합, 공격 총 네 가지 종류의 행동을 할 수 있다.</p>

<ul>
	<li><strong>이동</strong> : 플레이어가 현재 위치한 지역에서 <strong>다른</strong> 지역으로 이동한다. 즉, 현재 위치한 지역으로는 이동하지 않는다.</li>
	<li><strong>획득</strong> : 플레이어가 <strong>현재 위치한 지역에서만 획득할 수 있는</strong> 소재 아이템 1개를 획득한다. 즉, <em>x</em>번 지역에서는 <em>x</em>번 소재 아이템을 획득한다. 아이템의 수량은 충분해 부족할 일이 없으며, 한 플레이어가 같은 아이템을 여러 번 획득할 수 있다.</li>
	<li><strong>조합</strong> : 플레이어가 가지고 있는 <strong>서로 다른 종류</strong>의 두 소재 아이템을 1개씩 사용해 장비를 만든다.</li>
	<li><strong>공격</strong> : 플레이어가 다른 플레이어 한 명을 공격한다. 오직 같은 지역에 있는 플레이어만 공격할 수 있다.</li>
</ul>

<p>위 행동들에서 상민이는 아래 세 가지 경우를 부정행위라고 판단했다.</p>

<ol>
	<li>플레이어가 현재 위치한 지역에서 얻을 수 없는 소재 아이템을 획득한 경우</li>
	<li>플레이어가 가지고 있지 않은 소재 아이템을 사용해 조합하는 경우</li>
	<li>플레이어가 다른 지역에 있는 상대 플레이어를 공격하는 경우</li>
</ol>

<blockquote>
<p>상민: 부정행위로 보이는 모든 로그를 기록할 거야. 하지만, 공격할 때 위치를 속이는 것은 참을 수 없어. 그런 플레이어는 차단할 거야!</p>
</blockquote>

<p>게임 로그는 다음과 같이 주어진다.</p>

<pre>1 11 M 13
2 13 M 15
3 11 F 13
4 11 M 3
5 11 F 3
6 11 C 3 13
7 13 A 11
8 13 F 15
9 13 F 16
10 13 C 15 16
...</pre>

<p>게임 로그는 "<code>[번호] [플레이어 번호] [행동 코드] [행동 인자]</code>"의 형식으로 기록된다.</p>

<ul>
	<li><strong>번호</strong> : 로그의 줄 번호이다. <em>1</em>번부터 <em>T</em>번까지 순서대로 주어진다.</li>
	<li><strong>플레이어 번호</strong> : 각 플레이어가 가지는 고유한 번호이다. <em>1</em>번부터 <em>N</em>번 사이의 번호를 가지게 된다.</li>
	<li><strong>행동 코드</strong> : 플레이어가 한 행동이다. 이동은 <strong>M</strong>(Move), 획득은 <strong>F</strong>(Farming), 조합은 <strong>C</strong>(Crafting), 공격은 <strong>A</strong>(Attack)이다.</li>
	<li><strong>행동 인자</strong> : 플레이어가 한 행동과 관련된 정보이다. 이동은 <strong>새로 이동한 지역의 번호</strong>, 획득은 <strong>획득한 소재 아이템의 번호</strong>, 조합은 <strong>조합에 사용된 두 소재 아이템의 번호</strong>, 공격은 <strong>공격한 플레이어 번호</strong>를 행동 인자로 가진다.</li>
</ul>

<p>부정행위로 획득한 소재 아이템 역시 획득한 것으로 인정되며, 부정행위로 조합 시 가지고 있는 소재 아이템만이 사용된다.</p>

<p>위 로그를 예로 들면, 11번 플레이어는 13번 지역으로 이동하여(1) 13번 소재 아이템을 획득하고(3), 이후 3번 지역으로 이동하여(4) 3번 소재 아이템을 획득해(5) 3번과 13번 소재 아이템을 조합했다(6). 모두 정상적인 행동이다.</p>

<p>13번 플레이어는 15번 지역으로 이동한 후(2), 3번 지역에 있는 11번 플레이어를 공격했다(7). 다른 지역에 있는 플레이어를 공격하는 것은 부정행위이기 때문에 7번 로그를 기록하고, 공격 부정행위이기 때문에 13번 플레이어는 차단해야 한다. 이어서, 15번 소재 아이템을 획득하고(8), 16번 소재 아이템을 획득 후에(9), 15번과 16번 소재 아이템을 조합했다(10). 15번 지역에서 16번 소재 아이템을 획득하는 것은 부정행위이기 때문에 9번 로그를 기록한다. 하지만, 16번 소재 아이템을 획득한 것은 인정되기 때문에 10번 로그는 부정행위가 아니다.</p>

<p>상민이를 위해 게임의 로그를 분석하고, 기록된 부정행위와 차단할 플레이어를 상민에게 알려주자.</p>

### 입력 

 <p>첫 번째 줄에는 게임 로그의 줄 수 <em>T</em>, 플레이어 수 <em>N</em>이 주어진다. (1 ≤ <em>T</em> ≤ 200,000, 1 ≤ <em>N</em> ≤ 100,000)</p>

<p>두 번째 줄부터 <em>T</em>개 줄 동안 게임 로그가 입력된다. 각 줄의 게임 로그는 <em>번호,</em> <em>플레이어 번호,</em> <em>행동 코드,</em> <em>행동 인자</em>가 공백 한 칸을 사이에 두고 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 부정행위로 기록된 로그의 수를 출력한다. 기록된 로그가 없다면 "<code>0</code>"을 출력한다.</p>

<p>부정행위로 기록된 로그가 있다면 다음 줄에 기록된 로그의 <strong>번호</strong>를 공백 한 칸씩 띄어서 <strong>오름차순</strong>으로 출력한다. 기록된 로그가 없다면 해당 줄은 출력하지 않는다.</p>

<p>다음 줄에 차단할 플레이어 수를 출력한다. 차단할 플레이어가 없다면 "<code>0</code>"을 출력한다.</p>

<p>차단할 플레이어가 있다면 다음 줄에는 차단할 플레이어의 <strong>번호</strong>를 공백 한 칸씩 띄어서 <strong>오름차순</strong>으로 출력한다. 한 플레이어가 여러 번 부정행위를 저지르더라도 한 번만 출력하며, 차단할 플레이어가 없다면 해당 줄은 출력하지 않는다.</p>

