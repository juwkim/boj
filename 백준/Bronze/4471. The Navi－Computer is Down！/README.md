# [Bronze II] The Navi-Computer is Down! - 4471 

[문제 링크](https://www.acmicpc.net/problem/4471) 

### 성능 요약

메모리: 28776 KB, 시간: 92 ms

### 분류

기하학(geometry), 3차원 기하학(geometry_3d), 수학(math), 문자열(string)

### 문제 설명

<p>An Imperial Cruiser and its cohort of Tie Fighters are hot on the tail of the Millennium Falcon. The Falcon has taken minimal damage to the aft and port thrusters, but the Navi-Computer has been damaged preventing a jump to hyperspace and escape.</p>

<ul>
	<li>Luke: Han, why not just jump to hyperspace? We can’t hold up to that Imperial Cruiser much longer! </li>
	<li>Han: Travelin' through hyperspace ain't like dustin' crops, boy! Without precise calculations we could fly right through a star or bounce too close to a supernova, and that'd end your trip real quick, wouldn't it?</li>
	<li>Leia: He’s right Luke, we need proper calculations entered or... </li>
	<li>C3PO: We’re doomed!</li>
	<li>R2D2: whistle, chirp, beep, beeeeeeeeeeeeeeeeeeep! </li>
	<li>Chewbacca: Grooooooooooooooaaaaaaaaannnnn!</li>
	<li>Luke: I have a very bad feeling about this.</li>
	<li>Leia: There must be something we can do! We can’t go out like this. The Rebel Alliance is depending on us!</li>
	<li>C3PO: Your Highness, R2D2 says he has a star map of the galaxy with coordinates in 3-space for each location!</li>
	<li>Han: Great, but since the Navi-Computer is down, we need not only the 3-space coordinates, but the distance between our current location and our destination. I’m not up on the tech math to do that and I don’ t see anyone else here that’ s a likely candidate.</li>
	<li>Leia: I beg your pardon, but it doesn’t take a math tech to do those kinds of calculations...</li>
	<li>Han: Oh really, your worship? I suppose you’re going to tell us they taught you that in ‘Princess School’ .</li>
	<li>Leia: Grow up. Anyone that’s been to school through the 10th galactic grade knows that the distance between two points, or star systems, in 3-space is the square root of the sum of the difference between the x-coordinates squared, the difference between the y-coordinates squared, and the difference between the z-coordinates squared. The result is in galactic units, of course.</li>
	<li>Luke: Hey, I remember that! It looks like this (he draws out the formula):</li>
</ul>

<p>\( d = \sqrt{(\Delta{x})^2 + (\Delta{y})^2 + (\Delta{z})^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} \)</p>

<ul>
	<li>Han: Great, so everyone’s a genius but me! I’ll congratulate you all on your brilliance later...</li>
	<li>Leia (interrupting): They also teach manners and hygiene in school, but those are usually before grade 4. Looks like you didn’t pay much attention, Han.</li>
	<li>Han: ...if you can get me the name and coordinates of the current star system, followed by the name and coordinates of the destination star system, followed by the distance in galactic units between the two, so I can enter it all in the Hyper-Computer and make the jump to hyperspace.</li>
	<li>Luke: No problem Han, R2 will provide the coordinates and Leia will do the math, let’s get out of here! </li>
	<li>Han: Leia, I hope your math is accurate to two digits of precision to the right of the decimal point. The Hyper-Computer will need it.</li>
</ul>

<p>Your task is to aid Leia in calculating the distance between two star systems with accuracy of two digits to the right of the decimal. Help save the Millennium Falcon and its crew so they can help the Rebel Alliance defeat the Empire!</p>

### 입력 

 <p>The input file will begin with a line containing the integer n (0 < n < 200), representing the number of entries to process. n entries follow. An entry will consist of the name of the current star system on a line of its own, followed by the x, y, and z coordinates of that star system, all on the same line, all separated by a single space. Next will be the name of the destination star system (which is always different than the current star system) on a line of its own, followed by the x, y, and z coordinates of that star system, all on the same line, all separated by a single space.</p>

<p>Star system names may contain alpha-numeric characters, whitespace, and punctuation. Star system names will be no larger than 30 characters. The x, y, and z coordinates will be real numbers listed with two digits of precision to the right of the decimal point, with -100,000.00 < x, y, z < 100,000.00, thus double precision real numbers should be used to avoid rounding errors. Finally, the distance between star systems will always be at least one galactic unit.</p>

### 출력 

 <p>For each entry in the input file, output on one line: the name of the current star system, then the string ‘ to ’, then the name of the destination star system, followed by a colon and a space, followed by the distance between the two systems to two digits of precision to the right of the decimal. See the sample output below for details.</p>

