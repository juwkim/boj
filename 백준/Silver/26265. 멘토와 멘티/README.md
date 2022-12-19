# [Silver V] 멘토와 멘티 - 26265 

[문제 링크](https://www.acmicpc.net/problem/26265) 

### 성능 요약

메모리: 157412 KB, 시간: 548 ms

### 분류

정렬(sorting)

### 문제 설명

<p>서울사이버대학교에는 멘토링 프로그램이 있다. 멘토링 프로그램은 한 명의 멘토(선배학습자)가 여러 명의 멘티(후배학습자)에게 대학 생활에 대한 노하우와 정보 등을 전수하는 것이다.</p>

<p>빅데이터·AI 센터에서 딥러닝 서버를 돌리며 바쁜 나날을 보내던 노교수는, 어느 날 멘토링 회의 참석 요청이 들어와 이를 준비하던 도중 멘토-멘티 순서쌍 목록이 적힌 노트를 찾았다. 하지만 노트가 제대로 정리되어 있지 않아 분석이 어려웠으므로, 마침 센터에서 인턴을 하는 대학원생 뚜루에게 목록의 정렬을 맡기기로 했다.</p>

<p>하지만 논문을 쓰느라 수면 부족에 시달리고 있는 뚜루는 이러한 프로그램을 짤 틈이 나지 않았기 때문에, 당신에게 다시 목록을 맡겼다. 목록이 주어질 때 멘토를 기준으로 사전 순으로 정렬하되, 멘토가 같은 순서쌍들에 대해선 멘티의 사전 역순으로 정렬하자.</p>

### 입력 

 <p>첫 번째 줄에 멘토-멘티 순서쌍의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 100\,000$</span></mjx-container>)</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 목록에 포함된 각 순서쌍의 멘토의 이름과 멘티의 이름이 공백 하나로 구분되어 주어진다. 이름은 소문자로만 구성되며, 20자를 넘지 않는다. A가 B의 멘토인 동시에 B가 A의 멘토일 수 있다. 멘토와 멘티가 동일할 수 있다. 똑같은 멘토-멘티 순서쌍이 중복해서 주어지지 않는다.</p>

### 출력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 정렬된 멘토-멘티 순서쌍 목록을 입력과 동일한 형식으로 출력한다.</p>

