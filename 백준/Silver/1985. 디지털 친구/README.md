# [Silver IV] 디지털 친구 - 1985 

[문제 링크](https://www.acmicpc.net/problem/1985) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>두 정수가 만약에 완전히 같은 숫자들로만 이루어져 있으면 두 숫자를 friends(친구)라고 부른다. 예를 들어 123과 32331313323213은 friends 이지만 123과 22121221은 아니다.</p>

<p>그러나 friends가 아닌 두 개의 정수가 만약에 이웃한 두 숫자를 규칙에 따라 고쳤을 때 friends가 되면 almost friends(거의 친구)라고 부른다. 그 규칙은 만약에 a와 b가 붙어 있으면 a에 1을 빼고 b에 1을 더하거나 a에 1을 더하고 b에 1을 뺄 수 있다는 것이다. 하지만 그 결과에서 맨 앞자리 숫자가 0이라면 이것은 허용이 되지 않는다. 예를 들어 123과 2223042는 almost friends이다. (2223042 -> 2223132) 하지만 137과 470은 friends도 almost friends도 아니다. (137 -> 047)은 허용이 되지 않는다. <span style="color:#555555; font-family:open sans,helvetica neue,helvetica,arial,apple sd gothic neo,noto sans cjk kr,noto sans kr,나눔바른고딕,나눔고딕,nanumgothic,맑은고딕,malgun gothic,nanum gothic,sans-serif">연산은 두 수 중 하나에게만, 최대 한 번 사용할 수 있다.</span></p>

<p>만약에 두 정수가 주어져 있을 때, 두 정수가 friends인지, almost friends인지, 아니면 아무것도 아닌지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>세 개의 입력 데이터가 주어지며, 각각의 입력 데이터는 한 개의 줄로 이루어져 있다. 각 데이터의 첫째 줄에 두 정수 x, y가 공백을 사이에 두고 주어진다.</p>

### 출력 

 <p>세 개의 줄에 걸쳐 입력된 순서대로 x, y가 friends면 “friends", almost friends이면 ”almost friends", 둘 다 아니면 “nothing" 이라고 출력한다.</p>

