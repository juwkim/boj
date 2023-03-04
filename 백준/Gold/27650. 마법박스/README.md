# [Gold IV] 마법박스 - 27650 

[문제 링크](https://www.acmicpc.net/problem/27650) 

### 성능 요약

메모리: 13676 KB, 시간: 4 ms

### 분류

이분 탐색(binary_search), 수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>무지는 길을 가다 마법박스를 주웠다. 이 마법박스 안에는 $2$ 이상의 양의 정수들이 들어 있고 같은 수가 중복되어 들어 있지 않다. <strong>또한 마법박스는 신기한 특성을 지니고 있는데 박스 안에 있는 모든 수에 대해 그 수의 모든 배수 또한 무한히 박스 안에 들어 있다는 사실이다.</strong></p>

<p>무지는 마법박스에 들어 있지 않은 $2$ 이상의 양의 정수 중 가장 작은 수를 알고 싶다. $N$ 이하에 그러한 수가 있음은 밝혀냈지만 정확히 어떤 수인지는 모른다. 당신은 무지를 도와 박스에게 특정 수 이하의 $2$ 이상의 양의 정수가 모두 박스에 들어있는지 질의하여 정답을 알아내야 한다.</p>

<p><strong>중요:</strong> 채점 시스템은 여러분의 질문에 따라 정답을 바꾸지 않으며 이전까지의 답변들과 모순되는 답변은 하지 않는다.</p>

### 입력 

 <p>입력의 첫 줄에 정수 $N$이 주어진다. $\left( 2 \leq N \leq 5\,000\,000\right)$  </p>

### 출력 

 <p>다음을 표준 출력 스트림(stdout)으로 한 줄에 출력하여, $i$ 이하의 $2$ 이상의 양의 정수가 마법박스에 모두 들어있는지 질의할 수 있다. 질의에 대한 답변은 모두 들어있다면 $1$, 그렇지 않다면 $0$으로 주어진다.</p>

<ul>
	<li> "<span style="color:#e74c3c;">?</span> <span style="color:#e74c3c;">i </span>: $i$ 이하의 $2$ 이상의 양의 정수가 마법박스에 모두 들어있는가." $(2 \leq i \leq N;$ $i$는 정수$)$</li>
</ul>

<p>각 질문을 출력한 후에는 반드시 표준 출력 버퍼를 flush해야 하고, 표준 입력 스트림(stdin)을 통해 질문에 대한 답을 입력받아야 한다. 그렇지 않으면, <span style="color:#e74c3c;">시간 초과</span> 또는 <u>런타임 에러</u>를 받는다.</p>

<p>질문하는 $i$의 범위가 정해진 구간을 벗어나는 경우, <span style="color:#e74c3c;">틀렸습니다</span>를 받는다.</p>

<p>질문은 최대 $20$번만 할 수 있고, 이보다 더 많이 질문을 하면 <span style="color:#e74c3c;">틀렸습니다</span>를 받는다.</p>

<p>최대 $20$번의 질문을 이용해, 정답을 아래의 표준 출력 스트림(stdout)을 이용해 한 번만 출력한다.</p>

<ul>
	<li> "<span style="color:#e74c3c;">!</span> <span style="color:#e74c3c;">T</span> : 마법박스에 들어 있지 않은 $2$ 이상의 양의 정수 중 가장 작은 수는 $T$이다." $\left( 2 \leq T \leq N\right)$</li>
</ul>

<p>그 후 반드시 표준 출력 버퍼를 flush해야 하고, 프로그램을 종료한다. 이것은 질문 횟수에 포함되지 않는다.</p>

<p>언어별로 표준 출력 버퍼를 flush하는 방법은 다음과 같다.</p>

<ul>
	<li> C: <code>fflush(stdout)</code></li>
	<li> C++: <code>std::cout << std::flush</code></li>
	<li> Java: <code>System.out.flush()</code></li>
	<li> Python: <code>sys.stdout.flush()</code></li>
</ul>

