# [Silver V] Wizard of Odds - 15436 

[문제 링크](https://www.acmicpc.net/problem/15436) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 수학(math)

### 문제 설명

<p>You have just completed a brave journey to see <em>The Wizard of Odds</em>, who agrees to grant you any wish, so long as you can complete the following puzzle:</p>

<p>The Wizard starts by telling you two integers: <em>N</em> and <em>K</em>. He then secretly selects a number from 1 to <em>N</em> (inclusive), and does not tell you this number.</p>

<p>Your goal is to correctly guess the secret number. Before guessing, you are allowed to ask <em>K</em> "true/false" questions about the number, for example, <em>"Is the number even?"</em> or <em>"Is the number between 7 and 10?"</em>, or <em>"Is the number 17 or 22?"</em>, or <em>"Is the number prime?"</em>. And the Wizard will answer with "true" or "false" to each question. The Wizard will always answer honestly. After answering the <em>K</em> questions, you must guess the number. If you win (guess the number correctly), you will be granted your wish; but if the Wizard wins (you guess incorrectly), you will be turned into a flying monkey.</p>

<p>(Formally, you can think of a "question" as a function from <em>{1, 2, ..., N}</em> to <em>{true, false}</em>, and the Wizard will answer by telling you whether the value of the function is <em>true</em> or <em>false</em> for his secret number.)</p>

<p>Assuming that you have been told <em>N</em> and <em>K</em>, can you always exactly determine the Wizard's secret number (and guarantee that you win) using only <em>K</em> questions?</p>

### 입력 

 <p>The input consists of a single line containing two integers <em>N</em> and <em>K</em> (<em>2 ≤ N ≤ 10<sup>101</sup></em>, <em>0 ≤ K ≤ N</em>), separated by a single space.</p>

<p><em>Note: These inputs might NOT fit into a 64-bit integer.</em></p>

### 출력 

 <p>Output <code>"Your wish is granted!"</code> (without the quotes) if it is possible for you to guarantee that you win the game (regardless of the number the Wizard picks). Otherwise, print <code>"You will become a flying monkey!"</code> (without the quotes) if it is not possible.</p>

