# [Silver V] Clothes - 26558 

[문제 링크](https://www.acmicpc.net/problem/26558) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

자료 구조(data_structures), 구현(implementation), 스택(stack), 문자열(string)

### 문제 설명

<p>Billy’s mom recently washed his clothes. When his mom finishes washing his clothes, she folds them and stacks them in one large pile. It is then Billy’s responsibility to sort the clothes into three drawers for shirts, pants, and socks. When he places these items in the drawers he takes the top one off of the stack his mom gave to him and places it at the top of the stack in the respective drawer.</p>

<p>Each day Billy must wear a shirt, pants, and socks. He simply picks the top one off each stack in each drawer to wear for that day. Given the original stack of washed clothes, determine what Billy will wear up until he needs more clothes washed. Billy needs more clothes when he runs out of any necessary article of clothing for the day. Billy will only wear a piece of clothing once before it is declared dirty and needs washing. He does not ever wear dirty clothes.</p>

### 입력 

 <p>The first line of input will contain a single integer n that indicates the number datasets to follow. Each dataset begins with an integer c which is between 1 and 50. The next c lines are the stack of clean clothing in the format “article (type)” where article is the name of the article of clothing and type is the type of clothing. The value of type will be shirt, pants, or socks.</p>

### 출력 

 <p>The output will be a series of lines. Each line will contain the three articles of clothing for the specific day separated by a comma and one space. The shirt will be printed first followed by the pants and socks. The type should not be printed. There should be one blank line after each dataset.</p>

