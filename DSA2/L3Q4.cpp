#include <bits/stdc++.h>
using namespace std;
void minDistance(int n, int k, vector<vector<int> >& point)
{
    for (int i = 0; i < k; ++i)
    {
        // cout<<point[i][0]<<" ";
        sort(point[i].begin(), point[i].end());
        // cout<<point[i][0]<<" ";
    }
    // cout << point[0][];
    for (int i = 0; i < k; ++i)
    {
        cout << point[i][(ceil((double)n / 2) - 1)] << " ";
    }
}
int main()
{
    int n = 4, k = 4;
    vector<vector<int> > point = { { 1, 5, 2, 4 },
    { 2, 3, 0, 4 },
    { 11, 7, 1, 3 },
    { 6, 7, 5, 1 } };
    minDistance(n, k, point);
    return 0;
}