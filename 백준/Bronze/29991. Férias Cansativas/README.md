# [Bronze III] Férias Cansativas - 29991 

[문제 링크](https://www.acmicpc.net/problem/29991) 

### 성능 요약

메모리: 110844 KB, 시간: 132 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2023년 10월 17일 13:04:49

### 문제 설명

<p>William está planejando suas próximas férias. Um tema recorrente em todas as suas férias é a necessidade de lidar com o cansaço. Alguns dias ele nem aproveita muito, pois depois de várias atividades o cansaço começa a ser maior do que ele consegue suportar.</p>

<p>Desta vez, William teve uma ideia. Ele vai estimar o impacto de cada uma das atividades de turismo em sua disposição. Ele notou que algumas das atividades de férias, como esportes e caminhadas, são cansativas, consumindo sua disposição, enquanto outras atividades, como peças de teatro e musicais, são revigorantes, recuperando sua disposição.</p>

<p>Mais precisamente, William começa com D unidades de disposição e separa suas atividades em dois grupos: C atividades cansativas e R atividades revigorantes. Cada atividade cansativa requer uma certa quantidade de disposição e, portanto, consome tal quantidade, quando realizada. Cada atividade revigorante lhe fornece uma certa quantidade de disposição, quando realizada. Além disso, ele ordena as atividades de cada um dos grupos segundo suas preferências, pois há atividades que ele está mais ansioso para realizar. Note que atividades dos dois conjuntos podem ser intercaladas, mas William nunca fará uma atividade de um grupo sem ter feito todas as anteriores, pois isto violaria suas preferências.</p>

<p>Ao longo de suas férias, ao decidir qual atividade realizar em seguida, ele escolherá a primeira atividade cansativa ainda não realizada, se tiver disposição suficiente para fazê-la. Caso contrário, ele realizará a próxima atividade revigorante ainda não realizada, se ainda houver, recuperando uma certa quantidade de disposição. Naturalmente, caso não haja mais atividades cansativas remanescentes em algum momento, ele poderá simplesmente realizar todas as atividades revigorantes restantes.</p>

<p>Agora, tendo em vista este processo, ele pediu sua ajuda para determinar quantas atividades (incluindo cansativas e revigorantes) ele conseguirá realizar.</p>

### 입력 

 <p>A primeira linha da entrada contém 3 inteiros, D, C e R, indicando respectivamente a quantidade de disposição inicial, o número de atividades cansativas e o número de atividades revigorantes (1 ≤ D ≤ 10<sup>5</sup>, 1 ≤ C ≤ 10<sup>4</sup> e 1 ≤ R ≤ 10<sup>4</sup>). Cada uma das C linhas seguintes contém um inteiro C<sub>i</sub> (1 ≤ C<sub>i</sub> ≤ 10<sup>5</sup> para 1 ≤ i ≤ C), indicando o consumo de disposição para uma atividade cansativa, em ordem de preferência. Finalmente, cada uma das R linhas seguintes contém um inteiro R<sub>i</sub> (1 ≤ R<sub>i</sub> ≤ 10<sup>5</sup> para 1 ≤ i ≤ R), indicando o retorno de disposição para uma atividade revigorante, em ordem de preferência.</p>

### 출력 

 <p>Imprima uma única linha contendo um único inteiro, o número total de atividades (incluindo cansativas e revigorantes) que William conseguirá realizar.</p>

