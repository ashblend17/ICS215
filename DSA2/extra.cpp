#include<bits/stdc++.h>
using namespace std;
int calculate(const vector<pair <int,int> > &seg)
{
	int n = seg.size();
	vector <pair <int, bool> > points(n * 2);
	for (int i = 0; i < n; i++)
	{
		points[i*2]	 = make_pair(seg[i].first, false);
		points[i*2 + 1] = make_pair(seg[i].second, true);
	}
	sort(points.begin(), points.end());
	int result = 0;
	int Counter = 0;
	for (int i=0; i<n*2; i++)
	{
		if (Counter)
        {
			result += (points[i].first - points[i-1].first);
        }
		if(points[i].second)
        {
            Counter--;
        }
        else 
        {
            Counter++;
        }
	}
	cout<<result;
}
int main()
{
	vector< pair <int,int> > segments;
	segments.push_back(make_pair(4, 8));
	segments.push_back(make_pair(1, 9));
	segments.push_back(make_pair(133, 144));
    calculate(segments);
	return 0;
}