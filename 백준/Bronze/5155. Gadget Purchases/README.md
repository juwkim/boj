# [Bronze II] Gadget Purchases - 5155 

[문제 링크](https://www.acmicpc.net/problem/5155) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>aOne of the reasons why health care in the US is expensive is that many hospitals are equipped with very advanced, and expensive, machines. The cost for these machines must be recovered somehow, including by using them on a lot of patients, and charging those patients (or their insurance) for the expensive usage. Of course, there are many legitimate reasons for purchasing expensive hospital equipment, such as helping advance technology for the future to bring down the price, or actual concern for patients, even if the machine only helps a few.1 Here, we will consider the purchasing decision as a solely economic problem, i.e., find out which machines will bring in more money than they cost.</p>

<p>You will be given a list of machines, each with a purchasing cost p<sub>i</sub>, a usage cost c<sub>i</sub>, and a maximum number of usages u<sub>i</sub>. In addition, for each machine, you will have a suggested amount charged to the patient or insurance, r<sub>i</sub>. This means that you pay p<sub>i</sub> to buy the machine, and c<sub>i</sub> each time you use it; however, the patient pays you r<sub>i</sub> for using it. No machine can be used more than u<sub>i</sub> times. If the demand is higher than u<sub>i</sub>, you can only serve the first u<sub>i</sub> patients. You will also be given a list of patients, and for each of them, which machine he or she would need to use. From this information, you should determine which machines are profitable.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of each data set contains two integers n, m. n ≤ 10000 is the number of patient visits, and m ≤ 1000 the number of machines you are considering.</p>

<p>This is followed by m lines, each describing one machine by giving you the four integer numbers p<sub>i</sub>, c<sub>i</sub>, u<sub>i</sub>, r<sub>i</sub>. Finally, there are n lines, each containing one integer m<sub>j</sub>, 1 ≤ m<sub>j</sub> ≤ m, the number of the machine that would be needed for the jth visit.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, output all the machines whose purchase would be profitable (meaning that the total revenue is strictly more than the total expenditure). The numbers should be output one per line, in sorted order. Each data set should be followed by a blank line.</p>

