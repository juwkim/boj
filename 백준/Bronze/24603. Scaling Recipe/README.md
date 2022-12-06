# [Bronze III] Scaling Recipe - 24603 

[문제 링크](https://www.acmicpc.net/problem/24603) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>You've got a recipe which specifies a number of ingredients, the amount of each ingredient you will need, and the number of portions it produces. But, the number of portions you need is not the same as the number of portions specified in the recipe! How can you scale it?</p>

### 입력 

 <p>The first line of input contains three integers $n$ ($1 \le n \le 40$), $x$ and $y$ ($1 \le x,y \le 40{,}000$), where $n$ is the number of ingredients in the recipe, $x$ is the number of portions that the recipe produces, and $y$ is the number of portions you need.</p>

<p>Each of the next $n$ lines contains a single integer $a$ ($1 \le a \le 40{,}000$). These are the amounts of each ingredient needed for the recipe.</p>

<p>The inputs will be chosen so that the amount of each ingredient needed for $y$ portions will be an integer.</p>

### 출력 

 <p>Output $n$ lines. On each line output a single integer, which is the amount of that ingredient needed to produce $y$ portions of the recipe. Output these values in the order of the input.</p>

