# [Silver I] PHONE - 8943 

[문제 링크](https://www.acmicpc.net/problem/8943) 

### 성능 요약

메모리: 1116 KB, 시간: 0 ms

### 분류

구현, 브루트포스 알고리즘, 기하학, 많은 조건 분기

### 제출 일자

2025년 6월 25일 03:33:45

### 문제 설명

<p>Mobile phones prevail in everyday life. Every mobile phone has a number pad for users to dial the telephone number. Figure 1 shows a typical layout of number pads, which can be represented as 4 by 3 rectangular cells. We know that some mobile phone numbers are easy to memorize, since entering in sequence of digits implies an easy-to-remember geometric figure. </p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8943/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-17%20%EC%98%A4%ED%9B%84%204.10.15.png" style="height:159px; width:134px"></p>

<p style="text-align: center;">Figure 1</p>

<p>For each phone number, we can make a corresponding geometric figure, Phone Plot, which is a sequence of connected line segments. Assume that a phone number with n digits is d<sub>1</sub> d<sub>2</sub> d<sub>3</sub> . . . . . d<sub>n-1</sub> d<sub>n</sub> . The first line segment of Phone Plot is a line segment connecting the center points of pad d<sub>1</sub> and pad d<sub>2</sub> . The second line segment of Phone Plot connects the center points of pad d<sub>2</sub> and d<sub>3</sub> . In a similar way the k-th line segment connects the center points of pad d<sub>k</sub> and pad d<sub>k+1</sub> , and the last segment connects d<sub>n-1</sub> and d<sub>n</sub> .</p>

<p>Let us show a few examples. The Phone Plot for the number 1023289873 is shown as the thick lines in Figure 2(a). Figure 2(b) shows that the Phone Plot for a number 1159533969. </p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8943/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-17%20%EC%98%A4%ED%9B%84%204.11.44.png" style="height:156px; width:134px"></p>

<p style="text-align: center;">Figure 2(a)</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8943/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-17%20%EC%98%A4%ED%9B%84%204.11.50.png" style="height:157px; width:134px"></p>

<p style="text-align: center;">Figure 2(b)</p>

<p>You should note that some connecting line segments may overlap other line segment collinearly.</p>

<p>We characterize a Phone Plot by the Minimal Number of Decomposing Segments(MNDS). MNDS is the minimal number of line segments to reconstruct the given Phone Plot. So we easily find that the MNDS of the number 1023289873 is 5, and the MNDS of 1159533969 is 3. If the Phone Plot is reduced to a single point for a number (e.g., 0000000000), then MNDS of such a point Phone Plot is defined 0.</p>

<p>We want to classify the phone number into three disjoint classes; EXCELLENT, GOOD and BAD by the complexity of Phone Plot. Thus if the MNDS of Phone Plot is at most 3, then this number is classified to EXCELLENT. If MNDS is exactly 4, then this number is classified to GOOD. If the MNDS is greater than or equal to 5, that number is classified to BAD.</p>

<p>According to this classification, we say 1023289873 is BAD and 1159533969 is EXCELLENT. Figure 3 shows another example with 5233999008. Since the MNDS of 5233999008 is 5, so this number is BAD. </p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/8943/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-17%20%EC%98%A4%ED%9B%84%204.11.57.png" style="height:159px; width:134px"></p>

<p style="text-align: center;">Figure 3</p>

<p>You have to decide whether the phone number given is EXCELLENT or GOOD or BAD according to the MNDS of the Phone Plot. </p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case starts with a string representing a phone number. The length of a phone number string is greater than 5 and less than 20. </p>

### 출력 

 <p>Your program is to write to standard output. For each test case, print EXCELLENT or GOOD or BAD in a line. The following shows four test cases. </p>

