#include<bits/stdc++.h>
using namespace std;
int main()
{
int n; //number of points
cin>>n;
int ar[n*2];
for(int i=0;i<n*2;i++)
{
cin>>ar[i];
}
int ans=abs(ar[2]-ar[0]) + abs(ar[3]-ar[1]);
cout<<ans<<endl;
return 0;
}
