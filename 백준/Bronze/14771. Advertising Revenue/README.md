# [Bronze II] Advertising Revenue - 14771 

[문제 링크](https://www.acmicpc.net/problem/14771) 

### 성능 요약

메모리: 30840 KB, 시간: 336 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>One of the motivations for producing fake news stories is money, obtained from ads that are shown to or clicked on by the site’s visitors. Mysterious, surprising, or scandalous stories tend to attract a lot of readers; hence the often outrageous and vague nature of fake news stories (“You won’t believe . . .”) Online ads typically come in two forms: display ads and clickthrough ads. For the former, the advertiser will pay the site money just for displaying the ad (the idea is to build brand recognition); for the latter, the advertiser only pays when you click on the ad (the idea is that some fraction of clicks will lead to purchases, now or in the future). Prices for online ads range from a few cents per display/click to as much as $100 per click<sup>1</sup>. In this problem, you will be presented with a list of ads (clickthrough and display) and a history of visitors, what they saw, and what they clicked. Your goal is to calculate how much money the fake news website made.</p>

<p><sup>1</sup>Class-action lawyers</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains two integers n, v. 2 ≤ n ≤ 1000 is the number of ads the site has as customers, and 0 ≤ v ≤ 1000 is the number of visitors to the site.</p>

<p>This is followed by n lines, each describing one ad i with two integers d<sub>i</sub>, p<sub>i</sub>. The number d<sub>i</sub> will always be either 0 or 1; a value of 1 means that the ad is a display ad (the site gets paid just for displaying it), and a value of 0 means that the ad is a clickthrough ad (the site only gets paid when the user clicks on it). 1 ≤ p<sub>i</sub> ≤ 1000 is the payment for the ad, which will be paid for displaying it (display ad) or clicking it (clickthrough ad).</p>

<p>Next come v lines, each describing one visitor j with three integers a<sub>j,1</sub>, a<sub>j,2</sub>, c<sub>j</sub> . The first two numbers a<sub>j,1</sub>, a<sub>j,2</sub> are the two ads the user is shown when visiting the site; they will be distinct and will always be between 1 and n, inclusive. The number c<sub>j</sub> ∈ {0, 1, 2} is the ad the user clicked on. A value of 0 means the user did not click on anything, 1 means that the user clicked on a<sub>j,1</sub>, and 2 means that he/she clicked on a<sub>j,2</sub>. Notice that a user might click on a display ad — the site does not get extra payment for this.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the total payment that the fake news site receives.</p>

<p>Each data set should be followed by a blank line.</p>

