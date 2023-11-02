#include <bits/stdc++.h>
using namespace std;
long long int bio_coeff(int A, int B)
{
    long long int temp = 1;
    if (B > A - B)
    {
        B = A - B;
    }
    for (int i = 0; i < B; ++i)
    {
        temp = temp * (A - i);
        temp = temp / (i + 1);
    }
    return temp;
}
long long int Manhattan_distance(int x1, int y1, int x2, int y2)
{
    int A = abs(x1 - x2);
    int B = abs(y1 - y2);
    int count = bio_coeff(A + B, B);
    return count;
}
int main()
{
    int x1 = 6, y1 = 8, x2 = 2, y2 = 10;
    cout<<"Count of paths with distance equal to Manhattan distance are: "<<Manhattan_distance(x1, y1, x2, y2);
    return 0;
}