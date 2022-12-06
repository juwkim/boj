# [Bronze II] Loop Musical - 13682 

[문제 링크](https://www.acmicpc.net/problem/13682) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Um loop musical é um trecho de música que foi composto para repetir continuamente (ou seja, o trecho inicia novamente toda vez que chega ao final), sem que se note descontinuidade. Loops são muito usados na sonorização de jogos, especialmente jogos casuais pela internet.</p>

<p>Loops podem ser digitalizados por exemplo utilizando PCM. PCM, do inglês Pulse Code Modulation, é uma técnica para representação de sinais analógicos, muito utilizada em áudio digital. Nessa técnica, a magnitude do sinal é amostrada a intervalos regulares de tempo, e os valores amostrados são armazenados em sequência. Para reproduzir a forma de onda amostrada, o processo é invertido (demodulação).</p>

<p>Fernandinha trabalha para uma empresa que desenvolve jogos e compôs um bonito loopmusical, codificando-o em PCM. Analisando a forma de onda do seu loop em um software de edição de áudio, Fernandinha ficou curiosa ao notar a quantidade de “picos” existentes. Um pico em uma forma de onda é um valor de uma amostra que representa um máximo ou mínimo local, ou seja, um ponto de inflexão da forma de onda. A figura abaixo ilustra (a) um exemplo de forma de onda e (b) o loop formado com essa forma de onda, contendo 48 picos.</p>

<p><img alt="" src="" style="height:284px; width:433px"></p>

<p>Fernandinha é uma amiga muito querida e pediu sua ajuda para determinar quantos picos existem no seu loop musical.</p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro N, representando o número de amostras no loop musical de Fernandinha (2 ≤ N ≤ 10<sup>4</sup>). A segunda linha contém N inteiros H<sub>i</sub>, separados por espaços, representando a sequência de magnitudes das amostras(-10<sup>4</sup> ≤ H<sub>i</sub> ≤ 10<sup>4</sup> para 1 ≤ i ≤ N, H<sub>1</sub> ≠ H<sub>N</sub> e H<sub>i</sub> ≠ H<sub>i+1</sub> para 1 ≤ i < N). Note que H<sub>1</sub> segue H<sub>N</sub> quando o loop é reproduzido.</p>

<p>O final da entrada é indicado por uma linha que contém apenas o número zero.</p>

### 출력 

 <p>Para cada caso de teste da entrada seu programa deve imprimir uma única linha, contendo apenas um inteiro, o número de picos existentes no loop musical de Fernandinha.</p>

