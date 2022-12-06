# [Bronze II] Enigma - 16446 

[문제 링크](https://www.acmicpc.net/problem/16446) 

### 성능 요약

메모리: 28776 KB, 시간: 292 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>Dada uma configuração inicial, a máquina de criptografia alemã Enigma, da Segunda Guerra Mundial, substituía cada letra digitada no teclado por alguma outra letra. A substituição era bastante complexa, mas a máquina tinha uma vulnerabilidade: uma letra nunca seria substituída por ela mesma! Essa vulnerabilidade foi explorada por Alan Turing, que trabalhou na criptoanálise da Enigma durante a guerra. O objetivo era encontrar a configuração inicial da máquina usando a suposição de que a mensagem continha uma certa expressão usual da comunicação, como por exemplo a palavra <code>ARMADA</code>. Essas expressões eram chamadas de cribs. Se a mensagem cifrada era, por exemplo, <code>FDMLCRDMRALF</code>, o trabalho de testar as possíveis configurações da máquina era simplificado porque a palavra <code>ARMADA</code>, se estivesse nessa mensagem cifrada, só poderia estar em duas posições, ilustradas na tabela abaixo com uma seta. As demais cinco posições não poderiam corresponder ao crib <code>ARMADA</code> porque ao menos uma letra do crib, sublinhada na tabela abaixo, casa com sua correspondente na mensagem cifrada; como a Enigma nunca substituiria uma letra por ela própria, essas cinco posições poderiam ser descartadas nos testes.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 308px; height: 164px;"></p>

<p>Neste problema, dada uma mensagem cifrada e um crib, seu programa deve computar o número de posições possíveis para o crib na mensagem cifrada.</p>

### 입력 

 <p>A primeira linha da entrada contém a mensagem cifrada, que é uma sequência de pelo menos uma letra e no máximo 10<sup>4</sup> letras. A segunda linha da entrada contém o crib, que é uma sequência de pelo menos uma letra e no máximo o mesmo número de letras da mensagem. Apenas as 26 letras maiúsculas, sem acentuação, aparecem na mensagem e no crib.</p>

### 출력 

 <p>Imprima uma linha contendo um inteiro, indicando o número de posições possíveis para o crib na mensagem cifrada.</p>

