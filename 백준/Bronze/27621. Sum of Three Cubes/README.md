# [Bronze III] Sum of Three Cubes - 27621 

[문제 링크](https://www.acmicpc.net/problem/27621) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 런타임 전의 전처리(precomputation)

### 문제 설명

<p>Recently, a mathematician has just found three cube numbers that sum up to 42 using over a million hours of computing time. With this breakthrough, we have found three cube numbers that sum up to all non-negative integers less than 100 if it is possible to do so. In other words, for every 0 ≤ N < 100, we have found the triples (X, Y, Z) such that X<sup>3</sup> + Y<sup>3</sup> + Z<sup>3</sup> = N, or we have proved that no such triplet exists.</p>

<p>The following is a table of (X, Y, Z) that satisfies X<sup>3</sup> + Y<sup>3</sup> + Z<sup>3</sup> = N for 0 ≤ N < 50.</p>

<table class="table table-bordered th-center td-center">
	<tbody>
		<tr>
			<th>N</th>
			<th>X</th>
			<th>Y</th>
			<th>Z</th>
		</tr>
		<tr>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>5</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>6</td>
			<td>-1</td>
			<td>-1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>7</td>
			<td>0</td>
			<td>-1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>8</td>
			<td>0</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>9</td>
			<td>0</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>10</td>
			<td>1</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>11</td>
			<td>-2</td>
			<td>-2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>12</td>
			<td>7</td>
			<td>10</td>
			<td>-11</td>
		</tr>
		<tr>
			<td>13</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>14</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>15</td>
			<td>-1</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>16</td>
			<td>-511</td>
			<td>-1609</td>
			<td>1626</td>
		</tr>
		<tr>
			<td>17</td>
			<td>1</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>18</td>
			<td>-1</td>
			<td>-2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>19</td>
			<td>0</td>
			<td>-2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>20</td>
			<td>1</td>
			<td>-2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>21</td>
			<td>-11</td>
			<td>-14</td>
			<td>16</td>
		</tr>
		<tr>
			<td>22</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>23</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>24</td>
			<td>-2901096694</td>
			<td>-15550555555</td>
			<td>15584139827</td>
		</tr>
		<tr>
			<td>25</td>
			<td>-1</td>
			<td>-1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>26</td>
			<td>0</td>
			<td>-1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>27</td>
			<td>0</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<td>28</td>
			<td>0</td>
			<td>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>29</td>
			<td>1</td>
			<td>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>30</td>
			<td>-283059965</td>
			<td>-2218888517</td>
			<td>2220422932</td>
		</tr>
		<tr>
			<td>31</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>32</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>33</td>
			<td>8866128975287528</td>
			<td>-8778405442862239</td>
			<td>-2736111468807040</td>
		</tr>
		<tr>
			<td>34</td>
			<td>-1</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>35</td>
			<td>0</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>36</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>37</td>
			<td>0</td>
			<td>-3</td>
			<td>4</td>
		</tr>
		<tr>
			<td>38</td>
			<td>1</td>
			<td>-3</td>
			<td>4</td>
		</tr>
		<tr>
			<td>39</td>
			<td>117367</td>
			<td>134476</td>
			<td>-159380</td>
		</tr>
		<tr>
			<td>40</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>41</td>
			<td colspan="3">No solution</td>
		</tr>
		<tr>
			<td>42</td>
			<td>-80538738812075974</td>
			<td>80435758145817515</td>
			<td>12602123297335631</td>
		</tr>
		<tr>
			<td>43</td>
			<td>2</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>44</td>
			<td>-5</td>
			<td>-7</td>
			<td>8</td>
		</tr>
		<tr>
			<td>45</td>
			<td>2</td>
			<td>-3</td>
			<td>4</td>
		</tr>
		<tr>
			<td>46</td>
			<td>-2</td>
			<td>3</td>
			<td>3</td>
		</tr>
		<tr>
			<td>47</td>
			<td>6</td>
			<td>7</td>
			<td>-8</td>
		</tr>
		<tr>
			<td>48</td>
			<td>-23</td>
			<td>-26</td>
			<td>31</td>
		</tr>
		<tr>
			<td>49</td>
			<td colspan="3">No solution</td>
		</tr>
	</tbody>
</table>

<p>Reading a long table is a tedious job, so you would like to create a program that takes N as an input, and produce X, Y, Z as the output. The value of X, Y, and Z must be an integer not less than −10<sup>18</sup> and not more than 10<sup>18</sup>.</p>

### 입력 

 <p>Input begins with a line containing an integer: N (0 ≤ N < 50).</p>

### 출력 

 <p>Output in a line three integers (separated by a single space): X Y Z that satisfies the condition given in the problem statement. If there is more than one solution, you can output any of them. If there is no solution, output 0 instead.</p>

