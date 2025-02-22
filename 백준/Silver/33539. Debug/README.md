# [Silver IV] Debug - 33539 

[문제 링크](https://www.acmicpc.net/problem/33539) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

수학, 정수론, 소수 판정

### 제출 일자

2025년 2월 22일 14:58:49

### 문제 설명

<p>You just joined a new team to participate in the FPC, because the previous member left the team frustrated. Frustrated that he could not beat a time limit<sup>1</sup> of a certain problem of an earlier FPC. To show you indeed posses the skills to solve problems during a FPC, you decide to solve the problem the other member could not. Unfortunately, he never told anyone which problem he was actually trying to solve. Luckily, you still got his code!</p>

<p>Your task is to debug the problem his code is solving and speed it up. You may assume that in its current state, it is correct but too slow. The (Java) code is given below.</p>

<pre>import java.util.Scanner;

class D {
    public static int n(int n) {
        int p = 1;
        if (n == 1 || n == 0) p = 0;
        for (int i = 1; i < n; i++) {
            if (i == 1) continue;
            if (n % i == 0) p = 0;
        }
        return p;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (n(sc.nextInt()) == 1) System.out.println("yes");
        else System.out.println("no");
    }
}
</pre>

<hr>
<p><sup>1</sup>This was based on the text "Correct but TIME LIMIT! AARGH!" being scratched in the wall.</p>

### 입력 

 <p>As can be seen in the provided code. The only input is an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq n \leq 10^9$</span></mjx-container>.</p>

### 출력 

 <p>Keep the same output as provided in the code. You only need to speed up things.</p>

