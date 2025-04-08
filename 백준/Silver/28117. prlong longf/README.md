# [Silver I] prlong longf - 28117 

[문제 링크](https://www.acmicpc.net/problem/28117) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

다이나믹 프로그래밍, 수학, 문자열

### 제출 일자

2025년 4월 8일 11:14:13

### 문제 설명

<p>성서는 <strong><span style="color:#ad5600;">Bronze 5</span></strong> 난이도의 문제를 풀다가 <span class="result-text result-wa " data-color="wa">틀렸습니다</span>를 받았다.</p>

<p>계산 도중 수가 너무 커져서 오버플로우가 발생했다고 생각한 성서는 코드 에디터의 “찾기 및 바꾸기” 기능을 사용해서 코드의 <code>int</code>를 모두 동시에 <code>long long</code>으로 바꾸었는데, <code>printf</code>도 모두 <code>prlong longf</code>로 바뀌는 사고가 일어났다!</p>

<pre><code>#include <stdio.h>

long long main(){
    long long n, res = 1;
    scanf("%d", &n);
    for(long long i = 1; i <= n; i++){
        res *= i;
    }
    prlong longf("%d\n", res);
    return 0;
}</code></pre>

<p>스스로 코드를 고치기 귀찮았던 성서는 대회 참가자들에게 바뀐 코드를 주고 초기 상태로 복원해 달라고 부탁하려고 했지만, 주어진 코드에 따라 복원 방법이 유일하지 않을 수 있다는 사실을 깨달았다. 좋은 문제 아이디어를 발견한 성서는 2023 SCON에 다음과 같은 문제를 출제했다.</p>

<p>모든 <code>int</code>가 <code>longlong</code>으로 바뀐 문자열이 주어진다. 가능한 원래 문자열은 모두 몇 가지인가?</p>

### 입력 

 <p>첫째 줄에 바뀐 문자열의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>둘째 줄에 <code>int</code>가 모두 <code>longlong</code>으로 바뀐 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어진다.</p>

### 출력 

 <p>문자열의 초기 상태로 가능한 경우의 수를 출력한다.</p>

