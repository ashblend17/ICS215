#include <iostream>
#include <cmath>
using namespace std;

// Function to count lattice points on the circumference of a circle
int countLatticePointsOnCircle(int r) {
    int count = 0;
    
    for (int x = -r; x <= r; x++) {
        for (int y = -r; y <= r; y++) {
            // Check if the point (x, y) lies on the circle
            if (x*x + y*y == r*r) {
                count++;
            }
        }
    }
    
    cout << count << "\n";
    
    for (int x = -r; x <= r; x++) {
        for (int y = -r; y <= r; y++) {
            // Check if the point (x, y) lies on the circle
            if (x*x + y*y == r*r) {
                cout << "(" << x << ", " << y << "), ";
            }
        }
    }
}

int main() {
    int r;
    cin >> r;
    int points = countLatticePointsOnCircle(r);
    return 0;
}