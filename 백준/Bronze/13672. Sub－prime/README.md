# [Bronze I] Sub-prime - 13672 

[문제 링크](https://www.acmicpc.net/problem/13672) 

### 성능 요약

메모리: 30840 KB, 시간: 348 ms

### 분류

구현(implementation)

### 문제 설명

<p>The most recent economic crisis was partly caused by the manner in which banks made loans to people unable to repay them and resold such loans to other banks as debentures. Obviously, when people failed to repay their loans, the whole system collapsed.</p>

<p>The crisis was so deep that it affected countries all over the world, including Nlogonia, where the honored prime minister Man Dashuva ordered the Central Bank chairman to come up with a solution. He came up with a brilliant idea: if all banks could liquidate its debentures only with its own monetary reserves, all banks would survive and the crisis would be averted.</p>

<p>However, with the elevated number of debentures and banks involved, this was an extremely complicated task, so he asked for your help in writing a program that, given the banks and the debentures printed by them, determines if it is possible that all banks pay back their debts using only their monetary reserves and credits.</p>

### 입력 

 <p>The input consists of several test cases. The first line of each test case contains two integers <em>B</em> and <em>N</em>, indicating the number of banks (1 ≤ B ≤ 20) and the number of debentures printed by the banks (1 ≤ N ≤ 20). The banks are identified by integers between 1 and <em>B</em>. The second line contains <em>B</em> integers <em>R</em><sub>i</sub> separated by spaces, indicating the monetary reserves of each one of the <em>B</em> banks (0 ≤ R<sub>i </sub>≤ 10<sup>4</sup>, for 1 ≤ i ≤ B). The <em>N</em> following lines contain each one three integers separated by spaces: an integer <em>D</em>, indicating the debtor bank (1 ≤ D ≤ B), an integer <em>C</em> , indicating the creditor bank (1 ≤ C ≤ B e D ≠ C) and an integer <em>V</em>, indicating the debenture value (1 ≤ V ≤ 10<sup>4</sup>).</p>

<p>The end of input is indicated by a line containing only two zeros, separated by spaces.</p>

### 출력 

 <p>For each test case, your program should print a single line, containing a single character: 'S', if it is possible to liquidate all debentures without a bailout from the Central Bank of Nlogonia, or 'N' if a bailout is necessary.</p>

