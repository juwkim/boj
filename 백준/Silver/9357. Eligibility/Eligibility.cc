#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
struct ssss    //杠杠滴直接结构体搞起
{
    char name[55];  //名字
    int len;  //名字这个字符串的总长度
}ss[555];
bool cmp(const ssss &a,const ssss &b)  //字典序排序的小sort函数--!
{
    if(strcmp(a.name,b.name)<0)return 1;  //非递增
    return 0;
}
int main (void)
{
    int t,n,i,j,k,l,flog,m=1;
    char s[55];
    scanf("%d",&t);
    while(t--&&scanf("%d%*c",&n))
    {
        for(i=0;i<n;i++)
        cin.getline(ss[i].name, 500),ss[i].len=strlen(ss[i].name);  //不知道名字尾端空格数，所以直接gets
        sort(ss,ss+n,cmp);  //排序时带上年龄直接排序，没影响
        for(i=0;i<n;i++)ss[i].name[ss[i].len-5]='\0';  //打断，就是把字符串最后的年份切出来，这可是我的精华啊--!
        cout<<"Case #"<<m++<<":"<<endl;
        for(i=k=0;i<n;i++)
        {
            if(i==0){strcpy(s,ss[i].name),k=1;continue;}  //第一次直接在s里面放进第一个名字，同时记录出现次数为1
            if(!strcmp(ss[i].name,ss[i-1].name))  //如果名字相同
            {
                if(strcmp(ss[i].name+ss[i].len-4,ss[i-1].name+ss[i].len-4))k++;  //如果年份不同就出现次数加一，先前是切断了，只是在名字最后面那个后面画上‘\0’，但是实际内存还是存在的，我只要能找到他的位置就可以再次利用他，就相当于年份被我变成了一个没有名字的静态字符串数组
            }
            else  //名字不同
            {
                if(k<5)cout<<s<<endl;  //如果没有出现5次以上就输出
                strcpy(s,ss[i].name);k=1;  //替换s，初始化k
            }
        }
        if(k<5)cout<<s<<endl;  //注意，最后那一个还是要考虑哦
    }
    return 0;
}