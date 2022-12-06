# [Bronze I] Lie Detector - 16581 

[문제 링크](https://www.acmicpc.net/problem/16581) 

### 성능 요약

메모리: 36684 KB, 시간: 80 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Andi is a young and prominent detective in the police force. His ability to track down criminals, uncover the truth, and solve cases never ceases to amaze all of his colleagues. One day, he is faced with a suspicious eyewitness testimony when working on a certain case. In usual cases, Andi simply ignores such unreliable testimony; however, in this case, the eyewitness testimony is too important to be ignored. To resolve this situation, Andi has to rely on technology, i.e. using a lie detector.</p>

<p>Andi proceeds to use a lie detector to detect whether the eyewitness testimony is true. However, Andi notices that the lie detector he used might have been tampered, thus, he employs a second lie detector to detect whether the first lie detector’s result is correct. This situation happens repeatedly such that Andi ends up employing N lie detectors in total. The i<sup>th</sup> lie detector reports the truth of the (i−1)<sup>th</sup> lie detector for i = 2..N, and the 1<sup>st</sup> lie detector reports the truth of the eyewitness testimony.</p>

<p>In the end, Andi knows that the last (N<sup>th</sup>) lie detector has not been tampered and always report the truth correctly. Now, he needs to determine whether the eyewitness testimony is true given the result of all lie detectors.</p>

<p>For example, let N = 4 and the lie detectors result are (LIE, LIE, TRUTH, TRUTH).</p>

<ul>
	<li>The 4<sup>th</sup> lie detector reports that the 3<sup>rd</sup> lie detector is TRUTH. As the 4<sup>th</sup> lie detector always report the truth correctly, then the 3<sup>rd</sup> lie detector’s result is correct as it is.</li>
	<li>The 3<sup>rd</sup> lie detector reports that the 2<sup>nd</sup> lie detector is TRUTH. As the 3<sup>rd</sup> lie detector’s result is correct as it is, then the 2<sup>nd</sup> lie detector’s result is also correct as it is.</li>
	<li>The 2<sup>nd</sup> lie detector reports that the 1<sup>st</sup> lie detector is LIE. As the 2<sup>nd</sup> lie detector’s result is correct as it is, then the 1<sup>st</sup> lie detector’s result is wrong.</li>
	<li>The 1<sup>st</sup> lie detector reports that the eyewitness testimony is LIE. As the 1<sup>st</sup> lie detector’s result is wrong, then the eyewitness testimony is correct; in other words, what the eyewitness says is true.</li>
</ul>

<p>Therefore, the eyewitness testimony in this example is true.</p>

### 입력 

 <p>Input begins with a line containing an integer N (2 ≤ N ≤ 100000). The next N lines, each contains a string S<sub>i</sub> (either TRUTH or LIE) representing the output of the i<sup>th</sup> lie detector for i = 1..N respectively.</p>

### 출력 

 <p>Output contains a string TRUTH or LIE in a line whether the eyewitness testimony is true or false.</p>

