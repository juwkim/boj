# [Silver I] URLs - 6324 

[문제 링크](https://www.acmicpc.net/problem/6324) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

많은 조건 분기, 파싱, 정규 표현식, 문자열

### 제출 일자

2025년 4월 5일 07:53:42

### 문제 설명

<p>In the early nineties, the World Wide Web (WWW) was invented. Nowadays, most people think that the WWW simply consists of all the pretty (or not so pretty) HTML-pages that you can read with your WWW browser. But back then, one of the main intentions behind the design of the WWW was to unify several existing communication protocols.</p>

<p>Then (and even now), information on the Internet was available via a multitude of channels: FTP, HTTP, E-Mail, News, Gopher<sup>2</sup>, and many more. Thanks to the WWW, all these services can now be uniformly addressed via URLs (Uniform Resource Locators). The syntax of URLs is defined in the Internet standard RFC 1738. For our problem, we consider a simplified version of the syntax, which is as follows:</p>

<p style="text-align: center;"><strong>< protocol > "://" < host > [ ":" < port > ] [ "/" < path > ]</strong></p>

<p>The square brackets [] mean that the enclosed string is optional and may or may not appear. Examples of URLs are the following:</p>

<ul>
	<li>http://www.informatik.uni-ulm.de/acm</li>
	<li>ftp://acm.baylor.edu:1234/pub/staff/mr-p</li>
	<li>gopher://veryold.edu</li>
</ul>

<p>More specifically,</p>

<ul>
	<li>< protocol > is always one of http, ftp or gopher.</li>
	<li>< host > is a string consisting of alphabetic (a-z, A-Z) or numeric (0-9) characters and points (.), dash (-), underscore(_).</li>
	<li>< port > is a positive integer, smaller than 65536.</li>
	<li>< path > is a string that contains no spaces.</li>
</ul>

<p>You are to write a program that parses an URL into its components.</p>

<p><sup>2</sup>The ancestor of today’s WWW. Now nearly extinct, but quite important when the WWW was invented.</p>

### 입력 

 <p>The input starts with a line containing a single integer n, the number of URLs in the input file. The following n lines contain one URL each, in the format described above. The URLs will consist of at most 60 characters each.</p>

### 출력 

 <p>For each URL in the input first print the number of the URL, as shown in the sample output. Then print four lines, stating the protocol, host, port and path specified by the URL. If the port and/or path are not given in the URL, print the string <default> instead. Adhere to the format shown in the sample output.</p>

<p>Print a blank line after each test case.</p>

