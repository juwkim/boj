# [Silver III] Kemija - 24718 

[문제 링크](https://www.acmicpc.net/problem/24718) 

### 성능 요약

메모리: 114300 KB, 시간: 164 ms

### 분류

파싱, 문자열

### 제출 일자

2024년 4월 21일 12:20:49

### 문제 설명

<p>Fran didn’t pay attention in school during chemistry class and now he needs your help in doing his homework. His homework consists of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> chemical equations for which he needs to check if they are balanced. A chemical equation is a way of representing chemical reactions using symbols and formulas. In a chemical reaction, some set of initial molecules react to produce a new set of molecules.</p>

<p>A chemical equation has a left side and a right side. The left side contains chemical formulas of the initial molecules, while the right side contains chemical formulas of the product molecules. The left and the right sides of the equation are separated by an arrow (characters <code>-></code>). Different molecules appearing on the left or the right side are separated by a <code>+</code>.</p>

<p>Molecules are substances made from atoms, tiny particles which are denoted with capital letters of the Latin alphabet (for the purposes of this task). The formula of a molecule is written by listing the labels of all the different atoms which make up the molecule. If a molecule has multiple instances of some atom, then the number of occurrences of this atom is written after the atom in the formula. For example, <code>AC4B</code> is a formula for a molecule which has one atom <code>A</code>, 4 atoms <code>C</code> and one atom <code>B</code>. If on one side of the equation a molecule appears more than once, then this number of occurrences is written as a coefficient in front of the formula. For example, <code>3AC4B</code> denotes 3 molecules of <code>AC4B</code>, for a total of 3 atoms <code>A</code>, 12 atoms <code>C</code> and 3 atoms <code>B</code>.</p>

<p>A chemical equation is said to be balanced if the right side and the left side contain an equal number of atoms of each kind. Your task is to determine whether or not each of the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> chemical equations is balanced. The test cases will be such that all the numbers appearing in the reactions (the numbers of atoms in molecules and the numbers of molecules in the ractions) will have only a <strong>single digit</strong> (and they will be larger than 1).</p>

### 입력 

 <p>The first line contains a positive integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ n ≤ 10$</span></mjx-container>), the number of chemical equations.</p>

<p>Each of the next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines contains a sequence of characters representing a chemical equation. Each equation consists of at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1000$</span></mjx-container> characters. The equations will not necessarily be balanced, but they will be correctly written as described in the statement.</p>

### 출력 

 <p>For each of the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> equations print <code>DA</code> if it is balanced, and <code>NE</code> if it is not, in separate lines.</p>

