# [Silver II] Unreliable Messengers - 3932 

[문제 링크](https://www.acmicpc.net/problem/3932) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현, 시뮬레이션, 문자열

### 제출 일자

2025년 1월 7일 20:15:08

### 문제 설명

<p>The King of a little Kingdom on a little island in the Pacific Ocean frequently has childish ideas. One day he said, “You shall make use of a message relaying game when you inform me of something.” In response to the King’s statement, six servants were selected as messengers whose names were Mr. J, Miss C, Mr. E, Mr. A, Dr. P, and Mr. M. They had to relay a message to the next messenger until the message got to the King.</p>

<p>Messages addressed to the King consist of digits (‘0’–‘9’) and alphabet characters (‘a’–‘z’, ‘A’– ‘Z’). Capital and small letters are distinguished in messages. For example, “ke3E9Aa” is a message.</p>

<p>Contrary to King’s expectations, he always received wrong messages, because each messenger changed messages a bit before passing them to the next messenger. Since it irritated the King, he told you who are the Minister of the Science and Technology Agency of the Kingdom, “We don’t want such a wrong message any more. You shall develop software to correct it!” In response to the King’s new statement, you analyzed the messengers’ mistakes with all technologies in the Kingdom, and acquired the following features of mistakes of each messenger. A surprising point was that each messenger made the same mistake whenever relaying a message. The following facts were observed.</p>

<p>Mr. J rotates all characters of the message to the left by one. For example, he transforms “aB23d” to “B23da”.</p>

<p>Miss C rotates all characters of the message to the right by one. For example, she transforms “aB23d” to “daB23”.</p>

<p>Mr. E swaps the left half of the message with the right half. If the message has an odd number of characters, the middle one does not move. For example, he transforms “e3ac” to “ace3”, and “aB23d” to “3d2aB”.</p>

<p>Mr. A reverses the message. For example, he transforms “aB23d” to “d32Ba”.</p>

<p>Dr. P increments by one all the digits in the message. If a digit is ‘9’, it becomes ‘0’. The alphabet characters do not change. For example, he transforms “aB23d” to “aB34d”, and “e9ac” to “e0ac”.</p>

<p>Mr. M decrements by one all the digits in the message. If a digit is ‘0’, it becomes ‘9’. The alphabet characters do not change. For example, he transforms “aB23d” to “aB12d”, and “e0ac” to “e9ac”.</p>

<p>The software you must develop is to infer the original message from the final message, given the order of the messengers. For example, if the order of the messengers is A→J→M→P and the message given to the King is “aB23d”, what is the original message? According to the features of the messengers’ mistakes, the sequence leading to the final message is</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-munderover space="4"><mjx-over style="padding-bottom: 0.111em; padding-left: 0.265em;"><mjx-mpadded size="s"><mjx-block style="width: 0.833em; position: relative;"><mjx-rbox style="left: 0.278em; top: 0.2em; max-width: 0.833em;"><mjx-mspace style="height: 0.25em; vertical-align: -0.25em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base><mjx-mstyle><mjx-mo class="mjx-n"><mjx-stretchy-h class="mjx-c2192" style="width: 1.119em;"><mjx-ext><mjx-c></mjx-c></mjx-ext><mjx-end><mjx-c></mjx-c></mjx-end></mjx-stretchy-h></mjx-mo></mjx-mstyle></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-mpadded size="s"><mjx-block style="width: 1.583em; position: relative;"><mjx-rbox style="left: 0.278em; top: -0.15em; max-width: 1.583em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-mspace style="height: 0.75em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-munderover space="4"><mjx-over style="padding-bottom: 0.111em; padding-left: 0.224em;"><mjx-mpadded size="s"><mjx-block style="width: 0.833em; position: relative;"><mjx-rbox style="left: 0.278em; top: 0.2em; max-width: 0.833em;"><mjx-mspace style="height: 0.25em; vertical-align: -0.25em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base style="padding-left: 0.018em;"><mjx-mstyle><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-mstyle></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-mpadded size="s"><mjx-block style="width: 1.466em; margin: 0px 0px -0.022em; position: relative;"><mjx-rbox style="left: 0.278em; top: -0.15em; max-width: 1.466em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43D TEX-I"></mjx-c></mjx-mi><mjx-mspace style="height: 0.75em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-munderover space="4"><mjx-over style="padding-bottom: 0.111em; padding-left: 0.372em;"><mjx-mpadded size="s"><mjx-block style="width: 0.833em; position: relative;"><mjx-rbox style="left: 0.278em; top: 0.2em; max-width: 0.833em;"><mjx-mspace style="height: 0.25em; vertical-align: -0.25em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base><mjx-mstyle><mjx-mo class="mjx-n"><mjx-stretchy-h class="mjx-c2192" style="width: 1.332em;"><mjx-ext><mjx-c></mjx-c></mjx-ext><mjx-end><mjx-c></mjx-c></mjx-end></mjx-stretchy-h></mjx-mo></mjx-mstyle></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-mpadded size="s"><mjx-block style="width: 1.884em; position: relative;"><mjx-rbox style="left: 0.278em; top: -0.15em; max-width: 1.884em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mspace style="height: 0.75em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-munderover space="4"><mjx-over style="padding-bottom: 0.111em; padding-left: 0.266em;"><mjx-mpadded size="s"><mjx-block style="width: 0.833em; position: relative;"><mjx-rbox style="left: 0.278em; top: 0.2em; max-width: 0.833em;"><mjx-mspace style="height: 0.25em; vertical-align: -0.25em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base><mjx-mstyle><mjx-mo class="mjx-n"><mjx-stretchy-h class="mjx-c2192" style="width: 1.12em;"><mjx-ext><mjx-c></mjx-c></mjx-ext><mjx-end><mjx-c></mjx-c></mjx-end></mjx-stretchy-h></mjx-mo></mjx-mstyle></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-mpadded size="s"><mjx-block style="width: 1.584em; position: relative;"><mjx-rbox style="left: 0.278em; top: -0.15em; max-width: 1.584em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-mspace style="height: 0.75em;"></mjx-mspace></mjx-rbox></mjx-block></mjx-mpadded></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mn>32</mn><mi>B</mi><mi>a</mi><mi>d</mi><munderover><mstyle scriptlevel="0"><mo data-mjx-texclass="REL">→</mo></mstyle><mpadded width="+0.833em" lspace="0.278em" voffset=".15em" depth="-.15em"><mi>A</mi><mspace height=".75em"></mspace></mpadded><mpadded width="+0.833em" lspace="0.278em" voffset="-.2em" height="-.2em"><mspace depth=".25em"></mspace></mpadded></munderover><mi>d</mi><mi>a</mi><mi>B</mi><mn>23</mn><munderover><mstyle scriptlevel="0"><mo data-mjx-texclass="REL">→</mo></mstyle><mpadded width="+0.833em" lspace="0.278em" voffset=".15em" depth="-.15em"><mi>J</mi><mspace height=".75em"></mspace></mpadded><mpadded width="+0.833em" lspace="0.278em" voffset="-.2em" height="-.2em"><mspace depth=".25em"></mspace></mpadded></munderover><mi>a</mi><mi>B</mi><mn>23</mn><mi>d</mi><munderover><mstyle scriptlevel="0"><mo data-mjx-texclass="REL">→</mo></mstyle><mpadded width="+0.833em" lspace="0.278em" voffset=".15em" depth="-.15em"><mi>M</mi><mspace height=".75em"></mspace></mpadded><mpadded width="+0.833em" lspace="0.278em" voffset="-.2em" height="-.2em"><mspace depth=".25em"></mspace></mpadded></munderover><mi>a</mi><mi>B</mi><mn>12</mn><mi>d</mi><munderover><mstyle scriptlevel="0"><mo data-mjx-texclass="REL">→</mo></mstyle><mpadded width="+0.833em" lspace="0.278em" voffset=".15em" depth="-.15em"><mi>P</mi><mspace height=".75em"></mspace></mpadded><mpadded width="+0.833em" lspace="0.278em" voffset="-.2em" height="-.2em"><mspace depth=".25em"></mspace></mpadded></munderover><mi>a</mi><mi>B</mi><mn>23</mn><mi>d</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[32Bad\xrightarrow [ A ]{  } daB23\xrightarrow [ J ]{  } aB23d \xrightarrow [ M ]{  } aB12d\xrightarrow [ P ]{  } aB23d\]</span> </mjx-container></p>

<p>As a result, the original message should be “32Bad”.</p>

### 입력 

 <p>The input format is as follows.</p>

<pre>n
The order of messengers
The message given to the King
...
The order of messengers
The message given to the King
</pre>

<p>The first line of the input contains a positive integer n, which denotes the number of data sets. Each data set is a pair of the order of messengers and the message given to the King. The number of messengers relaying a message is between 1 and 6 inclusive. The same person may not appear more than once in the order of messengers. The length of a message is between 1 and 25 inclusive.</p>

### 출력 

 <p>The inferred messages are printed each on a separate line.</p>

