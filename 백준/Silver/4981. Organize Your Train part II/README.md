# [Silver IV] Organize Your Train part II - 4981 

[문제 링크](https://www.acmicpc.net/problem/4981) 

### 성능 요약

메모리: 115160 KB, 시간: 144 ms

### 분류

브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵, 문자열

### 문제 설명

<p>RJ Freight, a Japanese railroad company for freight operations has recently constructed exchange lines at Hazawa, Yokohama. The layout of the lines is shown in Figure B-1.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/4981/1.gif" style="height:194px; width:407px"></p>

<p style="text-align:center">Figure B-1: Layout of the exchange lines</p>

<p>A freight train consists of 2 to 72 freight cars. There are 26 types of freight cars, which are denoted by 26 lowercase letters from "a" to "z". The cars of the same type are indistinguishable from each other, and each car's direction doesn't matter either. Thus, a string of lowercase letters of length 2 to 72 is sufficient to completely express the configuration of a train.</p>

<p>Upon arrival at the exchange lines, a train is divided into two sub-trains at an arbitrary position (prior to entering the storage lines). Each of the sub-trains may have its direction reversed (using the reversal line). Finally, the two sub-trains are connected in either order to form the final configuration. Note that the reversal operation is optional for each of the sub-trains.</p>

<p>For example, if the arrival configuration is "abcd", the train is split into two sub-trains of either 3:1, 2:2 or 1:3 cars. For each of the splitting, possible final configurations are as follows ("+" indicates final concatenation position):</p>

<pre>  [3:1]
    abc+d  cba+d  d+abc  d+cba
  [2:2]
    ab+cd  ab+dc  ba+cd  ba+dc  cd+ab  cd+ba  dc+ab  dc+ba
  [1:3]
    a+bcd  a+dcb  bcd+a  dcb+a
</pre>

<p>Excluding duplicates, 12 distinct configurations are possible.</p>

<p>Given an arrival configuration, answer the number of distinct configurations which can be constructed using the exchange lines described above.</p>

### 입력 

 <p>The entire input looks like the following.</p>

<pre>the number of datasets = m
1st dataset 
2nd dataset 
... 
m-th dataset </pre>

<p>Each dataset represents an arriving train, and is a string of 2 to 72 lowercase letters in an input line.</p>

### 출력 

 <p>For each dataset, output the number of possible train configurations in a line. No other characters should appear in the output.</p>

