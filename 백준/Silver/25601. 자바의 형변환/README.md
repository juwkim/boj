# [Silver I] 자바의 형변환 - 25601 

[문제 링크](https://www.acmicpc.net/problem/25601) 

### 성능 요약

메모리: 137968 KB, 시간: 216 ms

### 분류

자료 구조, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 트리

### 제출 일자

2025년 4월 6일 18:04:20

### 문제 설명

<p>자바의 클래스끼리는 상속을 통해 자신의 기능 일부를 다른 클래스에게 이식할 수 있다. 여기서 상속을 받은 클래스는 자식 클래스, 상속을 한 클래스는 부모 클래스가 된다. 클래스를 이용해서 만든 객체는 다른 클래스로 형태를 변환할 수 있는데, 이를 형변환(Casting)이라고 한다. 만약 자식 클래스에서 부모 클래스로 변환한다면 업캐스팅(Upcasting), 부모 클래스에서 자식 클래스로 변환한다면 다운캐스팅(Downcasting) 이라고 부른다. 즉, 자식 클래스와 부모 클래스 관계에 놓여있다면 형변환이 가능하다. Downcasting의 경우 런타임에 문제를 발생시킬 수 있지만 이는 본 문제에서 고려하지 않는다. 또한, 자바에서는 클래스의 다중 상속은 지원하지 않는다</p>

<p>예를 들자면, number 클래스는 object 클래스를 상속받는다. 따라서, number 클래스는 object 클래스의 자식 클래스가 되고, object 클래스는 number 클래스의 부모 클래스가 된다.</p>

<p>또한, 자식 클래스가 여러 단계를 거쳐 상속을 받은 경우, 이 자식 클래스에게 상속을 해준 클래스들 모두 부모 클래스가 된다. 예를 들면, integer 클래스의 경우 number 클래스로 부터 상속을 받고, 이 number 클래스는 object 클래스의 상속을 받았으니, integer 클래스는 number, object 클래스로부터 상속을 받은 것과 같다. 따라서, integer 클래스와 object 클래스는 부모 - 자식 관계가 되기 때문에 두 클래스간 형변환이 가능하다.</p>

<p>입력으로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 임의의 클래스들간의 관계를 입력받고, 검사할 두 클래스에 대한 정보가 주어진다. 만약, 서로 형변환이 가능하면 <span style="color:#e74c3c;"><code>1</code></span>, 아니면 <span style="color:#e74c3c;"><code>0</code></span>을 출력한다.</p>

### 입력 

 <p>첫 줄에 클래스의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mtext> </mtext><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le N \le 100\ 000$</span></mjx-container>)</p>

<p>다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N - 1$</span></mjx-container>개의 줄에 각 클래스 간의 관계 정보가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$B$</span></mjx-container>가 순서대로 주어지며 이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$B$</span></mjx-container>의 자식 클래스란 뜻이다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$B$</span></mjx-container>는 알파벳 소문자로 구성된 길이 2 이상 50 이하의 문자열이다.</p>

<p>마지막 줄엔 서로 형변환이 가능한지 확인할 두 클래스가 주어진다. 항상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N - 1$</span></mjx-container>개 줄의 입력에서 주어졌던 클래스만 나오며, 두 클래스의 이름은 서로 다르다.</p>

<p>입력을 통해 만들어지는 트리는 하나의 루트가 있는 트리이다.</p>

### 출력 

 <p>두 클래스가 형변환이 가능하면 <span style="color:#e74c3c;"><code>1</code></span>, 아니라면 <span style="color:#e74c3c;"><code>0</code></span>을 출력한다.</p>

