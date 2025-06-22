# [Silver I] Galactic Import - 4692 

[문제 링크](https://www.acmicpc.net/problem/4692) 

### 성능 요약

메모리: 110064 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 수학

### 제출 일자

2025년 6월 23일 03:37:10

### 문제 설명

<p>With the introduction of the new ThrustoZoom gigadimensional drive, it has become possible for HyperCommodities, the import/export conglomerate from New Jersey, to begin trading with even the most remote galaxies in the universe. HyperCommodities wants to import goods from some of the galaxies in the Plural Z sector. Planets within these galaxies export valuable products and raw materials like vacuuseal, transparent aluminum, digraphite, and quantum steel. Preliminary reports have revealed the following facts:</p>

<ul>
	<li>Each galaxy contains at least one and at most 26 planets. Each planet within a galaxy is identified by a unique letter from A to Z.</li>
	<li>Each planet specializes in the production and export of one good. Different planets within the same galaxy export different goods.</li>
	<li>Some pairs of planets are connected by hyperspace shipping lines. If planets A and B are connected, they can trade goods freely. If planet C is connected to B but not to A, then A and C can still trade goods with each other through B, but B keeps 5% of the shipment as a shipping fee. (Thus A only receives 95% of what C shipped, and C receives only 95% of what A shipped.) In general, any two planets can trade goods as long as they are connected by some set of shipping lines, but each intermediate planet along the shipping route keeps 5% of what it shipped (which is not necessarily equal to 5% of the original shipment).</li>
	<li>At least one planet in each galaxy is willing to open a ThrustoZoom shipping line to Earth. A ThrustoZoom line is the same as any other shipping line within the galaxy, as far as business is concerned. For example, if planet K opens a ThrustoZoom line to Earth, then the Earth can trade goods freely with K, or it can trade goods with any planet connected to K, subject to the usual shipping fees.</li>
</ul>

<p>HyperCommodities has assigned a relative value (a positive real number less than 10) to each planet's chief export. The higher the number, the more valuable the product. More valuable products can be resold with a higher profit margin in domestic markets. The problem is to determine which planet has the most valuable export when shipping fees are taken into account.</p>

### 입력 

 <p>The input consists of one or more galaxy descriptions. Each galaxy description begins with a line containing an integer N which specifies the number of planets in the galaxy. The next N lines contain descriptions of each planet, which consist of:</p>

<ol>
	<li>The letter used to represent the planet.</li>
	<li>A space.</li>
	<li>The relative value of the planet's export, in the form d.dd.</li>
	<li>A space.</li>
	<li>A string containing letters and/or the character '*'; a letter indicates a shipping line to that planet, and a '*' indicates a willingness to open a ThrustoZoom shipping line to Earth.</li>
</ol>

### 출력 

 <p>For each galaxy description, output a single line which reads "Import from P" where P is the letter of the planet with the most valuable export, once shipping fees have been taken into account. (If more than one planet have the same most valuable export value then output the plant which is alphabetically first).</p>

