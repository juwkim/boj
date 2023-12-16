# [Silver IV] Where Are My Genes - 5756 

[문제 링크](https://www.acmicpc.net/problem/5756) 

### 성능 요약

메모리: 114196 KB, 시간: 744 ms

### 분류

구현

### 제출 일자

2023년 12월 17일 02:11:29

### 문제 설명

<p>One way that scientists try to measure how one species evolved into another is to find out how the ancestor’s genome changed into the other’s. Closely related species have several genes in common and it turns out that a good way to compare them is comparing how the common genes changed place.</p>

<p>One of the most common mutations that change the order of a genomes’ genes is the reversal. If we model a genome as a sequence of N genes with each gene being an integer from 1 to N, then a reversal is a mutation that changes the genome by reverting the order of a block of consecutive genes. A reversal can be described by two indexes (i, j), 1 ≤ i ≤ j ≤ N, indicating that it reverts the order of the genes within indexes from i to j. So, when it is applied to a genome [g<sub>1</sub>, . . . , g<sub>i−1</sub>, g<sub>i</sub>, g<sub>i+1</sub>, . . . , g<sub>j−1</sub>, g<sub>j</sub>, g<sub>j+1</sub>, . . . , g<sub>N</sub>], we obtain the genome [g<sub>1</sub>, . . . , g<sub>i−1</sub>, g<sub>j</sub>, g<sub>j−1</sub>, . . . , g<sub>i+1</sub>, g<sub>i</sub>, g<sub>j+1</sub>, . . . , g<sub>N</sub>]. As an example, the reversal (3, 6) applied to the genome [1, 2, 3, 4, 5, 6, 7] gives [1, 2, 6, 5, 4, 3, 7]. If after that the reversal (1, 3) is applied, we obtain the genome [6, 2, 1, 5, 4, 3, 7].</p>

<p>A scientist studying the evolution of a species wants to try a series of reversals on its genome. Then he wants to query the final position of several genes. Would you take the challenge and help him?</p>

### 입력 

 <p>The input contains several test cases. The first line of a test case contains one integer N indicating the number of genes in the genome (1 ≤ N ≤ 50000). You may assume that the initial order of the genes is the sequence of integers from 1 to N in increasing order. The second line of a test case contains one integer R (0 ≤ R ≤ 1000) indicating the number of reversals to be applied to the genome. Then R lines follow, each containing two integers i, j (1 ≤ i ≤ j ≤ N), separated by a single space, indicating the two indexes that define the corresponding reversal. After the description of the reversals there is a line containing one integer Q (0 ≤ Q ≤ 100), indicating the number of queries for genes, followed by Q lines, where each line contains an integer representing a gene whose final position you must determine.</p>

<p>The end of input is indicated by N = 0.</p>

### 출력 

 <p>For each test case in the input your program must produce Q + 1 lines of output. The first line must contain the string “Genome ” followed by the number of the test case. The following Q lines must contain one integer each representing the answers of the queries.</p>

