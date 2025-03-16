# [Silver II] BSP Trees - 7007 

[문제 링크](https://www.acmicpc.net/problem/7007) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

기하학, 정렬

### 제출 일자

2025년 3월 17일 07:01:14

### 문제 설명

<p>When rendering a scene with multiple objects onto a screen, the order in which the objects are drawn is very important. In general, the farther an object is from the screen, the earlier it should be drawn allowing later, closer objects to be drawn on top of them. If two objects do not overlap, the order of drawing is immaterial. A binary space-partitioning (BSP) tree is one type of data structure which attempts to simplify the determination of the ordering of objects. It works as follows. Assume that the screen lies in the xy-plane centered on the z-axis and that the z-axis points away from the user looking at the screen. (For our purposes, assume the user lies near -∞ on the z-axis.) We also assume that all the objects lie on the opposite side of the screen (z > 0). The BSP tree is built by placing a series of planes parallel to the y-axis. The first plane divides space into two regions: a region containing the viewer and a region not containing the viewer. We partition all objects in space according to which of these two regions they lie in, and observe that all objects in the region containing the viewer should be drawn after all the objects in the other region. The BSP tree can be viewed at this point as a root with only two children, each child containing one of the partitions. We can now add a second plane, which subdivides the space again. We split each of the two partitions from the first plane in two, making a total of 4 partitions, and the resulting BSP tree now has three levels, with the partitions in the leaves (note that some of these partitions may contain several objects and some may contain none). This process is continued until each partition has at most one object in it, or until some predetermined number of planes has been used. The diagram below gives an example of using 1, 2 and 3 planes (looking down along the y-axis). For simplicity we assume that all objects lie parallel to the z-axis, so we need only deal this 2-d image to determine the BSP tree.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/7007/1645_1.jpg" style="height:133px; width:650px"></p>

<p>Assuming you have split the partitions correctly, a simple traversal of the BSP tree will give you an appropriate ordering for which to render the objects in the scene. Note in the example above that once a node contains just one object it need not be split as additional planes are added. </p>

### 입력 

 <p>Input will consist of one problem instance. The first line will contain a positive integer n <= 20 indicating the number of objects in the scene. The next n lines will contain a description of these objects using the format m x<sub>1</sub> z<sub>1</sub> x<sub>2</sub> z<sub>2</sub> ... x<sub>m</sub> z<sub>m</sub>, where m is the number of vertices in the object and the remaining values are the vertices of the intersection of the object with the xz-plane. All objects will have between 3 and 6 vertices. Objects are assumed to be labeled "A", "B", "C", ... in the order they are defined. Next in the input will be a positive integer p <= 10 indicating the number of planes used to create the BSP tree. The last p input lines will contain a description of each plane of the form x<sub>1</sub> z<sub>1</sub> x<sub>2</sub> z<sub>2</sub> representing two points on the intersection line of the plane and the xz-plane. You may assume that no line will intersect any object (including edges and vertices) and that no plane is parallel to the z-axis.All coordinates will be integers.</p>

### 출력 

 <p>Output will consist of a single line containing the names of the objects in the order that they should be rendered for the specified BSP tree. In the case when some partition contains two or more objects,you should list the objects in alphabetical order.</p>

