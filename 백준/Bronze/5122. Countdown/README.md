# [Bronze I] Countdown - 5122 

[문제 링크](https://www.acmicpc.net/problem/5122) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Many say that the world is going to end on 12/21/2012 G (dates in our calendar, the Gregorian calendar, will have the suffix G), but how did they come up with this exact date? Sadly, most of them are probably just repeating what everyone else is saying, but there is some evidence for this date. The theory is based on the beliefs of the Maya civilization and their calendar, the Mesoamerican Long Count calendar (dates in this calendar will have the suffix MLC). It is said that the Maya believed that there were three unsuccessful worlds before the current fourth one. The last one is said to have ended on 13.0.0.0.0 MLC. Since this date is also the beginning of the current world, the calendar is reset and the date is referred to as 0.0.0.0.0 MLC. When we reach 13.0.0.0.0 MLC again, it could mean the end of our current world if history is to repeat itself. Given a mapping from MLC to G, we would like to know how many days are left until the end of the world.</p>

<p>Unfortunately, we need two additional calendars in order figure this out! But before we get into that, what are these MLC dates anyway? MLC dates are just a count of the number of days since the creation of our current world. It is a base-20 number delimited by dots, except that the second digit is base-18. So, the day before the end of the current world is 12.19.19.17.19 MLC.</p>

<p>So why do we need two more calendars? Well, when astronomers try to match up Mayan astronomical records with known dates for astronomical events, they specify the known date by its Julian Day Number (dates in this calendar will have the suffix JDN). JDN has the benefit that it is easy to do computations with because, like the MLC calendar, JDN is a count of the number of days since a starting day, 0 JDN. Since we want to know the number of days until the end of the world, all we need is the JDN of today’s date, 5/6/2012 G, and the JDN of the end of the world, 13.0.0.0.0 MLC. The JDN of the end of the world can easily be computed given the MLC of an astronomical event and its equivalent JDN. On the other hand, figuring out the JDN of today’s date is not so easy and requires use of another calendar.</p>

<p>0 JDN is specified in terms of the Julian calendar (dates in this calendar will have the suffix J). When history books refer to dates before 10/15/1582 G, they’re usually referring to a Julian calendar date because the Gregorian calendar wasn’t used until 10/5/1582 J at which time the Gregorian calendar skipped 10 days and started at 10/15/1582 G. The Julian calendar is exactly the same as the Gregorian calendar except that the Julian calendar has an easier leap-year rule (and the 10 day difference just mentioned). A year Y is a leap-year when:</p>

<pre>Julian: Y % 4 == 0
Gregorian: (Y % 4 == 0 && Y % 100 != 0) || Y % 400 == 0</pre>

<p>0 JDN is equivalent to 1/1/4713 BCE J (BCE stands for “before common era” and is used to denote a date before 1/1/1 J. These dates behave the same except that the year counts down to 1 BCE J. The year after that is the start of the “common era”, 1 J). BCE dates don’t follow the leap-year rule because 4 years before 1/1/4J is 1/1/1 BCE J. So the leap-year rule becomes:</p>

<pre>BCE J: (Y-1) % 4 == 0</pre>

<p>We can use this to count the number of days from 0 JDN to 10/5/1582 J. From there, we can use the Gregorian leap-year rules to count the number of days from 10/15/1582 G to today’s date. Summing up both of these counts will tell us the JDN of today’s date:</p>

<pre># of Julian days = 4713 * 365
                 + (4713-1) / 4 + 1 // leap-days
                 + 1581 * 365
                 + 1581 / 4 // leap-days
                 + 5*31 + 3*30 + 28 + 4 // days in 1582
                 = 2299161</pre>

<pre># of Gregorian days = ( ((2012-1)-1200) * 365 // days since 1200
                    + ((2012-1)-1200) / 4 // overcount leap-days
                    - ((2012-1)-1200) / 100 // adjust count
                    + ((2012-1)-1200) / 400 // adjust count
                    + 2*31 + 30 + 29 + 6 ) // days in 2012
                    - ( ((1582-1)-1200) * 365 // days from 1200 to 1582
                    + ((1582-1)-1200) / 4
                    - ((1582-1)-1200) / 100
                    + ((1582-1)-1200) / 400
                    + 5*31 + 3*30 + 28 + 14 ) // days in 1582
                    = 156894</pre>

<pre>Total = 2299161 + 156894
      = 2456055</pre>

<p>This includes 0 JDN, so 5/6/2012 G is equivalent to 2456054 JDN.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line contains a date M in the MLC calendar, made up of five integer digits 0 ≤ Mi ≤ 19 where 0 ≤ M4 ≤ 17. This is the date of an astronomical event. The next line contains a single integer 0 ≤ J indicating the most probable JDN of the same astronomical event.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line output the number of days until the end of the world assuming we have the correct JDN for the astronomical event. However, if the number is negative, output “It’s a hoax!”, and if the number is 0, output “Panic!”. Each data set should be followed by a blank line.</p>

