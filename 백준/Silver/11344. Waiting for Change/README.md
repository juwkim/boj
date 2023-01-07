# [Silver IV] Waiting for Change - 11344 

[문제 링크](https://www.acmicpc.net/problem/11344) 

### 성능 요약

메모리: 117912 KB, 시간: 264 ms

### 분류

자료 구조(data_structures), 구현(implementation), 큐(queue), 시뮬레이션(simulation)

### 문제 설명

<p>Each student in a certain high school Calculus class must pay <span>$</span>15 for the latest review book. The problem is that not all of the students have exact change and the teacher, of course, has no money at all. Every student has the money to pay but some do not have exact change. To keep it simple, each student has exactly one <span>$</span>5 bill and one <span>$</span>10 bill or has exactly one <span>$</span>20 bill. Eager to begin their review, the students line up to purchase their new review books. This line will be called line A. The teacher forms a second line as needed for students who will have to wait for the teacher to make change. The second line is line B and will start out empty.</p>

<p>Review books will be purchased as follows. If the teacher is able to give the correct change, s/he will sell a review book to the first student in line B, if there is one, and give back the correct change. Otherwise, if the first student in line A has exact change, the teacher will sell that student a review book. However, if the first student in line A does not have exact change, then that student will go to the back of line B. Sadly, it is possible that not every student will be able to get a review book because there might not be enough <span>$</span>5 bills in the room.</p>

<p>Your program must print out the names of the students in line B when line B is at its longest.</p>

### 입력 

 <p>The input consists of several test cases. The input starts with the number of test cases. Each test case starts with the number of students followed by a list of students names and the amount that they can use to pay for the book (either 15 or 20). Fortunately, there are never two students by the same name.</p>

### 출력 

 <p>For each test case, your output should be a list of the names of the students waiting in line B when it is at its longest, from the front of the line to the back. If there is a tie, it should print the state of the line the first time it reached its maximum length. If no students ever get in line B, your output should print “Line B stayed empty.”</p>

<p>There will be at most 100 students in line A.</p>

