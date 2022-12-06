# [Silver V] Singin' in the Rain - 25883 

[문제 링크](https://www.acmicpc.net/problem/25883) 

### 성능 요약

메모리: 114976 KB, 시간: 128 ms

### 분류

그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>During the time of the 2016 UCF Local Programming Contest, Arup's younger daughter Anya (3 years old at the time), made Arup incessantly listen to Taylor Swift's song "Wildest Dreams". A full year later, we are proud to report that Anya's listening habits have matured greatly. Rather than wanting to hear the same song over and over again, Anya has embraced an embryonic notion of diversity in music. Now, she wants to hear various different tracks, in sequence, all from the same CD.</p>

<p>This year, it turns out that Anya's favorite CD is "Singing in the Rain", which her older sister Simran obtained when she performed in the "Singing in the Rain" production at a local theater. Whenever Anya is in the car with Arup, she'll listen to a track and then call out the number of the next track that she wants to listen to. The problem is that Arup's car has a rather primitive CD player:</p>

<ul>
	<li>If track number k has completed, then track k+1 will play. If track k is the last track on the CD, the CD will wrap around and track 1 will play.</li>
	<li>Arup can also change tracks by pressing a forward button. If track number k has completed, if Arup presses the forward button, then track k+2 will play. If k is the last track and Arup presses forward when k finishes, the CD will wrap around and track 2 will play next. If k is next to the last track and Arup presses forward when k finishes, track 1 will play next.</li>
	<li>Arup can also change tracks by pressing a backward button. If track number k has completed, if Arup presses the backward button, track number k will play again. If k is the first track and Arup presses the backward button twice right after track 1 completes, the CD will wrap around and track t will play next, where t is the number of tracks on the CD.</li>
</ul>

<p>This means Arup is pressing either the forward or backward button a great deal. Help him minimize the number of times he presses the buttons.</p>

<p>Given the number of tracks on Anya's favorite CD and the sequence of tracks Anya wants to be played, determine the minimum number of button presses Arup must make to get the appropriate sequence of songs played. For the purposes of this problem, assume that at the very beginning the CD player is cued up to play the first song in the sequence (the first song Anya wants to be played), so Arup does not have to press any buttons for the first song in the sequence to be played, i.e., the first time any buttons might have to be pressed is in between the first and second songs in the sequence (after the first song in the sequence plays).</p>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of test cases to process. Each test case starts with two space separated integers on a single line: t (1 ≤ t ≤ 10<sup>9</sup>), the number of tracks on Anya's favorite CD and s (1 ≤ s ≤ 1000), the number of songs Anya would like to listen to from the CD. The second line of each test case contains s space separated integers, representing the sequence of tracks from the CD that Anya would like to listen to. Each of these will be in between 1 and t, inclusive.</p>

### 출력 

 <p>For each test case, output a single integer on a line by itself indicating the minimum number of button presses Arup can use to play the desired sequence of songs from the CD.</p>

