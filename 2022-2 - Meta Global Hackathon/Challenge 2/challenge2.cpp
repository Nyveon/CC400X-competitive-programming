// Eric K.
// Meta Global Hackathon 2022

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <cmath>

using namespace std;


bool in_right_isoceles_triangle(int x, int y, int tx, int ty, int td) {
    // Normalize the coordinates
    x -= tx;
    y -= ty;

    // Check if the point is in the right triangle
    return (x >= 0 && x <= td && y >= 0 && y <= td && x + y <= td);
}

bool compare_points_diagonally(const pair<int, int> &a, const pair<int, int> &b) {
    // Compare the points diagonally
    return (a.first + a.second < b.first + b.second);
}

int main() {
    // Input
    int n, q;
    cin >> n >> q;

    // Read in the data centers, as coordinate pairs
    vector<pair<int, int>> data_centers;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        data_centers.push_back(make_pair(x, y));
    }

    // Sort the data centers diagonally
    sort(data_centers.begin(), data_centers.end(), compare_points_diagonally);

    // Process the queries
    for (int i = 0; i < q; i++) {
        int tx, ty, td;
        cin >> tx >> ty >> td;

        // Binary search for the first data center in the range
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (data_centers[mid].first + data_centers[mid].second < tx + ty) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int first = left;

        // Binary search for the last data center in the range
        left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (data_centers[mid].first + data_centers[mid].second > tx + ty + td) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        int last = left;


        // Count the number of data centers in the range
        int count = 0;
        for (int j = max(0, first - 3); j <= min(n - 1, last + 3); j++) {
            if (in_right_isoceles_triangle(data_centers[j].first, data_centers[j].second, tx, ty, td)) {
                count++;
            }
        }

        cout << count << endl;
    }

    return 0;
}