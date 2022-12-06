# [Bronze II] Adding Reversed Numbers - 3486 

[문제 링크](https://www.acmicpc.net/problem/3486) 

### 성능 요약

메모리: 124568 KB, 시간: 732 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>The Antique Comedians of Malidinesia prefer comedies to tragedies. Unfortunately, most of the ancient plays are tragedies. Therefore the dramatic advisor of ACM has decided to transfigure some tragedies into comedies. Obviously, this work is very hard because the basic sense of the play must be kept intact, although all the things change to their opposites. For example the numbers: if any number appears in the tragedy, it must be converted to its reversed form before being accepted into the comedy play.</p>

<p>Reversed number is a number written in arabic numerals but the order of digits is reversed. The first digit becomes last and vice versa. For example, if the main hero had 1245 strawberries in the tragedy, he has 5421 of them now. Note that all the leading zeros are omitted. That means if the number ends with a zero, the zero is lost by reversing (e.g. 1200 gives 21). Also note that the reversed number never has any trailing zeros.</p>

<p>ACM needs to calculate with reversed numbers. Your task is to add two reversed numbers and output their reversed sum. Of course, the result is not unique because any particular number is a reversed form of several numbers (e.g. 21 could be 12, 120 or 1200 before reversing). Thus we must assume that no zeros were lost by reversing (e.g. assume that the original number was 12).</p>

### 입력 

 <p>The input consists of <var>N</var> cases. The first line of the input contains only positive integer <var>N</var>. Then follow the cases. Each case consists of exactly one line with two positive integers separated by space. These are the reversed numbers you are to add. Two integers are less than 100,000,000.</p>

### 출력 

 <p>For each case, print exactly one line containing only one integer - the reversed sum of two reversed numbers. Omit any leading zeros in the output.</p>

