# [Bronze I] A Towering Problem - 11762 

[문제 링크](https://www.acmicpc.net/problem/11762) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

브루트포스 알고리즘

### 문제 설명

<p>You’ve been put in charge of an art exhibit from the famous minimalist sculptor J (even his name is minimalist!). J’s work involves the careful layout of vertically dispositioned orthogonal parallelpipeds in a set of tapering obelisks — in other words, he puts smaller boxes on top of larger boxes. His most recent triumph is called “2 by 3’s Decreasing,” in which he has various sets of six boxes arranged in two stacks of three boxes each. One such set is shown below:</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11762/1.png" style="height:175px; width:139px"></p>

<p>J has sent you the art exhibit and it is your job to set up each of the six-box sets at various locations throughout the museum. But when the sculptures arrived at the museum, uncultured barbarians (i.e., delivery men) simply dropped each set of six boxes on the floor, not realizing the aesthetic appeal of their original layout. You need to reconstruct each set of two towers, but you have no idea which box goes on top of the other! All you know is the following: for each set of six, you have the heights of the two towers, and you know that in any tower the largest height box is always on the bottom and the smallest height box is on the top. Armed with this information, you hope to be able to figure out which boxes go together before tomorrow night’s grand opening gala.</p>

### 입력 

 <p>The input consists of eight positive integers. The first six represent the heights of the six boxes. These values will be given in no particular order and no two will be equal.</p>

<p>The last two values (which will never be the same) are the heights of the two towers.</p>

<p>All box heights will be ≤ 100 and the sum of the box heights will equal the sum of the tower heights.</p>

### 출력 

 <p>Output the heights of the three boxes in the first tower (i.e., the tower specified by the first tower height in the input), then the heights of the three boxes in the second tower. Each set of boxes should be output in order of decreasing height. Each test case will have a unique answer.</p>

