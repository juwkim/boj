# [Silver II] Combination Lock - 9573 

[문제 링크](https://www.acmicpc.net/problem/9573) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2024년 12월 12일 21:06:12

### 문제 설명

<p>Farmer John's cows keep escaping from his farm and causing mischief. To try and prevent them from leaving, he purchases a fancy combination lock to keep his cows from opening the pasture gate.</p><p>Knowing that his cows are quite clever, Farmer John wants to make sure they cannot easily open the lock by simply trying many different combinations. The lock has three dials, each numbered 1..N (1 <= N <= 100), where 1 and N are adjacent since the dials are circular.  There are two combinations that open the lock, one set by Farmer John, and also a "master" combination set by the lock maker.  The lock has a small tolerance for error, however, so it will open even if the numbers on the dials are each within at most 2 positions of a valid combination.  For example, if Farmer John's combination is (1,2,3) and the master combination is (4,5,6), the lock will open if its dials are set to (1,N,5) (since this is close enough to Farmer John's combination) or to (2,4,8) (since this is close enough to the master combination).  Note that (1,5,6) would not open the lock, since it is not close enough to any one single combination.</p><p>Given Farmer John's combination and the master combination, please determine the number of distinct settings for the dials that will open the lock.  Order matters, so the setting (1,2,3) is distinct from (3,2,1).</p>

### 입력 

 <ul><li>Line 1: The integer N.</li><li>Line 2: Three space-separated integers, specifying Farmer John's combination.</li><li>Line 3: Three space-separated integers, specifying the master combination (possibly the same as Farmer John's combination).</li></ul>

### 출력 

 <ul><li>Line 1: The number of distinct dial settings that will open the lock.</li></ul>

