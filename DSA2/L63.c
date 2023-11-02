#include<stdio.h>
int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int a = n*(n+1)/2 * m*(m+1)/2;
    printf("%d",a);
}