# [Silver I] Thread Tree - 16795 

[문제 링크](https://www.acmicpc.net/problem/16795) 

### 성능 요약

메모리: 111160 KB, 시간: 116 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 재귀, 트리

### 제출 일자

2025년 5월 6일 14:10:05

### 문제 설명

<p>Nathan O. Davis has been running an electronic bulletin board system named JAG-channel. He is now having hard time to add a new feature there --- threaded view.</p>

<p>Like many other bulletin board systems, JAG-channel is thread-based. Here a thread (also called a topic) refers to a single conversation with a collection of posts. Each post can be an opening post, which initiates a new thread, or a reply to a previous post in an existing thread.</p>

<p>Threaded view is a tree-like view that reflects the logical reply structure among the posts: each post forms a node of the tree and contains its replies as its subnodes in the chronological order (i.e. older replies precede newer ones). Note that a post along with its direct and indirect replies forms a subtree as a whole.</p>

<p>Let us take an example. Suppose: a user made an opening post with a message <code>hoge</code>; another user replied to it with <code>fuga</code>; yet another user also replied to the opening post with <code>piyo</code>; someone else replied to the second post (i.e. <code>fuga</code>”) with <code>foobar</code>; and the fifth user replied to the same post with <code>jagjag</code>. The tree of this thread would look like:</p>

<pre>hoge
├─fuga
│　├─foobar
│　└─jagjag
└─piyo
</pre>

<p>For easier implementation, Nathan is thinking of a simpler format: the depth of each post from the opening post is represented by dots. Each reply gets one more dot than its parent post. The tree of the above thread would then look like:</p>

<pre>hoge
.fuga
..foobar
..jagjag
.piyo
</pre>

<p>Your task in this problem is to help Nathan by writing a program that prints a tree in the Nathan's format for the given posts in a single thread.</p>

### 입력 

 <p>Input contains a single dataset in the following format:</p>

<pre><var>n</var>
<var>k<sub>1</sub></var>
<var>M<sub>1</sub></var>
<var>k<sub>2</sub></var>
<var>M<sub>2</sub></var>
:
:
<var>k<sub>n</sub></var>
<var>M<sub>n</sub></var>
</pre>

<p>The first line contains an integer <var>n</var> (<var>1 ≤ n ≤ 1,000</var>), which is the number of posts in the thread. Then <var>2n</var> lines follow. Each post is represented by two lines: the first line contains an integer <var>k<sub>i</sub></var> (<var>k<sub>1</sub> = 0</var>, <var>1 ≤ k<sub>i</sub> < i</var> for <var>2 ≤ i ≤ n</var>) and indicates the <var>i</var>-th post is a reply to the <var>k<sub>i</sub></var>-th post; the second line contains a string <var>M<sub>i</sub></var> and represents the message of the <var>i</var>-th post. <var>k<sub>1</sub></var> is always 0, which means the first post is not replying to any other post, i.e. it is an opening post.</p>

<p>Each message contains 1 to 50 characters, consisting of uppercase, lowercase, and numeric letters.</p>

### 출력 

 <p>Print the given <var>n</var> messages as specified in the problem statement.</p>

