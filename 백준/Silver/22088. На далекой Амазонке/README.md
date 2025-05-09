# [Silver II] На далекой Амазонке - 22088 

[문제 링크](https://www.acmicpc.net/problem/22088) 

### 성능 요약

메모리: 112648 KB, 시간: 128 ms

### 분류

해 구성하기, 그리디 알고리즘

### 제출 일자

2025년 4월 2일 10:58:13

### 문제 설명

<p>Программист Гоша любит читать сказки на ночь своим детям. Однажды сказка, которую он решил прочитать, начиналась так:</p>

<p>«В одной далекой деревне в долине реки Амазонки живет племя, в котором нет ни одного мужчины. Живет в этой деревне четыре женщины: три матери и три дочери».</p>

<p>Это место показалось подозрительным детям Гоши, и ему пришлось срочно объяснять, как среди четырех человек может быть одновременно три матери и три дочери.</p>

<p>Предполагая, что дальше в сказке может быть описание других деревень, Гоша хочет научиться быстро строить пример племени, в котором всего <i>n</i> женщин, причем среди них <i>a</i> женщин являются матерью кого-то в этом племени, и <i>b</i> женщин являются дочерью кого-то в этом племени.</p>

<p>Помогите ему быстро придумывать пример такого племени для данных <i>n</i>, <i>a</i> и <i>b</i>.</p>

### 입력 

 <p>Первая строка содержит целое число <i>T</i> (1 ≤ <i>T</i> ≤ 10<sup>4</sup>) — количество тестовых примеров. В каждой из следующих <i>T</i> строк содержится по три натуральных числа: <i>n</i>, <i>a</i> и <i>b</i>. (1 ≤ <i>n</i>, <i>a</i>, <i>b</i> ≤ 10<sup>5</sup>).</p>

<p>Сумма всех значений <i>n</i> во вводе не превосходит 10<sup>5</sup>.</p>

### 출력 

 <p>Для каждого из <i>T</i> тестовых примеров выведите «IMPOSSIBLE», если искомого племени не существует. Если племя существует, то выведите описание племени в <i>n</i> строках. Занумеруем всех членов племени от 1 до <i>n</i>. В <i>i</i>-й строке выведите сначала число <i>k</i> — количество дочерей <i>i</i>-й женщины, а затем <i>k</i> чисел — номера ее дочерей. У каждой женщины мать может быть максимум одна.</p>

<p>Если допустимых ответов несколько, выведите любой. Естественно, мать всегда старше дочери, поэтому в племени должен существовать способ задать возраст всем женщинам так, чтобы это правило выполнялось.</p>

