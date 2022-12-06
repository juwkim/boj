#include <stdio.h>
#include <string.h>
int main(){
    int n, x1, y1, x2, y2, ans[100];
    int paper[1001][1001];
    memset(paper, -1, 1001*1001*sizeof(int));
    scanf("%d", &n);
    for(int num=0; num<n; num++){
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        for(int i=x1; i<x1+x2; i++){
            for(int j=y1; j<y1+y2; j++){
                if(paper[i][j] != -1){
                    ans[paper[i][j]]--;
                }
                    ans[num]++;
                    paper[i][j]=num;
            }
        }
    }
    for(int num=0; num<n; num++)
        printf("%d\n", ans[num]);
}