# [Silver IV] Moo Sick - 5930 

[문제 링크](https://www.acmicpc.net/problem/5930) 

### 성능 요약

메모리: 117144 KB, 시간: 172 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 정렬(sorting)

### 문제 설명

<p>Everyone knows that cows love to listen to all forms of music.  Almost all forms, that is -- the great cow composer Wolfgang Amadeus Moozart once discovered that a specific chord tends to make cows rather ill.  This chord, known as the ruminant seventh chord, is therefore typically avoided in all cow musical compositions.</p><p>Farmer John, not knowing the finer points of cow musical history, decides to play his favorite song over the loudspeakers in the barn.  Your task is to identify all the ruminant seventh chords in this song, to estimate how sick it will make the cows.</p><p>The song played by FJ is a series of N (1 <= N <= 20,000) notes, each an integer in the range 1..88.  A ruminant seventh chord is specified by a sequence of C (1 <= C <= 10) distinct notes, also integers in the range 1..88.  However, even if these notes are transposed (increased or decreased by a common amount), or re-ordered, the chord remains a ruminant seventh chord!  For example, if "4 6 7" is a ruminant seventh chord, then "3 5 6" (transposed by -1), "6 8 9" (transposed by +2), "6 4 7" (re-ordered), and "5 3 6" (transposed and re-ordered) are also ruminant seventh chords.</p><p>A ruminant seventh chord is a sequence of C consecutive notes satisfying the above criteria. It is therefore uniquely determined by its starting location in the song. Please determine the indices of the starting locations of all of the ruminant seventh chords.</p>

### 입력 

 <ul><li>Line 1: A single integer: N.</li><li>Lines 2..1+N: The N notes in FJ's song, one note per line.</li><li>Line 2+N: A single integer: C.</li><li>Lines 3+N..2+N+C: The C notes in an example of a ruminant seventh chord.  All transpositions and/or re-orderings of these notes are also ruminant seventh chords.</li></ul>

### 출력 

 <ul><li>Line 1: A count, K, of the number of ruminant seventh chords that appear in FJ's song.  Observe that different instances of ruminant seventh chords can overlap each-other.</li><li>Lines 2..1+K: Each line specifies the starting index of a ruminant seventh chord (index 1 is the first note in FJ's song, index N is the last).  Indices should be listed in increasing sorted order.</li></ul>

