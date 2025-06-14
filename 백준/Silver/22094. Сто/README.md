# [Silver IV] Сто - 22094 

[문제 링크](https://www.acmicpc.net/problem/22094) 

### 성능 요약

메모리: 111452 KB, 시간: 116 ms

### 분류

구현, 많은 조건 분기

### 제출 일자

2025년 6월 14일 18:15:07

### 문제 설명

<p>Все люди любят круглые числа. У этого явления достаточно много причин, главной из которых является то, что число, которое делится, например, на 100, существенно проще запомнить. К сожалению, в нашей жизни круглых чисел существенно меньше, чем всех остальных. Первоклассник Петя очень переживает по этому поводу. Поэтому он придумал свое определение круглого числа.</p>

<p>По версии Пети, число является круглым только в том случае, если из него можно удалить ровно <i>k</i> цифр так, что после этого число не будет содержать ведущих нулей, но будет делиться на 100. Например, при <i>k</i> равным 2, число 10304 является круглым, а число 1000 — нет.</p>

<p>Теперь Петя хочет узнать, какие числа при каких <i>k</i> являются круглыми, а какие — нет. Помогите ему.</p>

### 입력 

 <p>Первая строка содержит целое число <i>n</i> — количество пар чисел <i>k</i> и <i>x</i>, про которые Петя хочет что-то узнать. Следующие <i>n</i> строк содержат по два целых положительных числа <i>k</i> и <i>x</i> каждая. Гарантируется, что любое число <i>k</i> строго меньше количества цифр в соответствующем числе <i>x</i>. Гарантируется, что все числа <i>x</i> не содержат ведущих нулей. Гарантируется, что сумма количеств цифр во всех числах <i>x</i> не превышает 10<sup>5</sup>.</p>

### 출력 

 <p>Для каждой пары чисел <i>k</i> и <i>x</i> из входного файла выведите -1 в случае, если число <i>x</i> не является круглым при данном <i>k</i>. В случае же, если число <i>x</i> являетсы круглым при данном <i>k</i>, выведите число <i>x</i>, из которого вычеркнули ровно <i>k</i> цифр, после чего оно стало делиться на 100. Выведенное вами число не должно содержать ведущих нулей, но может быть равно нулю.</p>

