# [Bronze III] Divisão da Nlogõnia - 13684 

[문제 링크](https://www.acmicpc.net/problem/13684) 

### 성능 요약

메모리: 29200 KB, 시간: 208 ms

### 분류

많은 조건 분기(case_work), 구현(implementation)

### 문제 설명

<p>Depois de séculos de escaramuças entre os quatro povos habitantes da Nlogônia, e de dezenas de anos de negociações envolvendo diplomatas, políticos e as forças armadas de todas as partes interessadas, com a intermediação da ONU, OTAN, G7 e SBC, foi finalmente decidida e aceita por todos a maneira de dividir o país em quatro territórios independentes.</p>

<p>Ficou decidido que um ponto, denominado ponto divisor, cujas coordenadas foram estabelecidas nas negociações, definiria a divisão do país, da seguinte maneira. Duas linhas, ambas contendo o ponto divisor, uma na direção norte-sul e uma na direção leste-oeste, seriam traçadas no mapa, dividindo o país em quatro novos países. Iniciando no quadrante mais ao norte e mais ao oeste, em sentido horário, os novos países seriam chamados de Nlogônia do Noroeste, Nlogônia do Nordeste, Nlogônia do Sudeste e Nlogônia do Sudoeste.</p>

<p><img alt="" src="" style="height:237px; width:356px"></p>

<p>A ONU determinou que fosse disponibilizada uma página na Internet para que os habitantes pudessem consultar em qual dos novos países suas residências estão, e você foi contratado para ajudar a implementar o sistema.</p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro K indicando o número de consultas que serão realizadas (0 < K ≤ 10<sup>3</sup>). A segunda linha de um caso de teste contém dois números inteiros N e Mrepresentando as coordenadas do ponto divisor (-10<sup>4</sup> < N, M < 10<sup>4</sup>). Cada uma das K linhas seguintes contém dois inteiros X e Y representando as coordenadas de uma residência (-10<sup>4</sup> ≤ X, Y ≤ 10<sup>4</sup>).Em todas as coordenadas dadas, o primeiro valor  corresponde à direção leste-oeste, e o segundo valor corresponde à direção norte-sul.</p>

<p>O final da entrada é indicado por uma linha que contém apenas o número zero.</p>

### 출력 

 <p>Para cada caso de teste da entrada seu programa deve imprimir uma linha contendo:</p>

<ul>
	<li>a palavra divisa se a residência encontra-se em cima de uma das linhas divisórias (norte-sul ou leste-oeste);</li>
	<li>NO se a residência encontra-se na Nlogônia do Noroeste;</li>
	<li>NE se a residência encontra-se na Nlogônia do Nordeste;</li>
	<li>SE se a residência encontra-se na Nlogônia do Sudeste;</li>
	<li>SO se a residência encontra-se na Nlogônia do Sudoeste.</li>
</ul>

