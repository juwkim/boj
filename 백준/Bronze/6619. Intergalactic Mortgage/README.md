# [Bronze I] Intergalactic Mortgage - 6619 

[문제 링크](https://www.acmicpc.net/problem/6619) 

### 성능 요약

메모리: 118280 KB, 시간: 572 ms

### 분류

수학

### 문제 설명

<p>Many people on Earth want to solve their housing. When they have not enough money to buy their house or flat, they get mortgage<sup>∗</sup> from some bank and then they pay fixed monthly payments until they redeem the mortgage.</p>

<p>You may think that paying mortgage for 30 years is a long time, but that is quite short time compared to galactic mortgages. Aliens are not buying houses, but whole planets. Since planets are a “little” more expensive, the mortgage periods are longer.</p>

<p>The mortgages work the same way for aliens as for us earthlings. If an alien wants to buy a planet, he comes to GCB (Galactic Central Bank) to borrow an amount of X. Bank offers a mortgage with the interest rate r% p.a. (= “per year”). Interests are computed at the end of each month (1 alien year has 12 months). At the end of every month, the current debt is raised by (r/12)% and then the alien pays back to bank some fixed amount Y , which is subtracted from the debt.</p>

<p>Because of intergalactic financial crisis, bank rules are quite strict. Every mortgage must start on the first day of a year. If an alien does not pay enough money to cover the principal and interests within first N years, the bank will then confiscate his planet.</p>

<p>On the other hand, galactic employment works quite nice. Once you have a job, you are guaranteed to have it forever. An alien can give the same amount Y at the end of each month for the whole mortgage period.</p>

<p>Your task is to decide whether an alien is able to pay his mortgage or not.</p>

<p><sup>∗</sup>hypot´eka</p>

### 입력 

 <p>The input contains several test cases. Each test case is described by a line containing numbers X, Y , N, r separated by space. X is principal (the initial amount borrowed), Y is the monthly payment (paid at the end of each month), N is number of years in which the alien is required to pay the mortgage, r is interest rate p.a. in percent.</p>

<p>X, Y are integer numbers (1 ≤ X,Y ≤ 1 000 000 000). N is integer number (1 ≤ N ≤ 10 000). r is float (0 ≤ r ≤ 100, 2 digits precision). Values X, Y , N, r for each test case were chosen so that even if the alien would not pay anything for the whole time, the resulting debt after N year would be at most 10<sup>25</sup>. Also, the precision of double should be sufficient for most computations (differences in the rate less then 10<sup>-8</sup>% will not affect the result).</p>

<p>The last test case is followed by a line containing four zeros.</p>

### 출력 

 <p>For each test case output “YES” if the alien can pay the mortgage within N years and “NO” if his salary is too small to pay the mortgage on time.</p>

