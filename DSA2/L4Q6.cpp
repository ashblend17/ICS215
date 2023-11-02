#include <bits/stdc++.h>
using namespace std;
int findManhaƩanEuclidPair(pair<int, int> arr[], int n)
{
    map<int, int> X;
    map<int, int> Y;
    map<pair<int, int>, int> XY;
    for (int i = 0; i < n; i++) {
        int xi = arr[i].first;
        int yi = arr[i].second;
        X[xi]++;
        Y[yi]++;
        XY[arr[i]]++;
    }
    int xAns = 0, yAns = 0, xyAns = 0;
    for (auto xCoordinatePair : X) {
        int xFrequency = xCoordinatePair.second;
        int sameXPairs= (xFrequency * (xFrequency - 1)) / 2;
        xAns += sameXPairs;
    }
    for (auto yCoordinatePair : Y) {
        int yFrequency = yCoordinatePair.second;
        int sameYPairs = (yFrequency * (yFrequency - 1)) / 2;
        yAns += sameYPairs;
    }
    for (auto XYPair : XY) {
        int xyFrequency = XYPair.second;
        int samePointPairs = (xyFrequency * (xyFrequency - 1)) / 2;
        xyAns += samePointPairs;
    }
    return (xAns + yAns - (2 * xyAns));
}
int main()
{
    pair<int, int> arr[] = { { 1, 2 }, { 1, 2 }, { 4, 3 }, { 1, 3 } };
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << findManhaƩanEuclidPair(arr, n) << endl;
    return 0;
} 