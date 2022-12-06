# [Bronze I] Fastminton - 20281 

[문제 링크](https://www.acmicpc.net/problem/20281) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A Comissão RegionaL de Fastminton (CRLF) organiza torneiros anuais deste novo e inusitado esporte derivado do badminton. Neste ano, ocorrerá a terceira edição do grande torneio.</p>

<p>O antigo programador da comissão (sobrinho da diretora) desenvolveu um sistema para capturar e armazenar o resultado de cada ponto de uma partida, cujo resultado é salvo para um arquivo. Com a saída do antigo programador, que deixou para trás algumas versões defeituosas de seus programas, a CRLF precisa de você para garantir que os registros das emocionantes jogadas não sejam perdidos, confiando-lhe a tarefa de escrever um programa para ler os resultados dos arquivos de registro.</p>

<p>Para auxiliá-lo, a CRLF disponibilizou um resumo com as regras relevantes do Fastminton, que é, basicamente, uma versão mais curta (menor número de games) do badminton:</p>

<ul>
	<li>As partidas de Fastminton são jogadas sempre com dois jogadores (oponentes) em uma quadra separada ao meio por uma rede;</li>
	<li>Os jogadores são identificados pela sua posição no placar (jogador da esquerda, jogador da direita);</li>
	<li>Uma partida é composta por três <em>games</em>. Ganha quem alcançar dois <em>games</em>;</li>
	<li>Ganha o <em>game</em> quem alcançar ao menos 5 pontos e tiver uma diferença de ao menos 2 pontos do oponente, ou o primeiro a chegar em 10 pontos;</li>
	<li>O jogador da esquerda inicia sacando no primeiro <em>game</em> da partida; nos demais, o jogador que inicia sacando é o que ganhou o último game;</li>
	<li>Cada jogada resulta em um ponto, de quem sacou ou de quem recebeu o saque. Quem ganhou o ponto irá sacar na próxima jogada.</li>
</ul>

### 입력 

 <p>A entrada é composta por uma única linha contendo uma sequência de caracteres representando a sequência completa dos eventos de uma partida, podendo conter os caracteres <code>S</code> (ponto de quem sacou), <code>R</code> (ponto de quem recebeu o saque) ou <code>Q</code> (anúncio de placar). A entrada não contém anúncios de placar consecutivos.</p>

### 출력 

 <p>O programa deverá imprimir uma linha contendo o placar atual para cada anúncio de placar (Q) encontrado.</p>

<p>Caso a partida esteja em andamento, o anúncio deverá ser na forma “<code>GL (PL) - GR (PR)</code>”, onde <code>GL</code> e <code>GR</code> representam o número de <em>games</em> ganhos pelos jogadores da esquerda e da direita, e <code>PL</code> e <code>PR</code> são os pontos atuais dos jogadores da esquerda e da direita. Um asterisco (<code>*</code>) deverá ser adicionado no final do marcador de pontos do jogador que irá sacar na próxima jogada.</p>

<p>Caso a partida já esteja concluída, o anúncio será na forma “<code>GL - GR</code>” com a palavra “<code>(winner)</code>” adicionada no final do marcador de games do jogador ganhador da partida.</p>

