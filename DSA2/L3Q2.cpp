#include<bits/stdc++.h>
using namespace std;
int main()
{
    int m;
    cout<<"Enter Manhattan distance :";
    cin>>m;
    if(m%2==0)
        cout<<"Points are:"<<"(0,0)"<<"(0,"<<m<<"),("<<m<<",0),("<<m<<","<<m<<"),("<<m/2<<","<<m/2<<")";
    else
        cout<<"Points are :"<<"(0,0)"<<"(0,"<<m<<"),("<<m<<",0),("<<m<<","<<m<<")";
}
