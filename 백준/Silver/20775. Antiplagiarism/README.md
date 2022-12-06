# [Silver V] Antiplagiarism - 20775 

[문제 링크](https://www.acmicpc.net/problem/20775) 

### 성능 요약

메모리: 159296 KB, 시간: 244 ms

### 분류

문자열(string)

### 문제 설명

<p>Students of a specialized arts school must paint a picture as their graduation qualification work. In the course of their study, the students have mastered a technique of painting on a square canvas using two types of brushstroke: <<asterisk>> and <<hash>>. Using this technique, the prodigies must paint a square masterpiece of the size $N \times N$, using only the two types of strokes. </p>

<p>This is a tedious task, and every year a few students decide they could benefit from the hard work of the previous generations of their alumni-to-be. However, their imagination is quite limited. A student takes someone else's picture and applies the following operations several times: 1) rotate the image 90 degrees, 2) mirror it along the vertical or horizontal axis. After that, he submits the result as his own picture. Some students have even tried presenting unchanged old works as their own.</p>

<p>Their professors can feel something is wrong, but unfortunately, it is beyond their own powers to find out for sure whether the paintings are plagiarized or not. It's time to put an end to this disgraceful business and write a program that would automate the plagiarism check by defining whether a painting is a copy or not, thus helping the professors to find cheating students.</p>

### 입력 

 <p>The first line of the input file contains a single integer: $N$ is the size of the side of the square canvas ($1 \leq N \leq 500$). Each of the following $N$ lines contains $N$ symbols \verb|*| or \verb|#|, denoting the types of the corresponding strokes of the first painting. Next comes an empty line. The next $N$ lines describe the second painting in the same format.</p>

### 출력 

 <p>The only line of the output file is the word <code>YES</code>, if one of the paintings is plagiarized from another, or <code>NO</code> if not.</p>

