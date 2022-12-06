# [Silver V] Dogs and Cats - 23261 

[문제 링크](https://www.acmicpc.net/problem/23261) 

### 성능 요약

메모리: 114464 KB, 시간: 172 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>You work for an animal shelter and you are responsible for feeding the animals. You already prepared $D$ portions of dog food and $C$ portions of cat food.</p>

<p>There are a total of $N$ animals waiting in a line, some of which are dogs and others are cats. It might be possible that all the animals in the line are dogs or all the animals are cats. A string $S$ of $N$ characters <code>C</code> and <code>D</code> represents the order of cats and dogs in the line. The $i$-th character is equal to <code>C</code> if the $i$-th animal in the line is a cat. Similarly, the $i$-th character is equal to <code>D</code> if the $i$-th animal in the line is a dog.</p>

<p>The animals are fed in the order they stay in the line. Each dog eats exactly $1$ portion of dog food and similarly each cat eats exactly $1$ portion of cat food. Moreover, you have extra portions of cat food. Every time <u>a dog</u> eats food, you bring $M$ extra portions of cat food for cats.</p>

<p>Animals have to be fed in the order they wait in line and an animal can only eat if the animal before it has already eaten. That means that if you run out of dog (or cat) food portions and a dog (or a cat) is about to get fed, the line will not move, as all the animals will wait patiently.</p>

<p>You need to determine if in this scenario <u>all the dogs</u> in the line will be fed. Note that this means that some cats might remain in the line, but worry not, you will eventually feed them later!</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ test cases follow.</p>

<p>The first line of each test case contains four integers $N$, $D$, $C$, and $M$: the number of animals, the initial number of dog food portions, the initial number of cat food portions, and the additional portions of cat food that we add after a dog eats a portion of dog food, respectively.</p>

<p>The next line contains a string $S$ of length $N$ representing the arrangement of animals.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from $1$) and $y$ is <code>YES</code> if all the dogs will be fed and <code>NO</code> otherwise.</p>

