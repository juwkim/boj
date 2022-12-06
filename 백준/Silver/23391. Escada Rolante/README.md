# [Silver V] Escada Rolante - 23391 

[문제 링크](https://www.acmicpc.net/problem/23391) 

### 성능 요약

메모리: 115544 KB, 시간: 164 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Você acaba de inventar um novo tipo de escada rolante: uma escada rolante dupla. Escadas rolantes normais levam as pessoas de uma das pontas para a outra, mas não na direção contrária, enquanto que as escadas rolantes duplas podem levar pessoas de qualquer uma das pontas para a outra.</p>

<p>Leva-se 10 segundos para que a escada rolante dupla leve uma pessoa de uma das pontas até a outra. Isto é, se a pessoa entra na escada rolante dupla em uma das pontas no momento T, então vai sair na outra ponta no momento T + 10 – esta pessoa não estará mais na escada rolante dupla no momento T + 10.</p>

<p>A todo momento que ninguém esteja usando a escada rolante dupla, ela estará parada. Portanto, inicialmente ela está parada.</p>

<p>Quando a escada rolante dupla está parada e uma pessoa entra por uma das pontas, a escada rolante dupla se ligará automaticamente e se moverá na direção que aquela pessoa quer ir.</p>

<p>Se uma pessoa chegar na escada rolante dupla e esta já estiver movendo-se na direção que a pessoa quer ir, então a pessoa entrará nela imediatamente. Caso contrário, se a escada rolante estiver se movendo na direção oposta, a pessoa terá que esperar até que a escada rolante pare e só então a pessoa poderá entrar nela. A escada rolante dupla é tão larga que ela pode acomodar inúmeras pessoas entrando nela ao mesmo tempo.</p>

<p>A escada rolante dupla tem um efeito bem estranho, provavelmente relacionado a alguma propriedade da física quântica (ou simplesmente ao acaso): nenhuma pessoa vai chegar na escada rolante dupla no momento exato em que ela está prestes a parar.</p>

<p>Agora que você sabe como a escada rolante dupla funciona, você terá a tarefa de simulá-la. Dada a informação de N pessoas, incluindo o momento em que elas chegaram na escada rolante dupla e em qual direção elas querem andar, você tem que descobrir qual o último momento em que a escada para.</p>

### 입력 

 <p>A primeira linha contém um inteiro N (1 ≤ N ≤ 10<sup>4</sup>), representando quantas pessoas usarão a escada rolante.</p>

<p>Em seguida haverão N linhas contendo dois inteiros t<sub>i</sub> e d<sub>i</sub> cada (1 ≤ t<sub>i</sub> ≤ 10<sup>5</sup>, 0 ≤ d<sub>i</sub> ≤ 1), representando o momento em que a i-ésima pessoa chegará na escada rolante dupla e em qual direção ela quer ir. Se d<sub>i</sub> é igual a 0, então a pessoa quer ir da ponta esquerda para a ponta direita, e se d<sub>i</sub> é igual 1, então a pessoa quer ir da ponta direita para a ponta esquerda. Todos os valores de t<sub>i</sub> são distintos e dados em ordem crescente.</p>

### 출력 

 <p>Imprima uma linha contendo o momento no qual a última pessoa saiu da escada rolante.</p>

