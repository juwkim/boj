# [Silver II] Getting Chorded - 6422 

[문제 링크](https://www.acmicpc.net/problem/6422) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

많은 조건 분기, 파싱, 문자열

### 제출 일자

2025년 1월 9일 00:47:31

### 문제 설명

<p>The "names" of the notes on a standard 88-key piano keyboard start with A (the lowest note on the keyboard) and then proceed sequentially with A# (A-sharp), B, C, C#, D, D#, E, F, F#, G, and finally G#. After the first 12 notes are named, the pattern repeats, proceeding through the last key, which is named C. Some notes have other common names. A# may also be called B♭ (B-flat), C# may be called D♭, D# may be called E♭, F# may be called G♭, and G# may be called A♭. (There are still other names, like C##, but we won't worry about those here!)</p>

<p>Most music includes <strong>chords</strong>, or groups of notes played at the same time. Many of these chords are given standard names. For example, the notes C, E, and G sounded together are called a <strong>C Major chord</strong>. While the particular C, E and G in the chord are frequently close together on the keyboard, for our purposes here, any C, E, and G played at the same time will constitute a C Major chord. It is the spacing between the notes on the keyboard that distinguishes a Major chord from others. As you can see, there are exactly three notes skipped between the C and the E (namely C#, D and D#), and then only two skipped between the E and the G (namely F and F#). If we start with a different note, say F#, we can easily tell that the notes in an F# Major chord are F#, A#, and C# (skipping G, G#, and A between F# and A#, and skipping B and C between A# and C#).</p>

<p>Another frequently encountered chord is the Minor chord. C Minor, for example, is played by sounding C, D#, and G. As you can see, C# and D are skipped between C and D#, and E, F and F# are skipped between D# and G. You should now be able to tell that the notes in an F# Minor chord are F#, A, and C#.</p>

### 입력 

 <p>In this problem you will be presented with a sequence of lines, each containing the names of three notes. You are to identify if these three notes, taken together, form a Major or Minor chord. If they do, you will display the name of the chord. If they don't you'll also report that fact. Remember that the notes need not appear in the usual sequence. Case will be ignored in the input, and the symbol ♭ will be indicated by the letter <code>b</code>. A blank or blanks will appear between the notes on each line, and may also precede the first note on the line or follow the third note on the line. Each line except the last will contain exactly three properly formed notes, so you need not check for errors. The last line will be entirely blank, and marks the end of the input data.</p>

### 출력 

 <p>The output is to be in the same style as shown in the examples below; do not use ♭ to name chords--use only # when necessary.</p>

