# [Silver III] Over the Hill, Part 1 - 21154 

[문제 링크](https://www.acmicpc.net/problem/21154) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 선형대수학(linear_algebra), 수학(math), 문자열(string)

### 문제 설명

<p>Hill encryption (devised by mathematician Lester S. Hill in 1929) is a technique that makes use of matrices and modular arithmetic.  It is ideally used with an alphabet that has a prime number of characters, so we'll use the $37$ character alphabet <code>A</code>, <code>B</code>, $\ldots$, <code>Z</code>, <code>0</code>, <code>1</code>, $\ldots$, <code>9</code>, and the space character.  The steps involved are the following:</p>

<ol>
	<li>Replace each character in the initial text (the <em>plaintext</em>) with the substitution <code>A</code>$\rightarrow 0$, <code>B</code>$\rightarrow 1$, $\ldots$, <code>(space)</code>$ \rightarrow 36$.  If the plaintext is <code>ATTACK AT DAWN</code> this becomes $$0\ 19\ 19\ 0\ 2\ 10\ 36\ 0\ 19\ 36\ 3\ 0\ 22\ 13$$.</li>
	<li>Group these number into three-component vectors, padding with spaces at the end if necessary.  After this step we have \[ \left( \begin{array}{c} 0 \\ 19 \\ 19 \end{array} \right) \left( \begin{array}{c} 0 \\ 2 \\ 10 \end{array} \right) \left( \begin{array}{c} 36 \\ 0 \\ 19 \end{array} \right) \left( \begin{array}{c} 36 \\ 3 \\ 0 \end{array} \right) \left( \begin{array}{c} 22 \\ 13 \\ 36 \end{array} \right) \]</li>
	<li>Multiply each of these vectors by a predetermined $3 \times 3$ encryption matrix using modulo $37$ arithmetic. If the encryption matrix is \[ \left( \begin{array}{ccc} 30 &  1 &  9 \\ 4 & 23 &  7 \\ 5 &  9 & 13 \end{array} \right) \] then the first vector is transformed as follows: \[\begin{eqnarray*} \left( \begin{array}{ccc} 30 &  1 &  9 \\ 4 & 23 &  7 \\ 5 &  9 & 13 \end{array} \right) \left( \begin{array}{c} 0 \\ 19 \\ 19 \end{array} \right) & = & \left( \begin{array}{c} (30 \times 0 + 1 \times 19 + 9 \times 19) \mod 37 \\ (4 \times 0 + 23 \times 19 + 7 \times 19) \mod 37 \\ (5 \times 0 + 9 \times 19 + 13 \times 19) \mod 37 \end{array} \right) \\ & = & \left( \begin{array}{c} 5 \\ 15 \\ 11 \end{array} \right) \end{eqnarray*}\]</li>
	<li>After multiplying all the vectors by the encryption matrix, convert the resulting values back to the $37$-character alphabet and concatenate the results to obtain the encrypted <em>ciphertext</em>.  In our example the ciphertext is <code>FPLSFA4SUK2W9K3</code>.</li>
</ol>

<p>This method can be generalized to work with any $n \times n$ encryption matrix in which case the initial plaintext is broken up into vectors of length $n$.  For this problem you will be given an encryption matrix and a plaintext and must compute the corresponding ciphertext.</p>

### 입력 

 <p>Input begins with a line containing a positive integer $n \leq 10$ indicating the size of the matrix and the vectors to use in the encryption.  After this are $n$ lines each containing $n$ non-negative integers specifying the encryption matrix. After this is a single line containing the plaintext consisting only of characters in the $37$-character alphabet specified above.</p>

### 출력 

 <p>Output the corresponding ciphertext on a single line.</p>

