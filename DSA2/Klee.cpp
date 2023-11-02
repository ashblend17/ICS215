#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector <int> v;
    int n;
    cin>>n;
    int m;
    for(int i=0;i<n*2;i++)
    {
        cin >> m;
        v.push_back(m);
    }
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(v[i*2]>v[j*2])
            {
                swap(v[i*2],v[j*2]);
                swap(v[(i*2)+1],v[(j*2)+1]);
            }
        }
    }
    int sum=0,overlap=0;
    for(int i=0;i<n;i++)
    {
        sum+=v[(i*2)+1]-v[i*2];
    }
    for(int i=0;i<n-1;i++)
    {
        if(v[(i*2)+1]>v[(i*2)+2])
        {
            overlap+=v[(i*2)+1]-v[(i*2)+2];
        }
    }
    cout<<(sum-overlap)<<endl;
}