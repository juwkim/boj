# [Silver II] カードシャッフル (Small) - 12453 

[문제 링크](https://www.acmicpc.net/problem/12453) 

### 성능 요약

메모리: 110704 KB, 시간: 100 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 2월 7일 18:44:38

### 문제 설명

<p>フランクはカードゲームが好きで、週末は友達の家でゲームパーティーに参加しています。彼らがゲームに使うカードは <strong>M</strong> 枚からなり、それぞれ 1 から <strong>M</strong> までの数字が重複しないように書かれています。フランクはパーティーで友人が使っている自動カードシャッフル装置と同じものを持っていて、どのように動作するか理解しています。その装置はカードの山を <strong>C</strong> 回カットすることでシャッフルを行います。<strong>i</strong> 回目のカットではカードの山の上から <strong>A<sub>i</sub></strong> 番目から <strong>B<sub>i</sub></strong> 枚、つまり <strong>A<sub>i</sub></strong> 番目から <strong>A<sub>i</sub></strong> + <strong>B<sub>i</sub></strong> - 1 番目のカードがそのままの順番で山の上に移動します。</p>

<p>ある日、いつも使っているカードが汚れたため、新しいカードを使うことになりました。新しいカードは上から順番に 1 から <strong>M</strong> まで並んだ状態でそのままシャッフル装置にかけられました。フランクはシャッフル装置の性質を利用し、シャッフル後に上から <strong>W</strong> 番目にあるカードが何かを知ろうとしています。</p>

### 입력 

 <p>最初の行はテストケースの個数 <strong>T</strong> を表す正の整数です。続いて、各テストケースが次のようなフォーマットで与えられます。</p>

<pre>M C W
A<sub>1</sub> B<sub>1</sub>
...
A<sub>C</sub> B<sub>C</sub>
</pre>

<p>1行目では、1 つのスペースで区切られた 3 つの整数 <strong>M</strong>, <strong>C</strong>, <strong>W</strong> が与えられます。ここで <strong>M</strong> はカードの枚数 、<strong>C</strong> はカットの回数、<strong>W</strong> は知りたいカードの位置です。 続く <strong>C</strong> 行の各行では、1 つのスペースで区切られた 2 つの整数 <strong>A<sub>i</sub></strong>, <strong>B<sub>i</sub></strong> が与えられます。 ここで <strong>A<sub>i</sub></strong>, <strong>B<sub>i</sub></strong> はカットの操作で、<strong>i</strong> 回目の操作で上から <strong>A<sub>i</sub></strong> 番目から <strong>B<sub>i</sub></strong> 枚のカードを山の上に移動させることを意味しています。</p>

<h3>制約</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 200</li>
	<li>1 ≤ <strong>C</strong> ≤ 100</li>
	<li>1 ≤ <strong>W</strong> ≤ <strong>M</strong></li>
	<li>1 ≤ <strong>A<sub>i</sub></strong> ≤ <strong>M</strong></li>
	<li>1 ≤ <strong>B<sub>i</sub></strong> ≤ <strong>M</strong></li>
	<li>1 ≤ <strong>A<sub>i</sub></strong> + <strong>B<sub>i</sub></strong> - 1 ≤ <strong>M</strong></li>
	<li>1 ≤ <strong>M</strong> ≤ 100</li>
</ul>

### 출력 

 <p>各テストケースに対し、</p>

<pre>Case #X: P
</pre>

<p>という内容を1行出力してください。ここで <strong>X</strong> は 1 から始まるテストケース番号、<strong>P</strong> はシャッフル後のカードの山の上から <strong>W</strong> 番目にあるカードを表します。</p>

