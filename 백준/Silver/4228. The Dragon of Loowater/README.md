# [Silver I] The Dragon of Loowater - 4228 

[문제 링크](https://www.acmicpc.net/problem/4228) 

### 성능 요약

메모리: 111772 KB, 시간: 124 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 5월 10일 02:22:16

### 문제 설명

<p>Once upon a time, in the Kingdom of Loowater, a minor nuisance turned into a major problem.</p>

<p>The shores of Rellau Creek in central Loowater had always been a prime breeding ground for geese. Due to the lack of predators, the geese population was out of control. The people of Loowater mostly kept clear of the geese. Occasionally, a goose would attack one of the people, and perhaps bite off a finger or two, but in general, the people tolerated the geese as a minor nuisance.</p>

<p>One day, a freak mutation occurred, and one of the geese spawned a multi-headed fire-breathing dragon. When the dragon grew up, he threatened to burn the Kingdom of Loowater to a crisp. Loowater had a major problem. The king was alarmed, and called on his knights to slay the dragon and save the kingdom.</p>

<p>The knights explained: "To slay the dragon, we must chop off all its heads. Each knight can chop off one of the dragon's heads. The heads of the dragon are of different sizes. In order to chop off a head, a knight must be at least as tall as the diameter of the head. The knights' union demands that for chopping off a head, a knight must be paid a wage equal to one gold coin for each centimetre of the knight's height."</p>

<p>Would there be enough knights to defeat the dragon? The king called on his advisors to help him decide how many and which knights to hire. After having lost a lot of money building Mir Park, the king wanted to minimize the expense of slaying the dragon. As one of the advisors, your job was to help the king. You took it very seriously: if you failed, you and the whole kingdom would be burnt to a crisp!</p>

### 입력 

 <p>The input contains several test cases. The first line of each test case contains two integers between 1 and 20000 inclusive, indicating the number n of heads that the dragon has, and the number m of knights in the kingdom. The next n lines each contain an integer, and give the diameters of the dragon's heads, in centimetres. The following m lines each contain an integer, and specify the heights of the knights of Loowater, also in centimetres.</p>

<p>The last test case is followed by a line containing:</p>

<pre>0 0</pre>

### 출력 

 <p>For each test case, output a line containing the minimum number of gold coins that the king needs to pay to slay the dragon. If it is not possible for the knights of Loowater to slay the dragon, output the line:</p>

<pre>Loowater is doomed!</pre>

