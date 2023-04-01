# [Silver IV] Diamonds Are for Evers - 17847 

[문제 링크](https://www.acmicpc.net/problem/17847) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현, 문자열

### 문제 설명

<p>Top secret agent Claude L. Evers has a unique way to send encoded messages. The message is implanted in a square grid of letters as follows: starting at the middle letter at the left-most side of the grid he writes the message along the diagonal heading to the top of the grid. After he hits the top, he then continues the message on a diagonal heading right until he hits the right hand side. He continues this way, tracing out a diamond until he reaches the left side again. At this point he continues the message in the diamond nested inside the diamond he just filled in, and after this the next diamond inside, and so on. Any left over squares both inside and outside the original diamond are filled with random letters.</p>

<p>The grids below show the steps in encoding the message <code>GENERAL TSO NEEDS CHICKEN NOW</code>. The first grid shows the encoding after the first diamond has been filled in. The second, third and fourth grids show successively smaller diamonds being filled in. Finally, the last grid shows the final message after random letters have been placed in the empty squares around the grid.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/cdfeb3ab-e6e1-402d-8dda-aba4113e1ff4/-/preview/" style="width: 516px; height: 272px;"></p>

<p>Note that if the original message had not filled in the entire set of diamonds then random letters would have been used to fill those empty slots as well (see Sample Input 2 for an example of this when encoding <code>GENERAL TSO HATES CHICKEN</code>). To send the message, Evers concatenates all the rows together, topto-bottom. The above grid would be sent as</p>

<blockquote>
<p><code>THEESEARENSRNTAEDNCACGEEWNHLTEKOITUALNCSLYRANODOM</code></p>
</blockquote>

<p>Evers has made one fatal mistake, however: he just explained to us how he encodes messages! Now we can write a program that can decode any message he sends. And by “we” of course we mean you.</p>

### 입력 

 <p>Input consists of a single string of uppercase alphabetic letters. The length of each string will be a square of an odd integer and less than 1 000 in length.</p>

### 출력 

 <p>Output the decoded message. Note that this message might contain some random letters at the end if the original message did not fill the entire set of diamonds.</p>

