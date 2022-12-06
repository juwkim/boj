# [Bronze III] Floppies - 6436 

[문제 링크](https://www.acmicpc.net/problem/6436) 

### 성능 요약

메모리: 29200 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>In this age of Internet, on-line connections, instantaneous email, etc., there are still some people who need to work with floppy disks. John is one of those. Every evening he goes home and continues what he has been doing in his office on his private UNIX system. He copies all the files he needs to floppy disks according to the following procedure:</p>

<ol>
	<li>Put all files in one big SHAR file.</li>
	<li>Compress the file.</li>
	<li><tt>uuencode</tt> it, such that it is split in nice lines of 62 characters each (including the newline).</li>
	<li>Split it in files of 30,000 lines each (about 1.86Mb).</li>
	<li>Compress each of the files and put it on a floppy by itself.</li>
</ol>

<p>So far, this procedure always worked, since 1.86Mb of uuencoded text, after compression, will nicely fit on a 1.44Mb floppy disk.</p>

<p>Now, given that through compression the size of the SHAR file halves and that uuencoding a compressed file adds 50% to its size (each rounded to the nearest integer number of bytes), we would like to know for a given size of the SHAR file how many floppies John needs.</p>

### 입력 

 <p>The input file contains several test cases. Each test case consists of a single line containing one integer <i>s</i> (0 ≤ <i>s </i>≤ 1,000,000,000), specifying the size of the SHAR file in bytes.</p>

<p>The file ends with a file having <i>s = 0</i>. Do not generate output for this file.</p>

### 출력 

 <p>For each test case, first output the number of the test case (<tt>'File #1'</tt>, <tt>'File #2'</tt>, etc.), followed by a line that contains the minimal number of floppies needed for the transfer and a blank line. Adhere to the format shown below in the sample output.</p>

