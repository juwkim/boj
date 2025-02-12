# [Silver II] Travel the Skies - 16514 

[문제 링크](https://www.acmicpc.net/problem/16514) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

그래프 이론, 구현, 시뮬레이션

### 제출 일자

2025년 2월 13일 08:27:08

### 문제 설명

<p>One day your boss explains his new planning scheme for your company, Fly Away Air. Rather than having customers book tickets between destinations, they’ll say when they want to leave and from where, and your company will take care of the rest. That means you get to generate their flight schedules and destinations for them! He has an eye on the books though and wants to make sure all your flights are fully booked. He tasks you with the job of determining if a set of flight plans in a given flight window is financially optimal in that regard.</p>

<p>You assure him that he put his trust—and his pocket book—in the hands of the right employee. Your job is to plan flight schedules for customers so that you fill each of the flights scheduled in the given flight window. To ensure you don’t lose customers due to air sickness, you decide that each customer can only take one flight a day. Further, since you’re sure that all of your customers are gracious folks, you decide to help your boss out and let them fly on any day on or after their suggested departure date. Finally, to simplify things, you do not worry about ensuring each customer return to their original departure airport, though this is allowed to be scheduled. If needed, they can book their own return flights!</p>

### 입력 

 <p>On the first line, you’re given three integers: k, (2 ≤ k ≤ 12), the number of airports; n, (1 ≤ n ≤ 8), the number of days of the flight departure window; and m, (1 ≤ m ≤ k · (k − 1) · n); the number of flights in the window. Then, m lines follow with four integers each: u, (1 ≤ u ≤ k), the flight’s starting location; v, (1 ≤ v ≤ k, u 6= v), the flight’s ending destination; d, (1 ≤ d ≤ n), the day on which the flight flies in the window; and z, (1 ≤ z ≤ 30 000), the capacity of the flight. It is guaranteed there will be at most one flight in each direction between any two airports on a given day. Following are kn lines with three integers each: a, (1 ≤ a ≤ k), the airport; b, (1 ≤ b ≤ n), the day; and c, (1 ≤ c ≤ 30 000), the number of customers wishing to begin their travels by leaving their homes to their local airport a on day b (notably, this does not include those who may be arriving from other flights, which is for you to decide). Each airport-day pair will appear exactly once.</p>

### 출력 

 <p>Output only the word optimal if all m flights can be filled to capacity, else output only the word suboptimal if it is not possible to fill all m flights. It is not necessary that each customer arriving at an airport ever be booked on a flight.</p>

