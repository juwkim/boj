# [Silver IV] Where To Go? - 14010 

[문제 링크](https://www.acmicpc.net/problem/14010) 

### 성능 요약

메모리: 115408 KB, 시간: 212 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p><strong><a href="https://en.wikipedia.org/wiki/RioCard" target="_blank">RioCard</a> only works in Rio??</strong> - Dudu, 2014</p>

<p>Dudu doesn't know any Thai, so before traveling to <a href="https://en.wikipedia.org/wiki/Bangkok" target="_blank">Bangkok, Thailand</a> from his hometown of <a href="https://en.wikipedia.org/wiki/Rio_de_Janeiro" target="_blank">Rio de Janeiro, Brazil</a> he prepared a paper with some common sentences.</p>

<p>Most of the sentences were normal small talk conversations, like: "sà-wàt-dee" (Hello), "pŏm chêu Dudu" (My name is Dudu), and "hoh wer-krâaf kŏng pŏm dtem-bpai-dûay bplaa lăi" (My hovercraft is full of eels).</p>

<p>He also prepared a sentence where it was written in Thai: <strong>"Help me, I am a tourist and I don't speak Thai. Please let me know what train I should take to go to the Lumphini subway station."</strong></p>

<p>When he arrived there he got really surprised; both because he couldn't use his RioCard, and because they don't use Latin Characters to write, so "Hello" would actually be written as สวัสดี.</p>

<p>At one point he got lost and wanted to go back to the hotel. He pulled out his big "help me" note and thought: "somewhere in this note there is the name of my station. Maybe I can figure out how to write it in Thai using the list of all stations."</p>

<p>For example, if his station in latin characters is "ABLA," he knows that in Thai characters it will be a four-letter word with the first and the fourth being the same. Can you help Dudu finding his station?</p>

### 입력 

 <p>The first line of input will contain an integer N with the number of stations in the subway system.</p>

<p>The second line will contain a string s with the sentence Dudu had prepared.</p>

<p>The following N lines will contain the names of the stations, one per line.</p>

<ul>
	<li>1 ≤ N ≤ 1000</li>
	<li>1 ≤ |s| ≤ 1000</li>
</ul>

<p>Each station name will not be empty, and the sum of the sizes of all names of stations will not be greater than 1000.</p>

<p>s will consist entirely of upper case letters. All station names will consist entirely of lower case Latin letters (which will represent Thai characters).</p>

### 출력 

 <p>Output N lines, one for each station name.</p>

<p>On the i-th line, output a single dash in case that station name cannot be in s. Otherwise output a single number with the first position in s where the station name could appear.</p>

<p>See the sample below for a complete example.</p>

